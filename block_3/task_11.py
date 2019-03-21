import requests

with open("dataset_3378_2 (1).txt", "r") as file:
    req = file.read().strip()

r = requests.get(req)
r = r.text

num_lines = len(r.splitlines())

print(num_lines)


# import requests
#
# with open('dataset_3378_2.txt') as inf:
#     r = requests.get(inf.readline().strip())
#     print(len(r.text.splitlines()))