print("Hi im a chatbot!")
name = input ("what is your name?")
print("hello" + name + "!" )  
age = input ("How old are you?") 



def chatbot_guide():
    while True:
        print("\nThis is the menu guide") 
        print("1. Placeholder opition 1") 
        print("2. Placeholder opition 2") 
        print("3. Placeholder opition 3") 
        print("4. Quit Chatbot") 
        choice = input (" Please select and opition above(1-4): ") 
        if choice == '1':
            print("You selected opition 1. (This is unavailable)")
        elif choice == '2':
            print("You selected opition 2. (This is unavailable)") 
        elif choice == '3':
            print("You selected opition 3. (This is unavailable)") 
        elif choice == '4': 
            print(" Exiting Chatbot!") 
            break
        else:
            print(" Invalid opition!") 


if __name__== "__main__":
    chatbot_guide()              