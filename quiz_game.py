import random #randomize library
import sqlite3

quiz_capitals={
    "USA?":"Washington", "UK?":"London",
    "Russia?":"Moscow", "India?":"Delhi",
    "China?":"Beijing", "South Korea?":"Seoul",
    "Germany?":"Berlin", "Netherlands?":"Amsterdam",
    "France?":"Paris", "Egypt?":"Cairo"
}

connection=sqlite3.connect("results.db")
crsr = connection.cursor()

def menuDict():
    printMenu()
    try:
        choice=int(input("Select an option in menu to start: "))
        if choice is int:
            pass
    except(UnboundLocalError, ValueError, TypeError, Exception):
        quit('No such menu item found. Quiz Master is shutting down.')
    if choice==0:
        exit()
    elif choice==1:
        geo_exam()
    elif choice==2:
        mathQuiz()
    elif choice==3:
        helpg()
    else:
        print('Invalid selection. Try again\n')
        menuDict()

def printMenu():
    delimiter=100*'#'
    menu_items={'0':'Quit', '1':'Start GEO Quiz', '2':'Start MATH Quiz', '3':'Help Page'}
    print(delimiter)
    for x, y in menu_items.items():
        print(x+'. '+y)
    print(delimiter)

def exit():
    quit("Shutting down Quiz Master. Bye!")

def mathQuiz():
    print("\nIt's not ready yet. Choose another option.")
    menuDict()

def helpg():
    delimiter=100*'#'
    rules='\t=== Instruction on how to use QUIZ PARADISE ===\n* Each quiz has 10 questions dedicated to 1 scientific area;\n** Correct answer gives you 1 point;\n*** To successfully pass quiz you must earn 8 or more points;\n**** There is no time limits to finish quizes;\n***** To exit QUIZ PARADISE at any stage press Ctrl+C;'
    print(delimiter+'\n'+rules+'\n'+delimiter)
    back_to_menu=input("If you would like to continue to the main menu, type: MENU or EXIT to quit the Master: ").lower()
    if back_to_menu=='menu':
        menuDict()
    else:
        quit("Shutting down Quiz Master. Bye!")

def geo_exam():
    student_name=input("Enter your name: ").strip().capitalize()
    questions=list(quiz_capitals.items()) # get list of Q&A
    random.shuffle(questions)
    exam_score=0 # set exam score to 0 (zero)
    mistakes=0
    # loop through questions
    for q in questions:
        print("\nWhat is the capital of",q[0])
        # get user's input
        raw_answer=input("Enter your answer: ").strip()
        answer=raw_answer.capitalize()
        # check if input is correct
        if answer==q[1]:
            print("Correct answer! You've got 1 point!")
            exam_score+=1        # update score for 1 per each correct answer
        else:
            print("Incorrect")   # count mistakes if any
    print("\nYour score is:",exam_score)
    if exam_score<=7:
        print("You failed an exam!")
    else:
        print("Congratulations, you've passed an exam!")
    mistakes=(len(quiz_capitals))-exam_score
    print('\n',student_name,"made", mistakes,"mistake(s) and got", exam_score, "points.")
    global final
    final=[student_name,mistakes,exam_score]
    return final

def geo_exam_params():
    geo_exam_params=tuple(final)
    return geo_exam_params

def addingToDB():
    crsr.execute('''CREATE TABLE IF NOT EXISTS geo_results (student_name TEXT,mistakes INTEGER,exam_score INTEGER);''')
    crsr.execute('INSERT INTO geo_results VALUES (?,?,?)', geo_exam_params())
    connection.commit()

def getDataFromDB():
    for rows in connection.execute('SELECT * FROM geo_results'):
        fetched = [rows]
    print("You final results have been successfully added to the database")

menuDict()
geo_exam_params()
addingToDB()
getDataFromDB()
connection.close()
