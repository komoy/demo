import faker

import random

from faker import Factory
from random import randint
fake = Factory.create()
fake = faker.Faker()
f = open ("indgredients.sql","a")
def solve ():

    diet = []
    lst1 = ['salted butter,' 'unsalted butter', 'whipped cream', 'olive oil', 'corn oil', 'canola oil', 'vegetable oil', 'coconut oil', 'blue cheese', 'brie',
'cheddar cheese', 'cheshire cheese', 'cottage cheese', 'creamed cheese', 'curd', 'feta cheese', 'gouda', 'monterey cheese', 'mozzarella cheese', 'whole milk',
'low-fat milk', 'full cream milk', 'non-fat milk', 'sweetened condensed milk', 'skimmed milk', 'parmesan cheese', 'provolone cheese', 'ricotta', 'swiss cheese',
'pimento', 'sunflower seed', 'coffee', 'heavy cream', 'whipping cream', 'sour cream, egg', 'egg yolk', 'egg white', 'icing sugar', 'brown sugar', 'granulated sugar',
'buttermilk', 'dark chocolate', 'milk chocolate', 'white chocolate', 'caramel', 'chocolate chip', 'evaporated milk', 'cocoa powder', 'vanilla extract', 'mint', 'whey',
'plain yogurt', 'glucose', 'water', 'vinegar', 'apple cider vinegar', 'turkey bacon', 'bacon', 'italian sausage', 'turkey sausage', 'chicken', 'chicken sausage',
'turkey', 'fish', 'pork', 'porkchop', 'duck', 'ham', 'pepperoni', 'pineapple', 'dried pineapple', 'apple', 'dried apple', 'grapes', 'peach', 'quail','dried peach', 'almond',
'peanut', 'cashew',' baking powder', 'baking soda', 'olive', 'goose', 'lemon juice', 'lime juice', 'tomato sauce', 'tomato', 'lettuce', 'onion',' sweet pepper']


    lst2=['scotch bonnet', 'pepper', 'thyme', 'parsley', 'basil', 'mushroom', 'kale', 'sweet potato', 'potato', 'white yam', 'yellow yam', 'plantain', 'banana', 'scallion', 'avocado',
'pear', 'ginger', 'jalapeno pepper', 'carrot', 'turnip', 'okra', 'cassava', 'cucumber', 'cabbage', 'callaloo', 'pak choy', 'black eyed pea', 'kidney bean', 'sweet corn',
'corn', 'stringed bean', 'lima bean, broccoli', 'cauliflower, garlic', 'ceery', 'flour', 'ice cream', 'yeast', 'peanut butter, almond butter', 'jam', 'jelly',
'blackberry', 'honey, cinnamon', 'nutmeg, chilli pepper', 'coriander, cilantro, cumin', 'paprika, garlic powder', 'onion powder, pickle, relish','mustard',
'ketchup', 'mayonnaise, oregano, rosemary, saffron, turmeric', 'sea salt', 'radish', 'peppermint', 'red herring', 'salted fish', 'salted mackerel', 'pig tail',
'chicken foot', 'salmon', 'tuna', 'beef', 'minced beef', 'lobster', 'shrimp', 'bread', 'oats', 'macaroni', 'penne pasta', 'fettucine pasta', 'spaghetti', 'angel hair pasta',
'panko', 'cranberry', 'raisins', 'soy bean', 'sesame oil', 'shortening', 'hazelnut', 'wheat rice', 'white rice', 'margarine', 'bread crumbs', 'black bean', 'soy sauce',
'oster sauce', 'maple syrup', 'passion fruit']



    for i in range (0,100):
        diet1 = random.choice(lst1)
        diet2=random.choice(lst2)
        new = (diet1 +diet2)
       # print(new)
        a=str(new)
        f.write("insert into ingredients (name) values ")
        f.write("(")
        f.write("'")
        f.write(a)
        f.write("'")
        f.write(")")
        f.write(";")
        f.write ('\n')
    f.close()
        

solve ()

