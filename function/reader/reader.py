import json
import re
from os.path import basename

# TODO: 진짜 antanswer.function.reader.reader.py 는 전설이다.
# 어떻게 얘들 어떻게 처리하냐



"""
CONSTANT-STRING MAPS/DICTS
"""
OPT_DICT_MODE_MAIN = {1: "AnwCli", 2: "AnwGui", -1: "debug"}

PARSER_DICT_E_MODE = {"default": 1, "choice": 2}
PARSER_LIST_COND_BOOL_STRING_TRUE = ["true", "yes"]
PARSER_LIST_COND_BOOL_STRING_FALSE = ["false", "no"]

"""
PATTERNS
"""

pattern_ignore_sharp = re.compile(r"\\#")
SSHARP = "%§%SHP%§%"

line_comment = r"###.*"
block_comment = "/##/(.|[\n])*/##/"

pattern_line_comment = re.compile(line_comment)
pattern_block_comment = re.compile(block_comment)

def_dvar = r"(?:\n|^)##\$([ \t]*\{[^{}]*\}|[ \t]*[^{}\n]*)"
pattern_def_dvar = re.compile(def_dvar)
sep_def_dvar = ";"

def_stage = r"(?:\n|^)##\@[ \t]*(.*)"
def_stage_without_group = r"(?:\n|^)##\@[ \t]*.*"
pattern_def_stage = re.compile(def_stage)
pattern_def_stage_without_group = re.compile(def_stage_without_group)

pattern_ignore_L1 = re.compile(r"\\:")
pattern_ignore_L2 = re.compile(r"\\\|")
pattern_ignore_L3 = re.compile(r"\\;")

pattern_ignore_bracket_left = re.compile(r"\\\{")
pattern_ignore_bracket_right = re.compile(r"\\\}")

SL3 = "%§%SL3%§%"
SL2 = "%§%SL2%§%"
SL1 = "%§%SL1%§%"

LBR = "%§%LBR%§%"
RBR = "%§%LBR%§%"

# ind type = "&§%ind%§&"

seps_L3 = r":|;" + "{}"
seps_L2 = r":|" + "{}"
seps_L1 = r":" + "{}"

iobject_L3 = r"[ \t]*\{[^%s]*\}[ \t]*|[^%s\n]+" % (seps_L3, seps_L3)
iobject_L2 = r"[ \t]*\{[^%s]*\}[ \t]*|[^%s\n]+" % (seps_L2, seps_L2)
iobject_L1 = r"[ \t]*\{[^%s]*\}[ \t]*|[^%s\n]+" % (seps_L1, seps_L1)

pattern_iobject_L3 = re.compile(iobject_L3)
pattern_iobject_L2 = re.compile(iobject_L2)
pattern_iobject_L1 = re.compile(iobject_L1)

token_index = []

ind = -1




def except_comment(string):
    string = pattern_ignore_sharp.sub(SSHARP, string)

    string = pattern_block_comment.sub("", string)
    string = pattern_line_comment.sub("", string)

    string = string.replace(SSHARP, "#")
    return string


def define_default_variable(string):  # cond & detail & etc..
    t = pattern_def_dvar.search(string)
    temp1 = {}
    while t:
        string = string[:t.start()] + string[t.end():]
        temp_matched = t.group(1)
        temp_matched = re.sub(r"{((?:.|[\n])*)}", lambda m: m.group(1), temp_matched)
        temp_seped = temp_matched.split(";")
        for i in temp_seped:
            if not i.strip():
                continue
            temp_seped_kv = i.split("=")
            if len(temp_seped_kv) != 2:
                raise Exception
            temp1[temp_seped_kv[0].strip()] = temp_seped_kv[1].strip()
        t = pattern_def_dvar.search(string)
    return string, temp1


def define_variable(string):
    return string, {}


def define_stage(string):
    seped_by_stage = pattern_def_stage_without_group.split(string)
    t = pattern_def_stage.findall(string)
    temp1 = {}

    ft = seped_by_stage[0].strip()
    if ft:
        temp1["main"] = seped_by_stage[0].strip()
    else:
        pass
    if len(seped_by_stage) == 1:
        return temp1

    for i, st in enumerate(seped_by_stage[1:]):
        if not st.strip():
            continue
        else:
            if t[i].strip() in temp1:
                temp1[t[i].strip()] += st.strip()
            else:
                temp1[t[i].strip()] = st.strip()
    return temp1


def repl(m):
    global ind
    ind += 1
    token_index.append(m.group())
    return f"&§%{ind}%§&"


def derepl(m):
    return token_index[int(m.group(1))]


