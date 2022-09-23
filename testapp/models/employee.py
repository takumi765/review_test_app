from testapp import db
from datetime import datetime


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)  # システムで使う番号
    name = db.Column(db.String(255))  # 社員名
    mail = db.Column(db.String(255))  # メール
    is_remote = db.Column(db.Boolean)  # リモート勤務しているか
    department = db.Column(db.String(255))  # 部署
    year = db.Column(db.Integer, default=0)  # 社歴
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時