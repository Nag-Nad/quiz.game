import sys
import PySimpleGUI as sg

def ask_question(question, answer):
    layout = [
        [sg.Text(question)],
        [sg.Input(key="answer")],
        [sg.Button("Submit")]
    ]

    window = sg.Window("Quiz App", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Submit":
            user_answer = values["answer"].lower()
            if user_answer == answer.lower():
                sg.popup("Good job!")
                return 1
            else:
                sg.popup("Incorrect!")
                return -1

    window.close()

layout = [
    [sg.Text("Welcome to the Quiz Show. Please answer the questions. Each correct answer has one score.")],
    [sg.Text("Are you ready?")],
    [sg.Button("Yes"), sg.Button("No")]
]

window = sg.Window("Quiz App", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Yes":
        sg.popup("Let's Go!")
        break
    elif event == "No":
        sys.exit()

score = 0

score += ask_question("Which animal is known as the 'Ship of the Desert?", "Camel")
score += ask_question("Baby frog is known as.......", "Tadpole")
score += ask_question("Which is the smallest month of the year?", "February")
score += ask_question("Name the largest planet of our Solar System?", "Jupiter")
score += ask_question("Which festival is called the festival of colours?", "Holi")

sg.popup(f"Your score is {score}")
sg.popup("Your percentage is: " + str((score / 5) * 100))

window.close()
