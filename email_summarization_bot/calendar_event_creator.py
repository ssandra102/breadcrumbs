import spacy
import re
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import streamlit as st


class CalendarEventCreator:

    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.scopes = "https://www.googleapis.com/auth/calendar"
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_path, scopes=[self.scopes]
        )
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def extract_dates(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        return dates

    def extract_events(self, text):
        event_keywords = ["meeting", "event", "conference"]
        pattern = re.compile(r'\b(?:' + '|'.join(event_keywords) + r')\b', re.IGNORECASE)
        matches = re.findall(pattern, text)
        return matches

    def extract_event_info(self, email_text):
        dates = self.extract_dates(email_text)
        events = self.extract_events(email_text)
        event_info = {"dates": dates, "events": events}
        return event_info

    def create_event(self, start_time, end_time, summary, description, location):
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Kolkata',
            },
            'location': location,
            'visibility': 'private',
        }

        # Insert the event into the calendar
        event = self.service.events().insert(calendarId='primary', body=event).execute()

        print(f'Event created: {event}')

    def add_event(self, email_text):
        result = self.extract_event_info(email_text)
        start_time = datetime.datetime.now()  # + datetime.timedelta(days=1, hours=3)
        end_time = start_time + datetime.timedelta(hours=2)
        summary = result["events"][1]
        description = result["events"][1]
        location = 'Conference Room'
        self.create_event(start_time.isoformat(), end_time.isoformat(), summary, description, location)

    def list_events(self):
        events_result = self.service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            st.write('No upcoming events found.')
        else:
            st.write('Upcoming events:')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                st.write(f'{start} - {event["summary"]}')

    def delete_all_events(self):
        events_result = self.service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            st.write('No events found to delete.')
        else:
            st.write('Deleting all events:')
            for event in events:
                try:
                    # Delete each event by its eventId
                    self.service.events().delete(calendarId='primary', eventId=event['id']).execute()
                    st.write(f"Deleted event: {event['summary']}")
                except HttpError as e:
                    st.write(f"Error deleting event: {event['summary']}, Error: {e}")


