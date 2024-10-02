# Programmers: Lucas and Jose
# Course:  CS:151
# Due Date: 10/2/24
# Lab Assignment: 03
# Problem Statement: Winter is coming! One winter sport is the ski jump,
# where the score is determined by the distance traveled after skiing down a ramp and into the air.
# What type of speed does a ski jumper need to achieve on the ramp to make a good distance on their jump?
# Let’s make a program to calculate the distance traveled based on speed and determine how many points
# they’d receive if they went that distance.
# Data In: hill type and jumper speed
# Data Out: points earned and distance traveled
# Credits: readMe file
# This program calculates the distance traveled by a skier based on
# their speed and determines how many points they would get

# Prompts the user to input the type of ski jump and makes it lowercase
ski_jump = str(input("Is the skier skiing normal or large jump? "))
ski_jump = ski_jump.lower()

# Establishes variables
height = 0
points_per_meter = 0
par = 0

# Defines variables used in calculations and exits program if the user inputs the wrong hill type.
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

# Prompts user to input the jumpers speed
jumper_speed = int(input("What was the jumpers speed at the end of the ramp? "))

# Calculates time in air, distance traveled, and points earned
time_in_air = ((2*height)/9.8)**.5
distance_traveled = jumper_speed * time_in_air
points_earned = 60 + (distance_traveled - par)*points_per_meter

# Expresses how good the skier performed on the jump
if points_earned > 60:
    print("Great job for doing better than par!")
elif points_earned < 10:
    print("What happened??")
else:
    print("Sorry, you didn't go very far.")

# Outputs the points the jumper earned and their distance traveled.
print(f"The jumper earned {points_earned} points and traveled {distance_traveled} meters.")

