import requests
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from data import ACTORS
from modules import get_names, get_actor, get_id

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfA7'

# Flask-Bootstrap requires this line
Bootstrap(app)

# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
class NameForm(FlaskForm):
    language = SelectField('Language', choices=[
    ("kenny ","kenny  " ),
    ("newspeak   ","newspeak   " ),
    ("scottish  ","scottish  " ),
    ("uniencode","uniencode" ),
    ("b1ff  ","b1ff " ),
    ("eleet  ","eleet  " ),
    ("jibberish  ","jibberish  " ),
    ("kraut ","kraut  " ),
    ("nyc    ","nyc    " ),
    ("scramble  ","scramble  " ),
    ("upside-down","upside-down" ),
    ("censor  ","censor " ),
    ("fanboy","fanboy" ),
    ("jive      ","jive     " ),
    ("ky00te  ","ky00te " ),
    ("pirate     ","pirate     " ),
    ("spammer","spammer" ),
    ("chef  ","chef " ),
    ("fudd   ","fudd   " ),
    ("ken     ","ken      " ),
    ("nethackify  ","nethackify " ),
    ("rasterman  ","rasterman  " ),
    ("studly","studly" )
    ])
    plaintext = StringField('Enter your text below:', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        p = request.args.get('plaintext')
        l = request.args.get('language')
        print(p)
        if p == "":
            message = "No plaintext input"
        else:
            #go do the api lookup
            url = "http://filters:8877/translate?language="+l+"&plaintext="+p
            response = requests.get(url)
            data = response.json()
            message = "The translation is: " + data['translated']
    except Exception as e:
        message = "This message will change after you call the api."
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    if form.validate_on_submit():
        language = form.language.data
        plaintext = form.plaintext.data
        return redirect( url_for('index', language=language, plaintext=plaintext))
    return render_template('index.html', form=form, message=message )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
