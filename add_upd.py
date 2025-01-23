def Add_participant (data , name , date , score ) :

    new_participant = {

        "Name" : name,
        "Participations" : [{"Date": date , "Score" : score}]
    }

    data.append(new_participant)

    return data

def Update_participant (data ,name  , date , score ) :
    for participant in data :
        if participant["Name"] == name :
            participant["Participations"].append({"Date": date , "Score" : score})
            return data 

    return data
