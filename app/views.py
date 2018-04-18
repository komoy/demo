import os
from app import app, mysql
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user, login_required
from forms import *

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserForm()
    
    if request.method == "POST":
        conn = mysql.connect()
        cursor = conn.cursor()
        
        entry= "insert into user_profile(first_name,last_name,gender,user_dob,meal_preference,username,password) values('{}','{}','{}','{}','{}','{}','{}')".format(form.first_name.data,form.last_name.data,form.gender.data,form.DOB.data,form.meal_preference.data,form.username.data,form.password.data)
        
        cursor.execute(entry)
        conn.commit()

        cursor.close()
        conn.close()
        flash("You successfully created a profile")
        return redirect(url_for('home'))
        
    return render_template('register.html', form=form)
    
@app.route('/listrecipe', methods=['GET'])

def listrecipe():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select  * from recipe')
    d = cursor.fetchall()
    cursor.close()
    conn.close()
    return str(res)

@app.route('/recipe',methods=['POST','GET'])
def recipe():
     form = RecipeForm()
    
     if request.method == "POST":
        conn = mysql.connect()
        cursor = conn.cursor()
        
        entry= "insert into recipe(recipe_name,prep_time,serving_quantities,calories) values('{}','{}','{}','{}')".format(form.recipe_name.data,form.prep_time.data,form.serving_quantities.data,form.calories.data)
        
        cursor.execute(entry)
        conn.commit()

        cursor.close()
        conn.close()
        flash("You successfully added a recipe")
        return redirect(url_for('home'))
     return render_template('recipe.html',form=form)
    
@app.route('/mealplan',methods=['POST','GET'])

def mealplan():
    return render_template('mealplan.html')
    
#Procedure a    
@app.route('/mealcreation', methods=["GET","POST"])
def mealcreation():
    form = MealForm()
    if request.method == "POST":
        if form.validate_on_submit():
            conn = mysql.connect()
            cursor = conn.cursor()
            
            """stmt = "call getDiagnosisInRange('{}','{}','{}')".format(form.diagnosis.data,form.startdate.data,form.enddate.data)
            cursor.execute(stmt)
            res = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            return "<ul>" + "".join(["<li>" + item[0] + " " +item[1] + "</li>" for item in res]) + "</ul>"
            """
        
    return render_template('mealcreation.html',form=form)
    

            
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        if request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

# Error handling route
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
