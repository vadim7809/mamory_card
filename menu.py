from PyQt6.QtWidgets import*

import database


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Запитання")
    quest_input = QLineEdit()
    right_answer = QLabel("Правильна відповідь")
    right_input = QLineEdit()
    wrong_answer1 = QLabel("Неправильна відповідь")
    wrong_input1 = QLineEdit()
    wrong_answer2 = QLabel("Неправильна відповідь")
    wrong_input2 = QLineEdit()
    wrong_answer3 = QLabel("Неправильна відповідь")
    wrong_input3 = QLineEdit()

    add_lbl = QPushButton("Додати")


    main_line = QVBoxLayout()

    h2 = QHBoxLayout()
    h2.addWidget(right_answer)
    h2.addWidget(right_input)

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    main_line.addLayout(h1)




    h3 = QHBoxLayout()
    h3.addWidget(wrong_answer1)
    h3.addWidget(wrong_input1)

    h4 = QHBoxLayout()
    h4.addWidget(wrong_answer2)
    h4.addWidget(wrong_input2)

    h5 = QHBoxLayout()
    h5.addWidget(wrong_answer3)
    h5.addWidget(wrong_input3)

    main_line.addLayout(h2)
    main_line.addLayout(h5)
    main_line.addLayout(h3)
    main_line.addLayout(h4)
    main_line.addWidget(add_lbl)


    window.setLayout(main_line)


    def add_func():
        database.questions.append(
            {
       "Запитання": quest_lbl.text(),
       "Відповідь": right_answer.text(),
       "Неправильна Відповідь": wrong_answer1.text(),
       "Неправильна Відповідь2": wrong_answer2.text(),
       "Неправилина Відповідь3": wrong_answer3.text(),
    }
        )
    add_lbl.clicked.connect(add_func)






    window.exec()