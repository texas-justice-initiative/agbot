# Not used at this time, feel free to ignore
DOCUMENT_CLOUD = {
    'email': 'EMAIL_ADDRESS',
    'password': 'SUPER_SECURE_PASSWORD',
}

EMAIL = {
    'from': 'EMAIL_FROM@domain.com',
    'to': ['ADDRESS_1@domain.com', 'ADDRESS_2@domain.com'],

    'account_password': 'SUPER_DUPER_SECRET',
    'server_address': 'smtp.mailgun.org',
    'server_port': 587,
}

GSHEETS = {
    # Json generated during service account key creation:
    # https://console.developers.google.com/apis/credentials
    #
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
}
