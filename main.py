import importlib as ilib
from anwFunctions.anwReaders.reader import READ_OPT
from PySide2.QtWidgets import QApplication
import sys
# TODO: Exception 만들기

__version__ = "0.77"


try:
    fo = open(r'anwOpt.json', 'r', encoding='utf-8-sig')
except FileNotFoundError:
    fo = open(r'anwOpt.json', 'w', encoding='utf-8-sig')
    fo.write(
            """{
  "version"          : "0.77",
  "anw_standard"     : "ANW0.9",
  "mode"             : "gui",
  "basic_wil"        : 10,
  "basic_recent"     : 10,
  "basic_recentValue": 0.9
}""")
except Exception as e:
    raise e
finally:
    try:
        opt = READ_OPT(fo)
        fo.close()
    except Exception as e:
        raise e

if __version__ != opt["version"]:
    raise Exception("version incorrect")


try:
    import components.gui.main as oabm
except Exception as e:
    raise e

app = QApplication(sys.argv)
runner = oabm.Main(opt)
runner.show()
app.exec_()
input("type any")







