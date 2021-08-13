// Client ID and API key from the Developer Console
const CLIENT_ID = '426823219026-mc1s07da31ime86pj7hp11iu3f61vedm.apps.googleusercontent.com';
const API_KEY = 'AIzaSyD_XgaW_WBdzj8FfPbcUaQPQf_ccNihHlo';

// Array of API discovery doc URLs for APIs used by the quickstart
var DISCOVERY_DOCS = ["https://sheets.googleapis.com/$discovery/rest?version=v4"];

// Authorization scopes required by the API; multiple scopes can be
// included, separated by spaces.
var SCOPES = "https://www.googleapis.com/auth/spreadsheets";

/**
 *  On load, called to load the auth2 library and API client library.
 */
function handleClientLoad() {
   gapi.load('client:auth2', initClient);
}

/**
 *  Initializes the API client library and sets up sign-in state
 *  listeners.
 */
function initClient() {
   gapi.client.init({
      clientId: CLIENT_ID,
      apiKey: API_KEY,
      discoveryDocs: DISCOVERY_DOCS,
      scope: SCOPES
   }).then(async function () {
      let signInData = getSignInData();
      let signOutData = getSignOutData();
      let data = await Promise.all([signInData, signOutData]);
      chartData(data[0], data[1])
   }, function(error) {
      console.log(JSON.stringify(error, null, 2));
   });
}

/** 
 * getSignInData(): asynchronously gets the data from the google spreadsheets api
 * gets data from Sign In Responses
*/
function getSignInData() {
   let data = gapi.client.sheets.spreadsheets.values.get({
      spreadsheetId: '1lEbtiqa7cnzikZQxYiNoji7QuGID2K_8JDjmGAPq0IQ',
      range: 'Responses!A:E'
   })
   .then(
      function(response) {
         let range = response.result.values;
         let signInData;
         // console.log(range)
         if (range.length > 0) {
            // for(let i = 1; i < range.length; i++)
            //    signInData.push(range.values[i])
            signInData = range.slice(1);    
         } else {
            console.log('No sign-in data found.');
         }

         return signInData;
       }, 
      // catch error
      function(response) {
         console.log('Error: ' + response.result.error.message);
      }
   );  
   
   return data;
}

/** 
 * getSignInData(): asynchronously gets the data from the google spreadsheets api
 * gets data from Sign Out Responses
*/
async function getSignOutData() {
   let data = gapi.client.sheets.spreadsheets.values.get({
      spreadsheetId: '13zJvWVaZFekomDEn1c0Jg-tPawePVlvVFCmPY8cIwug',
      range: 'Responses!A:F'
   })
   .then(
      function(response) {
         let range = response.result.values;
         let signOutData;
         if (range.length > 0) {
            signOutData = range.slice(1);            
         } else {
            console.log('No sign out data found.');
         }
         
         return signOutData;
       }, 
      // catch error
      function(response) {
         console.log('Error: ' + response.result.error.message);
      }
   )

   return data;
}

/**
 * Charts the data using charts.js 
 * @param {array} signInData : data from google spreadsheets API (sign in responses)
 * @param {array} signOutData : data from google spreadsheets API (sign out responses)
 */
