#!/usr/bin/env python3
"""
Logging data and hiding PII data from database
"""

import logging
import re
from os import getenv
from typing import List, Tuple

import mysql.connector

PII_FIELDS: Tuple[str, str, str, str, str] = (
    "name",
    "email",
    "phone",
    "ssn",
    "password"
)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate some fields of a string

    Args:
        fields (List[str]): Fields for obfuscate
        redaction (str): Obfuscated chars
        message (str): Message to obfuscate
        separator (str): Field separator on message

    Return:
        str -> A copy of the string obfuscated
    """
    for field in fields:
        message = re.sub("{}=(.*?){}".format(field, separator), "{}={}{}"
                         .format(field, redaction, separator), message)
    return message


def get_logger() -> logging.Logger:
    """
    The logger should be named "user_data" and
    only log up to logging. INFO level.

    It should not propagate messages to other loggers.
    It should have a StreamHandler with RedactingFormatter as formatter.

    Returns:
    logging.Logger: New logger
    """
    new_logger: logging.Logger = logging.getLogger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False

    new_stream_handler: logging.StreamHandler = logging.StreamHandler()
    new_stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    new_logger.addHandler(new_stream_handler)

    return new_logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record object using FORMAT

        Args:
        record (logging.LogRecord): LogRecord Object to get format

        Returns:
        str: The message of the record with self.FORMAT
        """
        logging.basicConfig(format=self.FORMAT, level=logging.INFO)

        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to MySQL database

    Returns:
        mysql.connector.connection.MySQLConnection: MySQLConnection instance
    """

    try:
        connection = mysql.connector.connect(
            host=getenv("PERSONAL_DATA_DB_HOST") or "localhost",
            user=getenv("PERSONAL_DATA_DB_USERNAME") or "root",
            password=getenv("PERSONAL_DATA_DB_PASSWORD") or "",
            database=getenv("PERSONAL_DATA_DB_NAME") or ""
        )
    except mysql.connector.Error as error:
        print("Error to connect to DB", error)
        exit()

    return (connection)


def main() -> None:
    """
    Retrieve all rows in the users table and
    display each row under a filtered format.
    """
    fields = ["name", "email", "phone", "ssn",
              "password", "ip", "last_login", "user_agent"]
    db_connection = get_db()
    logger = get_logger()

    cursor = db_connection.cursor()
    cursor.execute("""SELECT name, email, phone, ssn,
                   password, ip, last_login, user_agent FROM users""")

    rows = cursor.fetchall()

    for row in rows:
        msg = ''
        for k, v in zip(fields, row):
            msg += '{}={}; '.format(k, v)
        logger.info(msg)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    main()
