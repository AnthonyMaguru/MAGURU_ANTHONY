student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student)
print(student.get("age"))

student["city"] = "New York"   
student["age"] = 21            

print(student)

#student.pop("grade")   
#del student["city"]    

#print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

    