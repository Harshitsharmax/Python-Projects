# Import the pyttsx3 library, which is a text-to-speech conversion library in Python.
# If it shows error on running then write the command pip install pyttsx3 in terminal
import pyttsx3

# Main program under which the project is created:
if __name__ == '__main__':
    # Print a welcome message to my project.
    print("Welcome to Robo-speaker created by Harshit Sharma")

    # Starting an infinite loop which continues until the user types 'qq'.
    while True:
        # Asks the user to enter text to be spoken.
        x = input("Enter what you want me to speak: ")

        # Check if the user entered 'qq'.
        if x == 'qq':
            # If the user entered 'qq', speak a goodbye message and exit the loop.
            robo = pyttsx3.init()
            robo.say("Bye, I will come later.")
            robo.runAndWait()
            break
        # Main logic how pyttsx3 works:
        # Initialize a pyttsx3 engine.
        robo = pyttsx3.init()
        # Use the engine to speak the text entered by the user.
        robo.say(x)
        # Wait for the speech to finish.
        robo.runAndWait()
