import re
import json
from anwFunctions.anwExceptions import *
from lxml import etree
from os.path import basename
from logging import debug, warning, error, log, info

"""
INFORMATION OF VERSION
"""
AFD_VERSION = "AFD_1h"  # Antanswer Format Document
ANW_VERSION = "AMW_0_9a"  # Antanswer

"""
CONSTANT-STRING MAPS/DICTS
"""
OPT_DICT_MODE_MAIN = {1: "AnwCli", 2: "AnwGui", -1: "debug"}


def READ_OPT(file_opt):
    """
    :param file_opt: anwOpt.json stream

    :return optret: the dictionary that contains
        -mainMode
        -bVariables
            -bWil
            -bRecent
            -bRecentValue
    """
    optret = {"mainMode": 0, 'bVariables': None}
    optret_detail = {"bWil": 0, "bRecent": 0, "bRecentValue": 0}

    opt = json.load(file_opt)

    ### mode
    t = opt['mode']
    if isinstance(t, int):
        try:
            value = OPT_DICT_MODE_MAIN[t]
        except KeyError:
            return Exception("'mode' value of 'anwOpt.json' has incorrect integer")
    elif isinstance(t, str):
        value = t
    else:
        raise Exception("'mode' value of 'anwOpt.json' has incorrect value\n"
                        "why don't you match the exact type?"
                        "it is recommended to be str, but, restrictively, it can be int.")

    optret['mainMode'] = value

    ### basic_value
    t = opt['basic_wil']
    if isinstance(t, int):
        if 0 <= t:
            optret_detail['bWil'] = t
        else:
            raise Exception("'basic_wil' value of 'anwOpt.json' has incorrect integer\n",
                            "why don't you match greater than or equal to 0")
    else:
        raise Exception("'basic_wil' value of 'anwOpt.json' has incorrect value\n"
                        "why don't you match the exact type?"
                        "it must be int")

    t = opt['basic_recent']
    if isinstance(t, int):
        if 0 <= t:
            optret_detail['bRecent'] = t
        else:
            raise Exception("'basic_recent' value of 'anwOpt.json' has incorrect integer\n",
                            "Why don't you match greater than or equal to 0")
    else:
        raise Exception("'basic_recent' value of 'anwOpt.json' has incorrect value\n"
                        "why don't you match the exact type?"
                        "it must be int")

    t = opt['basic_recentValue']
    if isinstance(t, (int, float)):
        if 0 <= t <= 1:
            optret_detail['bRecentValue'] = t
        else:
            raise Exception("'basic_recentValue' value of 'anwOpt.json' has incorrect integer or incorrect float\n",
                            "it must be 0 <= 'basic_recentValue' <= 1")
    else:
        raise Exception("'basic_recentValue' value of 'anwOpt.json' has incorrect value\n"
                        "why don't you match the exact type?'"
                        "it must be (int, float)")

    optret['bVariables'] = optret_detail

    ### return
    return optret


def sort_element(element_aqlist: list):
    """
    :param
    """
    ordered = list()
    non_ordered = list()
    for k in element_aqlist:
        try:
            k.attrib["order"]
        except KeyError:
            non_ordered.append(k)
        except Exception:
            raise Exception("why?")
        else:
            ordered.append(k)



    def aqfilter(k):
        try:
            v = int(k.attrib["order"])
            if -2147483648 <= v <= 2147483647:
                return v
            else:
                raise ValueError("order value can't greater than 2147483647")

        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    prc_element_aqlist = sorted(ordered, key=aqfilter) + non_ordered
    ret_aqlist = []
    for aq in prc_element_aqlist:

        items_aq = aq.findall("item")
        temp = []
        if items_aq:
            for item in items_aq:
                aq_lines = item.findall("l") # 겹침(1) -> 함수화 예정
                if aq_lines:
                    temp.append("\n".join(line.text for line in aq_lines))
                else:
                    temp.append(item.text.strip())
        else:
            aq_lines = aq.findall("l")
            if aq_lines: # 겹침(1)
                temp.append("\n".join(line.text for line in aq_lines))
            else:
                temp.append(aq.text.strip())
        ret_aqlist.append(temp)
    return tuple(ret_aqlist)


