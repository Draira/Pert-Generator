from camino_mas_largo import Calculate_pert
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Resolver = QtWidgets.QPushButton(self.centralwidget)
        self.Resolver.setGeometry(QtCore.QRect(500, 460, 161, 61))
        self.Resolver.setObjectName("Resolver")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(70, 20, 651, 401))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 460, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.cantidad_actividades = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidad_actividades.setGeometry(QtCore.QRect(310, 380, 211, 41))
        self.cantidad_actividades.setObjectName("cantidad_actividades")
        self.TItulo = QtWidgets.QLabel(self.centralwidget)
        self.TItulo.setGeometry(QtCore.QRect(140, 20, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TItulo.setFont(font)
        self.TItulo.setObjectName("TItulo")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(80, 380, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.Instrucciones = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Instrucciones.setEnabled(True)
        self.Instrucciones.setGeometry(QtCore.QRect(73, 87, 651, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Instrucciones.setFont(font)
        self.Instrucciones.setAutoFillBackground(False)
        self.Instrucciones.setReadOnly(True)
        self.Instrucciones.setObjectName("Instrucciones")
        self.texto_error = QtWidgets.QLabel(self.centralwidget)
        self.texto_error.setGeometry(QtCore.QRect(70, 480, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.texto_error.setFont(font)
        self.texto_error.setAlignment(QtCore.Qt.AlignCenter)
        self.texto_error.setObjectName("texto_error")
        self.Inicio_button = QtWidgets.QPushButton(self.centralwidget)
        self.Inicio_button.setGeometry(QtCore.QRect(500, 460, 161, 61))
        self.Inicio_button.setObjectName("Inicio_button")
        self.Tabla_solucion = QtWidgets.QTableWidget(self.centralwidget)
        self.Tabla_solucion.verticalHeader().setVisible(False)
        self.Tabla_solucion.setGeometry(QtCore.QRect(95, 21, 611, 271))
        self.Tabla_solucion.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Tabla_solucion.setObjectName("Tabla_solucion")
        self.Tabla_solucion.setColumnCount(4)
        self.Tabla_solucion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_solucion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_solucion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_solucion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_solucion.setHorizontalHeaderItem(3, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(100, 310, 361, 121))
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.Duracion_final = QtWidgets.QLabel(self.centralwidget)
        self.Duracion_final.setGeometry(QtCore.QRect(600, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Duracion_final.setFont(font)
        self.Duracion_final.setObjectName("Duracion_final")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.camino = []
        self.tiempos_tar_tem = []

        self.pushButton.clicked.connect(self.Generate)

        self.Resolver.clicked.connect(self.Solve)

        self.Inicio_button.clicked.connect(self.Return_init)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pert PG"))
        self.Resolver.setText(_translate("MainWindow", "Resolver"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Actividad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actividades Sucesoras"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempo pesimista"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tiempo probable"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo Optimista"))
        self.pushButton.setText(_translate("MainWindow", "Generar"))
        self.TItulo.setText(_translate("MainWindow", "Generador de problemas PERT:"))
        self.label1.setText(_translate("MainWindow", "Cantidad de actividades:"))
        self.Instrucciones.setPlainText(_translate("MainWindow", "Instrucciones:\n"
"\n"
"1) Ingresa en la casilla inferior la cantidad de actividades.\n"
"2) Haz click en el botón \"Generar\" para crear un problema de forma aleatorio con el valor ingresado.\n"
"3) Una vez creado, se presentará una tabla con la información relevante del problema para ser desarrollado a mano.\n"
"4) Haz click en el botón \"Resolver\" para ver la solución.\n"
"\n"
"Nota: Para el calculo de la esperanza se aplica la regla del redondeo."
))
        self.texto_error.setText(_translate("MainWindow", "¡Favor ingresa un número!"))
        self.Inicio_button.setText(_translate("MainWindow", "Inicio"))
        item = self.Tabla_solucion.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Actividad"))
        item = self.Tabla_solucion.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tiempos Tempranos"))
        item = self.Tabla_solucion.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempos Tardios"))
        item = self.Tabla_solucion.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Holgura"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Caminos Criticos"))
        self.Duracion_final.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Duración:"))
        self.texto_error.hide()
        self.tableWidget.hide()
        self.Resolver.hide()
        self.Inicio_button.hide()
        self.tableWidget_2.hide()
        self.Tabla_solucion.hide()
        self.label.hide()
        self.Duracion_final.hide()

    

    def Generate(self):
            number = self.cantidad_actividades.text()
            if(number!= '' and number.isnumeric()):
                self.texto_error.hide()
                nodes = int(number)
                lis_node,conec,corto,tt = Calculate_pert(nodes)
                self.cantidad_actividades.clear()

                #Añadir elementos a la tabla:

                for i in lis_node:
                    nodo_i = str(i[0])
                    #print(nodo_i)
                    tupla = i[1]
                    #print(tupla)
                    opti = str(tupla[0])
                    prob = str(tupla[1])
                    pesi = str(tupla[2])

                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    rows = self.tableWidget.rowCount()
                    #self.tableWidget.setItem(rows-1, QtWidgets.QTableWidgetItem("hola"))
                    item0 = QtWidgets.QTableWidgetItem(nodo_i)
                    item0.setTextAlignment(QtCore.Qt.AlignCenter)
                    item2 = QtWidgets.QTableWidgetItem(pesi)
                    item2.setTextAlignment(QtCore.Qt.AlignCenter)
                    item3 =QtWidgets.QTableWidgetItem(prob)
                    item3.setTextAlignment(QtCore.Qt.AlignCenter)
                    item4 = QtWidgets.QTableWidgetItem(opti)
                    item4.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(rows-1, 0, item0)
                    self.tableWidget.setItem(rows-1, 2, item2)
                    self.tableWidget.setItem(rows-1, 3, item3)
                    self.tableWidget.setItem(rows-1, 4, item4)
                    self.tableWidget.verticalHeader().setVisible(False)
                    self.tableWidget.resizeColumnsToContents()
                    

                for i in range(len(lis_node)):
                    conexiones = []
                    for j in conec:
                        if(j[0] == i+1):
                            conexiones.append(j[1])
                        item1 = QtWidgets.QTableWidgetItem(str(conexiones))
                        item1.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tableWidget.setItem(i,1, item1)


                header = self.tableWidget.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.show()
                self.Resolver.show()
                self.TItulo.hide()
                self.cantidad_actividades.hide()
                self.pushButton.hide()
                self.label1.hide()
                self.Instrucciones.hide()

                self.camino = corto
                self.tiempos_tar_tem = tt
            else:
                self.cantidad_actividades.clear()
                self.texto_error.show()

    def Solve(self):

        for i in self.tiempos_tar_tem:
            nodo_i = str(i[0])
            #print(nodo_i)
            tiempo_temp = str(i[1])
            #print(tupla)
            tiempo_tar = str(i[2])
            Holg = str(i[3])

            rowPosition = self.Tabla_solucion.rowCount()
            self.Tabla_solucion.insertRow(rowPosition)
            rows = self.Tabla_solucion.rowCount()
            item0 = QtWidgets.QTableWidgetItem(nodo_i)
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item1 = QtWidgets.QTableWidgetItem(tiempo_temp)
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item2 =QtWidgets.QTableWidgetItem(tiempo_tar)
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            item3 = QtWidgets.QTableWidgetItem(Holg)
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Tabla_solucion.setItem(rows-1, 0, item0)
            self.Tabla_solucion.setItem(rows-1, 1, item1)
            self.Tabla_solucion.setItem(rows-1, 2, item2)
            self.Tabla_solucion.setItem(rows-1, 3, item3)
            self.Tabla_solucion.verticalHeader().setVisible(False)
            self.Tabla_solucion.resizeColumnsToContents()

        header = self.Tabla_solucion.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.Tabla_solucion.resizeColumnsToContents()

        rutas_criticas = self.camino[0]
        duracion_total = self.camino[1]

        for i in rutas_criticas:

            rowPosition2 = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition2)
            rows2 = self.tableWidget_2.rowCount()
            item0 = QtWidgets.QTableWidgetItem(str(i))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_2.setItem(rows2-1, 0, item0)
            self.Tabla_solucion.resizeColumnsToContents()


        header = self.tableWidget_2.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.resizeColumnsToContents()

        self.Duracion_final.setText(str(duracion_total))


        self.tableWidget.hide()
        self.Resolver.hide()
        self.Inicio_button.show()
        self.Tabla_solucion.show()
        self.tableWidget_2.show()
        self.label.show()
        self.Duracion_final.show()


    def Return_init(self):

        self.Tabla_solucion.hide()
        self.tableWidget_2.hide()
        self.label.hide()
        self.Duracion_final.hide()
        self.Inicio_button.hide()


        self.Tabla_solucion.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.Duracion_final.setText(str(0))

        self.TItulo.show()
        self.Instrucciones.show()
        self.cantidad_actividades.show()
        self.label1.show()
        self.pushButton.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
