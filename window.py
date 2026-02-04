# pip install PyQt6 PyQt6-WebEngine
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys

class RobloxWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Roblox Browser")
        self.setGeometry(100, 100, 1200, 800)

        browser = QWebEngineView()
        browser.setUrl(QUrl("https://www.roblox.com/home"))
        self.setCentralWidget(browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobloxWindow()
    window.show()
    sys.exit(app.exec())