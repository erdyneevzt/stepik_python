import requests


with open("dataset_3378_3 (5).txt", "r") as file:
    first_line = file.readline().strip()

while first_line != 'https://stepic.org/media/attachments/course67/3.6.3/We':
    first_line  = requests.get(first_line)
    all_text    = first_line.text
    first_line  = all_text.split()
    print(first_line[0])
    first_line  = 'https://stepic.org/media/attachments/course67/3.6.3/'+first_line[0]


print(all_text)


#
# import requests
# with open('dataset_3378_3 (5).txt') as txt:
#     a = txt.readline().strip()
# print(a)
# a = str(requests.get(a).text)
# b = 'https://stepic.org/media/attachments/course67/3.6.3/'
# while 'we' not in a:
#     print(a)
#     a = requests.get(b + a).text
# print(a)