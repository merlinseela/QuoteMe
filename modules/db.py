"""
This module contains a variety of functions to connect to a database and perform operations on it.
"""

def create_table(cursor, table_name:str, columns: dict) -> None:
    """
    Creates a table in the database with a specified name and columns. WARNING: This function will not return an error if the table already exists. However, it will not create a new table if the table already exists.
    Args:
        cursor: The database cursor to execute the SQL command
        table_name (str): The name of the table to create
        columns (dict): A dictionary where keys are column names and values are their data types. Each entry in the dictionary has to look like this: {"<column_name>": "<data_type>"}.
    Raises:
        ValueError: If the columns dictionary is empty
    """
    if not columns:
        raise ValueError("Columns dictionary cannot be empty")

    column_str = ", ".join([f"{column_name} {data_type}" for column_name, data_type in columns.items()])
    
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_str}
        );
        """
    )

def create_entry(cursor, table_name:str, entry: dict) -> None:
    """
    Inserts an entry into a specified table in the database.
    Args:
        cursor: The database cursor to execute the SQL command
        table_name (str): The name of the table to insert the entry into
        entry (dict): A dictionary where keys are column names and values are their corresponding values to be inserted.
    Raises:
        ValueError: If the entry dictionary is empty
    """
    if not entry:
        raise ValueError("Entry dictionary cannot be empty")

    columns = ", ".join(entry.keys())
    values = ", ".join([f"'{value}'" for value in entry.values()])
    
    cursor.execute(
        f"""
        INSERT INTO {table_name} ({columns}) VALUES ({values});
        """
    )