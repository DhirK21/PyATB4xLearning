# Dict
# Key and Value
# name -> "Pramod"

student_infor = {
    "name": "Dhir",
    # "age": 65,
    "age": 30,
    "address": "Brampton",
    "License": "G2",
    "Weight": 72

}

print(student_infor)
print("**********************")
print(student_infor["name"])
print("**********************")
print(student_infor["License"])
print("**********************")
print(student_infor["address"])
print("**********************")
student_infor["age"] = 100
print(student_infor)
print("**********************")

student_infor = dict(name="Pramod", age=67, address="KA")
print(student_infor)
# A dictionary is an unordered collection of data
print("**********************")

student_infor1 = {
    "name": "Dhir",
    # "age": 65,
    "age": 30,
    "address": {
        "home_address": "ND",
        "office_address": "KA"

    },
    "Phone": {
        "home_phone": 5199927152,
        "office_phone": None

    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_list = [student_infor1]
print(student_list)
print("****************")

student_list2 = [student_infor1, student_infor2]
print(student_list2)

