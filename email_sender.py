import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Buddy Love'
email['to'] = 'XXXX'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('XXXX', 'XXXX')
    smtp.send_message(email)
    print('All good.')