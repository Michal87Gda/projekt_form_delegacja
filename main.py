from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project
'''
users = ['', "Jan Brzechwa", "Adam Mickiewicz", "Jan Kochanowski"]
position = ['', "Programista PLC", "elektromonter"]
transportation_form = ['', 'Samochód', 'Samolot', 'Prom']

class LoginForm(FlaskForm):
    delegation_date = DateField(label='Data polecenia wyjazdu służbowego (data sprzed wyjazdu, najpóżniej z dania wyjazdu', validators=[DataRequired()])
    user = SelectField(label='Imię i Nazwisko', choices=users, validators=[DataRequired()])
    position = SelectField(label='Stanowisko', choices=position, validators=[DataRequired()])
    place = StringField(label="Miejsce docelowe", validators=[DataRequired()])
    date_from = DateField(label='Delegacja od dnia', validators=[DataRequired()])
    date_to = DateField(label='Delegacja do dnia', validators=[DataRequired()])
    transportation = SelectField(label="Środki lokomocji", choices=transportation_form, validators=[DataRequired()])
    project = StringField(label='Wybierz kod projektu', validators=[DataRequired(), Length(min=8)])
    breakfast = IntegerField(label='Śniadania', validators=[DataRequired()])


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "some secret string"


@app.route("/")
def home():
    login_form = LoginForm()
    return render_template('index.html', form=login_form)

@app.route("/test")
def column_test():
    return render_template('column_test.html')

if __name__ == '__main__':
    app.run(debug=True)
