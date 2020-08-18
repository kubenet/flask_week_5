from flask_wtf import FlaskForm
from wtforms import RadioField, StringField
from wtforms.validators import InputRequired, Length


class RequestForm(FlaskForm):  # объявление класса формы для WTForms
    name = StringField('name', [InputRequired(), Length(min=2)])
    phone = StringField('phone', [InputRequired(), Length(min=6, max=12)])
    goal = RadioField("Какая цель занятий?",
                      choices=[('0', '⛱ Для путешествий'), ('1', '🏫 Для учебы'), ('2', '🏢 Для работы'),
                               ('3', '🚜 Для переезда'), ('4', '💻 Для программирования')])
    time = RadioField("Сколько времени есть?",
                      choices=[('0', '1-2 часа в неделю'), ('1', '3-5 часов в неделю'),
                               ('2', '5-7 часов в неделю'), ('3', '7-10 часов в неделю')])
