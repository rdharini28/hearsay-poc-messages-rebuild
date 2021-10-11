import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "dev-message-poc.cluster-cbtpcemj4cis.us-west-2.rds.amazonaws.com")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "placeholder")
    user = os.environ.get("DB_USER", "placeholder")
    db_name = os.environ.get("DB_NAME", "messages")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "0.0.0.0")
    port = 5000 if host == "localhost" else 80
    return f"http://{host}:{port}"