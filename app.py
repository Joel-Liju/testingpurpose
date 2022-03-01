from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tp.db'
db = SQLAlchemy(app)

class Info(db.Model):
    __tablename__='data'
    name = db.Column(
      db.String(8),
      primary_key=True
    )
    age = db.Column(
      db.String(8)
    )
    
    def __repr__(self):
      return self.name+" "+self.age
    

db.create_all()

@app.route('/')
def tester():
  return "<h1> Hello world!</h1>"+str(Info.query.all()))

if __name__ == "__main__":
  app.run()
