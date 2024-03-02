from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMainWindow
from recorder import record_audio
import sys
from os import listdir, path, remove
from PyQt5.uic import loadUiType

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "mainWin.ui"))
class VoiceRecorder(QMainWindow, FORM_CLASS):
  def __init__(self, parent=None):
    super(VoiceRecorder, self).__init__(parent)
    QMainWindow.__init__(self, parent=None)
    self.setupUi(self)
    self.setWindowTitle("Voice recorder")
    self.record_button.clicked.connect(self.record_voice)

  def record_voice(self):
    filename = self.filename_lineedit.text()
    try:
      record_audio(filename=filename)
      self.status_label.setText(f"Voice recorded and saved as '{filename}'")
    except Exception as e:
      self.status_label.setText(f"Error recording: {e}")

if __name__ == "__main__":
  app = QApplication([])
  window = VoiceRecorder()
  window.show()
  app.exec_()
