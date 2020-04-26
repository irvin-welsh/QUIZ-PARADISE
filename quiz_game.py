import random #randomize library

quiz_capitals={
    "What is the capital of USA?":"Washington", "What is the capital of UK?":"London",
    "What is the capital of Russia?":"Moscow", "What is the capital of India?":"Delhi",
    "What is the capital of China?":"Beijing", "What is the capital of South Korea?":"Seoul",
    "What is the capital of Germany?":"Berlin", "What is the capital of Netherlands?":"Amsterdam",
    "What is the capital of France?":"Paris", "What is the capital of Egypt?":"Cairo"
}

def geo_exam():
    student_name=input("Enter your name: ")
    questions=list(quiz_capitals.items()) # get list of Q&A
    random.shuffle(questions)
    # set exam score to 0 (zero)
    attempt=0
    exam_score=0
    mistakes=0
    # loop through questions
    for q in questions:
        print(q[0])
        # take user's input
        answer=input("Enter your answer: ")
        # check if input is correct
        if answer==q[1]:
            print("Correct answer! You've got 1 point!")
            exam_score+=1        # update score for 1 per each correct answer
        else:
            print("Incorrect")
            mistakes+=1            # count mistakes if any
    print("Your score:",exam_score, "Your mistakes:", mistakes)
    if exam_score<=7:
        print("You failed an exam!")
    else:
        print("Congratulations, you've passed an exam!")
    attempt+=1
    print(student_name,", you've made", attempt,"attempt(s) and got", exam_score, "points.")

def help_page():
    print("\n\t=== Instruction on how to use QUIZ PARADISE ===\n* Each quiz has 10 questions dedicated to 1 scientific area;\n** Correct answer gives you 1 point;\n*** To successfully pass quiz you must earn 8 or more points;")
    print("**** There is no time limits to finish quizes;\n***** To exit QUIZ PARADISE at any stage press Ctrl+C;\n\n")
    go_to_menu=input("If you would like to continue to the main menu, type: menu or exit to quit the Master: ").lower()
    if go_to_menu=="menu":
        return main_menu()
    elif go_to_menu=="exit":
        quit("Shutting down Quiz Master. Bye!")
    else:
        quit("Wrong choice. Shutting down Quiz Master. Bye!")

def main_menu():
    print("\n##################################\nWelcome to QUIZ PARADISE\n##################################\nPlease select an option:\n1. Take GEO Quiz\n2. Take MATH Quiz\n3. Help page\n4. Quit\n##################################")
    try:
        choice=int(input("Enter your choice: "))
        pass
    except (UnboundLocalError,ValueError):
        print("\nOoops! Your choice was wrong. Made another one \n\u2193 \u2193 \u2193")
        return main_menu()
    if choice==1:
        print("Welcome to the GEO quiz. To pass you need to have 8 points or higher. 1 question = 1 point. Let's start")
        geo_exam()
    elif choice==2:
        print("It's not ready yet!")
        choice2=int(input("Make another choice: "))
        if choice2==1:
            print("Welcome to the GEO quiz. To pass you need to have 8 points or higher. 1 question = 1 point. Let's start")
            geo_exam()
    elif choice==3:
        return help_page()
    elif choice in range(5,10):
        print("There is no such option. Would you like to make another choice?")
        choice3=input("Type yes to continue to Main Menu or no to quit: ").lower()
        if choice3=="yes":
            return main_menu()
        else:
            quit("Shutting down Quiz Master. Bye!")
    else:
        quit("Shutting down Quiz Master. Bye!")
main_menu()
