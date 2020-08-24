import re
import json
from enum import Enum, auto
from typing import List, Tuple, Dict


class Reader:
    def __init__(self, src: str, name: [str, None]=None):
        self.src: str = src
        self.src_size: int = len(src)
        self.src_iter: List[str] = []

        self.scope_default = "main"

        self._name: [str, None] = name
        self._description: str = ""
        self._predefined_value: dict = {"wil": None, "recentValue": None, "recent": None, }
        self._conditional_value: Dict[str, bool] = {
            "COMP_IGNORE_SPACE": True,  ### ignoring space, blank like '\t' won't be replaced
            "COMP_IGNORE_CASE": True,  ### ignoring case, replace upper to lower
            "ANSWER_WITHOUT_ORDER": True,  ### when answering quest, order don't interrupt you
            "COMP_NOT": True,  ### ignoring sequence matcher(compare) method
            "RESULT_DISPLAY_QUEST": True,  ### not displaying Quest
            "COMP_IGNORE_LAST_PERIOD": True,  ### ignoring the last period
            "RESULT_MANUAL_POST_CORRECTION": True,  ### post correction at result time GUI main cond
            "REVERSE_AQ": False
        }
        self._variables = {}

        self._stages: Dict[str, list] = {'main': []}

    def read(self):
        self.preprocess()
        self.parse()

    def preprocess(self) -> None:
        """
        pre-processing (e.g. delete comment, make src_iter)
        :return: Void
        """
        self.preprocess_comment()
        self.src_iter = self.src.split("\n")

    def preprocess_comment(self) -> None:
        """
        process \# escape & delete comment
        :return: Void
        """
        pattern_sharp = re.compile(r"\\#")
        pattern_comment = re.compile(r"###.*")

        self.src = pattern_sharp.sub("%§%SHP%§%", self.src)
        self.src = pattern_comment.sub("", self.src)

        self.src = self.src.replace("%§%SHP%§%", "#")

    def parse(self):
        """
        parse based on src_iter
        :return: Void
        """
        scope = self.scope_default
        for i, s in enumerate(self.src_iter):
            if not s.strip():
                continue

            t = self.parse_stage(s, i)
            if t is not False:
                scope = t
                if scope not in self._stages:
                    self._stages[scope] = []
                continue

            t = self.parse_let(s, i)
            if t is not False:
                for k, v in t.items():
                    if k == 'name':
                        self._name = v
                    elif k == 'desc' or 'description':
                        self._description = v
                    elif k in self._predefined_value:
                        if k == 'wil':
                            self._predefined_value[k] = int(float(v))
                        elif k == 'recent_value':
                            self._predefined_value[k] = float(v)
                        elif k == 'recent':
                            self._predefined_value[k] = int(float(v))
                    elif k in self._conditional_value:
                        if v.lower() == 'true':
                            self._conditional_value[k] = True
                        elif v.lower() == 'false':
                            self._conditional_value[k] = False
                        else:
                            raise Exception
                    else:
                        self._variables[k] = v

                continue

            t = self.parse_command(s, i)
            if t is not False:
                continue

            t = self.parse_element(s, i)
            if t is not False:
                self._stages[scope].append(t)
                continue

            raise Exception(f"unexpected expression: LineNumber: {i + 1}")

    def parse_stage(self, s: str, ln: int) -> [str, bool]:
        """
        parse stage starting with '##@'
        :param s: line string
        :param ln: line number
        :return: stage name or False
        """
        pattern_stage = re.compile(r"##@(.*)")
        t = pattern_stage.match(s)
        if not t:
            return False

        if not t.group(1).strip():
            return self.scope_default
        else:
            return t.group(1).strip()

    def parse_let(self, s: str, ln: int) -> [Dict, bool]:
        """
        parse let starting with '##$'
        :param s: line string
        :param ln: line number
        :return: variables dictionary or False
        """
        pattern_let = re.compile(r"##\$(.*)")
        t = pattern_let.match(s)
        if not t:
            return False

        if not t.group(1).strip():
            return {}
        else:
            seps = t.group(1).split(";")
            ret = {}
            for sep in seps:
                if not sep.strip():
                    continue
                kv = sep.split("=")
                if len(kv) != 2:
                    raise Exception(str(ln))
                else:
                    ret[kv[0].strip()] = kv[1].strip()
            return ret

    def parse_command(self, s: str, ln: int):
        """
        parse command starting with '##!'
        :param s: line string
        :param ln: line number
        :return: True or False
        """
        pattern_command = re.compile(r"##!(.*)")
        t = pattern_command.match(s)
        if not t:
            return False
        else:
            return True

    def parse_element(self, s: str, ln: int):
        """
        parse element
        :param s: line string
        :param ln: line number
        :return: recursive List that contains element itself or False
        """
        L1 = s.split(":")
        if len(L1) < 2:
            return False

        return [[[l.strip() for l in l3.split(";")] for l3 in l2.split("|")] for l2 in L1[:2]]

    @property
    def structure(self) -> dict:
        """
        convert information of this reader to dictionary to be processed easily in ADS
        :return: dict
        """
        return {
            "name": self._name,
            "description": self._description,
            "detail_infile": self._predefined_value,
            "cond": self._conditional_value,
            "stages": self._stages
        }

if __name__ == '__main__':
    r = Reader("""

##$ wil = 3; recent_value = 0.9; recent = 30; COMP_IGNORE_SPACE = True
##@ 결단력S
nn;a|b:nn\#:1
##@ 마단력K
iG:
##@ 스페시컬<T>

""")

    r.read()
    print(r.src_iter)
