# Generating a website for new semester
To run the script, run the following command in this directory:  
python3 newSemester.py

You will be prompted for the semester to copy from and the name of the new semester. Follow the exact format shown when running the script.


# README for lab.html and lab.js
Lab.html displays several quick links for students to use and navigate the course website.
The Google Calendar button directs students to an embedded calendar in their browser with the course due dates and some important college dates.

lab.js creates and displays a chart that tracks daily traffic in the labs. 
The script uses Google Sheets API to pull data from spreadsheets linked to sign-in and sign out forms that students will complete when entering and exiting the lab.
The script also uses charts.js for browser modules to create and display the bar graph.