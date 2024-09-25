# This program calculates the distance traveled by a skier based on
# their speed and determines how many points they would get

ski_jump = str(input("Is the skier skiing normal or large jump? "))
ski_jump = ski_jump.lower()

height = 0
points_per_meter = 0
par = 0

if ski_jump == "normal":
    height = 46
    points_per_meter = 2
    par = 90
elif ski_jump == "large":
    height = 70
    points_per_meter = 1.8
    par = 120
else:
    print("You idiot, input normal or large!!!")
    exit()

jumper_speed = int(input("What was the jumpers speed at the end of the ramp? "))


time_in_air = ((2*height)/9.8)**.5
distance_traveled = jumper_speed * time_in_air
points_earned = 60 + (distance_traveled - par)*points_per_meter

if points_earned > 60:
    print("Great job for doing better than par!")
elif points_earned < 10:
    print("What happened??")
else:
    print("Sorry, you didn't go very far.")

print(f"You earned {points_earned} points and traveled {distance_traveled} meters.")

