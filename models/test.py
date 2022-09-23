from __init__ import db

class Tests(db.Model):
	__tablename__ = 'tests'
	id = db.Column(db.Integer, primary_key = True)
	questions = db.Column(db.String(255), nullable=False)
	answer = db.Column(db.String(255), nulltable=False)
	correct_ans = db.Column(db.Integer(100))
	false_ans = db.Column(db.Integer(100))
	false_series = db.Column(db.Integer(50))
