from tkinter import filedialog, Tk
import importlib as ilib
from time import sleep
from anwFunctions.anwReaders.reader import READ_OPT

"""
root = Tk()
root.withdraw()

file_anw_path = filedialog.askopenfilename(title="anw 파일을 선택하세요.",
                                           initialdir="./anwdatapack",
                                           filetypes=(

                                               ("안탠서 파일", ".anw;.anp"),
                                               ("암호화 안탠서 파일", ".awc;.apc"),
                                               ("텍스트/xml 파일", ".txt;.xml")
                                           )
                                           )




with open(file_anw_path, 'r', encoding='utf-8-sig') as fa:
    with open(r'anwOpt.json', 'r', encoding='utf-8-sig') as fo:
        try:
            oabm = ilib.import_module("components.{}.main".format("AnwCli"))
        except:
            oabm = ilib.import_module("components.{}.main".format("AnwCli"))

        OABM = oabm.MainABM
        OABM.init_routine(fa, fo)

"""
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






