import requests

# Get your API key from Jobscan
API_KEY = "YOUR_API_KEY"

# Create the URL for the authentication endpoint
AUTH_URL = "https://api.jobscan.com/v1/auth"

# Make the authentication request
headers = {
    "Authorization": "Bearer " + API_KEY
}

response = requests.post(AUTH_URL, headers=headers)

# Check the response status code
if response.status_code == 200:
    # The authentication was successful
    session = response.json()
    print("Authenticated successfully")
else:
    # The authentication failed
    print("Authentication failed")

# Get the job description URL
JOB_DESCRIPTION_URL = "https://www.indeed.com/viewjob?jk=123456789"

# Create the URL for the resume matching endpoint
RESUME_MATCHING_URL = "https://api.jobscan.com/v1/resumes/match"

# Make the resume matching request
headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

data = {
    "resume": {
        "content": "YOUR_RESUME_CONTENT"
    }
}

response = requests.post(RESUME_MATCHING_URL, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 200:
    # The resume matching was successful
    results = response.json()
    print("Resume matched successfully")
    print("Match score:", results["match_score"])
else:
    # The resume matching failed
    print("Resume matching failed")
