import pandas as pd
import smtplib
import random
import datetime as dt

my_email = "random@gmail.com"
password = "totijbrfwpjzrjjp"

now = dt.datetime.now()
day = now.day
month = now.month
# print(date)
# print(month)

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
data = pd.read_csv("birthdays.csv")

for _ in range(len(data)):
    if data["month"][_] == month and data["day"][_] == day:
        recipient_email = data["email"][_]
        recipient_name = data["name"][_]

        choose_letter = random.choice(letter_list)
        try:
            with open(f"letter_templates/{choose_letter}") as letter_file:
                letter_format = letter_file.read()
                new_letter_format = letter_format.replace("[NAME]", recipient_name)
                # print(new_letter_format)
        except FileNotFoundError:
            print("Letter template file doesn't exist")
            continue

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                                    msg=f"Subject:Happy Birthday!\n\n{new_letter_format}")
                print(f"Birthday letter sent to {recipient_name}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}. Error: {e}")
