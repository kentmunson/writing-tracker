# Writing Tracker

As a hobby, I like to write. Someday I think it'd be fun to publish a short story, or something like that.

But: I'm not very good. So to help me practice and keep track of what I write, I built this very simple application, which I host on Google Cloud.

## Setup Instructions

### Create a service account

* Create a service account on GCP, via the console, CLI, whatever.
* Download the credentials to `credentials.json`

### Create a config

* Copy and edit `config.example.yaml`
* Add each document's id and title to the documents list

### Run the application

* Create a virtual environment and install `requirements.txt`
* Activate it, and run `python app.py`

## Backlog

This is very much a work in progress, and I imagine there's plenty more to do beyond what's listed here, but this is what's currently on my radar:

1. Simple UI
2. User authentication
3. Scheduled emails with current word counts
4. Scheduled emails with passages to edit
5. Proper logging
6. Better dependency management, via `pdm`, `poetry`, etc
7. Testing with some default dummy documents and credentials
