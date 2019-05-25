import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QShortcut, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtSql, QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
import sys
from main import Ui_MainWindow

url = "https://www.thetoptens.com/best-movie-villain-quotes/"

# game_state = True
# browser = webdriver.Firefox()
# browser.get(url)
# load_more = browser.find_element_by_id("loadmore")
# load_more.click()
# time.sleep(0.2)
# # game_active = True

# res = requests.get(url)
# soup = BeautifulSoup(res.text, "html.parser")
# quotes = soup.div.find_all("b")[1:]
# soup.find(class_="bluebutton")


class MainWindow(QMainWindow):
    """docstring for quote guessing game"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #button functions
        self.ui.nextButton.clicked.connect(self.say_hi)

# def initial_game_state():
#     print("Guess the name of the film based off the villain quote!")
#     get_movie_quote()

    def say_hi(self):
        self.ui.quotesBox.setText("Hello")



# def get_movie_quote():
#     game_active = True
#     score = 0
#     while game_active:
#         game_question = random.choice(quotes).text
#         correct_answer = game_question.rpartition("(")[2][:-1].upper()
#         print(game_question.rpartition("-")[0])
#         print(correct_answer)
#         answer = input("Name of movie: ").upper()
#         if answer == correct_answer:
#             print("Nice Job! You got it")
#             score += 1
#             print(f"You got {score} points")
#         else:
#             game_active = False
#             print("goodbye")
#     else:
#         print("would you like to play again? y/n")








    # print(quotes)
    # quotes = [quotes.text for quotes in soup.div.select("b")[1:]]
    # print(quotes)
    # split_quote = quotes.split(separate, 1)[0]
    # print(split_quote)
    # print(i)
    # quotes = soup.find(class_="i").next_sibling
    # while not url.endswith("#"):
    #     #request quotes
    #     res = requests.get(url)
    #     res.raise_for_status()


if __name__=="__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
# initial_game_state()
