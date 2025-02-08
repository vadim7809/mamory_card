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
Menu = QPushButton("Меню")
Vidpoch = QPushButton("Відпочити")
vidpovis_lbl = QPushButton("Відповісти")
asd = QSpinBox()
min = QLabel("хвилин")
quest_lbl = QLabel("Яблуко")
group=QGroupBox()
qwa = QLabel("Варіанти відповідей:")
an1 = QRadioButton("bulding")
an2 = QRadioButton("apple")
an3 = QRadioButton("application")
an4 = QRadioButton("caterpillar")
result_lbl = QLabel("Результат")
result_lbl.hide()
next_qes = QPushButton("Наступне завдання")
next_qes.hide()

main_line2.addWidget(Menu)
main_line2.addStretch(1)
main_line2.addWidget(Vidpoch)
main_line2.addWidget(asd)
main_line2.addWidget(min)
main_line.addLayout(main_line2)
main_line.addWidget(quest_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

group_line.addWidget(qwa)
main_line3.addWidget(an1)
main_line3.addWidget(an2)
main_line4.addWidget(an3)
main_line4.addWidget(an4)
group_line.addLayout(main_line3)
group_line.addLayout(main_line4)
group_line.addWidget(result_lbl)
group.setLayout(group_line)
main_line.addWidget(group)
main_line.addWidget(vidpovis_lbl)
main_line.addWidget(next_qes)


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
    vidpovis_lbl.hide()
    result_lbl.show()
    if answers[0].isChecked():
        result_lbl.setText("Правильно")
    else:
        result_lbl.setText("Неправильно")
vidpovis_lbl.clicked.connect(ans_func)

Menu.clicked.connect(menu.menu_window)





window.setLayout(main_line)
window.show()
app.exec()