function chartData(signInData, signOutData) {
   // create array of working lab hours to use as x-axis labels for chart
   const lab_hours = ["11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]
   
   // manipulate data from google spreadsheets to use for chart
   // returns an object with three arrays: 
   // students['students']: number of students currently in lab
   // students['signedIn']: number of students who signed in
   // students['signedOut']: number of students who signed out
   const students = getStudents(signInData, signOutData);
   console.log(students)

   const data = {
      labels: lab_hours,
      datasets: [
         {
            label: 'Total Visits Today',
            backgroundColor: generateVisitColors(),
            data: students['visits'],
            // hidden: true
         },
         {
            label: 'Currently in Lab' ,
            backgroundColor: generateCurrentColors(),
            data: students['in'],
         },
         {
            label: 'No Longer in Lab',
            backgroundColor: generateExitColors(),
            data: students['out'],
         }

      ]
   };

   // chart.js configurations
   const config = {
      type: 'bar',
      data: data,
      options: {
         scales: {
            y: {
               beginAtZero: true,
               max: 30,
               min: 0,
               grid: {
                  color: '#63625d'
               }
            }, 
            x: {
               grid: {
                  color: '#63625d'
               }
            }
         }, 
         plugins: {
            title: {
               display: true,
               text: 'CSci 127 Lab Traffic ',
               color: '#63625d',
               font: {
                  size: 24
               },
               padding: 10
            },
            subtitle: {
               display: true,
               text: new Date().toDateString() + "  |  Refresh page to update graph",
               font: {
                  size: 16
               },
               padding: 10
            },
            legend: {
               labels: {
                  padding: 20
               }
            }
         },
         maintainAspectRatio: false,
         
      }
   };

   // create chart
   let ctx = new Chart(document.getElementById('daily-container'), config);

}

function getStudents(signInData, signOutData) {
   // calculate date using mm/dd/yyyy format without leading zeroes to match spreadsheet timestamps
   const current_date = new Date();
   const today =((current_date.getMonth() > 8) ? (current_date.getMonth() + 1) : ((current_date.getMonth() + 1))) + '/' + ((current_date.getDate() > 9) ? current_date.getDate() : ('0' + current_date.getDate())) + '/' + current_date.getFullYear();

   const current_time = current_date.toTimeString().substr(0, 2);

   // for both signInData and signOutData, the 0th index is the timestamp column
   const TIMESTAMP = 0

   
   // create object to hold arrays for plotting on chart 
   // entries correspond to [11am,12pm,1pm,2pm,3pm,4pm,5pm]
   // signouts is only for calculation purposes, not used for charting
   let s = {'visits': [0, 0, 0, 0, 0, 0, 0], 'in': [0, 0, 0, 0, 0, 0, 0], 'out': [0, 0, 0, 0, 0, 0, 0], 'signouts': [0, 0, 0, 0, 0, 0, 0]}

   let date, time, key, num_students = 0, signouts = 0;
   for(let i = 0; i < signOutData.length; i++) {
      // split timestamp into date and time
      data = signOutData[i][TIMESTAMP].split(" ")
      date = data[0]
      time = data[1]

      // first two indices of time corresponds to hour (24hr format)
      key = time.substring(0, 2)
      // limit data to today and lab hours
      if (date === today && key >= 11 && key < 18) {   
         signouts++;
         s['out'][key-11]++; //key - 11 corresponds to the index in the array
         //update count of all signouts
         for(let n = key-11; n < s['signouts'].length; n++) s['signouts'][n] = signouts;
      }
   }

   for(let i = 0; i < signInData.length; i++) {
      // split timestamp into date and time
      data = signInData[i][TIMESTAMP].split(" ")
      date = data[0]
      time = data[1]

      // first two indices of time corresponds to hour (24hr format)
      // time formatted as 13:00:00 
      key = time.substring(0, 2)
      // limit data to today and lab hours
      if (date === today && key >= 11 && key < 18) {  
         num_students++;
         // s['visits'][key-11] = num_students; 
         for(let n = key; n <= current_time; n++) {
            s['visits'][n-11] = num_students;
            s['in'][n-11] = num_students - s['signouts'][n-11];

         }

      }
   }
   
   return s;
}

/* 
function generate__colors() : generates a list of colors to plot the bar graph
The color that corresponds to the current time is darker to highlight current lab hours.
 */
function generateVisitColors() {
   let lighter = "#99c7cf", darker="#54b4c4"
   let colors = [lighter, lighter, lighter, lighter, lighter, lighter, lighter]
   const current_time = new Date().toTimeString().substr(0, 2);

   colors[current_time-11] = darker
   return colors;
}


function generateCurrentColors() {
   let lighter = "#a9e3a3", darker="#4cb04c"
   let colors = [lighter, lighter, lighter, lighter, lighter, lighter, lighter]
   const current_time = new Date().toTimeString().substr(0, 2);

   colors[current_time-11] = darker
   return colors;
}


function generateExitColors() {
   let lighter = "#f2bab6", darker="#cf655d"
   let colors = [lighter, lighter, lighter, lighter, lighter, lighter, lighter]
   const current_time = new Date().toTimeString().substr(0, 2);

   colors[current_time-11] = darker
   return colors;
}