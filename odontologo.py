from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi

class SistemaOdontologo(QApplication):

    def iniciar(self):
        self.ui = loadUi('pacientes.ui')
        self.ui.show()
        self.exec()

app = SistemaOdontologo([])
app.iniciar()