def sep_element(string, stage_name, file_name):
    global token_index
    global ind
    token_index = []
    ind = -1
    string = pattern_ignore_L1.sub(SL1, string)
    string = pattern_ignore_L2.sub(SL2, string)
    string = pattern_ignore_L3.sub(SL3, string)

    string = pattern_ignore_bracket_left.sub(LBR, string)
    string = pattern_ignore_bracket_right.sub(RBR, string)

    string = pattern_iobject_L3.sub(repl, string)

    string = pattern_iobject_L2.sub(repl, string)

    string = pattern_iobject_L1.sub(repl, string)

    seped = string.split("\n")

    temp_seped_E = []

    temp_seped_L1 = []
    ci = 0
    for i in seped:

        temp_seped_L1 = i.split(":")
        if len(temp_seped_L1) < 2:
            temp_seped_L1 = temp_seped_L1[0]
            for i in range(3):
                temp_seped_L1 = re.sub("&§%([0-9]+)%§&", derepl, temp_seped_L1)

            if temp_seped_L1.strip():

                raise Exception("unrecognized element")
            else:
                continue

        temp1 = []
        for j in temp_seped_L1:
            if not re.fullmatch("&§%([0-9]+)%§&", j):
                raise Exception("ParsingError L1", j)
            j = re.sub("&§%([0-9]+)%§&", derepl, j)

            j = re.sub(r"\{(.*)\}", lambda m: m.group(1), j)

            temp_seped_L2 = j.split("|")

            temp2 = []
            for k in temp_seped_L2:
                if not re.fullmatch("&§%([0-9]+)%§&", k):
                    raise Exception("ParsingError L2")
                k = re.sub("&§%([0-9]+)%§&", derepl, k)
                k = re.sub(r"{(.*)}", lambda m: m.group(1), k)
                temp_seped_L3 = k.split(";")

                temp3 = []
                for l in temp_seped_L3:
                    l = re.sub("&§%([0-9]+)%§&", derepl, l)
                    l = l.strip()
                    l = re.sub(r"{((?:.|[\n])*)}", lambda m: m.group(1), l)

                    l = l.replace(SL1, ":")
                    l = l.replace(SL2, "|")
                    l = l.replace(SL3, ";")

                    l = l.replace(LBR, "{")
                    l = l.replace(RBR, "}")

                    temp3.append(l)
                temp2.append(temp3)
            temp1.append(temp2)
        temp1.insert(0, 1)
        temp1.insert(3, ci)
        temp_seped_E.append(temp1)
        ci += 1

    return temp_seped_E


def READ_ANW(string, file_name):
    """

    :param f: anw file
    :return: WBR that
    """
    WBR = {"name": None, "detail_infile": None, "cond": None, "description": None, "stages": {}}
    WBR_D = {"wil": None, "recent": None, "recentValue": None}

    COND = {  # string: bool
        # Anw ReaderMain
        "COMP_IGNORE_SPACE": None,  # ignoring space, blank like '\t' won't be replaced
        "COMP_IGNORE_CASE": None,  # ignoring case, replace upper to lower
        "ANSWER_WITHOUT_ORDER": None,  # when answering quest, order don't interrupt you
        "COMP_NOT": None,  # ignoring sequence matcher(compare) method
        "RESULT_DISPLAY_QUEST": None,  # not displaying Quest
        "COMP_IGNORE_LAST_PERIOD": None,  # ignoring the last period
        "RESULT_MANUAL_POST_CORRECTION": None,  # post correction at result time GUI main cond
        "REVERSE_AQ": None  # reverse AQ in element
    }

    VARS = {}

    string = except_comment(string)
    string, default_variables = define_default_variable(string)

    for k, v in default_variables.items():
        if k in WBR_D:
            try:
                WBR_D[k] = float(v)
            except ValueError as e:
                raise ValueError("ValueError while define default variables:", k, v)
        elif k in COND:
            if k.isdigit():
                WBR_D[k] = bool(v)
            else:
                if v.lower() in PARSER_LIST_COND_BOOL_STRING_TRUE:
                    COND[k] = True
                elif v.lower() in PARSER_LIST_COND_BOOL_STRING_FALSE:
                    COND[k] = False
                else:
                    raise ValueError("ValueError while define default variables:", k, v)
        elif k == "name":
            WBR["name"] = v

        else:
            # warn: unrecognized key
            pass

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

    WBR["detail_infile"] = WBR_D
    WBR["cond"] = COND
    # not completed
    string, VARS = define_variable(string)

    if WBR["name"] is None:
        try:
            WBR["name"] = basename(file_name)
        except AttributeError as e:
            WBR["name"] = "test.test.test"
        except Exception as e:
            raise e

    stages = define_stage(string)
    temp = {}
    for st_n, st_s in stages.items():
        temp[st_n] = sep_element(st_s, st_n, WBR["name"])

    WBR["stages"] = temp

    return WBR


if __name__ == "__main__":
    ### -> variable -> stage -> element 순으로 작업
    import io

    t = READ_ANW(io.StringIO("""
##$ name = 그레고리우스
##$ wil = 94; recentValue = 0.94; recent = 95; recentValue = 0.95
##$ recentValue = 0.4
##$ {
COMP_IGNORE_CASE=true;
COMP_IGNORE_LAST_PERIOD=true;
COMP_NOT=true;
RESULT_MANUAL_POST_CORRECTION=true;
}

### 다섯개

3:4


"""))

    t = READ_ANW(io.StringIO("""
###\## 다섯개의 시작\#
##@ 나밍
다섯개의 시작의 준비: 모든것은 준비되었나요? /##/
시작되었다.
/##/
##@ stagne1
은 : 사

"""))

    import pprint

    pprint.pprint(t)
