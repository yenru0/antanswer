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

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.L)


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

    def getRealQuestion(self, reverse_aq=False) -> List[str]:
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

    def __len__(self):
        return len(self.elements)

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

        self.detail_used = AntanswerDetail()
        self.result = AntanswerResult() # need initializing
        self.weights: Dict[str, List[int]] = {}
        self.weightMult = 1

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
            wbr["detail_infile"]["wil"] if wbr["detail_infile"]["wil"] else 0,
            wbr["detail_infile"]["recent"] if wbr["detail_infile"]["recent"] else 0,
            wbr["detail_infile"]["recentValue"] if wbr["detail_infile"]["recentValue"] else 0.0
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

    def sampling(self, detail: AntanswerDetail, weights: Dict[str, List[int]], weightAddAlt=0, weightMult=1):
        """
        :return:
        """
        self.weightMult = weightMult
        self.detail_used.set(
            wil=detail.wil if detail.wil else self.detail.wil,
            recent=detail.recent if detail.recent else self.detail.recent,
            recentValue=detail.recentValue if detail.recentValue else self.detail.recentValue
        )

        aqs = []
        weightList = []
        rct = 0
        for v in self.stages:

            if len(self.stages[v]) < len(weights[v]):
                weights[v] = weights[v][:len(self.stages[v])]
            elif len(self.stages[v]) > len(weights[v]):
                weights[v].extend([0] * (len(self.stages[v]) - len(weights[v])))
            else:
                pass

            if self.use[v]:
                weightList.extend(weights[v])
                for e in self.stages[v]:
                    aqs.append(e)

        self.weights = weights

        if self.detail_used.recentValue:
            rct = int(self.detail_used.recentValue * len(aqs))
        else:
            rct = self.detail_used.recent

        history = []

        weighted: bool = bool(weights)
        if weightAddAlt == 0:
            weighted = False
        elif weightAddAlt >= 1:
            s = sum(weightList) + len(weightList)
            if s == 0:
                weighted = False
            else:
                weightList = (np.array(weightList) + np.array([1] * len(weightList))) / s

        rng = np.random.default_rng()
        yield None
        for i in range(self.detail_used.wil):
            if weighted:
                r = rng.choice(aqs, p=weightList)
            else:
                r = rng.choice(aqs)
            if len(aqs) <= rct:
                rct = len(aqs) -1
            while r in history[-rct:]:
                if weighted:
                    r = rng.choice(aqs, p=weightList)
                else:
                    r = rng.choice(aqs)
            if rct != 0:
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

    def clearResult(self):
        self.result = AntanswerResult()


### U'routine

class AntanswerResult:
    def __init__(self, *args):
        self.result: List[List[List[str], AntanswerElement, List[float]]] = []
        self.score = 0
        self.count = 0

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
        isCorrection = False
        if self.result[index][2] is not None:
            isCorrection = True
        if self.result[index][0] is None:
            return False
        else:
            inp = self.result[index][0][:]
            ans: List[List[str]] = [[j for j in i] for i in self.result[index][1].answers

                                    ]
            print(ans)
            if cond["COMP_IGNORE_SPACE"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i])):

                        ans[i][j] = ans[i][j].replace(" ", "")
                for i in range(len(inp)):
                    inp[i] = inp[i].replace(" ", "")
            if cond["COMP_IGNORE_CASE"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i])):
                        ans[i][j] = ans[i][j].lower()
                for i in range(len(inp)):
                    inp[i] = inp[i].lower()
            if cond["COMP_IGNORE_LAST_PERIOD"]:
                for i in range(len(ans)):
                    for j in range(len(ans[i])):
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
            # else:
            if True:
                if cond["ANSWER_WITHOUT_ORDER"]:
                    mrs = []
                    for i in inp:
                        for k in range(len(ans)):
                            try:
                                if i in ans[k]:
                                    print(i, ans[k])
                                    del ans[k]
                                    mrs.append(1.0)
                                    break
                            except ValueError:
                                pass
                        else:
                            mrs.append(0)
                else:
                    mrs = [
                        any(i == a for a in als) for i, als in zip(inp, ans)
                    ]

            if not cond["COMP_NOT"]:
                pass
                #if min(mrs) > 0.92:
                    #return mrs, True
                #else:
                    #return mrs, False
                    #
            if True:
                if all(mrs):
                    if isCorrection:
                        if self.result[index][2]:
                            pass
                        else:
                            self.score += 1
                    else:
                        self.score += 1
                else:
                    if isCorrection:
                        if self.result[index][2]:
                            self.score -= 1
                        else:
                            pass
                    else:
                        pass
            self.count += 1
            self.result[index][2] = mrs

    def correct(self, cond: Dict[str, bool], index: int, state: (bool, int, float)) -> bool:
        old = self.result[index][2]

        if isinstance(state, float):
            if 0 <= state <= 1:
                self.result[index][2] = [state] * len(old)
            else:
                self.result[index][2] = [1.0 if state else 0.0] * len(old)
        else:
            self.result[index][2] = [1.0 if state else 0.0] * len(old)

        if old is None:
            if self.result[index][2]:
                self.score += 1
            else:
                pass
        else:
            # IG NOT COMP
            if any(old):
                if any(self.result[index][2]):
                    pass
                else:
                    self.score -= 1
            else:
                if any(self.result[index][2]):
                    self.score += 1
                else:
                    pass

        return True

    def answer(self, ans: List[str], index: int = -1) -> bool:
        self.result[index][0] = ans
        return True

    @property
    def latest(self):
        if len(self.result) > 0:
            return self.result[-1]

    def __getitem__(self, item):
        return self.result[item]

    def __setitem__(self, key, value):
        self.result[key] = value

    def __len__(self):
        return len(self.result)


