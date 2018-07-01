from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('reports_id_seq'::regclass)"))
    type = db.Column(db.Text, nullable=False)
