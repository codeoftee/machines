from app import db
from app import app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))

    def __repr__(self):
        return f'<User {self.username}>'


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ip_address = db.Column(db.String(120), unique=True, nullable=False)
    mac_address = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)
    uptime = db.Column(db.String(120), nullable=False)
    load_average = db.Column(db.String(120), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ip_address': self.ip_address,
            'mac_address': self.mac_address,
            'status': self.status,
            'uptime': self.uptime,
            'load_average': self.load_average
        }

    def __repr__(self):
        return f'<Machine {self.name}>'
