from flask_wtf import FlaskForm
from wtforms.fields import DecimalField, SubmitField
from wtforms.validators import InputRequired


class PredictionForm(FlaskForm):
    """Prediction form"""
    sepal_length = DecimalField('Sepal Length (cm)', validators=[InputRequired()])
    sepal_width = DecimalField('Sepal Width (cm)', validators=[InputRequired()])
    petal_length = DecimalField('Petal Length (cm)', validators=[InputRequired()])
    petal_width = DecimalField('Petal Width (cm)', validators=[InputRequired()])
    submit = SubmitField('Submit')
