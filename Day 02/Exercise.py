#Day 2 Python variables
first_name = "Gianni"
last_name = "Trujillo"
full_name = first_name + " " + last_name
country = "United States"
city = "California"
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
person_info = {
    "first_name": "Gianni",
    "last_name" : "Trujillo",
    "country" : "United States",
    "city" : "California",
    "age" : 21,
    "year" : 2026,
    "is_married" : False,
    "is_true" : True,
    "is_light_on" : True,
}
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(person_info)
print(len(first_name))
print(len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
modulus = num_one % num_two
print(modulus)
power = num_one ** num_two
print(power)
floor_division = num_one // num_two
print(floor_division)
area_of_circle = 3.14 * 30 ** 2
print(area_of_circle)
circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)
name_user = input("What is your name? ")
age_user = input("What is your age? ")
country_user = input("What is your country? ")
print("Your name is " + name_user + ", you are " + age_user + " years old, and you live in " + country_user)

