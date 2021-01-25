# from Google import Create_Service
# import base64
# import os
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
import os
os.chdir("C:/Users/Any1/Desktop/ecommerce-project/store")

# CLIENT_SECRET_FILE = 'client_secret.json'
# API_NAME = 'gmail'
# API_VERSION = 'v1'
# SCOPES = ['https://mail.google.com/']
#
# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# emailMsg = 'You won $100,000'
# mimeMessage = MIMEMultipart()
# mimeMessage['to'] = '<l.mihaly>@outlook.com'
# mimeMessage['subject'] = 'You won'
# mimeMessage.attach(MIMEText(emailMsg, 'plain'))
# raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
#
# message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
# print(message)

# import os
# print(os.getcwd())
