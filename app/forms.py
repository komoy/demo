from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField,SubmitField, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, DataRequired, EqualTo
ALLOWED_EXTENSIONS = [ 'png', 'jpg', 'jpeg', 'gif']

    


class UserForm(FlaskForm):
    
    """ For users to create new account """
    
    first_name= StringField("FirstName",validators=[InputRequired()])
    
    last_name= StringField("LastName",validators=[InputRequired()])
    
    username= StringField("UserName",validators=[InputRequired()])
    
    DOB= DateField('DOB', format='%m-%d-%Y')
    
    gender=SelectField('Gender', choices=[('Male', 'Male'),('Female','Female'),('PREFER NOT DISCLOSE',' None')])
    
    meal_preference= StringField("Meal Preference",validators=[InputRequired()])
    
    password = PasswordField('Password', validators=[InputRequired()],)

    
class MealForm(FlaskForm):
    calories = StringField('calories', validators=[InputRequired()]),
    
    meal_type = StringField('meal_type', validators=[InputRequired()]),
    
    meal_id = StringField('meal_id', validators=[InputRequired()]),
    
    image = FileField('image', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')])
    
    meal_name=StringField('Meal Name',validators=[InputRequired()])
    
class RecipeForm(FlaskForm):
   
    recipe_name = StringField('recipe name', validators=[InputRequired()])
    
    prep_time = StringField('prep time', validators=[InputRequired()])
    
    serving_quantities =StringField('serving quantity',validators=[InputRequired()])
    
    calories=StringField('calories',validators=[InputRequired()])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    
    password = PasswordField('Password', validators=[InputRequired()])

