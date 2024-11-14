import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Authentication function
def authenticate():
    # Specify the required scopes
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Load credentials from client_secret.json (downloaded from Google Cloud)
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)
    credentials = flow.run_local_server(port=0)

    # Save or refresh token for long-term usage
    return build("youtube", "v3", credentials=credentials)
