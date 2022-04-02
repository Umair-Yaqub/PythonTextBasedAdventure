name = str(input("Enter Your Name\n"))
print(f"{name} you are stuck in a forest. Your task is to get out of the forrest without dieing")
print("You are walking through a forrest and a wolf comes in your way. Now you have two options.")
print("1.Run\n2.Climb The Nearest Tree ")
user = int(input("choose one option 1 or 2"))
if user == 1:
    print("you died!!")
elif user == 2:
    print("You survived!!")
else:
    print("Incorrect Input")

# Add a loop and increase the story as much as you like.