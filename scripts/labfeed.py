from __future__ import print_function
from os import times
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import time, date, datetime, timedelta
"""
    Getting Sign-in sheet data via Google Sheets API
    Authorized via service account key file: service_key.json
"""
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service_key.json'

SPREADSHEET_ID = '1lWkUdQsn_bGEDb-MFFlh2deysNfRUH3XFRTqP_mk4zY'
RANGE_NAME = 'Responses!A:E'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets() 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

# Convert results from google sheets to dataframe
df = pd.DataFrame(values[1:], columns = values[0])

# split timestamp into date and time column
df[['Date', 'Time']] = df['Timestamp'].str.split(expand=True) 
# Limit data to today only [UNCOMMENT FOR ACTUAL USAGE]
# today = '{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())
# today_lims = datetime.datetime.now().strftime('%Y-%m-%d')
today_lims = '2021-07-30'
today = '7/30/2021'

today_df = df[df['Date'] == today] 

LAB_CAPACITY = 30
NUM_STUDENTS = len(today_df)

lab_hours = [time(hour=i).strftime("%H:%M") for i in range(10, 19)]

sns.set_theme(style='darkgrid')
plot = sns.lineplot(data=today_df,
             x='Time',
             y=NUM_STUDENTS
             )

plot.set(ylabel= 'Students in Lab',
         ylim = (0, LAB_CAPACITY),
         xticks = (range(len(lab_hours))),
         xticklabels = lab_hours
        )


fig = plt.gcf()
fig.autofmt_xdate()
fig.savefig('test.png')

