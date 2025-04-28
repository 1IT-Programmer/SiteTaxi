# routes.py
from app import app, db, bcrypt, login_manager
from forms import RegistrationForm, LoginForm, BookingForm
from models import User, Booking
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Login unsuccessful.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/booking', methods=['GET', 'POST'])
@login_required
def book_trip():
    form = BookingForm()
    if form.validate_on_submit():
        new_booking = Booking(
            user_id=current_user.id,
            departure_point=form.departure_point.data,
            destination_point=form.destination_point.data,
            date_time=form.date_time.data
        )
        db.session.add(new_booking)
        db.session.commit()
        flash("Your trip has been booked successfully.", 'success')
        return redirect(url_for('home'))
    return render_template('booking.html', title="Book a Trip", form=form)
