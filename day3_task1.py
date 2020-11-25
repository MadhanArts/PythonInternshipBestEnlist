my_details = {
    'name': 'Madhan',
    'age': 20
}

college_details = {
    "college_name": "Saveetha Engineering College",
    "department": "Computer Science and Engineering",
    "year": 3
}

print("my_details :", my_details)
print("college_details :", college_details)
my_details.update(college_details)
print("After merging :", my_details)
