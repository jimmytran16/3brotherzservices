
import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime, timedelta

def send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version):
    sender_email = sender_email
    company_email = company_email
    password = password
    today_date = datetime.today().strftime('%m-%d-%y')
    #check for contact type (either quote or contact) --
    if version == 1:
    #str that contains all of the body
        subject_field = "QUOTE REQUESTED {}".format(today_date)
    else:
        subject_field = "CONTACT FORM {}".format(today_date)
    body = "<tr><td><p>Name:</p></td><td><p>{}</p></td></tr><tr><td><p>Email:</p></td><td><p>{}</p></td></tr><tr><td><p>Phone:</p></td><td><p>{}</p></td></tr><tr><td><p>Message:</p></td><td><p>{}</p></td></tr>".format(_name,_email,_phone,_message)    
    # body = _message
    print(body)
    # Create the plain-text and HTML version of your message
    text = """\
    This is a test email!!
    """
    html = """\
    <table>
    """+body+"""
    </table>"""

    print(html)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    print(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        try:
            message = MIMEMultipart("alternative")
            message["Subject"] = subject_field
            message["From"] = sender_email
            message["To"] = company_email

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
            server.sendmail( #send the email
                sender_email, company_email, message.as_string()
            )
            # print(f'Success send email to {company_email}')
        except Exception as error:
            print(error)
            # print(f'Fail to send email to {company_email}')
