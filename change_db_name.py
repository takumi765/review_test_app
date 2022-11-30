with open('./config/settings.py') as reader:
    content = reader.read()
    
content = content.replace('db.sqlite3', 'review_test_db.sqlite3')

with open('./config/settings.py', 'w') as writer:
    writer.write(content)
