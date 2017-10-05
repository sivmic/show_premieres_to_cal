from __future__ import print_function
import httplib2
import os
import argparse

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from config import CAL_ID, CLIENT_SECRET_FILE, APPLICATION_NAME, SCOPES


class Cal:
    def __init__(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)

    def add_all_day_event(self, summary, description, date):
        event_info = {
            "summary": summary,
            "description": description,
            "start": {
                "date": date
            },
            "end": {
                "date": date
            }
        }

        event = self.service.events().insert(calendarId=CAL_ID, body=event_info).execute()
        print("Added this event: " + event.get("htmlLink"))

    def get_credentials(self):
        credential_dir = "./credentials"
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'calendar-python.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
            credentials = tools.run_flow(flow, store, flags)
            print('Storing credentials to ' + credential_path)

        return credentials
