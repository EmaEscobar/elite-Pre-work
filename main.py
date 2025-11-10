#asked for the user's name and asks what they can do to help
name = input ("what is your name?:")
print("hello " + name + " what can we help you with today" )  
 


#This defines what the options that the menu has along with allowing the user to see what the options are.
def chatbot_guide():
    while True:
        print("\nThis is the menu guide") 
        print("1. report an issue with the order") 
        print("2. food hasn't arried yet") 
        print("3. leave a review") 
        print("4. Quit Chatbot") 

        #this is what allows the user to select an option.
        choice = input (" Please select and opition above(1-4): ") 
        
        #this option allows the user to report an issue with their order
        if choice == '1':
            issue = input("We are sorry to hear that can you please tell us what is wrong with your order:")
            print (f"we are sorry about {issue}")
            refund = input("would you like a refund:").strip().lower()
            if refund == 'yes':
                print("Your refund is being processed.")
            elif refund == 'no':
                problem_fix = input("is there anything we can do to fix this")
                print("we will try our best to accommodate your request")

        #this option allows the user to report that they have not yet recived their food
        elif choice == '2':
            no_arrival = input(" we are so sorry that youre food hasn't arrived yet. Would you like to cancel your order and get a refund.").strip().lower() 
            if no_arrival == 'yes':
                print("your refund in being processed.")
            elif no_arrival == 'no':
                print("we are trying our hardest to get your order out to you as quick as possible")
        
        #this option allows the user to leave a review
        elif choice == '3':
            review = input("tell us how you you're vist was")
            print(f"thank you for leaving a review")
        
        #closes the chatbot
        elif choice == '4': 
            print(" Exiting Chatbot!") 
            #this ends the loop
            break
        #if the user enter an opition that is not promted this will be appear asking the user the select an opition and giving them the opitions
        else:
            print("Invalid opition! please select an opition between (1-4)") 


if __name__== "__main__":
    chatbot_guide()              