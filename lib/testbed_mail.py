#!/usr/bin/python3

import os, sys
import smtplib


MSG_SUCC = """From: LOG-a-TEC testbed
To: %s <%s>
Subject: Testbed resource reservation 

Hello %s!
Your reservation request for LOG-a-TEC testbed was accepted by the server.
We kindly ask to wait for admin conformation.

Technology: %s
Reserved from: %s
Until:  %s

This message was automatically generated by the LOG-a-TEC server - please do not reply.
"""

MSG_CONF = """From: LOG-a-TEC testbed
To: %s <%s>
Subject: Testbed resource reservation

Hello %s!
Your reservation request for LOG-a-TEC testbed was confirmed by the LOG-a-TEC testbed admin.
For any information please do not hesitate to contact us!

Technology: %s
Reserved from: %s
Until:  %s

This message was automatically generated by the LOG-a-TEC server - please do not reply.
"""

MSG_WARN = """From: LOG-a-TEC testbed
To: %s <%s>
Subject: Testbed resource reservation

Hello %s!
Your reservation for LOG-a-TEC testbed resources will end in one hour!
If you wish to continue, please make a request for new resource reservation.

Thank you for using our services.

This message was automatically generated by the LOG-a-TEC server - please do not reply.
"""#%(username, user_mail, username)




#_testbed_email = os.environ.get("EMAIL")
#_testbed_pwd = os.environ.get("PASSWORD")

_testbed_email = "email"
_testbed_pwd = "password"
try:
    message_type = sys.argv[1]
    receiver_name = sys.argv[2]
    receiver_mail = sys.argv[3]
    resource_start = sys.argv[4]
    resource_end = sys.argv[5]
    resource_type = sys.argv[6]
except:
    sys.exit()


# Check input request
if(message_type == "reservation_confirmed"):
    message = MSG_CONF%(receiver_name, receiver_mail, receiver_name, resource_type, resource_start, resource_end)
elif(message_type == "reservation_success"):
    message = MSG_SUCC%(receiver_name, receiver_mail, receiver_name, resource_type, resource_start, resource_end)
else:
    sys.exit()

# Send mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.ehlo()
    server.login(_testbed_email, _testbed_pwd)
    server.sendmail(_testbed_email, receiver_mail, message)
    server.close()