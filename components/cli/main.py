from random import randrange, choice
from time import sleep
from difflib import SequenceMatcher
from time import time
from tkinter import filedialog, Tk
from anwFunctions.anwReaders.reader import READ_ANW
import json
import sys
import os

# TODO: 후보정 만들기 (command_pork)
# TODO: aqs list 등 구조 문서화 하기

class Main():
    """
    main cli module
    antanswer 'main' cycle is

    - __init__
    - init_routine : dispatch command
    - command_set... : set anw file
    - starting routine

    """

    def __init__(self, opt):
        self.anw_standard = opt["anw_standard"]
        self.cond_default = {
            "COMP_IGNORE_SPACE": True,  # ignoring space, blank like '\t' won't be replaced
            "COMP_IGNORE_CASE": True,  # ignoring case, replace upper to lower
            "ANSWER_WITHOUT_ORDER": True,  # when answering quest, order don't interrupt you
            "COMP_NOT": True,  # ignoring sequence matcher(compare) method # in now deprecated sorry
            "RESULT_DISPLAY_QUEST": True,  # displaying Quest
            "COMP_IGNORE_LAST_PERIOD": True,  # ignoring the last period
            # support CLI, but main is GUI.
            "RESULT_MANUAL_POST_CORRECTION": True  # post correction at result time GUI main cond
        }  # default preferences
        self.bVariables = opt["bVariables"]  # bVariables

        # used in routine = core: initialized in 'set_anw'
        self.anw = None  # anw file
        self.aqs: list = None  # aqList real
        self.target_stages: list = None  # target stages list
        self.cond_used: dict = None  # cond used in routine


        # used in routine = sub-core: initialized in 'starting_routine' or 'sampling'
        self.detail = [None, None]  # details in routine [0]: wil, [1]: recent;

        self.score = 0  # count you answer correctly.

        self.start_time = None  # mark start time to calculate time
        self.result: list = None  # replies about quest
        self.samples: list = None  # pre-generated answer-quest list that will show you

    def init_routine(self):
        """
        loading etc. and starting command dispatcher system
        :return Boolean
            -True: correct exit
            -False: wrongthing some exit
        """

        print("loading...")
        sleep(0.75)
        print("completed.")
        while True:
            command = input(">>> ").strip().split(" ")
            c = self.command_dispatch(command)
            if c == 0:
                return True
            elif c == -1:
                print("<Small Error Occurred>")
            elif c == -2:
                print("<Critical Error Occurred>")
                return False
            elif c == 1:
                pass

    def starting_routine(self):
        if self.aqs is None:
            raise Exception("<error>: anw file isn't defined")

        self.start_time = time()  # start_time initial
        self.samples = list(self.sampling())  # samples initial
        self.result = []  # result initial
        for i, s in enumerate(self.samples):
            self.result.append(self.core_quest(s, i))

    def core_quest(self, aqi, ind):
        """
        core of quest
        :param aqi: sampled answer-question index
        :param ind: wil index
        :return:
        """
        emode = self.aqs[aqi][0][0]
        answers = self.aqs[aqi][0][1]
        questions = tuple(choice(i) for i in self.aqs[aqi][0][2])
        scope_stage = self.aqs[aqi][1]
        inputList = []

        self.view_quest(questions, scope_stage)
        for i in range(len(answers)):
            print("({})".format(i), end='')
            inputList.append(self.input_quest())

        print("\n" * 10)
        r = self.reward_quest(answers, inputList)
        print("{0}/{1} 정답률: {2:>3.2f}%".format(ind + 1, self.detail[0], self.score / (ind + 1) * 100))
        return zip(r, inputList)

    def view_quest(self, q, scope_stg, cat=None):
        """
        show quest to you
        :param q:
        :param scope_stg:
        :param cat:
        :return:
        """
        if len(q) < 2:
            print("=" * 18, "{0:<7}".format(scope_stg), "===") if cat == None else print("=" * 5,
                                                                                         "{0:<7}:{0:<15}".format(
                                                                                             scope_stg, " ".join(cat)),"=")

            print(q[0])
            print("=" * 30)
        else:
            print("=" * 30)
            for i, v in enumerate(q):
                print("({})".format(i + 1) + "-" * 24)
                print(v)
            print("=" * 30)

    def input_quest(self):
        """
        answering
        :return: answer
        """
        inp = input(": ").strip()
        return inp

    def reward_quest(self, ans, inputs):
        """
        check answer is correct
        :param ans: answers list
        :param inputs: input i answered
        :return mrs: 0..1 value list about each
        """
        ans = list(ans)
        # TODO: more simply
        if self.cond_used["COMP_IGNORE_SPACE"] is True:

            for i in range(len(ans)):

                ans[i] = [ans[i][j].replace(" ", "")for j in range(len(ans[i]))]

            for i in range(len(inputs)):
                inputs[i] = inputs[i].replace(" ", "")
        if self.cond_used["COMP_IGNORE_CASE"] is True:
            for i in range(len(ans)):
                ans[i] = [ans[i][j].lower() for j in range(len(ans[i]))]
            for i in range(len(inputs)):
                inputs[i] = inputs[i].lower()

        if self.cond_used["COMP_IGNORE_LAST_PERIOD"] is True:
            for i in range(len(ans)):
                ans[i] = [ans[i][j][:-1] if ans[i][j][-1] == "." else ans[i][j] for j in range(len(ans[i]))]
            for i in range(len(inputs)):
                inputs[i] = inputs[i][:-1] if inputs[i][-1] == "." else inputs[i]


        if self.cond_used["COMP_NOT"] is False:
            if self.cond_used["ANSWER_WITHOUT_ORDER"] is True:
                mrs = [max(round(self.compare(s, i), 2) for a in ans
                           for s in a) for i in inputs]
            else:
                mrs = [max(round(self.compare(a, i), 2) for a in als) for i, als in zip(inputs, ans)]
        else:
            if self.cond_used["ANSWER_WITHOUT_ORDER"] is True:
                mrs = []
                t = [list(a) for a in ans]
                for i in inputs:
                    for k in range(len(t)):
                        try:
                            if i in t[k]:
                                del t[k]
                                mrs.append(1)
                                break

                        except ValueError:
                            pass
                    else:
                        mrs.append(0)

            else:
                mrs = tuple(any(i == a for a in als) for i, als in zip(inputs, ans))

        if self.cond_used["COMP_NOT"] is False:
            if min(mrs) > 0.92:
                print("정답! : {}".format(";".join(map(str, mrs))))
                self.score += 1
            else:
                print("오답! : {}".format(";".join(map(str, mrs))))
        else:
            if all(mrs):
                print("정답! : {}".format(";".join(map(str, mrs))))
                self.score += 1
            else:
                print("오답! : {}".format(";".join(map(str, mrs))))

        return mrs

    def closing_routine(self):
        """
        close routine and exit the routine
        :return :
        """

        fin_time = time() - self.start_time
        if self.detail[0] == 0:
            return
        print("\n" * 24)
        print("RESULT :")
        print("정답률: {0:>3.2f}%".format(self.score / self.detail[0] * 100))
        print("걸린 시간: {0:<.4f}s".format(fin_time))
        print("걸린 시간/문항: {0:<.4f}s".format(fin_time / self.detail[0]))
        print()
        print()
        qc = 1  # questcount
        for r, i in zip(self.result, self.samples):
            if self.cond_used["RESULT_DISPLAY_QUEST"]:
                for c in range(len(self.aqs[i][0][2])):
                    print(">", self.aqs[i][0][2][c])
            for ii, mr in enumerate(r):

                print("({0})-{1} : ({2:.2f}){3} / {4}".format(qc, ii, mr[0], mr[1], self.aqs[i][0][1][ii]))
            print()
            qc += 1
        print()

    def sampling(self):
        """
        get correct wil & recent with checking recent & recentValue
        then, sample answer-question with recent & recentValue
        :return:
        """
        history = []
        # get correct wil & recent
        for k, v in self.anw["detail_infile"].items():  # priority: recentValue > recent
            if v is None:
                if k == "recentValue":
                    self.detail[1] = int(self.bVariables["bRecentValue"] * len(self.aqs))
                elif k == "wil":
                    self.detail[0] = self.bVariables["bWil"]
                elif k == "recent":
                    if self.detail[1] is not None:
                        pass
                    else:  # recent Check
                        if self.bVariables["bRecent"] > len(self.aqs):
                            self.detail[1] = len(self.aqs)
                        else:
                            self.detail[1] = self.bVariables["bRecent"]
                else:
                    raise Exception("?sampling0r")
            else:
                if k == "recentValue":
                    self.detail[1] = int(v * len(self.aqs))
                elif k == "wil":
                    self.detail[0] = v
                elif k == "recent":
                    if self.detail[1] is not None:
                        pass
                    else:
                        if v > len(self.aqs):
                            self.detail[1] = len(self.aqs)
                        else:
                            self.detail[1] = v
                else:
                    raise Exception("?sampling1r")

        for i in range(self.detail[0]):
            r = randrange(0, len(self.aqs))
            while r in history[-self.detail[1]:]:
                r = randrange(0, len(self.aqs))
            history.append(r)
            yield r

    def set_anw(self):
        """
        setting default anw vars etc. :core
        :return:
        """
        print("==| {} |==================".format(self.anw['name']))
        print(self.anw['description'])
        print("=" * 30)

        self.target_stages = []
        self.make_aqs()

        self.cond_used = {}
        for ck, v in self.anw["cond"].items():
            if v is None:
                self.cond_used[ck] = self.cond_default[ck]
            else:
                self.cond_used[ck] = v

    def make_aqs(self):
        if self.target_stages:
            self.aqs = [(aq, stage)
                        for stage in self.target_stages
                        for aq in self.anw["stages"][stage]]
        else:
            self.aqs = [(aq, stage)
                        for stage in self.anw["stages"].keys()
                        for aq in self.anw["stages"][stage]]

    def exit_process(self):
        print("exiting cli...")
        return 0


    # fixme: not good but now i'm not good at coding. someday i'll reform it.
    def compare(self, a: str, b: str) -> float:
        """
        find similarity between two strings by using SequenceMatcher
        :param a: compare string
        :param b: compare string2
        :return: raito of a, b match
        """

        return SequenceMatcher(None, a, b).ratio()

    def command_dispatch(self, cmd):
        mname = "command_" + str(cmd[0])
        if hasattr(self, mname):
            method = getattr(self, mname)
            return method(cmd[1:])
        else:
            print("<Wrong Command>: 'help' to help")

    def command_cut(self, args):
        """
        link to exit_process
        :param args:
        :return:
        """

        return self.exit_process()

    def command_run(self, args):

        self.starting_routine()
        self.closing_routine()
        return 1

    def command_set(self, args):
        pathtemp: list = []
        for i in args:
            if i == "-d":
                root = Tk()
                root.withdraw()

                path = filedialog.askopenfilename(title="anw 파일을 선택하세요.",
                                                  initialdir="./anwdatapack",
                                                  filetypes=(

                                                      ("안탠서 파일", ".anw;.anp"),
                                                      ("암호화 안탠서 파일", ".awc;.apc"),
                                                      ("텍스트/xml 파일", ".txt;.xml")
                                                  )
                                                  )
                break
            else:
                pathtemp.append(i)
        else:
            path = " ".join(pathtemp)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.anw = READ_ANW(f)
                self.set_anw()
        except FileNotFoundError as e:
            print(e)
            return -1
        return True

    def command_help(self, args):
        print("""<command>:
cut: exit process
set: set anw file
    -usage: 'set -d' open FileDialog to choose file
    -usage: 'set <filePath>' type path to specify file
run: run routine
help: show what you see now""")
        return 1

    def command_porc(self, args):
        pass

    def debug_log_traceback(self):
        e_type, e_obj, e_tb = sys.exc_info()
        fname = os.path.split(e_tb.tb_frame.f_code.co_filename)[1]
        print(e_obj, "in", "\""+fname+"\"", "line", e_tb.tb_lineno)

if __name__ == '__main__':
    runner = Main()
    runner.init_routine()