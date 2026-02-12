from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# initialize flask application
app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

from models import Machine

@app.route("/")
def index():
    return jsonify({'message': 'Welcome to Flask'})

@app.route("/machines", methods=["GET"])
def machines():
    machines = Machine.query.all()
    return jsonify([machine.as_dict() for machine in machines])

@app.route("/machines/<int:machine_id>", methods=["GET"])
def machine(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    return jsonify(machine.as_dict())

@app.route("/machines", methods=["POST"])
def create_machine():
    data = request.get_json()
    machine = Machine(
        name=data['name'],
        ip_address=data['ip_address'],
        mac_address=data['mac_address'],
        status=data['status'],
        uptime=data['uptime'],
        load_average=data['load_average']
    )
    db.session.add(machine)
    db.session.commit()
    return jsonify(machine.as_dict()), 201  

@app.route("/machines/<int:machine_id>", methods=["PUT"])
def update_machine(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    data = request.get_json()
    machine.name = data['name']
    machine.ip_address = data['ip_address']
    machine.mac_address = data['mac_address']
    machine.status = data['status']
    machine.uptime = data['uptime']
    machine.load_average = data['load_average']
    db.session.commit()
    return jsonify(machine.as_dict())

@app.route("/machines/<int:machine_id>", methods=["DELETE"])
def delete_machine(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    db.session.delete(machine)
    db.session.commit()
    return jsonify({'message': 'Machine deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5100)
