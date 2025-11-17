notes = int(input())
notestotal = 0
notes10 = 0
while notes != -1:
    if notes >=0 and notes <=10:
        notestotal += 1
    if notes == 10:
        notes10 += 1
    notes = int(input())
print(f"TOTAL NOTES: {notestotal} NOTES10: {notes10}")
