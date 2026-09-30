# new_range = [n * 2 for n in range(1, 5) if n % 2 == 0]
# print(new_range)

# import random

# names = ["leo", "emi", "jack", "alex", "dave"]



# student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)

# passed_student = {student:score for (student, score) in student_scores.items() if score > 60}
# print(passed_student)


import pandas

student_dict = {
    "student": ["Leo", "Emi", "Steve"],
    "score": [67, 99, 65],
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row)

# {new_key:new_value for (index, row)
#  in df.iterrows()}