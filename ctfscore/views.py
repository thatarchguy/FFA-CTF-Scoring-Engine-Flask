from flask import render_template, request, flash, redirect, url_for
from ctfscore import app, db, models
from .forms import InputFlag
import json


@app.route('/', methods=['GET', 'POST'])
def index_view():
    error = None
    InputFlagForm = InputFlag()
    title = "FFA CTF"

    # This handles the post request and determines if the form was submitted and validated
    if InputFlagForm.validate_on_submit():
        # Turn the flag name input into the corresponding flag object from the database
        flag = models.Flags.query.filter_by(flag=InputFlagForm.flag.data).first()
        if flag is None:
            # Flash will show a message on the application once.
            # Location of flash is handled in template
            flash("Flag does not exist!")
        else:
            # Put the user input into a variable for ease later
            user = InputFlagForm.user.data
            
            # Determine if flag was already submitted for that user
            # we use the .first because it will return None if nothing returns
            if models.Completed.query.filter_by(user=user, flag_id=flag.id).first() is None:
                # Add the flag to the database
                submission = models.Completed(user=user,  flag_id=flag.id)
                db.session.add(submission)
                db.session.commit() 
                flash("Flag " + flag.flag + " Submitted for User " + user)
            else:
                flash("Error: user already submitted flag")

    return render_template('index.html', error=error, title=title, InputFlagForm=InputFlagForm)


@app.route('/scoreboard')
def scoreboard_view():
    title = "FFA CTF"
    return render_template('scoreboard.html', title=title)


@app.route('/api/scores')
def score_api():
    # get all users & flags, then sum their score
    results = []
    completed = models.Completed.query.all()
    flags = models.Flags.query.all()
    users = db.session.query(models.Completed).group_by(models.Completed.user).all()
    for user in users:
        # We want to make each user a dicionary with the sum of their points
        d = dict()
        d['user'] = user.user
        d['points'] = 0
        for submission in completed:
            if submission.user == user.user:
                points = models.Flags.query.get(submission.flag_id).points
                d['points'] += points
        # Add the dictionary to an array and move onto the next user
        results.insert(0, d)

    # Jsonify the array and return it
    jsondump = json.dumps(results, indent=4)
    return jsondump
