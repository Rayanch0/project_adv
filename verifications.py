def Verify_Participant (data , name) :
    for participant in data :
        if participant["Name"] == name :
            return True
    return False

def verify_answer(data , question , answer) :
    for qst in data :
        if qst["question"] == question :
            if qst["answer"] == answer :
                return True
            else :
                return False