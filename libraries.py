print("================= STUDENT DETAILS =======================")

student_list = {
    "student_name": "harsha",
    "student_prn": "2024BTAM008",
    "student_college": "joy university",
    "student_address": "pamidi,pamidi mandal,anantapur district",
    "student_mbl": 9676791090
}


for key, value in student_list.items():
    print(f"{key} : {value}")



print("================ STUDENT UPDATE DETAILS =================")


student_list["age"] = 21
student_list["father_name"] = "prasad"

print(student_list.get("student_age"))

for key, value in student_list.items():
    print(f"{key} : {value}")



print("============== UPDATE DETAILS =========================")


student_list["student_language"] = "english"
student_list["dream"] = "software engineer"
student_list["salary"] = 80000

for key, value in student_list.items():
    print(f"{key} : {value}")



print("==================== ONLY KEYS ==========================")


for key in student_list.keys():
    print(key)



print("======================= ONLY VALUES =========================")


for value in student_list.values():
    print(value)



print("======================= REMOVE SPECIFIC VALUE =========================")


student_list.pop("student_prn")

for key, value in student_list.items():
    print(f"{key} : {value}") 
    


