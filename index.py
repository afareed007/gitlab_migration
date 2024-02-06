from dotenv import load_dotenv
import os
import gitlab

load_dotenv()

# Configuration from .env file
SOURCE_GITLAB_URL = os.getenv('SOURCE_GITLAB_URL')  # Replace with your GitLab instance URL from .env
PERSONAL_ACCESS_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')  # Replace with your personal access token from .env

# Initialize GitLab
gl = gitlab.Gitlab(SOURCE_GITLAB_URL, private_token=PERSONAL_ACCESS_TOKEN)

# Fetch and display groups
try:
    groups = gl.groups.list(all=True)  # Fetches all groups
    for group in groups:
        print(f"Group ID: {group.id}, Name: {group.name}")

except Exception as e:
    print(f"An error occurred: {e}")
