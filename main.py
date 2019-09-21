from tkinter import filedialog, Tk
import importlib as ilib
from time import sleep

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
            oabm = ilib.import_module("modules.{}.main".format("AnwCli"))
        except:
            oabm = ilib.import_module("modules.{}.main".format("AnwCli"))

        OABM = oabm.MainABM
        OABM.init_routine(fa, fo)

print("종료 중...")
sleep(1.25)
print("종료 완료...")
exit()
