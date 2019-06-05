# !/usr/bin/env python3
import argparse
import json
import os
import sys

import smtp
from message import Message
from smtp import SMTP, SMTP_PORT, SMTP_SERVER

FROM = "From"
RECEIVERS = "To"
TEXT = "Text"
SUBJECT = "Subject"
ATTACHMENTS = "Attachments"
INPUT = "input.json"


def main():
    smtp_con = SMTP(SMTP_SERVER, SMTP_PORT)
    print(smtp_con.connect())
    send_mail(smtp_con, INPUT)


def send_mail(smtp_con, settings_file):
    with open(settings_file, 'r', encoding=smtp.ENCODING) as f:
        config = json.loads(f.read())
    sender = config[FROM]
    receivers = config[RECEIVERS]
    subject = config[SUBJECT]
    attachments = config[ATTACHMENTS]
    with open(config[TEXT], 'r', encoding=smtp.ENCODING) as f:
        text_lines = f.readlines()
    message = Message(sender, receivers, subject, text_lines, attachments)
    email = message.get_email()
    print(smtp_con.ehllo())
    print(smtp_con.auth())
    print(smtp_con.mail_from(sender))
    for receiver in receivers:
        print(smtp_con.rcpt_to(receiver))
    print(smtp_con.data())
    print(smtp_con.send(email))
    print(smtp_con.quit())


if __name__ == '__main__':
    sys.exit(main())
