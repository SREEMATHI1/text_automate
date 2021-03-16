import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good Morning! Sarvam Krishnarpanam <3",
    "Good Morning Cheemy! You're born to win all the battles you step in <3",
    "You'll have a great day today, Jai Shreeman Narayana!!",
    "I know you will slay the day"
]

#messages of your choice
GOOD_EVENING_QUOTES = [
    "Good Evening! Jai Shreeman Narayana",
    "Sarvam Krishnaarpanam!",
    "Goodnight sweetie, dream about the beauty of our relationship - Your KannaPaapa!",
    "Love you! I hope you dream about me tonight-yours kannakutty <3"
]


def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = "AC8ea71fe8fe7fc84399531cc311a4c29d"
    token = "e7901e863f37611fce9eb7ac74f045ac"
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


schedule.every().day.at("10:58").do(send_message, GOOD_MORNING_QUOTES)

# send a message in the evening
schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)

# testing
schedule.every().day.at("13:55").do(send_message, GOOD_EVENING_QUOTES)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
