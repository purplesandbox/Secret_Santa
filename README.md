# Description of the app
An app that randomizes the list of Secret Santa draw participants, checks if the same person isn't the giver and recipient, and sends out a lovely message to participants informing them about their Secret Santa mission.  All discreetly and seamlessly. Only recipients of the email know their special person to provide a gift for.

The app makes use of the smtplib Python library (https://docs.python.org/3/library/smtplib.html) to send e-mails. Various e-mail service providers could be used for this purpose (e.g. yahoo, gmail, etc..). It is advisable to create a new e-mail account with your chosen e-mail services provider as you might need to lower security settings to allow apps to use their email services to send messages. This script uses gmail as host for Simple Mail Transfer Protocol connection ("smtp.gmail.com"). It needs to be changed depending on the host of email services.  

Important e-mail account settings to run this app
If you stick to gmail email services, please, mind the following: Since May 30, 2022, google has removed "Allow unsecure apps options". So now you need to follow these email account set-up steps to allow to send emails through apps:

Go to "Google Accounts" Page (Manage your Google Account> Security > Signing in to Google)
Set up and Turn on the 2-step verification process.
In the same "Signing in to Google" Section, click "App passwords" and select "Other apps" from the app menu and generate a unique password that you will use for this script (the regular e-mail password won't work for this script).
How to run this app
You would need to provide positional arguments: --names --emails --email --password

# An example of how it might look like:

python main.py --names Ellie Bob Pink --emails ellie@gmail.com Bob@yahoo.com Pink@hotmail.co.uk --email secretsanta2022@gmail.com password -- jhjgsdgshdg

Mind to provide emails of people in the exact order as their names!
Merry Christmas! 
