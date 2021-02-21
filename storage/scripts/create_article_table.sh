#!/bin/sh

sqlite3 ../../db.sqlite3 <<'END_SQL'
.timeout 2000
DROP TABLE articles;
CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  header TEXT NOT NULL,
  date TEXT NOT NULL,
  authors TEXT NOT NULL,
  tags TEXT NOT NULL,
  sections TEXT NOT NULL,
  html TEXT
);
END_SQL
