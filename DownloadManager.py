from PyQt4.QtGui import *
from PyQt4.QtCore import *
from urllib import urlretrieve
import os.path

class DownloadManager(QWidget):
	def __init__(self,parent=None):
		super(DownloadManager,self).__init__(parent)

		self.uriLabel = QLabel('Enter URI:')
		self.uriText = QLineEdit()
		self.uriText.setText("http://ts4.mm.bing.net/th?id=HN.607990966594438367&w=113&h=155&c=7&rs=1&pid=1.7")

		self.destinationLbl = QLabel("Type destination:")
		self.destinationDirName = QLineEdit()
		self.destinationDirName.setText("./downloaded")

		self.downloadBtn = QPushButton("Download")
		self.closeBtn = QPushButton("Exit")


		layout = QGridLayout()

		layout.addWidget(self.uriLabel)
		layout.addWidget(self.uriText)
		layout.addWidget(self.destinationDirName)
		layout.addWidget(self.downloadBtn)
		layout.addWidget(self.closeBtn)

		self.setLayout(layout)

		self.connect(self.downloadBtn,SIGNAL("clicked()"),self,SLOT("onDownloadBtnClicked()"))
		self.connect(self.closeBtn,SIGNAL("clicked()"),self,SLOT("close()"))

	@pyqtSlot()
	def onDestinationBtnClicked(self):
		pass

	@pyqtSlot()
	def onDownloadBtnClicked(self,url=""):
		destDir = str(self.destinationDirName.text())
		if self.isDestinationDir(destDir):
			testUrl = 'http://ts4.mm.bing.net/th?id=HN.607990966594438367&w=113&h=155&c=7&rs=1&pid=1.7'
			destination = testUrl.rsplit('/',1)[1]
			urlretrieve(testUrl, destDir+'/'+destination)
			self.show_info("Downloaded to %s"%(self.destinationDirName.text()+'/'+destination))
		else:
			self.show_info("Directory %s does not exist. Check it and try again."%(self.destinationDirName.text()))

	def show_info(self,e):
		msgBox = QMessageBox()
		msgBox.setText(str(e))
		msgBox.setStandardButtons(QMessageBox.Ok)
		ret = msgBox.exec_();

	def isDestinationDir(self,dirName):
		if os.path.exists(dirName):
			print "Directory exists."
			return True
		print "Directory does not exist"
		return False


