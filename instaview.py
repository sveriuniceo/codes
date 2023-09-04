from instagram_private_api import (
    Client, ClientCompatPatch, ClientError, ClientLoginRequiredError
)

# Replace with your own Instagram username and password
username = 'your_username'
password = 'your_password'

# Authenticate with the Instagram API
api = Client(username, password)
api.login()

# Get your own Instagram user ID
user_id = api.authenticated_user_id

# Get your own Instagram profile statistics
user_stats = api.user
