from app import app, db
from models import Machine, User

def seed_data():
    with app.app_context():
        """Seed the database with dummy users and machines."""
        # Dummy Users
        u1 = User(username='admin', email='admin@example.com', password='password123')
        u2 = User(username='staff', email='staff@example.com', password='password123')

        # Dummy Machines
        m1 = Machine(
            name='Web-Server-01', 
            ip_address='192.168.1.100', 
            mac_address='0B:1A:2B:3C:4D:5E', 
            status='Online', 
            uptime='15 days', 
            load_average='0.12, 0.08, 0.05'
        )
        m2 = Machine(
            name='Web-Server-02', 
            ip_address='192.168.1.101', 
            mac_address='0Q:1A:2B:3C:4D:5E', 
            status='Online', 
            uptime='15 days', 
            load_average='0.12, 0.08, 0.05'
        )
        m3 = Machine(
            name='Web-Server-03', 
            ip_address='192.168.1.102', 
            mac_address='00:CA:2B:3C:4D:5E', 
            status='Online', 
            uptime='15 days', 
            load_average='0.12, 0.08, 0.05'
        )
        m4 = Machine(
            name='Web-Server-04', 
            ip_address='192.168.1.103', 
            mac_address='R0:1A:2B:3C:4D:5E', 
            status='Online', 
            uptime='15 days', 
            load_average='0.12, 0.08, 0.05'
        )
        m5 = Machine(
            name='FS-Server-01', 
            ip_address='192.168.1.104', 
            mac_address='10:1A:2B:3C:4D:5F', 
            status='Offline', 
            uptime='0 days', 
            load_average='0.00, 0.00, 0.00'
        )

        m6 = Machine(
            name='MQT-Server-01', 
            ip_address='192.168.1.105', 
            mac_address='00:1K:25:3C:4M:5F', 
            status='Offline', 
            uptime='0 days', 
            load_average='0.00, 0.00, 0.00'
        )

        db.session.add_all([u1, u2, m1, m2, m3, m4, m5, m6])
        db.session.commit()
        print("Successfully seeded database with dummy data.")

seed_data()
