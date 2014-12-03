import sys, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from DownloadManager import DownloadManager

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dm = DownloadManager()
	dm.show()
	sys.exit(app.exec_())