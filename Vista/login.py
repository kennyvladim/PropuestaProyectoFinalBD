from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Vista.ventanaPrincipal import VentanaPrincipal

qtCreatorFile = "UI/login.ui" # Nombre del archivo aquí!!!
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/login.ui",self)
             
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()
        if usuario == "kenny" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()         
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos ingresados son incorrectos...!!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            #x = mensaje.exec_()