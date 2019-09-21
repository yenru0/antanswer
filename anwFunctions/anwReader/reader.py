import re
import json
from anwFunctions.anwExceptions import *
from lxml import etree
from os.path import basename

ANW_STANDARD = 'AMW_0_5a'

OPT_DICT_MODE_MAIN = {1: "AnwCli", 2: "AnwGui", -1: "debug"}

OPT_DICT_MODE_DETAIL = {"opt": 1, "default": 1, "opt_r": 2, "opt_rv": 3,
                        "file": 4, "infile": 4, "file_r": 5, "infile_r": 5,
                        "file_rv": 6, "infile_rv": 6, "standard": 15}


### Complete In 0.4
def READ_OPT(file_opt):
    """
    :param file_opt:stream:
    :return optret:dictionary:
    """
    optret = {"mainMode": 0, "detailMode": 0, 'bVariables': None}
    optret_detail = {"bWil": 0, "bRecent": 0, "bRecentValue": 0}

    opt = json.load(file_opt)

    ### mode
    t = opt['mode']
    if isinstance(t, int):
        try:
            value = OPT_DICT_MODE_MAIN[t]
        except KeyError:
            raise Exception
    elif isinstance(t, str):
        value = t
    else:
        raise Exception

    optret['mainMode'] = value

    ### detail
    t = opt['detail_mode']
    if isinstance(t, int):
        value = int(t)
    elif isinstance(t, str):
        try:
            value = OPT_DICT_MODE_DETAIL[t.lower()]
        except KeyError:
            raise Exception
    else:
        raise Exception

    if value in OPT_DICT_MODE_DETAIL.values():
        pass
    else:
        raise Exception

    optret['detailMode'] = value

    ### basic_value
    t = opt['basic_wil']
    if isinstance(t, int):
        if 0 <= t:
            optret_detail['bWil'] = t
        else:
            raise Exception
    else:
        raise Exception

    t = opt['basic_recent']
    if isinstance(t, int):
        if 0 <= t:
            optret_detail['bRecent'] = t
        else:
            raise Exception
    else:
        raise Exception

    t = opt['basic_recentValue']
    if isinstance(t, (int, float)):
        if 0 <= t <= 1:
            optret_detail['bRecentValue'] = t
        else:
            raise Exception
    else:
        raise Exception

    optret['bVariables'] = optret_detail

    ### return
    return optret


### Complete In 0.4
def sort_element(element_aqlist: list):
    def aqfilter(k):
        try:
            v = int(k.attrib["order"])
            if v > (1 << 31):
                raise AnwOrderOverError
            return v
        except (ValueError, KeyError):
            return 1 << 31

    element_aqlist.sort(
        key=aqfilter
    )
    ret_aqlist = []
    for aq in element_aqlist:

        items_aq = aq.findall("item")
        if items_aq:
            temp = []
            for item in items_aq:
                aq_lines = item.findall("l")
                if aq_lines:
                    temp.append("\n".join(line.text for line in aq_lines))
                else:
                    temp.append(item.text.strip())
        else:
            temp = []

            aq_lines = aq.findall("l")
            if aq_lines:
                temp.append("\n".join(line.text for line in aq_lines))
            else:
                temp.append(aq.text.strip())
        ret_aqlist.append(temp)
    return tuple(ret_aqlist)


### Complete In 0.4
def READ_ANW(file_anw, cond):
    ### WBR 지정
    WBR = {"name": None, "detail_infile": None, "description": None, "stages": {"main": None}}  ### WillBeReturned
    WBR_D = {"wil": None, "recent": None, "recentValue": None}

    ### define variables
    PARSER_DICT_E_MODE = {"default": 1, "choice": 2}

    try:
        WBR['name'] = basename(file_anw.name)
    except:
        pass

    tree = etree.parse(file_anw)
    root = tree.getroot()

    if root.tag != "anw":
        raise AnwRootNotFoundError

    ### detail attrib
    for k in ["wil", "recent", "recentValue"]:
        try:
            v = float(root.attrib[k])
            if v < 0:
                raise ValueError
            WBR_D[k] = v


        except KeyError:
            pass
        except ValueError:
            raise Exception

    if WBR_D["recentValue"] <= 1:
        pass
    else:
        raise Exception

    for v in WBR_D.values():
        if v == None:
            pass
        else:
            WBR["detail_infile"] = WBR_D
            break
    else:
        WBR["detail_infile"] = None

    ### description node
    node_desc = root.find("description")
    desc = node_desc.findall("l")
    if desc:
        desc = '\n'.join(i.text.strip() for i in desc)
    else:
        desc = node_desc.text.strip()

    WBR['description'] = desc

    ### stage node
    nodes_stage = root.findall("stage")
    for stage in nodes_stage:
        try:
            stage_name = stage.attrib["name"]
        except (KeyError):
            stage_name = "main"

        if stage_name == "main":
            if WBR["stages"]["main"]:
                raise AnwMultipleStageError

        else:
            if stage_name in WBR["stages"]:
                raise AnwMultipleStageError

        elements = []
        nodes_element = stage.findall("element")
        for element in nodes_element:
            nodes_answer = element.findall("answer")  ### answer_list
            nodes_question = element.findall("question")  ### question list
            answers = sort_element(nodes_answer)
            questions = sort_element(nodes_question)
            if not (questions and answers):
                raise AnwAQNotFoundError

            if len(answers) < len(questions):
                questions = questions[0:len(answers)]
            temp_ans = []
            for i in answers:
                temp = []
                for ii in i:
                    ii = ii.strip().replace("\n", " ")
                    if cond["COMP_WITHOUT_SPACE"]:
                        ii = ii.replace(" ", "")
                    if cond["COMP_IGNORE_CASE"]:
                        ii = ii.lower()
                    temp.append(ii)
                temp_ans.append(tuple(temp))
            answers = tuple(temp_ans)

            try:
                imsi_element_pref = element.attrib["mode"]
                if imsi_element_pref.replace(".", "", 1).isdigit():
                    value = int(element_pref)
                else:
                    if imsi_element_pref in PARSER_DICT_E_MODE:
                        value = PARSER_DICT_E_MODE[imsi_element_pref]
                    else:
                        raise AnwEModeInvalidError
            except KeyError:
                value = 1

            element_pref = value
            elements.append((element_pref, answers, questions))

        WBR["stages"][stage_name] = tuple(elements)

    return WBR


def READ_FULL(file_anw, file_opt, cond):
    temp_opt = READ_OPT(file_opt)
    temp_anw = READ_ANW(file_anw, cond)
    temp = {"name": None, "description": None, "mainMode": None, "detailMode": None, "detail": None, "stages": None}
    temp["description"] = temp_anw["description"]
    temp["name"] = temp_anw["name"]
    temp["mainMode"] = temp_opt["mainMode"]
    temp["detailMode"] = temp_opt["detailMode"]
    temp["stages"] = temp_anw["stages"]
    optc = temp_opt['detailMode']
    if optc in (1, 2, 3):
        temp['detail'] = tuple(temp_opt['bVariables'].values())
    elif optc in (4, 5, 6):
        temp['detail'] = tuple(temp_anw['detail'].values())
    elif optc in (7):
        temp = tuple((10, 5, 0.8))
    return temp
