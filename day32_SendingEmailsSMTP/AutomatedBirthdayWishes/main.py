import datetime as dt
import pandas
import random
import smtplib
my_email = "katalystcoding@gmail.com"
password = "Coding2022Fun!"

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in birthdays.iterrows()}

now = dt.datetime.now()
today_tuple =(now.month, now.day)
if today_tuple in birthdays_dict:
    print("WOOT")
    birthday_person = birthdays_dict[today_tuple]
    file_path = (f"letter_templates/letter_{random.randint(1,3)}.txt")
    with open(file_path) as template:
        template_data = template.read()
        template_data = template_data.replace("[NAME]", birthday_person["name"])
        print(template_data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n {template_data}"
        )

        ##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



