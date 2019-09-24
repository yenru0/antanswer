import re
from lxml.etree import *
from os.path import basename, splitext


def reader(file_anwold):
    stage = "main"

    detail = {"wil": None, "recent": None, "recentValue": None}
    stages = {"main": Element("stage", name=stage)}
    ignored = False
    root = Element("anw")
    desc = Element("description")
    desc.text = "made by anwO2N file"
    root.append(desc)

    for line in file_anwold:
        line = line.strip()
        if not line:
            continue
        t = re.match("/##/(.+)", line)
        if t:
            ignored = not ignored
            continue

        if ignored:
            continue
        t = re.match(r'##\$(.+)', line)
        if t:
            let_details = [[j.strip() for j in i.split("=")] for i in t.group(1).split(";")]
            for i in let_details:
                if i[0].lower() == "wil":
                    try:
                        value = int(i[1])
                    except TypeError:
                        raise
                    detail["wil"] = value
                elif i[0].lower() == "recent":
                    try:
                        value = int(i[1])
                    except TypeError:
                        raise
                    detail["recent"] = value
                elif i[0].lower() == "recentvalue" or i[0].lower() == "recval":
                    try:
                        value = float(i[1])
                    except TypeError:
                        raise
                    detail["recentValue"] = value
                else:
                    pass
            continue
        t = re.match("##!(.+)", line)
        if t:
            pass
            continue
        t = re.match("###(.+)", line)
        if t:
            pass
            continue

        t = re.match("##@(.+)", line)
        if t:
            stage = t.group(1)
            if stage not in stages:
                stages[stage] = Element("stage", stage)
            continue

        line = line.split("###")[0]

        element_node = Element("element")
        element = line.split(":")

        if len(element) < 2:
            raise

        mode = None
        for i in element[0].split("|"):
            answer_node = Element("answer")
            for j in i.split(";"):
                item_node = Element("item")
                item_node.text = j.strip()
                answer_node.append(item_node)
            element_node.append(answer_node)

        for i in element[1].split("|"):
            question_node = Element("question")
            for j in i.split(";"):
                item_node = Element("item")
                item_node.text = j.strip()
                question_node.append(item_node)
            element_node.append(question_node)

        if len(element) == 3:
            try:
                mode = int(element[2].strip())
            except TypeError:
                pass

        if mode:
            element_node.attrib["mode"] = str(mode)

        stages[stage].append(element_node)

    for i in stages.values():
        root.append(i)
    for k, v in detail.items():
        if v != None:
            root.attrib[k] = str(v)

    return ElementTree(root)
    return dump(root)


if __name__ == '__main__':
    from tkinter import filedialog, Tk

    root = Tk()
    root.withdraw()
    import sys

    file_anw_path = filedialog.askopenfilename(title="anwOld/txt 파일을 선택하세요.",
                                               initialdir="../../anwdatapack",
                                               filetypes=(

                                                   ("텍스트 파일", ".txt"),
                                               )
                                               )
    if file_anw_path:
        with open(file_anw_path, 'r', encoding='utf-8-sig') as f:
            with open("../../anwdatapack/" + basename(splitext(f.name)[0]) + ".anw", 'w', encoding="UTF-8") as fw:
                reader(f).write(fw.buffer, encoding="utf-8", pretty_print=True)
