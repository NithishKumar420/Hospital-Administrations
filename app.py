from flask import Flask, render_template, redirect, url_for , request 
from datetime import date, datetime
from models import add_staffs, book_appointments,websitesettings,db
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

##Function to generate unique staff ID based on role
def generate_staff_id(role):

    prefix = role[:3].upper()

    last_staff = add_staffs.query.filter(
        add_staffs.staff_id.like(f"{prefix}%")
    ).order_by(add_staffs.staff_id.desc()).first()

    if last_staff:
        last_number = int(last_staff.staff_id[3:])
        new_number = last_number + 1
    else:
        new_number = 1

    staff_id = f"{prefix}{new_number:03d}"

    return staff_id


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/hospitals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

##home page
@app.route('/')
def home():
    website = websitesettings.query.first()
    return render_template('admin/webpage.html', website=website)

##web login page

@app.route('/login')
def web_login():
    return render_template('admin/login.html')


##admin panel

@app.route('/admin')
def admin_dashboard():
    return render_template('admin/adminpanel.html')

##admin panel  appointments pages

@app.route('/admin/appointments')
def admin_appointments():

    today = date.today()

    today_appointments = book_appointments.query.filter_by(
    appointment_date=today
    ).order_by(book_appointments.appointment_time).all()

    return render_template(
        'admin/appointments.html',
        appointments=today_appointments
    )

##Attendance page
@app.route('/admin/attendance')
def admin_attendance():
    return render_template('admin/attendance.html')

##admin panel users pages
@app.route('/admin/users')
def admin_users():
    return render_template('admin/users.html')

##admin panel staffs pages

@app.route('/admin/staffs')
def admin_staffs():
    staffs = add_staffs.query.all()
    return render_template('admin/staffs.html', staffs=staffs)

##admin panel new staffs btn
@app.route('/admin/new_staffs')
def admin_new_staffs():
    return render_template('admin/new_staffs.html')

##Add new staff

@app.route('/admin/add', methods=['GET','POST'])
def add_staff():

    if request.method == 'POST':

        try:
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            role = request.form.get('role')
            email = request.form.get('email')
            password = request.form.get('password')
            phone_no = request.form.get('phone_no')
            alternate_no = request.form.get('alternate_no')
            address = request.form.get('address')
            aadhar_no = request.form.get('aadhar_no')
            pan_no = request.form.get('pan_no')

            # Generate Staff ID
            staff_id = generate_staff_id(role)

            new_staff = add_staffs(
                staff_id=staff_id,
                firstname=firstname,
                lastname=lastname,
                role=role,
                email=email,
                password=password,
                phone_no=phone_no,
                alternate_no=alternate_no,
                address=address,
                aadhar_no=aadhar_no,
                pan_no=pan_no
            )

            db.session.add(new_staff)
            db.session.commit()

            return redirect(url_for('admin_staffs'))

        except IntegrityError:
            db.session.rollback()
            return "Duplicate Email / Aadhaar / PAN not allowed!"

    return render_template('admin/new_staffs.html')

##Admin Panle website settings page
@app.route("/admin/websettings", methods=["GET", "POST"])
def websettings():

    settings = websitesettings.query.first()

    if request.method == "POST":

        if not settings:
            settings = websitesettings()
            db.session.add(settings)

        # Update only if form value is not empty
        if request.form.get("abt_content"):
            settings.abt_content = request.form.get("abt_content")

        if request.form.get("hospital_name"):
            settings.hospital_name = request.form.get("hospital_name")

        if request.form.get("contact_1"):
            settings.contact_1 = request.form.get("contact_1")

        if request.form.get("contact_2"):
            settings.contact_2 = request.form.get("contact_2")

        if request.form.get("email"):
            settings.email = request.form.get("email")

        if request.form.get("address"):
            settings.address = request.form.get("address")

        if request.form.get("service_time"):
            settings.service_time = request.form.get("service_time")

        db.session.commit()

        return redirect(url_for("websettings"))

    return render_template("admin/websettings.html", settings=settings)

##book appointments page
@app.route('/admin/book_appointments', methods=['GET', 'POST'])
def book_appointment():

    doctors = add_staffs.query.filter_by(role="Doctor").all()

    if request.method == 'POST':

        doctor_id = request.form.get('doctor')

        if not doctor_id or not doctor_id.isdigit():
            return "Please select a valid doctor."

        selected_doctor = add_staffs.query.get(int(doctor_id))

        if not selected_doctor:
            return "Invalid doctor selected."

        patient_name = request.form.get('patient_name')
        email = request.form.get('email')
        symptoms = request.form.get('message')

        date_str = request.form.get('appointment_date')
        time_str = request.form.get('appointment_time')

        if not date_str or not time_str:
            return "Date or Time missing!"

        appointment_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        appointment_time = datetime.strptime(time_str, '%H:%M').time()

        new_appointment = book_appointments(
            patient_name=patient_name,
            email=email,
            doctor_name=selected_doctor.full_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            symptoms=symptoms
        )

        db.session.add(new_appointment)
        db.session.commit()

        return "Appointment Booked Successfully"

    return render_template(
        'admin/book_appointments.html',
        doctors=doctors
    )

##admin panel settings pages

@app.route('/admin/settings')
def admin_settings():
    return render_template('admin/settings.html')

##registaration page

@app.route('/register')
def register():
    return render_template('admin/regiteration.html')

##after registration

@app.route('/registration')
def registration():
    return render_template('admin/login.html')

##already have an account

@app.route('/existinguser')
def existinguser():
    return render_template('admin/login.html')


if __name__ == "__main__":
    app.run(debug=True)