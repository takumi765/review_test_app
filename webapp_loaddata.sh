#!/bin/bash
python manage.py migrate && python manage.py loaddata db_sqlite3_dump.json
