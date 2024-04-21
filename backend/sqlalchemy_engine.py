import sqlalchemy
from sqlalchemy.engine import URL
from sqlalchemy import create_engine


def conn_db(
    username: str,
    password: str,
    host: str,
    db_name: str,
    port: int = 5432,
    drivername: str = "postgresql",
) -> sqlalchemy.Engine:
    """
    Generates an sqlalchemy.engine object to connect to the Database

    Args:
        username (str): login username
        password (str): password of user
        host (str): host ip "0.0.0.0"
        db_name (str): database name
        port (int, optional): port number. Defaults to 5432 (postgres)
        drivername (str, optional): db driver to use. Defaults to "postgresql".

    Returns:
        sqlalchemy.Engine: Engine object to perform queries
    """
    url = URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=db_name,
    )
    engine = create_engine(url)
    return engine


def format_query(sql: str) -> str:
    """
    Formats the query to remove linebreaks and empty spaces when using
    triple-quoted f-strings

    Args:
        sql (str): sql query

    Returns:
    str: formatted sql query
    """
    return " ".join([line.strip() for line in sql.splitlines()]).strip()
