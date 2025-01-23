def Add_participant (data , name , date ,category, score ) :

    new_participant = {

        "Name" : name,
        "Participations" : [{"Date": date ,"Category" : category ,"Score" : score}]
    }

    data.append(new_participant)

    return data

def Update_participant (data ,name  , date ,category, score ) :
    for participant in data :
        if participant["Name"] == name :
            participant["Participations"].append({"Date": date ,"Category" : category, "Score" : score})
            return data 

    return data