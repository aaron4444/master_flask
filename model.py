from main import db

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username= db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username
    def __repl__(self):
        return "<User '{}'>".format(self.username) 
