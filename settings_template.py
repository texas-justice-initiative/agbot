DATADOTWORLD = {
    'api_key': 'MY_SECRET_KEY',
    'dataset_slug': 'OWNER/DATASET',
}

# Emails must be sent from a gmail account
EMAIL = {
    'from': 'EMAIL_FROM@gmail.com',
    'to': ['ADDRESS_1@gmail.com', 'ADDRESS_2@gmail.com'],
    'gmail_password': 'SUPER_DUPER_SECRET',
}

GSHEETS = {
    # json generated during service account key creation
    # https://console.developers.google.com/apis/credentials
    # In the Google sheet: share with the 'client_email' and grant 'edit' rights
    'auth_params': {
        'type': 'service_account',
        'project_id': '',
        'private_key_id': '',
        'private_key': '',
        'client_email': '',
        'client_id': '',
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
        'client_x509_cert_url': '',
    },
    'sheet_id': 'GOOGLE_SPREADSHEET_ID',
}
