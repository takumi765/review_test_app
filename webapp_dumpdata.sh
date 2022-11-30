#!/bin/bash
python -Xutf8 manage.py dumpdata -o db_sqlite3_dump.json --indent 2 --format json && python change_db_name.py