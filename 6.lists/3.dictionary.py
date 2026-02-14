# This is the menu of a close-by restaurant:

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}

# What is the second meal in the list?
print(Menu['meal_2'])


Menu['meal_5'] = "Soup"

print(Menu)


Menu['meal_3'] = 'Cheeseburger'
print(Menu)



Dessert = ['Pancakes', 'Ice-cream', 'Tiramisu']
Menu['meal_5'] = 'Soup'
Menu['meal_6'] = Dessert
print(Menu)

Price_list = {'Cheeseburger': 8, 'Fries': 5, 'Lasagna': 12, 'Soup': 5, 'Spaghetti': 10}

print(Price_list.get('Spaghetti'))