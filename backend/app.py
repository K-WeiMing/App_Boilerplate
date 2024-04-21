from flask import Flask, request, make_response
from flask_cors import CORS
from sqlalchemy import text, Connection


import sqlalchemy_engine

app = Flask(__name__)

# Initialize DB connection
try:
    conn = sqlalchemy_engine.conn_db(
        username="admin",
        password="password",
        host="<docker service name, else 127.0.0.1",
        port=5432,
        db_name="your_db_name",
    ).connect()
except:
    print("Unable to connect to DB")
    raise Exception("DB Connection Error)")


@app.route("/get", methods=["GET"])
def example_api():
    if request.method == "GET":
        return make_response({"GET": "Request is working"})


@app.route("/post", methods=["GET"])
def example_api():
    if request.method == "POST":
        return make_response({"POST": "Request is working"})


@app.route("/db_query", methods=["GET"])
def example_query_db():
    conn = sqlalchemy_engine.conn_db(
        username="username",
        password="password",
        host="<docker service name, else 127.0.0.1",
        port=5432,  # Default port for postgres
        db_name="your_db_name",
    ).connect()

    SAMPLE_SQL = f"""
    SELECT * 
    FROM DB
    """

    result = conn.execute(text(sqlalchemy_engine.format_query(SAMPLE_SQL)))

    res = result.fetchall()

    print(res)


if __name__ == "__main__":
    app.run()
