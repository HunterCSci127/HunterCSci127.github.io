import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "client_secrets.json"
SPREADSHEET = "CSci 127 Tutoring Sign-In (Responses)"
# Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
# Load in the secret JSON key (must be a service account)
json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)
gc = gspread.authorize(credentials)
# Open up the workbook based on the spreadsheet name
workbook = gc.open(SPREADSHEET)
# Get the first sheet
sheet = workbook.sheet1
# Extract all data into a dataframe
results = pd.DataFrame(sheet.get_all_records())