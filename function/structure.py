from typing import Dict, List, Tuple
from random import choices

import function.reader.reader as reader
import numpy as np

### reader.struct

class AntanswerDetail:
    def __init__(self, wil: int = 0, recent: int = 0, recentValue: float = 0.0):
        self.wil: int = wil
        self.recent: int = recent
        self.recentValue: float = recentValue

    def set(self, wil: int = 0, recent: int = 0, recentValue=0.0):
        if not isinstance(recent, int):
            recent = 0
        if not isinstance(recentValue, (int, float)):
            recentValue = 0
        self.wil: int = wil
        self.recent: int = recent
        self.recentValue: float = recentValue


class AntanswerSub:
    def __init__(self, *args):
        self.L: List[str] = []
        for arg in args:
            self.append(arg)

    def append(self, other: str):
        if isinstance(other, str):
            self.L.append(other)
            return True
        else:
            return False

    @property
    def first(self):
        if len(self.L) > 0:
            return self.L[0]
        else:
            return None

    def __iter__(self):
        return iter(self.L)

    def __len__(self):
        return int(len(self.L))

    def __getitem__(self, item):
        return self.L[item]

    def __setitem__(self, key, value):
        self.L[key] = value


class AntanswerElement:
    def __init__(self, name: str, stage_name: str, id: int):
        self.name = name
        self.stage_name = stage_name
        self.id: int = id
        self.mode: int = 1
        self.answers: List[AntanswerSub] = []  # contatin SubElement
        self.questions: List[AntanswerSub] = []  # contain SubElement

    def getMode(self):
        """
        :return: mode
        """
        return self.mode

    def append(self, p, subel):
        """
        append subelement
        :param p: 0 -> call appendAnswer(), 1 -> call appendQuestion()
        :param subel: a subelement put in
        :return:
        """
        if p == 0:
            self.appendAnswer(subel)
        elif p == 1:
            self.appendQuestion(subel)
        else:
            return False
        return True

    def appendAnswer(self, subel: AntanswerSub):
        """
        append subelement
        :param subel: a subelement put in into 'self.answers'
        :return: True if succeed else False
        """
        if isinstance(subel, AntanswerSub):
            self.answers.append(subel)
            return True
        return False

    def appendQuestion(self, subel: AntanswerSub):
        """
        append subelement
        :param subel: a subelement put in into 'self.questions'
        :return: True if succeed else False
        """
        if isinstance(subel, AntanswerSub):
            self.questions.append(subel)
            return True
        else:
            return False

    def getRealQuestion(self, reverse_aq = False) -> List[str]:
        """
        Since Question displayed in antanswer is Only First Of 'questions',
        Antanswer need first of first of 'self.question'
        :return: first of first of 'self.question' or None if Empty
        """
        if not reverse_aq:
            return [i.first for i in self.questions]
        else:
            return [i.first for i in self.answers]

    @property
    def idpath(self):
        return self.name, self.stage_name, self.id

    @property
    def idpathstr(self):
        return "{}:{}:{}".format(self.name, self.stage_name, self.id)


class AntanswerStage:
    def __init__(self, name: str, stage_name: str):
        self.name = name
        self.stage_name: str = stage_name
        self.elements: List[AntanswerElement] = []  # contain AntanswerElement

    def append(self, e):
        if isinstance(e, AntanswerElement):
            self.elements.append(e)
        else:
            return False

    def __iter__(self):
        return iter(self.elements)


