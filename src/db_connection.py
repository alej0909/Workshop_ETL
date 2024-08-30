from decouple import config, UndefinedValueError
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def build_engine():
    try:
        dialect = config('PGDIALECT')
        user = config('PGUSER')
        passwd = config('PGPASSWD')
        host = config('PGHOST')
        port = config('PGPORT')
        db = config('PGDB')
    except UndefinedValueError as e:
        print(f"Missing environment variable: {e}")
        raise

    database_url = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"

    try:
        engine = create_engine(database_url)
        print(f"Successfully connected to the database {db}!")
        return engine
    except SQLAlchemyError as e:
        print(f"Failed to connect to the database: {e}")
