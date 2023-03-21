import smtplib
import random
import argparse


# defined command line options
parser=argparse.ArgumentParser()

if __name__ == "__main__":
    # create a names list argument
    parser.add_argument(
        "--names",  # name on the CLI - drop the `--` for positional/required parameters
        nargs="*",  # 0 or more values expected => creates a list
        type=str,
        help = "provide a list of people's names who participate in the Secret Santa draw. Commas for separation aren't necessary"
     )

    # create a list of the respective e-mails of people listed in the "names" list. 
    # both "names" and "emails" lists need to be in the same order and of the same length.
    parser.add_argument(
    "--emails",
    nargs="*",
    type=str,
    help = "provide their email addresses exactly in the same order as their names. Commas for separation aren't necessary"  
    )

    # create an argument for the your/sender's email (e.g. ""santaclaus@gmail.com"")
    parser.add_argument(
        "--email",
        help="provide your email address where to send the information to participants from",
        type=str
    )

    # create an argument for your/sender's email password
    parser.add_argument(
        "--password",
         help="provide your email password",
         type=str
    )

    # parse the command line
    args = parser.parse_args()


    names = args.names
    emails = args.emails

    my_email = args.email
    password = args.password

    names1 = names.copy()

    # Function to shuffle the "names1" list which is a copy of "names" list
    def shuffler(a,b,c):
        random.shuffle(c)
        list_of_tuples = list(zip(a, b, c))
        return list_of_tuples

    list_of_tuples = shuffler(names, emails, names1)


    # Function to check if items in the list "names1" don't match the order in the "names" list:
    def checker(list_to_check):
        m = []
        for i in list_to_check:
            if i[0] != i[2]:
                m.append(False)
            elif i[0] == i[2]:
                m.append(True)
        return m

    m = checker(list_of_tuples)



    # Function to send out the emails to addressees 
    def sendout_emails(my_email, password, list_of_tuples):
        for i in list_of_tuples:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user = my_email, password = password)
                connection.sendmail(
                    from_addr = my_email, 
                    to_addrs = i[1], 
                    msg = f"Subject: Secret Santa draw for CaunceMass\n\n Dear, {i[0]} \n\n I'm addressing you to inform that I've decided to delegate you to be a secret Santa to {i[2]} this year. \n Think how you could make them happy. That would make my life so much easier! Many thanks! ;) \n\n Faithfully yours, Santa Claus XOXOXO"
                    )
    if any(m) == False:
        print("No dupes from the first instance")
        sendout_emails(my_email, password, list_of_tuples)
    else:
        while any(m) == True:
            list_of_tuples = shuffler(names, emails, names1)
            m = checker(list_of_tuples)
        print("Needed reshuffling but here it is:")
        sendout_emails(my_email, password, list_of_tuples)
        













