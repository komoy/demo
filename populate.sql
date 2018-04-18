
CREATE DATABASE mealplanner_recipe_system;

USE mealplanner_recipe_system;

CREATE table user_profile(
    user_id int AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(30),
    gender varchar(10),
    username varchar(50),
    meal_preference varchar(50),
    password varchar(255)
    ) AUTO_INCREMENT=10000 ;
    
