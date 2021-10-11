dt = 13
start = 1
t = 13
startt = 1
AM = "AM"
PM = "PM"
while start and startt < 13:
    if start < dt:
        print(start, AM)
        start += 1
    else:
        print(startt, PM)
        startt += 1

# dt = 13
# start = 1
# t = 13
# startt = 13
# AM = "AM"
# PM = "PM"
# while start < dt:
#     print(start, AM)
#     start += 1
#
# while startt < t:
#     print(startt, PM)
#     startt += 1
