import random
import sqlite3

math_questions={}
connection=sqlite3.connect("results.db")
crsr = connection.cursor()

def assemble_question():
    for i in range(1,12):
        operators=['+','-','**','%','*']
        operators_value=random.choice(operators)
        math_question=(str(random.randint(1.00,15.00))+' '+operators_value+' '+str(random.randint(1.00,15.00)))
        correct_answer=eval(str(math_question))
        math_questions[math_question]=correct_answer
        i+=1

def math_exam():
    student_name=input("Enter your name: ").strip().capitalize()
    questions=list(math_questions.items()) # get list of Q&A
    question=random.sample(questions,10)
    mistakes=0
    math_score=0
    for q in question:
        print('\nEvaluate the following expression:',q[0])
        try:
            user_answer=int(input('Type your answer here: '))
            if user_answer is not int:
                raise TypeError("Only integers are allowed")
        except:
            if user_answer==q[1]:
                print("Correct answer! You've got 1 point!")
                math_score+=1        # update score for 1 per each correct answer
            else:
                print("Incorrect")
                mistakes+=1
    if math_score<=7:
        print("\nYou failed an exam!")
    else:
        print("\nCongratulations, you've passed an exam!")
    print('\n'+student_name,"made", mistakes,"mistake(s) and got", math_score, "points.")
    global final
    final=[student_name,mistakes,math_score]
    # return final

def get_math_params():
    math_params=tuple(final)
    print(math_params)
    return math_params

def addingToDB():
    crsr.execute('''CREATE TABLE IF NOT EXISTS math_results (student_name TEXT,mistakes INTEGER,exam_score INTEGER);''')
    crsr.execute('INSERT INTO geo_results VALUES (?,?,?)', get_math_params())
    connection.commit()

assemble_question()
math_exam()
addingToDB()
connection.close()
    # results_file = PrettyTable()
    # results_file.field_names = ["Student Name", "Attempts", "Exam Score"]
    # results_file = open("math.results.txt", 'a')
    # # results_file.write('Student Name,'+'Attempts,'+'exam_score')
    # results_file.write('Student Name : Attempts : Math Score\n')
    # results_file.write(str(student_name)+' : '+str(mistakes)+' : '+str(math_score)+'\n')
    # results_file.close()
