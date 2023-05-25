#!/usr/bin/env python3

import sqlite3
import json

class DBUtil:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self.connection = self.make_connection()
        self.cursor = self.sqlite_cursor()
        self.create_table_if_not_exists(table_name)

    def make_connection(self):
        connection = sqlite3.connect(self.db_path)
        return connection
    
    def sqlite_cursor(self):
        cursor = self.connection.cursor()
        return cursor
    
    def create_table_if_not_exists(self, table_name):
        query = "create table if not exists " + table_name + " (name CHAR, category CHAR, amount INT)"
        self.cursor.execute(query)

    def create_registery(self, name, category, amount):
        query = f"""INSERT INTO {self.table_name} VALUES ('{name}', '{category}', {amount})"""
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_entries(self):
        query = f""" SELECT * FROM {self.table_name};"""
        self.cursor.execute(query)
        all_entries = self.cursor.fetchall()
        data = []
        for entry in all_entries:
            data.append({"name": entry[0], "category": entry[1], "amount": entry[2]})
        return data


# my_db = DBUtil("../db.sqlite3", "test_table")
# print(my_db.get_all_entries())
