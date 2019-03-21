all_min     = int(input())
start_hour  = int(input())
start_min   = int(input())

full_min = all_min + start_hour*60 + start_min
hours = full_min // 60
minuts = full_min - hours*60
print(hours)
print(minuts)