from datetime import datetime
import json
import sys
import threading



def Add_participant (data , name , date ,category, score ) :  # add a new participant
   
    new_participant = {
       
        "Name" : name,
        "Participations" : [{"Date": date ,"Category" : category ,"Score" : score}]
    }
   
    data.append(new_participant)

    return data

def Update_participant (data ,name  , date ,category, score ) : # update the history of a participant
    for participant in data :
        if participant["Name"] == name :
            participant["Participations"].append({"Date": date ,"Category" : category, "Score" : score})
            return data 

    return data

def Show_Participant_history (name) : # show the history of a participant
    for participant in data :
        if participant["Name"] == name :
            print(f"Your name is : {participant['Name']} " )
            print (f"\n--------The history of {name} -----------\n\n")
            
            for participation in participant['Participations'] :
                print(f"Date : {participation['Date']} , Category :{participation['Category']} , Score : {participation['Score']}" )

def save_data(filename, data):   # save data in a file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_data(filename):   # load data from a file
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def Choose_Category() :   # choose a category
  while True :
     cat = input("Choose a category : \n\t1-Python\n\t2-Algorithmique\n\t3-Network\n\t4-Databases\n\t5-Animes\n")
     if cat in ["1" , "2" , "3", "4" , "5"] :   
        return cat
     else :
        print("Please choose a valid category")

def Category_name (cat) :    # return the name of the category
    if cat == "1" :
        return "Python"
    elif cat == "2" :
        return "Algorithmique"
    elif cat == "3" :
        return "Network"
    elif cat == "4" :
        return "DB"
    else :
        return "Animes"


def Verify_Participant (data , name) :    # verify if the participant is already exist
    for participant in data :
        if participant["Name"] == name :
            return True
    return False

def verify_answer(data , question , answer) :  # verify the answer of a question
    for qst in data :
        if qst["question"] == question :
            if qst["answer"] == answer :
                return True
            else :
                return False


def Ask_Questions(data, timing_choice):    # start the MCQ
    global time_expired, score
    time_expired = False  
    if timing_choice == "2":  
         start_global_timer(GLOBAL_TIMER_LIMIT)  

    for qst in data:
        if time_expired:
            print("\nTime is up ! The test has ended.")
            sys.exit() #quit the program when the timer is done

        print(qst["question"])
        for opt in qst["options"]:
            print("\t", opt)

        if timing_choice == "1":  
            answer = time_limit("Choose an answer : ", 10)
        elif timing_choice == "2": 
            answer = input("Choose an answer : ")
        else:
            print("invalid choice ")
            return

        if answer in ["a", "b", "c"]:
            user_answers.append(answer)

            questions.append({
                    "question": qst["question"],
                    "answer": qst["answer"]
                    })
            if verify_answer(data, qst["question"], answer):
                print("correct answer ")
                score += 1
            else:
                print("wrong answer ")
                print(f"the right answer : {qst['answer']}")
        else:
            print("choose a valid answer")

    print(f"Your score is : {score}\\10")






def start_global_timer(limit):    # start the global timer
    """Lance un timer global pour le test."""
    global time_expired
    time_expired = False

    def timer_function():
        global time_expired
        time_expired = True
        print("\nTime is up ! The test has ended ")
        sys.exit()  # Exit the program when the timer is done

    timer = threading.Timer(limit, timer_function)
    timer.start()
    return timer


def time_limit(prompt, limit):     # limit the time for each question
    """Obtenir une réponse dans un délai donné."""
    timer = threading.Timer(limit, print, args=["\nTime is up for this question !"])
    timer.start()
    try:
        answer = input(prompt)
    except:
        answer = None
    timer.cancel()
    return answer

def export_qcm_result(name, date, questions, user_answers, score, filename):  # export the result of the MCQ
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Date: {date}\n\n")
        file.write("QCM Results:\n")
        for i, question in enumerate(questions):
            file.write(f"Question {i+1}: {question['question']}\n")
            file.write(f"Your Answer: {user_answers[i]}\n")
            if user_answers[i] != question['answer']:
                file.write(f"Correct Answer: {question['answer']}\n")
            file.write("\n")
        file.write(f"Score: {score}/{len(questions)}\n")

               
participant_file = "participants.json"    

data = load_data(participant_file)

print("--------------------------------Welcome to the QCM app--------------------------------")

name = input("Please enter your name : ")
date =  datetime.now().strftime("%d/%m/%Y")


if Verify_Participant(data, name):
    Show_Participant_history(name)
else:
    print("\n--------You are a new participant-----------\n\n")


timing_choice = input(" Choose the timing method : \n\t1- Limit time for each question\n\t2- Limit time for the entire test\n")

GLOBAL_TIMER_LIMIT = 60  # limit time for the entire test (in seconds)
QUESTION_TIMER_LIMIT = 10  # limit time for each question (in seconds)


if timing_choice == "1":  
    global_timer = None
    question_timer = QUESTION_TIMER_LIMIT
    print(f"\n----------------You have  {QUESTION_TIMER_LIMIT} secondes for each question----------------\n")
elif timing_choice == "2":  
    question_timer = None
    global_timer = GLOBAL_TIMER_LIMIT
    print(f"\n------------You have {GLOBAL_TIMER_LIMIT} secondes for the entire test------------\n")
else:
    print("invalid choice , you are not limited by time")
    question_timer = None
    global_timer = None


category = Choose_Category()
if category == "1" :
    Qcm_file = "QcmPython.json"
elif category == "2" :
    Qcm_file = "QcmAlgo.json"
elif category == "3" :  
    Qcm_file = "QcmNetwork.json"
elif category == "4" :
    Qcm_file = "QcmDB.json"
else :
    Qcm_file = "QcmAnimes.json"

category_name = Category_name(category)
data = load_data(Qcm_file)
score = 0
questions = []
user_answers = []
print("\n----------Here are the questions : \n")

Ask_Questions(data, timing_choice=timing_choice)

data = load_data(participant_file)

if Verify_Participant(data, name):
    data = Update_participant(data, name, date,category_name, score) 
else:
    data = Add_participant(data, name, date,category_name, score)           

save_data(participant_file, data)

# Export QCM results to a new file
result_filename = f"{name}-qcm-result.txt"
export_qcm_result(name, date, questions, user_answers, score, result_filename)
print(f"\nQCM results saved in {result_filename}")