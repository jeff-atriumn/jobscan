#!/usr/bin/env python3

import pprint
import requests

from linkedin_api import Linkedin
from bs4 import BeautifulSoup


# Authenticate using any Linkedin account credentials
api = Linkedin('jrojers@gmail.com', 'password')

# # GET a job
# job = api.get_job('3610533462')

# pprint.pprint(job)


# Make an HTTP request to the website
response = requests.get('https://app.otta.com/jobs/b3liMFl5')

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

job_title_tag = soup.find('h1')
if job_title_tag:
    job_title = job_title_tag.text
    print(f'Job Title: {job_title}')

pprint.pprint(soup)