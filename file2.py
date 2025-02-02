import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(500, 500)

main_line = QVBoxLayout()
Menu = QPushButton("Меню")
Vidpoch = QPushButton("Відпочити")
vidpovis = QPushButton("Відповісти")
next_qes = QPushButton("Наступне запитання")
next_qes.hide()

spin = QSpinBox()
min = QLabel("хвилини")
quest_lbl = QLabel("Яблуко")

group = QGroupBox("Варіанти відповідей")
answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton("caterpillar")
answer3_btn = QRadioButton("apple")
answer4_btn = QRadioButton("application")
result_lbl = QLabel("Результат")
result_lbl.hide()
next_btn= QPushButton("Наступне запитання")
next_btn.hide()

h1 = QHBoxLayout()
h1.addWidget(Menu)
h1.addStretch(1)
h1.addWidget(Vidpoch)
h1.addWidget(spin)
h1.addWidget(min)
main_line.addLayout((h1))

h2 = QHBoxLayout()
h3 = QHBoxLayout()

main_line.addWidget(quest_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

group_line = QVBoxLayout()
h2.addWidget(answer1_btn)
h2.addWidget(answer2_btn)
h3.addWidget(answer3_btn)
h3.addWidget(answer4_btn)
group_line.addLayout(h2)
group_line.addLayout(h3)
group_line.addWidget(result_lbl)
group.setLayout(group_line)

main_line.addWidget(group)

main_line.addWidget(vidpovis)
main_line.addWidget(next_qes)

answers = [answer1_btn, answer2_btn, answer3_btn, answer4_btn]

def set_quest():
    random.shuffle

window.setLayout(main_line)
window.show()
app.exec()