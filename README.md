# project_adv
# QCM Application for Students

## Overview
This Python-based application allows students to participate in quizzes (QCM), track their progress, and view their performance history. The app provides a user-friendly console interface and supports multiple categories of questions.

## Features
1. **User Management**:
   - Existing users can view their quiz history.
   - New users can register and start fresh.
2. **Quiz Categories**:
   - Python
   - Algorithmics
   - Networks
   - Databases
   - Animes
3. **Scoring and Feedback**:
   - Each quiz question provides immediate feedback on correctness.
   - Final score is displayed at the end of the quiz.
4. **Timer Options**:
   - Limit time per question.
   - Limit total time for the entire quiz.
5. **Data Persistence**:
   - User data and quiz results are stored in JSON files for future retrieval.

## How It Works
1. **Start the App**:
   Run the script to access the application.
2. **Enter Your Name**:
   - If you're an existing user, your quiz history will be displayed.
   - If you're a new user, you'll be registered automatically.
3. **Choose a Quiz Category**:
   Select one of the available categories.
4. **Select Timing Mode**:
   - Per-question timer: Each question has a time limit.
   - Global timer: The entire quiz has a total time limit.
5. **Answer Questions**:
   Provide your answers to the displayed questions.
6. **View Results**:
   See your score and receive feedback on each question.
7. **Save Data**:
   Results are automatically saved to `participants.json`.

## File Structure
- **`participants.json`**: Stores user data, including name, quiz history (date, category, score).
- **`QcmPython.json`, `QcmAlgo.json`, `QcmNetwork.json`, `QcmDB.json`, `QcmAnimes.json`**: Contain quiz questions and answers for each category.
- **Main Script**: Implements user interaction, question management, and timing logic.

## Key Functions
- `Add_participant(data, name, date, category, score)`: Registers a new user.
- `Update_participant(data, name, date, category, score)`: Updates an existing user's quiz history.
- `Show_Participant_history(name)`: Displays the quiz history of a user.
- `Choose_Category()`: Allows the user to select a quiz category.
- `Ask_Questions(data, timing_choice, question_timer, global_timer)`: Handles the quiz process.
- `save_data(filename, data)` and `load_data(filename)`: Save and load data from JSON files.
- `start_global_timer(limit)` and `time_limit(prompt, limit)`: Implement timing features.

## Usage Instructions
1. Clone the repository or download the script.
2. Ensure Python 3.x is installed on your system.
3. Place the necessary JSON files (`participants.json` and question sets) in the same directory as the script.
4. Run the script:
   ```bash
   python qcm_app.py
   ```
5. Follow the on-screen instructions to participate in a quiz.

## Future Improvements
- Implement a graphical user interface (GUI).

## Example
### Console Output
```text
--------------------------------Welcome to the QCM app--------------------------------
Please enter your name : Alice
Your name is : Alice 
Date : 2024-12-15 , Category : Python , Score : 8

----------Here is the questions : 
Choose a category : 
	1-Python
	2-Algorithmics
	3-Network
	4-Databases
	5-Animes
2
Choose the timing method : 
	1- Limit time for each question
	2- Limit time for the entire test
1
Vous avez 10 secondes pour chaque question.
Question 1: What is the time complexity of binary search?
	a) O(1)
	b) O(log n)
	c) O(n)
choose an answer: b
Correct answer!
...
Test terminÃ© ! Votre score est : 7/10
```

## Contributors
- **Instructor**: MOUHOUN Said ([Email](mailto:s.mouhoun@gmail.com))
- **University**: USTHB - ENG-3 Cyber Security

## License
This project is for educational purposes and adheres to university guidelines.
