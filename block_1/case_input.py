rec_hour    = int(input())
max_hour    = int(input())
cur_hour    = int(input())

if (cur_hour >= rec_hour) and (cur_hour <= max_hour):
    print("Это нормально")
elif cur_hour > max_hour:
    print("Пересып")
elif cur_hour < rec_hour:
    print("Недосып")