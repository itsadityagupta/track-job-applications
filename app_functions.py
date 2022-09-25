def get_conn_string(db_path: str):
    """Generate a connection string for the database"""
    return "sqlite:///" + db_path
