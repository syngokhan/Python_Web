from typing import List,Tuple
from contextlib import contextmanager

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls 
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""

CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls (id));"""

CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes 
(username TEXT, option_id INTEGER, vote_timestamp INTEGER, FOREIGN KEY(option_id) REFERENCES options (id));"""


SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL = "SELECT * FROM polls WHERE id = %s;"
SELECT_POLL_OPTIONS = """SELECT * FROM options
WHERE polls_id = %s;"""

SELECT_LATEST_POLL = """SELECT * FROM polls
WHERE polls.id = (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
);"""

SELECT_OPTION = "SELECT * FROM options WHERE id = %s;"
SELECT_VOTES_FOR_OPTION = "SELECT * FROM votes WHERE option_id = %s"

INSERT_POLL_RETURN_ID = "INSERT INTO polls (title,owner_username) VALUES  (%s, %s) RETURNING id;"
INSERT_OPTION_RETURN_ID = "INSERT INTO options (option_text, poll_id) VAUES (%s,%s) RETURNING id;" 
INSERT_VOTE = "INSERT INTO votes (username,option_id,vote_timestamp) VALUES (%s,%s,%s);"

@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor

def create_tables(connection):
    with get_cursor(connection) as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)
 
# --- Polls ---- #
def create_poll(connection, title : str, owner : str ):
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_POLL_RETURN_ID,(title,owner))

            poll_id = cursor.fetchone()[0]
            return poll_id

Poll = Tuple[int,str,str]
def get_polls(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()

def get_poll(connection,poll_id) -> Poll:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_POLL,(poll_id,))
            return cursor.fetchone()

def get_lastest_poll(connection) -> Poll:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchone()

Option = Tuple[int, str, int]
def get_poll_options(connection,poll_id : int) -> List[Option]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
            return cursor.execute()

# --- options --- #
def get_option(connection,option_id : int) -> Option:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_OPTION, (option_id,))
            return cursor.fetchone()

def add_option(connection, option_text, poll_id: int):
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_OPTION_RETURN_ID, (option_text,poll_id,))
            option_id = cursor.fetchone()[0]
            return option_id

# --- vote --- #
Vote = Tuple[str,int]
def get_votes_for_option(connection,option_id : int) -> List[Vote]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_VOTES_FOR_OPTION, (option_id,))
            return cursor.fetchall()


def add_poll_vote(connection,username : str, vote_timestamp : float, option_id : int):
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_VOTE,( username, option_id, vote_timestamp))    