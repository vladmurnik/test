x = int(input("year: "))
y = int(input("month: "))
z = int(input("day: "))
n = int(input("how many days have you been away: "))
z = z + n
while True:
    if z >= 30:
        z = z - 30
        y = y + 1
    elif y >= 12:
        y = y - 11
        x = x + 1
    else:
        break
print("year:" + str(x) + " month:" + str(y) + " day:" + str(z))
