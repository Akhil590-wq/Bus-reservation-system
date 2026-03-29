from flask import Flask, render_template, request, redirect
from models import db, Booking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    bookings = Booking.query.all()
    return render_template('index.html', bookings=bookings)

@app.route('/add', methods=['GET', 'POST'])
def add_booking():
    if request.method == 'POST':
        passenger_name = request.form['passenger_name']
        bus_number = request.form['bus_number']
        seat_number = request.form['seat_number']
        date = request.form['date']
        new_booking = Booking(passenger_name=passenger_name,
                              bus_number=bus_number,
                              seat_number=seat_number,
                              date=date)
        db.session.add(new_booking)
        db.session.commit()
        return redirect('/')
    return render_template('add_booking.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_booking(id):
    booking = Booking.query.get_or_404(id)
    if request.method == 'POST':
        booking.passenger_name = request.form['passenger_name']
        booking.bus_number = request.form['bus_number']
        booking.seat_number = request.form['seat_number']
        booking.date = request.form['date']
        db.session.commit()
        return redirect('/')
    return render_template('update_booking.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True)