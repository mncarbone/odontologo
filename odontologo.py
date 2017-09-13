from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi
from sqlite3 import connect

class SistemaOdontologo(QApplication):

    def iniciar(self):
        self.ui = loadUi('pacientes.ui')
        self.ui.buttonBox.accepted.connect(self.btnBox_accepted)
        self.ui.show()
        self.exec()

    def btnBox_accepted(self):
        print('Guardando registro en la base de datos...')
        #Obtener datos de la UI
        dni = self.ui.txtDni.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        #Armar SQL
        sql = "INSERT INTO pacientes(dni, nombre, apellido) "
        sql+= "VALUES ('" + dni + "', '" + nombre + "', '" + apellido + "');"
        #Ejecutar SQL
        conexion = connect('odontologo.db')
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
        
app = SistemaOdontologo([])
app.iniciar()
