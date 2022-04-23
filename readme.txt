send_email.py will send you an email everyday of the current mortgage rates listed on MortgageNewsDaily.com and market data from Yahoo Finance.

You will need an email address to send from and one to receive the email although they can be the same. The email address(es) and password to the sender's email account should be stored as environment varibles on your system.

Varibles should be saved with the below names:
sender_email_address
email_password
receiver_email_address

The script should be set to run daily between 22:00 and 23:59 GMT. On Linux, it is easiest to execute a bash script containing the environment varibles and send_email.py script. send_email.sh is an example bash script.

To schedule this file to run type `crontab -e' in the terminal and add a cron job like the below example:
0 15 * * * /path/send_email.sh

You can add or remove tickers from in the conf.py file. You can also change perform_get_mortgage_data or perform_get_market_data to False if you do not want to receive one.
