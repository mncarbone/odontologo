from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi

class SistemaOdontologo(QApplication):

    def iniciar(self):
        self.ui = loadUi('pacientes.ui')
        self.ui.buttonBox.accepted.connect(self.btnBox_accepted)
        self.ui.show()
        self.exec()

    def btnBox_accepted(self):
        print('Guardando registro en la base de datos...')

app = SistemaOdontologo([])
app.iniciar()
