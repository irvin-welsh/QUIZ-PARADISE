import random #randomize library
import sqlite3
import math_quiz as math

connection=sqlite3.connect("results.db")
crsr = connection.cursor()

def getDataFromDB():
    for rows in crsr.execute('SELECT * FROM Country_Capitals'):
        cc_rows=crsr.fetchall()
    global quiz_capitals
    quiz_capitals=dict(cc_rows)
    return quiz_capitals

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
        geo_exam_params()
        addingToDB()
        connection.close()
        print("You've done with Geo Quiz.")
        a=input('Type MENU to go to the main menu or EXIT to close Quiz Master: ').strip().upper()
        if a=='MENU':
            menuDict()
        elif a=='EXIT':
            exit()
        else:
            print('Invalid selection. Try again\n')
            exit()
    elif choice==2:
        math.game_init()
        print("You've done with Math Quiz.")
        a=input('Type MENU to go to the main menu or EXIT to close Quiz Master: ').strip().upper()
        if a=='MENU':
            menuDict()
        elif a=='EXIT':
            exit()
        else:
            print('Invalid selection. Try again\n')
            exit()
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

def helpg():
    delimiter=100*'#'
    rules='\t=== Instruction on how to use QUIZ PARADISE ===\n* Each quiz has 10 questions dedicated to 1 scientific area;\n** Correct answer gives you 1 point;\n*** To successfully pass quiz you must earn 8 or more points;\n**** There is no time limits to finish quizes;\n***** To exit QUIZ PARADISE at any stage press Ctrl+C;'
    print(delimiter+'\n'+rules+'\n'+delimiter)
    back_to_menu=input("If you would like to continue to the main menu, type: MENU or EXIT to quit the Master: ").strip().lower()
    if back_to_menu=='menu':
        menuDict()
    else:
        exit()

def geo_exam():
    student_name=input("Enter your name: ").strip().capitalize()
    question=list(quiz_capitals.items()) # get list of Q&A
    questions=random.sample(question,10)
    exam_score=0 # set exam score to 0 (zero)
    mistakes=0
    # loop through questions
    for q in questions:
        print("\nWhat is the capital of",q[0]+'?')
        # get user's input
        raw_answer=input("Enter your answer: ").strip()
        answer=raw_answer.capitalize()
        # check if input is correct
        if answer==q[1]:
            print("Correct answer! You've got 1 point!")
            exam_score+=1        # update score for 1 per each correct answer
        else:
            print("Incorrect")   # count mistakes if any
        # print("Your score is:",exam_score)
    if exam_score<=7:
        print("\nYou failed an exam!")
    else:
        print("\nCongratulations, you've passed an exam!")
    mistakes=(len(questions))-exam_score
    print('\n',student_name,"made", mistakes,"mistake(s) and got", exam_score, "point(s).")
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


getDataFromDB()
menuDict()
