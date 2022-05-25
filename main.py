from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

app = QApplication([])

main_win = QWidget()
main_win.resize(600, 600)
main_win.setWindowTitle('Здоровье')
first_layout = QVBoxLayout()

timer = QLabel('00:00:00')
timer.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
fio = QLabel('Введите Ф.И.О:')
input_fio = QLineEdit()
ages = QLabel('Полных лет:')
input_ages = QLineEdit()
action1 = QLabel('''Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку "Начать первый тест,"
чтобы запустить таймер.\nРезультат запишите в соответствующее поле.''')
first_action_button = QPushButton('Начать первый тест.')
input_first_result = QLineEdit()
action2 = QLabel('''Выполните 30 приседаний за 45 секунд. Для этого нажмите на кнопку
"Начать делать приседания", чтобы запустить счетчик присдений''')
second_action_button = QPushButton('Начать делать приседания')
action3 = QLabel('''Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты,
а затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест",
чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо
проводить измерения, чёрным - минуты без замера пульса. Результаты
запишите в соответствующие поля.''')
final_action_button = QPushButton('Начать финальный тест')
input_final1 = QLineEdit()
input_final2 = QLineEdit()
send_results_button = QPushButton('Отправить результаты')

widgets_on_left = [fio, input_fio, ages, input_ages, action1,
                   first_action_button, input_first_result,
                   action2, second_action_button, action3,
                   final_action_button, input_final1, input_final2]
for el in widgets_on_left:
    if el == action2:
        timer_line = QVBoxLayout()
        timer_line.addWidget(action2, alignment=Qt.AlignLeft)
        timer_line.addWidget(timer, alignment=Qt.AlignRight)
        first_layout.addLayout(timer_line)
    else:
        first_layout.addWidget(el, alignment=Qt.AlignLeft)

first_layout.addWidget(send_results_button, alignment=Qt.AlignCenter)



main_win.setLayout(first_layout)
main_win.show()
app.exec_()
