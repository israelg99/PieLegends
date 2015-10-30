import sys

from PyQt5.QtGui import QFont, QPalette, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QDesktopWidget, \
    QWidget, QLabel, QLineEdit, QPushButton, QComboBox

from pielegends.PieLegends import PieLegends


class Window():
    
    defaultRegion = "North America"
    labelFont = QFont("Lucida Sans", 16, QFont.Bold)
    buttonFont = QFont("Lucida Sans", 10, QFont.Thin)
    inputFont = QFont("Century Gothic", 10, QFont.Thin)
    
    def __init__(self, version, width=600, height=420, dense = 6, title="Pie Legends", isDark=False):
        
        self.app = QApplication(sys.argv)
        self._window = QMainWindow()
        
        self.dense = dense
        
        self.window.statusBar().showMessage('Initiating..')
        self.initWindow(width, height, title, version, isDark)
        self.window.statusBar().showMessage('Ready..')
        
        sys.exit(self.app.exec_())
    
    @property
    def window(self):
        return self._window;

    def initWindow(self, width, height, title, version, isDark):       
        
        self.window.setWindowTitle(title  + " " + version)
        
        self.window.resize(width, height)
        self.centerWindow();
        
        self.window.setAutoFillBackground(True)
        self.window.setBackgroundRole(QPalette.AlternateBase if isDark else QPalette.Dark)
        
        self.window.setWindowIcon(QIcon('../assets/icon.png'))
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.initCentralWidget(isDark);
        
        self.window.show()
        
    def centerWindow(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
        
    def initCentralWidget(self, isDark):
        
        """ Logo """
        self.window.setCentralWidget(QWidget())
        self.window.centralWidget().setAutoFillBackground(True)
        self.window.centralWidget().setBackgroundRole(QPalette.Dark if isDark else QPalette.AlternateBase)
        
        self.picLabel = QLabel(self.window.centralWidget())
        pic = QPixmap("../assets/logo.png")
        self.picLabel.setPixmap(pic)
        self.picLabel.move(self.window.width()/2-pic.width()/2, 15)
        
        funcLine = pic.height()+50;
        
        
        
        
        """ Champion Section """
        
        """ Initiate """
        self.championLabel = QLabel(self.window.centralWidget())
        self.championLabel.setText("Enter Champion")
        self.championLabel.setFont(self.labelFont)
        
        championLabelWidth = self.championLabel.fontMetrics().boundingRect(self.championLabel.text()).width()
        championLabelHeight = self.championLabel.fontMetrics().boundingRect(self.championLabel.text()).height()
        
        self.championEdit = QLineEdit(self.window.centralWidget())
        self.championEdit.setFont(self.inputFont)
        
        self.countersBtn = QPushButton('Counters', self.window.centralWidget())
        self.countersBtn.setToolTip('Champion counters!')
        self.countersBtn.resize(self.countersBtn.sizeHint())
        self.countersBtn.setFont(self.buttonFont)
        
        self.buildsBtn = QPushButton('Builds', self.window.centralWidget())
        self.buildsBtn.setToolTip('Champion builds!')
        self.buildsBtn.setFont(self.buttonFont)
        
        """ Resize """
        self.buildsBtn.resize(self.buildsBtn.sizeHint())
        self.championEdit.resize(self.countersBtn.width() + self.buildsBtn.width(), 20)
        
        """ Move """
        self.championEdit.move(self.window.width()/self.dense, funcLine + championLabelHeight + 3)
        
        self.countersBtn.move(self.championEdit.x(), self.championEdit.y() + self.countersBtn.height())
        
        self.championLabel.move(self.championEdit.x()+self.championEdit.width()/2-championLabelWidth/2, funcLine)
        
        self.buildsBtn.move(self.championEdit.x() + self.countersBtn.width(), self.championEdit.y() + self.buildsBtn.height())
        
        """ Event Handling """
        self.buildsBtn.clicked.connect(self.handleBuildsBtn)
        self.countersBtn.clicked.connect(self.handleCountersBtn)
        
        self.championEdit.returnPressed.connect(self.countersBtn.click)
        
        
        
        
        """ Player Section """
        
        """ Initiate """
        self.playerLabel = QLabel(self.window.centralWidget())
        self.playerLabel.setText("Enter Player")
        
        self.playerLabel.setFont(self.labelFont)
        
        playerLabelWidth = self.playerLabel.fontMetrics().boundingRect(self.playerLabel.text()).width()
        playerLabelHeight = self.playerLabel.fontMetrics().boundingRect(self.playerLabel.text()).height()
        
        self.regionCheck = QComboBox(self.window.centralWidget())
        self.regionCheck.addItems(["North America", "Europe West", "EU Nordic & East", "Korea", "Russia", "Oceania", "Brazil", "Turkey", "Latin America North", "Latin America South"])
        self.regionCheck.setCurrentText("North America")
        PieLegends.regionUpdate(self.regionCheck.currentText())
        
        self.playerEdit = QLineEdit(self.window.centralWidget())
        self.playerEdit.setFont(self.inputFont)
        
        self.playerBtn = QPushButton('Search', self.window.centralWidget())
        self.playerBtn.setToolTip('Pie a player!')
        self.playerBtn.setFont(self.buttonFont)
        
        """ Resize """
        self.playerBtn.resize(self.playerBtn.sizeHint())
        self.playerEdit.resize(self.playerBtn.width()*2, 20)
        
        """ Move """
        self.regionCheck.move(0, funcLine + playerLabelHeight + 3) # We move the Y first
        
        playerEditWidth = self.playerEdit.frameGeometry().width()
        
        self.playerEdit.move(self.window.width()-self.window.width()/self.dense-playerEditWidth, self.regionCheck.y() + self.regionCheck.height()-6)
        
        self.playerLabel.move(self.playerEdit.x() + self.playerEdit.width()/2 - playerLabelWidth/2, funcLine)
        
        self.regionCheck.move(self.playerEdit.x(), self.regionCheck.y()) # Now we move just the X after all the sizes been formed
        
        self.playerBtn.move(self.playerEdit.x() + self.playerEdit.width()/2 - self.playerBtn.width()/2, self.playerEdit.y() + self.playerBtn.height())
        
        """ Event Handling """
        self.playerBtn.clicked.connect(self.handlePlayerBtn)
        
        self.playerEdit.returnPressed.connect(self.playerBtn.click)
    
        self.regionCheck.activated[str].connect(self.handleRegionCheck)
    
    
    """ Buttons - Event Handling Methods """      
    def handleBuildsBtn(self):
        PieLegends.championBuilds(self.championEdit.text())
    
    def handleCountersBtn(self):
        PieLegends.championCounters(self.championEdit.text())
        
    def handlePlayerBtn(self):
        PieLegends.playerPie(self.playerEdit.text())
        
    """ Combo Box - Event Handling Methods """
    def handleRegionCheck(self, region):
        PieLegends.regionUpdate(region)
        
        