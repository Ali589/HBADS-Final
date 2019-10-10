from PyQt5.QtWidgets import QMessageBox


def message(title,body):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle(title)
    msgBox.setText(body)
    msgBox.setStandardButtons(QMessageBox.Ok)
    # msgBox.buttonClicked.connect(msgButtonClick(a))
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')