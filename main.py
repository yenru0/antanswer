from PySide2.QtWidgets import QApplication
import sys
# TODO: Exception 만들기

__version__ = "0.9i5"




if __name__ == "__main__":
    try:
        import components.gui.main as oabm
    except Exception as e:
        raise e

    app = QApplication(sys.argv)
    runner = oabm.Main()
    #runner.ui.pages.setCurrentIndex(4)
    runner.show()
    app.exec_()