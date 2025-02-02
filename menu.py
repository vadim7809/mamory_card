from PyQt6.QtWidgets import *

import database


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Запитання")
    quest_input = QLineEdit()
    right_answer = QLabel("Правильна відоповідь")
    lose_answer1 = QLabel("Неправильна відповідь")
    lose_answer2 = QLabel("Неправильна відповідь")
    lose_answer3 = QLabel("Неправильна відповідь")


    main_line = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    main_line.addWidget(h1)

    h2 = QHBoxLayout()
    h2.addWidget(right_answer)
    h2.addWidget(lose_answer1)
    h2.addWidget(lose_answer2)
    h2.addWidget(lose_answer3)
    main_line.addLayout(h2)

    def add_func():
        database.questions.append(
            {
                "Запитання": quest_input.text(),
                "Відповідь": right_answer.text(),
                "Неправильна Відповідь1": lose_answer1,
                "Неправильна Відповідь2": lose_answer2,
                "Неправилина Відповідь3": lose_answer3,
            }
        )

    window.setLayout(main_line)
    window.exec()