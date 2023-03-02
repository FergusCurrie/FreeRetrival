#!/bin/bash


sqlite3 -batch free_retrival.db """CREATE TABLE retrivals (
    id INTEGER PRIMARY KEY,
    card_id INTEGER,
    score INTEGER,
    date DATE DEFAULT CURRENT_DATE
);"""

sqlite3 -batch free_retrival.db """CREATE TABLE cards (
    card_id INTEGER PRIMARY KEY,
    file_name TEXT,
    card_header TEXT
    date DATE DEFAULT CURRENT_DATE
);"""



