import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = psycopg2.connect(
            database=os.getenv("database"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )

        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "delete", "update", "create"]
        if query in data:
            database.commit()
            if query_type == "insert":
                return "Inserted data"

            elif query_type == "delete":
                return "Deleted data"

            elif query_type == "update":
                return "Updated data"

            elif query_type == "create":
                return "Created"

        else:
            return cursor.fetchall()
