import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

antikeimeno = QtGui.QWidget()

print dir(antikeimeno)

antikeimeno.setGeometry(300,300,300,300)
antikeimeno.setWindowTitle('Aplo programma')
antikeimeno.show()

sys.exit(app.exec_())
