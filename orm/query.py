import psycopg2
import psycopg2.extras
import json


class Connection:
    def __init__(self):
        self.con = psycopg2.connect(database="musicstore",
                                    user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432")

    def close(self):
        self.con.close()


class Query:
    def __init__(self, connection: Connection, query_string):
        self.connection = connection
        self.query_string = query_string
        self.cursor = self.connection.con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.results = []

    def execute(self):
        self.cursor.execute(self.query_string)

    def execute_no_return(self):
        cursor = self.connection.con.cursor()
        cursor.execute(self.query_string)
        self.connection.con.commit()

    def fetch_results(self):
        rows = self.cursor.fetchall()
        for row in rows:
            self.results.append(dict(row))
        return self.results

    def run(self):
        self.execute()
        return self.fetch_results()

    def json_results(self):
        if not self.results:
            self.execute()
            self.fetch_results()
        return json.dumps(self.results)