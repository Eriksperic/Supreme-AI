import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import numpy as np
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.setWindowTitle("Neural Network Manager")

      self.grid = QGridLayout()
      self.vBox = QVBoxLayout()
      self.hBox = QHBoxLayout() # Main layout

      self.vBox.setSpacing(1)

      self.button = QPushButton("Browse")
      self.image_label = QLabel()
      self.image_label.setFixedSize(200, 200)
      self.image_label.setStyleSheet("border: 1px solid black;")

      self.image_title = QLabel("Imported Image Title Here")

      self.button.clicked.connect(self.open_image)

      self.vBox.addWidget(self.image_label, 0)
      self.vBox.addWidget(self.image_title, 0)
      self.vBox.addWidget(self.button, 0)

      self.hBox.addLayout(self.vBox)


      self.hBox.addWidget()


      self.resize(200, 300)
      self.setLayout(self.hBox)

   def open_image(self):
      options = QFileDialog.Options()
      options |= QFileDialog.ReadOnly
      file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                 "Image Files (*.png *.jpg *.bmp *.gif);;All Files (*)",
                                                 options=options)
      if file_name:
         pixmap = QPixmap(file_name)
         self.image_title.setText(file_name)
         image = pixmap.toImage()
         self.qimage_to_numpy(image)
         scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.FastTransformation)
         self.image_label.setPixmap(scaled_pixmap)
         self.image_label.setScaledContents(True)

   def qimage_to_numpy(self, qimage):
      width = qimage.width()
      height = qimage.height()
      channels = 3  # (RGB)

      ptr = qimage.bits()
      ptr.setsize(height * width * channels)
      arr = np.array(ptr).reshape(height, width, channels)

      return arr

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()