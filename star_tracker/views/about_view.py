from PySide2.QtWidgets import QBoxLayout, QDialog, QDialogButtonBox, QLabel,QVBoxLayout,QPushButton

class About(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("About")

        buttons = QDialogButtonBox.Ok

        self._buttonBox = QDialogButtonBox(buttons)
        self._buttonBox.accepted.connect(self.accept)


        self._layout = QVBoxLayout()
        massage = QLabel("Late...")
        self._layout.addWidget(massage)
        self._layout.addWidget(self._buttonBox)
        self.setLayout(self._layout)