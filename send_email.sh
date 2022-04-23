#!/bin/bash

export receiver_email_address=email@example.com
export sender_email_address=email@example.com
export email_password=password

python3 /path/send_email.py 2>&1 >> /var/log/send_email.log
date >> /var/log/send_email.log
echo "Job Complete" >> /var/log/send_email.log
