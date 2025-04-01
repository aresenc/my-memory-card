from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

question_list = [Question("Сколько будет 2+10+3", "15", "20", "10", "2103"),
Question("Как будет на английском человек", "human", "animal", "book", "computer"),
Question("Каким символом обозначается сила притяжения", "g", "f", "h", "m")] 

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')
mw.resize(600,350)

btn = QPushButton("Ответить")
lb_question = QLabel("Сколько будет 2*2")

RadioGroupBox = QGroupBox("Варианты ответов")
rbt1 = QRadioButton("2")
rbt2 = QRadioButton("3")
rbt3 = QRadioButton("4")
rbt4 = QRadioButton("5")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt1)
RadioGroup.addButton(rbt2)
RadioGroup.addButton(rbt3)
RadioGroup.addButton(rbt4)

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()

Layout_ans2.addWidget(rbt1)
Layout_ans2.addWidget(rbt2)
Layout_ans3.addWidget(rbt3)
Layout_ans3.addWidget(rbt4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

AnsGroupBox = QGroupBox("Результаты теста")
lb_result = QLabel("правильно или нет")
lb_correct = QLabel("правильный ответ")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment = Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_correct, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addWidget(btn, alignment = Qt.AlignCenter)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

mw.setLayout(layout_card)

def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn.setText("Следующий вопрос")

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn.setText("Ответить")
        RadioGroup.setExclusive(False)
        rbt1.setChecked(False)
        rbt2.setChecked(False)
        rbt3.setChecked(False)
        rbt4.setChecked(False)
        RadioGroup.setExclusive(True)

def test():
    if btn.text() == 'Ответить':
        show_result()
    else:
        show_question()

answers = [rbt1, rbt2, rbt3, rbt4]

def ask(q):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_question.setText(q.question)
        lb_correct.setText(q.right_answer)
        show_question()

def show_correct(res):
        lb_result.setText(res)
        show_result()

def check_answer():
        if answers[0].isChecked():
                show_correct("Правильно")
                mw.score +=1
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct("Неправильно")
        print(f"Статистика\n-Всего вопросов: {mw.total}\n-Всего ответов: {mw.score}")
        print(f"Рейтинг: {mw.score/mw.total*100}%")

def next_qustion():
        if len(question_list) > 0:
                cur_question = randint(0, len(question_list) - 1)
                mw.total += 1
                print(f"Статистика\n-Всего вопросов: {mw.total}\n-Всего ответов {mw.score}")
                q = question_list[cur_question]
                ask(q)
                question_list.pop(cur_question)

def click_OK():
        if btn.text() == "Ответить":
                check_answer()
        else:
                next_qustion()

mw.cur_question = -1
btn.clicked.connect(click_OK)
mw.total = 0
mw.score = 0
next_qustion()

mw.show()
app.exec()