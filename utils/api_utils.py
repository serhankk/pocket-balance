#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
import db_utils

app = FastAPI()
my_db = db_utils.DBUtil("../db.sqlite3", "test_table")

class Entry(BaseModel):
    name: str
    category: str
    amount: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/allEntries")
async def read_item():
    return my_db.get_all_entries()

@app.post("/newEntry")
async def create_entry(item: Entry):
    my_db.create_registery(item.name, item.category, item.amount)
    return item