Python Flask REST API for Machine Management

This project is a simple REST API built with Flask and SQLAlchemy for managing machines.

Features

List all machines
Get a specific machine by ID
Create a new machine
Update an existing machine
Delete a machine
Prerequisites

Python 3.10+

Installation

Clone the repository:

git clone <repository-url>

cd cloud

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the development server:

flask run --port 5100

The API will be available at http://localhost:5100

API Endpoints

GET /machines - List all machines
GET /machines/<id> - Get a specific machine
POST /machines - Create a new machine
PUT /machines/<id> - Update an existing machine
DELETE /machines/<id> - Delete a machine
Example Usage

List all machines:

curl http://localhost:5100/machines

Get a specific machine:

curl http://localhost:5100/machines/1

Create a new machine:

curl -X POST -H "Content-Type: application/json" -d '{"name": "Web-Server-01", "ip_address": "[IP_ADDRESS]", "mac_address": "0B:1A:2B:3C:4D:5E", "status": "Online", "uptime": "15 days", "load_average": "0.12, 0.08, 0.05"}' http://localhost:5100/machines

Update an existing machine:

curl -X PUT -H "Content-Type: application/json" -d '{"name": "Web-Server-01", "ip_address": "[IP_ADDRESS]", "mac_address": "0B:1A:2B:3C:4D:5E", "status": "Online", "uptime": "16 days", "load_average": "0.12, 0.08, 0.05"}' http://localhost:5100/machines/1

Delete a machine:

curl -X DELETE http://localhost:5100/machines/1

Database

The application uses SQLite for the database. The database file is located at site.db.

To create the database tables, run:

flask db init
flask db migrate
flask db upgrade

To populate the database with dummy data, run:

python seed_data.py

Testing

To run the tests, use pytest:

pytest

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.