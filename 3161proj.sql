DROP DATABASE projectdatabase;
CREATE DATABASE projectdatabase;
use projectdatabase;

CREATE TABLE user_profile(
	first_name varchar(55),
	last_name varchar(55),
	user_id int AUTO_INCREMENT NOT NULL,
	gender varchar(2),
	user_dob DATE,
	meal_preference varchar(55),
	username varchar(55),
	password varchar(25),
	PRIMARY KEY(user_id)
)AUTO_INCREMENT=100000;



CREATE TABLE health_info(
	 weight int,
	 user_id int AUTO_INCREMENT NOT NULL,
	 health_id int,
	 blood_type varchar(55),
	 height int,
	 FOREIGN KEY(user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	 PRIMARY KEY(user_id, health_id)
);

CREATE TABLE health_information(
	user_id int AUTO_INCREMENT NOT NULL,
	health_id int,
	allergies varchar(55),
	PRIMARY KEY(user_id),
	FOREIGN KEY (user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE recipe(
	recipe_id int AUTO_INCREMENT NOT NULL,
	recipe_name varchar(55),
	prep_time TIME,
	serving_quantities int, 
	calories int,
	PRIMARY KEY(recipe_id)
)AUTO_INCREMENT=2000;

CREATE TABLE adds(
	recipe_id int , 
	user_id int AUTO_INCREMENT NOT NULL,
	creation_date DATETIME,
	PRIMARY KEY(recipe_id,user_id),
	FOREIGN KEY(user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE addition_log(
	recipe_id int ,
	user_id int AUTO_INCREMENT NOT NULL,
	date_add DATE,
	PRIMARY KEY(recipe_id,user_id),
	FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE instruction(
	measurement int,
	step int,
	recipe_id int AUTO_INCREMENT NOT NULL,
	instruction_id int,
	directions varchar(55),
	PRIMARY KEY(instruction_id, recipe_id),
	FOREIGN KEy(recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE meal(
	calories int,
	meal_type varchar(55),
	meal_id int,
	image LONGBLOB,
	meal_name varchar(55),
	PRIMARY KEY(meal_id)
);

CREATE TABLE meal_planner(
meal_id int,
plan_id int,
day varchar(55),
week varchar(55),
PRIMARY KEY(meal_id, plan_id),
FOREIGN KEY(meal_id) REFERENCES meal(meal_id) ON DELETE CASCADE ON UPDATE CASCADE,
UNIQUE(day)
);

CREATE TABLE ingredients(
	i_id int AUTO_INCREMENT NOT NULL,
	name varchar(55),
	PRIMARY KEY(i_id)
);

CREATE TABLE supermarket_list(
	quantity int,
	ingredient varchar(55),
	list_id int,
	price double,
	PRIMARY KEY(list_id)
);

CREATE TABLE contains(
	recipe_id int,
	i_id int,
	quantity int,
    UNIQUE(quantity),
    PRIMARY KEY(recipe_id),
    FOREIGN KEY(i_id) REFERENCES ingredients(i_id) ON DELETE CASCADE ON UPDATE CASCADE 
);
