# ==============================================================================================
# s = "Hello World"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.count("o"))
# print(s.center(30, "z"))
# print(s.isalpha())
# print(s.isalnum())
# print(s.islower())
# print(s.isupper())
# print(s.split('e'))
# print(s.partition('l'))

# ==============================================================================================
# set1 = {1, 2, 3, 4, 8, 9, 0}
# set2 = {1, 2, 3, 4, 5, 6, 7}
# print(set1.difference_update(set2))
# print(set1.difference(set2))
# print(set1.isdisjoint(set2))
# print(set2.isdisjoint(set1))

# ==============================================================================================
# d={"k1":1, "k2":2}
# d = {v:v**2 for v in range(10)}
# print(d)

# ==============================================================================================
# l = [1, 2, 3, 3, 3]
# l.append([4, 5])
# l.extend([4, 5])
# print(l)
#
# print(l.index(2))
# print(l.index(3))
#
# l.insert(2, "inserted")
# print(l)
# l.remove("inserted")
# l.remove([4, 5])
# print(l)
# l.sort(reverse=True)
# print(l)


# ============================================================================================== list comprehension
# list_comprehension1 = [x * 2 for x in range(100) if x % 2 == 0]
# print(list_comprehension1)
#
# list_comprehension2 = []
# for x in range(100):
#     if x % 2 == 0:
#         list_comprehension2.append(x * 2)
# print(list_comprehension2)


# def get_numbers(path):
#     with open(file=path, mode="r") as file:
#         temp = file.readlines()
#         return [int(line.strip()) for line in temp]
#
#
# list1 = get_numbers("file1.txt")
# list2 = get_numbers("file2.txt")
# result = [number for number in list1 if number in list2]
# print(list1)
# print(list2)
# print(result)


# ============================================================================================== dictionary comprehension
# student_scores = {
#     "John": 100,
#     "Jill": 89,
#     "Joe": 93,
#     "Janna": 80,
#     "Tom": 90
# }
#
# pass_student = {k: v for k, v in student_scores.items() if v >= 90}
# print(pass_student)


# ============================================================================================== iterate pandas dataframe
# import pandas
#
# student_scores = {
#     "name": ["John", "James", "Jill"],
#     "score": [68, 80, 99]
# }
# student_df = pandas.DataFrame(student_scores)
# # print(student_df)
#
# for (key, value) in student_df.iterrows():
#     print(key)
#     print("====")
#     print(value["name"])
#     print("====")


# ============================================================================================== json library
import json

new_data = {
    "name": "Jack",
    "age": 30,
    "contactNumbers": [
        {
            "type": "Home",
            "number": "123 123-123"
        },
        {
            "type": "Office",
            "number": "321 321-321"
        }
    ],
    "spouse": None,
    "favoriteSports": [
        "Football",
        "Cricket"
    ]
}
def write_json
with open(file="data.json", mode="w") as data_file:
    json.dump(new_data, data_file)
