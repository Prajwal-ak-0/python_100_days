import smtplib
import datetime as dt
import random
import os

DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

f = open("quotes.txt", "r")
quotes = f.readlines()
rand_ind = random.randint(0, len(quotes) - 1)
q = quotes[rand_ind]

date = dt.datetime.now()
day = date.weekday()
hr = date.hour
mn = date.min
sec = date.second

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

if DAY[day] == "Sunday":
    my_email = "amaangupta45@gmail.com"
    password = "fsbugdfhxyxkyltl"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="prajwalhassan7@gmail.com",
        msg=f"Subject: Morning Quote\n\n {q}"
    )
    connection.close()
