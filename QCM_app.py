def Show_Participant_history (name) :
    for participant in data :
        if participant["Name"] == name :
            print(f"Your name is : {participant['Name']} " )

            for participation in participant['Participations'] :
                print(f"Date : {participation['Date']} , Score : {participation['Score']}" )

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []