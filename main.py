from PySide2.QtWidgets import QApplication
import sys
import os
# TODO: Exception 만들기
# TODO: TimeRate 만들기
__version__ = "0.9"

if not os.path.isdir("preference"):
    os.makedirs("preference")

if not os.path.isdir("datapack"):
    os.makedirs("datapack")

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
    sys.exit()