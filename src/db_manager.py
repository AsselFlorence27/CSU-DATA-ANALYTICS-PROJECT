# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import os

class CSUDatabaseManager:
    """Manages SQLite database operations for the project."""
    
    def __init__(self, db_path="data/processed/csu_analytics.db"):
        self.db_path = db_path
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def load_table(self, df, table_name):
        """Loads a dataframe into the SQLite database."""
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            return f"Loaded {len(df)} rows into {table_name}."

    def query_to_df(self, query):
        """Executes a query and returns a dataframe."""
        with sqlite3.connect(self.db_path) as conn:
            return pd.read_sql(query, conn)

    def get_summary(self):
        """Returns a summary of tables in the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            summary = {}
            for table in tables:
                t_name = table[0]
                cursor.execute(f"SELECT COUNT(*) FROM {t_name}")
                summary[t_name] = cursor.fetchone()[0]
            return summary
