
import pandas
import smtplib
import random
import datetime

email = "mrafay280@gmail.com"
password = "gwcboacfvpjmdray"


file_data = pandas.read_csv("D:/Python/Happy Birthday Wisher/birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): {"name": row["name"], "email": row["email"]} for (index, row) in
                  file_data.iterrows()}

today = datetime.datetime.now()
today_month = today.month
today_day = today.day

for birthdate in birthdays_dict:
    if (today_month, today_day) == birthdate:
        choice = random.randint(1, 3)
        with open(f"D:/Python/Happy Birthday Wisher/letter_templates/letter_{choice}.txt") as letter:
            letter_content = letter.read()
            letter_content = letter_content.replace('[NAME]', birthdays_dict[birthdate]["name"])
            print(letter_content)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(email, birthdays_dict[birthdate]["email"],
                                f"Subject: HEY HAPPY BIRTHDAYYY\n\n{letter_content}")
