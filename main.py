from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
import random
import menu
import database

app = QApplication([])
window = QWidget()
window.resize(500,500)

main_line = QVBoxLayout()
main_line2 = QHBoxLayout()
group_line = QVBoxLayout()
main_line3 = QHBoxLayout()
main_line4 = QHBoxLayout()
knopka1 = QPushButton("Меню")
knopka2 = QPushButton("Відпочити")
knopka_lbl = QPushButton("Відповісти")
asd = QSpinBox()
nadpus = QLabel("хвилин")
quest_lbl = QLabel("Яблуко")
group=QGroupBox()
qwa = QLabel("Варіанти відповідей:")
an1 = QRadioButton("bulding")
an2 = QRadioButton("apple")
an3 = QRadioButton("application")
an4 = QRadioButton("caterpillar")
nadpus2 = QLabel("Результат")
nadpus2.hide()
knopka21 = QPushButton("Наступне завдання")
knopka21.hide()

main_line2.addWidget(knopka1)
main_line2.addStretch(1)
main_line2.addWidget(knopka2)
main_line2.addWidget(asd)
main_line2.addWidget(nadpus)
main_line.addLayout(main_line2)
main_line.addWidget(quest_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

group_line.addWidget(qwa)
main_line3.addWidget(an1)
main_line3.addWidget(an2)
main_line4.addWidget(an3)
main_line4.addWidget(an4)
group_line.addLayout(main_line3)
group_line.addLayout(main_line4)
group_line.addWidget(nadpus2)
group.setLayout(group_line)
main_line.addWidget(group)
main_line.addWidget(knopka_lbl)
main_line.addWidget(knopka21)


answers = [an1,an2,an3,an4]
def set_quest():
    random.shuffle(answers)
    quest = database.questions[database.number]
    quest_lbl.setText(quest["Запитання"])
    answers[0].setText(quest["Відповідь"])
    answers[1].setText(quest["Неправильна Відповідь"])
    answers[2].setText(quest["Неправильна Відповідь"])
    answers[3].setText(quest["Неправильна Відповідь"])

set_quest()

def ans_func():
    answers[0].hide()
    answers[1].hide()
    knopka_lbl.hide()
    nadpus2.show()
    if answers[0].isChecked():
        nadpus2.setText("Правильно")
    else:
        nadpus2.setText("Неправильно")
knopka_lbl.clicked.connect(ans_func)

knopka1.clicked.connect(menu.menu_window)





window.setLayout(main_line)
window.show()
app.exec()