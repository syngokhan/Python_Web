import os
import datetime
import pytz
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.envrion.get("DATABASE_URI"))

user_timezone = pytz.timezone("Europe/London")

with connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM posts;")
        for post in cursor:
            _id, content, timestamp = post
            naive_datetime = datetime.datetime.utcfromtimestamp(timestamp)
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(user_timezone)
            print(local_date)
            print(content)