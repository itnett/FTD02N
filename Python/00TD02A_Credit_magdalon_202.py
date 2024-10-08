python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Valider og prosesser brukernavn og passord
        # ...
        return redirect(url_for('index'))  # Omdiriger til en annen side etter vellykket innlogging
    return render_template('login.html', form=form)