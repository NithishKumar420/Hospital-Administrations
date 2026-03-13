from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class add_staffs(db.Model):

    staff_id = db.Column(db.String(10), primary_key=True)

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)

    role = db.Column(
        db.Enum('Doctor', 'Nurse', 'Receptionist', 'Admin'),
        nullable=False
    )

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(100), nullable=False)

    phone_no = db.Column(db.String(15), nullable=False)
    alternate_no = db.Column(db.String(15))

    address = db.Column(db.String(200), nullable=False)

    aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
    pan_no = db.Column(db.String(10), unique=True, nullable=False)

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


class book_appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    symptoms = db.Column(db.String(500), nullable=True)


class websitesettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abt_content = db.Column(db.Text(1000), nullable=True)
    hospital_name = db.Column(db.String(100), nullable=True)
    contact_1 = db.Column(db.String(12), nullable=True)
    contact_2 = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    service_time = db.Column(db.String(100), nullable=True)