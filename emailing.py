import smtplib
import imghdr
# note 'imghdr' is deprecated and slated for removal in Python 3.13
import os
from email.message import EmailMessage

PASSWORD = os.getenv("EMAIL_PASSWORD")
SENDER = "youremailaddr@gmail.com"
RECEIVER = "youremailaddr@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Motion detected!"
    email_message.set_content("Hey, we just captured an image on the security camera.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    # subtype=imghdr.what(None, content)
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    finished = 1
    return finished

if __name__ == "__main__":
    send_email(image_path="images/19.JPG")
