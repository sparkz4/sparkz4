# Example program; adapted from
# Online Python Supplement, Figure 1.2

speed = input("Enter speed (mph): ")
speed = int(speed)
distance = input("Enter distance (miles): ")
distance = float(distance)

time = distance / speed

print("At", speed, "mph, it will take")
print(time, "hours to travel", \
distance, "miles.")
