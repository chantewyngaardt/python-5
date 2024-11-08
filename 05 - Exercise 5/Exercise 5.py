# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "orange", "guava"]
# TODO: Add a fruit to the end of the list
fruits.append("strawberry")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "kiwi") 
# # TODO: Remove a fruit from the list
fruits.remove("guava")
# # TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared
squared_numbers = [num**2 for num in numbers ]
print(squared_numbers)

# # TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum/len(numbers)
# TODO: Print the results
print(f"This is the average: {average}")

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries = {
    "Japan": "Tokyo",
    "Malaysia": "Kuala Lumpur",
    "South Korea": "Seoul",
    "South Africa": "Cape Town"
}
# TODO: Add a new country-capital pair
countries["Brazil"] = "Rio de Janeiro"
# TODO: Update the capital of an existing country
countries.update({"South Africa": "Johannesburg"})
# TODO: Remove a country-capital pair
countries.pop("Malaysia")
# TODO: Print the modified dictionary
print(countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Apple": "Red",
    "Grape": "Purple",
    "Naartjie": "Orange",
    "Banana": "Yellow"
}
# TODO: Print all the fruits (keys)
print(list(fruit_colors.keys()))
# TODO: Print all the colors (values)
print(list(fruit_colors.values()))
# TODO: Print each fruit and its color
print(fruit_colors)
# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = "Apple"  

if fruit_to_check in fruit_colors:
    print(f"The color of {fruit_to_check} is {fruit_colors[fruit_to_check]}")
else:
    print(f"{fruit_to_check} is not in the dictionary.")
