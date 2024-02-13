# Find if user wants to play the game
playing = input("Do you want to play? ").strip().lower()

if playing != "yes":
    quit()

print("Okay! Let's play!")

# score for the scoreboard
score = 0

# Q1 - CPU
cpu_answer = input("What does CPU stand for? ").strip().lower()
if (cpu_answer == "central processing unit") :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

# Q2 - GPU
gpu_answer = input("What does GPU stand for? ").strip().lower()
if (gpu_answer == "graphical processing unit") :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

# Q3 - RAM
ram_answer = input("What does RAM stand for? ").strip().lower()
if (ram_answer == "random access memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q4 - PSU
psu_answer = input("What does PSU stand for? ").strip().lower()
if (psu_answer == "power supply unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Print the user score
print("You got " + str(score) + " correct answers")
print("You got " + str((score / 4) * 100) + "%")