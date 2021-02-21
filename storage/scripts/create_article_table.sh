#!/bin/sh

sqlite3 ../../db.sqlite3 <<'END_SQL'
.timeout 2000
DROP TABLE IF ExISTS articles;
CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  url TEXT NOT NULL,
  header TEXT NOT NULL,
  date TEXT NOT NULL,
  authors TEXT NOT NULL,
  tags TEXT NOT NULL,
  category TEXT NOT NULL,
  sections TEXT NOT NULL,
  html TEXT NOT NULL,
  preview_html TEXT NOT NULL,
  js TEXT NOT NULL,
  css TEXT NOT NULL
);
END_SQL
