from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)
#db = SQLAlchemy(app)



@app.route('/')
def home():
    return '<h1>Hello Batya</h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0')
