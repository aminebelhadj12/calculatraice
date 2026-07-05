import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel
)

class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()

        # Fenêtre
        self.setWindowTitle("Calculatrice - Amine Belhadj")
        self.setGeometry(400, 150, 350, 500)

        # Style général
        self.setStyleSheet("""
            QWidget{
                background-color:#1e1e1e;
            }

            QLineEdit{
                background-color:white;
                border-radius:10px;
                padding:10px;
                font-size:24px;
                height:50px;
            }

            QPushButton{
                background-color:#2d2d2d;
                color:white;
                font-size:18px;
                border-radius:15px;
                height:60px;
            }

            QPushButton:hover{
                background-color:#444444;
            }

            QLabel{
                color:white;
                font-size:13px;
            }
        """)

        layout = QVBoxLayout()

        # Nom
        titre = QLabel("Créé par : Amine Belhadj")
        layout.addWidget(titre)

        # Ecran
        self.ecran = QLineEdit()
        self.ecran.setReadOnly(True)
        layout.addWidget(self.ecran)

        # Grille boutons
        grid = QGridLayout()

        boutons = [
            ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
            ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
            ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
            ('C',3,0), ('0',3,1), ('=',3,2), ('+',3,3)
        ]

        for text,row,col in boutons:
            button = QPushButton(text)

            # Couleur spéciale
            if text in ['+','-','*','/','=']:
                button.setStyleSheet("""
                    QPushButton{
                        background-color:#ff9800;
                        color:white;
                        font-size:20px;
                        border-radius:15px;
                        height:60px;
                    }
                    QPushButton:hover{
                        background-color:#ffb74d;
                    }
                """)

            elif text == "C":
                button.setStyleSheet("""
                    QPushButton{
                        background-color:red;
                        color:white;
                        font-size:20px;
                        border-radius:15px;
                        height:60px;
                    }
                """)

            button.clicked.connect(self.clickButton)

            grid.addWidget(button,row,col)

        layout.addLayout(grid)

        # Signature
        footer = QLabel("Python + PyQt5")
        layout.addWidget(footer)

        self.setLayout(layout)

    def clickButton(self):
        button = self.sender()
        texte = button.text()

        if texte == "=":
            try:
                resultat = str(eval(self.ecran.text()))
                self.ecran.setText(resultat)
            except:
                self.ecran.setText("Erreur")

        elif texte == "C":
            self.ecran.clear()

        else:
            self.ecran.setText(self.ecran.text()+texte)


app = QApplication(sys.argv)

window = Calculatrice()
window.show()

sys.exit(app.exec_())