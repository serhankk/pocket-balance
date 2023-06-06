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
        query = "create table if not exists " + table_name + " (id INTEGER PRIMARY KEY, name CHAR, category CHAR, amount INT, spending BOOL)"
        self.cursor.execute(query)

    def create_registery(self, name, category, amount, spending):
        query = f"""INSERT INTO {self.table_name} (name, category, amount, spending) VALUES ('{name}', '{category}', {amount}, {spending})"""
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_entries(self):
        query = f""" SELECT * FROM {self.table_name};"""
        self.cursor.execute(query)
        all_entries = self.cursor.fetchall()
        data = []
        for entry in all_entries:
            data.append({"id": entry[0], "name": entry[1], "category": entry[2], "amount": entry[3], "spending": entry[4]})
        return data
    

class AccountUtil(DBUtil):
    def create_spending(self, name, category, amount):
        self.create_registery(name, category, amount, True)

    def create_incoming(self, name, category, amount):
        self.create_registery(name, category, amount, False)
    


x = AccountUtil("../db.sqlite3", "test_table")
print(x.create_spending("xbox", "elektronik", 12200))

print(x.get_all_entries())
