from tkinter import filedialog, Tk
import importlib as ilib
from time import sleep
from anwFunctions.anwReaders.reader import READ_OPT

try:
    fo = open(r'anwOpt.json', 'r', encoding='utf-8-sig')
except FileNotFoundError:
    fo = open(r'anwOpt.json', 'w', encoding='utf-8-sig')
    fo.write(
            """{
  "version"          : "0.55",
  "ANW_STANDARD"     : "ANW_0_5a",
  "mode"             : "anwCli",
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

if opt["mainMode"].lower() == "cli":
    try:
        import components.cli.main as oabm
    except Exception as e:
        raise e

elif opt["mainMode"].lower() == "gui":
    try:
        import components.cli.main as oabm
    except Exception as e:
        raise e

else :
    try:
        oabm = ilib.import_module("components.{0}.main".format(opt["mainMode"].lower()))
    except Exception as e:
        raise e


runner = oabm.Main()







