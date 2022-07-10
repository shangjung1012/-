from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
from pathlib import Path
from function import download
import sys

# path = Path(__file__).parent # 取得檔案所在資料夾之位置
path = Path(sys.argv[0]).parent
path_download = path/'download'# 設定在同目錄下的download資料夾

            
    
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        

    def setup_control(self):
        self.setLayout(self.ui.gridLayout)
        self.ui.folder_path.setText(str(path_download.absolute()))
        self.ui.change_folder.clicked.connect(self.change_folder)
        self.ui.Download_Button.clicked.connect(self.download_genus)   
    
    def change_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")    # start path
        self.ui.folder_path.setText(folder_path)

        
    def download_genus(self):
        genuses = self.ui.genus.text().split(';')
        folder_path = Path(self.ui.folder_path.toPlainText())
        for s in download(genuses, folder_path):
            self.ui.logview.append(s) #append string
            QtWidgets.QApplication.processEvents() #update gui for pyqt
            

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
