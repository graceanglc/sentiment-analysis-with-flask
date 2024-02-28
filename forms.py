from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, ValidationError

def validate_feedback_content(_, field):
    if len(field.data) > 1000:
        raise ValidationError("Feedback length exceeds the maximum amount of 1000")
    elif len(field.data) < 2:
        raise ValidationError("Feedback is too short")
    elif len(field.data) == 0:
        raise ValidationError("Feedback text is required to submit feedback")

class SubmitFeedbackForm(FlaskForm):
    feedback_text = TextAreaField('Feedback Input', validators=[DataRequired(), validate_feedback_content])