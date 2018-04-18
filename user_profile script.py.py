from __future__ import print_function

from faker import Factory
from faker import Faker
from random import randint
fake=Faker('en_US')
fake=Factory.create()
lst=[]
meal_type=["Breakfast", "Lunch", "Dinner", "Snack"]
meal_preference=["Vegetarian", "Vegan", "Fruitarian", "Pescatarian", "Flexible","Pollotarian","Pollo-Pescatarian"]
gender=["Male", "Female"]
blood_type=["A","B","AB","O"]

with open("population.sql","a") as f:
    for i in range(0,100000):
        f.write("INSERT INTO user_profile (first_name,last_name,gender,user_dob,meal_preference,username,password) values")
        f.write("(")
        f.write("'")
        f.write(fake.first_name())
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(fake.last_name())
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(gender[randint(0,1)])
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(fake.date(pattern="%Y-%m-%d", end_datetime=1998-31-12))
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(meal_preference[randint(0,6)])
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(fake.profile(fields=['username'])['username'])
        f.write("'")
        f.write(",")
        f.write("'")
        f.write(fake.password())
        f.write("'")
        f.write(")")
        f.write(";")
        f.write('\n')
    f.close()
   
        
        

        
        
        



        
        
        
    

    
            