def READ_ANW(file_anw):
    """
    :param file_anw: anw file
    :return: WBR that contains
        -name
        -detail_infile
        -description
        -stages
            -main
            -
            -
            ...
    """

    ### COMP_

    ### set WBR(Will Be Returned)
    WBR = {"name": None, "detail_infile": None, "cond": None, "description": None, "stages": {}}  # WillBeReturned
    WBR_D = {"wil": None, "recent": None, "recentValue": None}
    COND = {
        # Anw ReaderMain
        "COMP_IGNORE_SPACE": None, # ignoring space, blank like '\t' won't be replaced
        "COMP_IGNORE_CASE": None,   # ignoring case, replace upper to lower
        "ANSWER_WITHOUT_ORDER": None, # when answering quest, order don't interrupt you
        "COMP_NOT": None,             # ignoring sequence matcher(compare) method
        "RESULT_DISPLAY_QUEST": None, # not displaying Quest
        "COMP_IGNORE_LAST_PERIOD": None, # ignoring the last period
        # support CLI, but main is GUI.
        "RESULT_MANUAL_POST_CORRECTION": None # post correction at result time GUI main cond
    }
    ### define variables
    PARSER_DICT_E_MODE = {"default": 1, "choice": 2}  # 2 is not used now

    tree = etree.parse(file_anw)
    root = tree.getroot()

    ### name
    try:
        if "name" in root.attrib:
            WBR["name"] = root.attrib["name"]
        else:
            WBR["name"] = basename(file_anw.name)
    except AttributeError as e:
        print("it has something wrong name. are you test-ing?\n"
              "i assign 'test.test.test' to your file.\n")
        WBR["name"] = "test.test.test"
    except Exception as e:
        raise e

    ### tag
    if root.tag != "anw":
        raise Exception("root is not found in anw file\n"
                        "root tag must be 'anw'!\n")

    ### cond attrib
    if "cond" in root.attrib:  # not require
        cond_string: str = root.attrib["cond"]
        try:
            cond_json: dict = json.loads(cond_string)
            for k, v in cond_json.items():

                COND[k] = v

        except ValueError as e:
            # wrong cond_string
            raise e
        except KeyError as e:
            # wrong key
            raise e
        except Exception as e:
            raise e

    else:
        pass



    ### detail attrib
    for k in ["wil", "recent", "recentValue"]:
        try:
            v = float(root.attrib[k])
            WBR_D[k] = v
        except KeyError as e:
            continue
        except ValueError as e:
            raise e

    if WBR_D["recentValue"] is None:
        pass
    else:  # float
        if 0 <= WBR_D["recentValue"] <= 1:
            pass
        else:
            raise ValueError("'recentValue' value of '{}' has incorrect value".format(WBR["name"]))

    if WBR_D["recent"] is None:
        pass
    else:  # float -> int
        if 0 <= int(WBR_D["recent"]):
            WBR_D["recent"] = int(WBR_D["recent"])
        else:
            raise ValueError("'recent' value of '{}' has incorrect value".format(WBR["name"]))

    if WBR_D["wil"] is None:
        pass
    else:  # float -> int
        if 0 <= int(WBR_D["wil"]):
            WBR_D["wil"] = int(WBR_D["wil"])
        else:
            raise ValueError("'wil' value of '{}' has incorrect value".format(WBR["name"]))

    # Will be Deprecated Just WBR[D-if] = WBR_D
    # Because for looping after this process
    if all(map(lambda k: True if k is None else False, WBR_D.values())):
        WBR["detail_infile"] = None
    else:
        WBR["detail_infile"] = WBR_D

    ### description node
    node_desc = root.find("description")

    if node_desc is None:
        print("description is not found in '{}'".format(WBR["name"]))
        desc_text = ""
    else:
        desc = node_desc.findall("l")
        desc_text = '\n'.join(i.text.strip() for i in desc) if desc else node_desc.text.strip()

    WBR['description'] = desc_text

    ### cond node
    node_cond = root.find("cond")
    if node_cond is None:
        pass
    else:
        try:
            cond_json_noded = json.loads(node_cond.text)
            for k, v in cond_json_noded.items():
                COND[k] = v
        except ValueError as e:
            raise e
        except KeyError as e:
            raise e
        except Exception as e:
            raise e


    ### stage node
    nodes_stage = root.findall("stage")
    for stage in nodes_stage:
        try:
            stage_name = stage.attrib["name"]
        except KeyError:
            stage_name = "main"

        if stage_name in WBR["stages"]:
            raise Exception("multi core stages defined in '{}'".format(WBR["name"]))

        elements = []
        nodes_element = stage.findall("element")
        for element in nodes_element:
            nodes_answer = element.findall("answer")  ### answer_list
            nodes_question = element.findall("question")  ### question list
            answers = sort_element(nodes_answer)
            questions = sort_element(nodes_question)
            if not (questions and answers):
                raise Exception("answer, question nodes are not found in element in '{0}' of '{1}'".format(
                    stage_name, WBR["name"])
                )

            if len(answers) < len(questions):
                questions = questions[0:len(answers)]



            temp_ans = []
            for i in answers:
                temp = []
                for ii in i:
                    ii = ii.strip().replace("\n", " ")
                    temp.append(ii)
                temp_ans.append(tuple(temp))
            answers = tuple(temp_ans)

            try:
                imsi_element_pref = element.attrib["mode"]

                value = int(imsi_element_pref)

            except KeyError as e:
                value = 1
            except ValueError as e1:
                try:
                    value = PARSER_DICT_E_MODE[imsi_element_pref.lower()]
                except KeyError as e2:
                    raise Exception("element mode is invalid in stage '{0}' of '{1}'".format(
                        stage_name, WBR["name"])
                    )
            finally:
                element_pref = value
            elements.append((element_pref, answers, questions))

        WBR["stages"][stage_name] = tuple(elements)


    WBR["cond"] = COND
    return WBR

### deprecated
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


if __name__ == '__main__':
    import io
