import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi('profile.ui', self)
        self.setWindowTitle("Профиль")


class Statistics(QMainWindow):
    def __init__(self):
        super(Statistics, self).__init__()
        loadUi('statistics.ui', self)
        self.setWindowTitle("Статистика")

class Achievements(QMainWindow):
    def __init__(self):
        super(Achievements, self).__init__()
        loadUi('achievements.ui', self)
        self.setWindowTitle("Достижения")

class CustomCabinet(QMainWindow):
    def __init__(self):
        super(CustomCabinet, self).__init__()
        loadUi('cabinet.ui', self)
        self.setWindowTitle("Личный кабинет")

        self.button_profile = self.findChild(QPushButton, 'profile')
        self.button_statistics = self.findChild(QPushButton, 'statistics')
        self.button_achievements = self.findChild(QPushButton, 'achievements')

        self.button_profile.clicked.connect(self.show_profile)
        self.button_statistics.clicked.connect(self.show_statistics)
        self.button_achievements.clicked.connect(self.show_achievements)

        self.profile_window = None
        self.statistics_window = None
        self.achievements_window = None

    def show_profile(self):
        if not self.profile_window:
            self.profile_window = Profile()
        self.profile_window.show()

    def show_statistics(self):
        if not self.statistics_window:
            self.statistics_window = Statistics()
        self.statistics_window.show()

    def show_achievements(self):
        if not self.achievements_window:
            self.achievements_window = Achievements()
        self.achievements_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cabinet = CustomCabinet()
    cabinet.show()
    sys.exit(app.exec_())