class AntanswerDataStruct:
    def __init__(self):
        self.name = None
        self.detail = AntanswerDetail()
        self.cond: Dict[str, bool] = {}
        self.desc = None
        self.stages: Dict[str, AntanswerStage] = {}
        self.use: Dict[str, bool] = {}


        self.result = AntanswerResult()

        self.isloaded: bool = False
        self.isfin: bool = False

    def load(self, file_anw):
        try:
            fn = file_anw.name
        except AttributeError as e:
            fn = "test.test.test"
        except Exception as e:
            raise e
        finally:
            self.load_fromstring(file_anw.read(), fn)

    def load_fromstring(self, string: str, name: str):
        wbr = reader.READ_ANW(string, name)
        print("D")
        self.name = wbr["name"]
        self.detail.set(
            wbr["detail_infile"]["wil"],
            wbr["detail_infile"]["recent"],
            wbr["detail_infile"]["recentValue"]
        )
        self.cond = wbr["cond"]
        self.desc = wbr["description"]
        for k, v in wbr["stages"].items():
            stage = AntanswerStage(self.name, k)
            for i, j in enumerate(v):
                e = AntanswerElement(self.name, k, i)
                for a_s in j[1]:
                    s = AntanswerSub(*a_s)
                    e.appendAnswer(s)
                for q_s in j[2]:
                    s = AntanswerSub(*q_s)
                    e.appendQuestion(s)
                stage.append(e)
            self.stages[k] = stage
            self.use[k] = True
        self.isfin = False
        self.isloaded = True

    def sampling(self):
        """

        :return:
        """
        aqs = []
        rct = 0
        for v in self.stages.values():
            if self.use[v]:
                for e in v:
                    aqs.append(e)

        if self.detail.recentValue:
            rct = int(self.detail.recentValue * len(aqs))
        else:
            rct = self.detail.recent

        history = []
        for i in range(self.detail.wil):
            r = np.random.choice(aqs)
            while r in history[-self.detail.wil:]:
                r = np.random.choice(aqs)
            history.append(r)
            self.result.append(r)
            yield r
        self.isfin = True


    def check(self, stage: str, state: bool) -> bool:
        if stage in self.stages:
            if isinstance(state, bool):
                self.use[stage] = state
            else:
                return False
        else:
            return False
        return True



### U'routine

class AntanswerResult:
    def __init__(self, *args):
        self.result: List[List[List[str], AntanswerElement, List[float]]] = []
        self.score = 0
    def append(self, a) -> bool:
        if isinstance(a, AntanswerElement):
            self.result.append([None, a, None])
        else:
            return False
        return True

    def getElementsWithAnwPath(self, name, stage_name, id) -> list:
        return [i for r, i, f in self.result
                if i.name == name and i.stage_name == stage_name and i.id == id]

    def check(self, cond: Dict[str, bool], index: int = -1) -> bool:
        if self.result[index][0] is None:
            return False
        else:
            inp = self.latest[0][:]
            ans: List[List[str]] = [j for i in self.latest[1].answers
                                    for j in i
                                    ]
            if cond["COMP_IGNORE_SPACE"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i])):
                        ans[i][j] = ans[i][j].replace(" ", "")
                for i in range(len(inp)):
                    inp[i] = inp[i].replace(" ", "")
            if cond["COMP_IGNORE_CASE"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i]))
                        ans[i][j] = ans[i][j].lower()
                for i in range(len(inp)):
                    inp[i] = inp[i].lower()
            if cond["COMP_IGNORE_LAST_PERIOD"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i]))
                        if ans[i][j]:
                            if ans[i][j][-1] == ".":
                                ans[i][j] = ans[i][j][:-1]
                for i in range(len(inp)):
                    if inp[i]:
                        if inp[i][-1] == ".":
                            inp[i] = inp[i][:-1]
            if not cond["COMP_NOT"]:
                pass
                # mrs
            #else:
            if True:
                if cond["ANSWER_WITHOUT_ORDER"]:
                    mrs = []
                    for i in inp:
                        for k in range(len(ans)):
                            try:
                                if i in ans[k]:
                                    del ans[k]
                                    mrs.append(1.0)
                                    break
                            except ValueError:
                                pass
                    else:
                        mrs.append(0)
                else:
                    mrs = [
                        any(i==a for a in als) for i, als in zip(inp, ans)
                    ]
            self.latest[2] = mrs


    def answer(self, ans: List[str], index: int = -1) -> bool:
        self.result[index][0] = ans
        return True

    @property
    def latest(self) -> List[List[str], AntanswerElement, List[float]]:
        if len(self.result) > 0:
            return self.result[-1]

    def __getitem__(self, item):
        return self.result[item]

    def __len__(self):
        return len(self.result)


if __name__ == '__main__':
    T = AntanswerDataStruct()
    T.load_fromstring("""##$ name = 그레고리우스
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
    """, "ggg")
    for i in T.stages["main"]:
        for j in i.questions:
            for d in j:
                print(d)
        for j in i.answers:
            for d in j:
                print(d)
