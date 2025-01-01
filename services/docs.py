import io
import os
from typing import Dict

import google.auth
import yaml
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from models.docs import Config, Document

# service account scopes for reading documents
SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]

# read config from default location
CONFIG = Config.from_file("config.yaml")


def authenticate_google_docs():
    """Authenticates the user and returns the Docs API client."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists("credentials.json"):
        creds = service_account.Credentials.from_service_account_file(
            "credentials.json", scopes=SCOPES
        )

    try:
        # Build the Docs API client
        service = build("docs", "v1", credentials=creds)
        return service
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


def get_document_content(service, document_id):
    """Fetches the document content."""
    try:
        # Call the Docs API to fetch the document
        document = service.documents().get(documentId=document_id).execute()
        return document
    except HttpError as err:
        print(f"An error occurred: {err}")
        return None


def count_words_in_document(document):
    """Counts the words in the fetched Google Document."""
    word_count = 0

    # Loop through the document content
    for element in document.get("body").get("content"):
        if "paragraph" in element:
            for para_element in element["paragraph"].get("elements"):
                if "textRun" in para_element:
                    text = para_element["textRun"].get("content")
                    # Count words by splitting by whitespace and filtering empty strings
                    word_count += len([word for word in text.split() if word])

    return word_count


def get_word_counts(config: Config):
    """Read each document in the given config, and return its number of words, as well as a total."""
    # Authenticate and get the service
    service = authenticate_google_docs()
    if service is None:
        return

    results = {}

    for document in config.documents:
        # Fetch the document content
        content = get_document_content(service, document.google_doc_id)
        if content:
            # Count the words
            word_count = count_words_in_document(content)
            results[content["title"]] = word_count
            print(f"{content['title']} word count: {word_count}")
        else:
            print(f"Document {content['title']} not found.")

    return results
