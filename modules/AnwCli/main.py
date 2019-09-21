from random import randrange, choice
from time import sleep
from difflib import SequenceMatcher
from time import time
import json

from anwBaseMoudules.AnwBaseModule import AnwBaseModule


class AnwMainCliModule(AnwBaseModule):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_routine(self, file_anw, file_opt):
        with open("modules\\AnwCli\\preference.opt", 'r', encoding="utf-8-sig") as f:
            try:
                pref = json.load(f)

                self.COMP_WITHOUT_SPACE = pref["COMP_WITHOUT_SPACE"]
                self.ANS_NON_ORDER = pref["ANS_NON_ORDER"]
                self.NOT_COMP = pref["NOT_COMP"]  # if ANS_NON_ORDER is True: setting it True is recommended
                self.RESULT_QUEST_DISPLAY = pref["RESULT_QUEST_DISPLAY"]
                self.COMP_IGNORE_CASE = pref["COMP_IGNORE_CASE"]
            except (KeyError, FileNotFoundError, json.JSONDecodeError):
                raise

        self.file_anw = file_anw
        self.file_opt = file_opt
        self.score = 0

        self.reset_init_routine(pref)
        print("로딩 중")
        sleep(1)
        print()
        while True:
            command = input(">>> ").strip()
            c = self.command_dispatch(command)
            if c == "EC00":
                break

    def starting_routine(self):
        self.samples = tuple(self.sampling())  #
        self.result = []  #
        self.start_time = time()
        for i, s in enumerate(self.samples):
            self.result.append(self.core_quest(s, i))

    def core_quest(self, aqi, ind):
        questions = tuple(choice(i) for i in self.Aqs[aqi][0][2])
        answers = self.Aqs[aqi][0][1]
        scope_stage = self.Aqs[aqi][1]
        inputList = []
        self.view_quest(questions, scope_stage)
        for i in range(len(answers)):
            print("({})".format(i), end='')
            inputList.append(self.input_quest())

        print("\n" * 10)
        r = self.reward_quest(answers, inputList)
        print("{0}/{1} 정답률: {2:>3.2f}%".format(ind + 1, self.anw["detail"][0], self.score / (ind + 1) * 100))
        return zip(r, inputList)

    def view_quest(self, q, scope_stg, cat=None):
        if len(q) < 2:
            print("=" * 18, "{0:<7}".format(scope_stg), "===") if cat == None else print("=" * 5,
                                                                                         "{0:<7}:{0:<15}".format(
                                                                                             scope_stg, " ".join(cat)),
                                                                                         "=")
            print(q[0])
            print("=" * 30)
        else:
            print("=" * 30)
            for i, v in enumerate(q):
                print("({})".format(i + 1) + "-" * 24)
                print(v)
            print("=" * 30)

    def input_quest(self):
        inp = input(": ").strip()
        if self.COMP_WITHOUT_SPACE:
            inp = inp.replace(" ", "")
        if self.COMP_IGNORE_CASE:
            inp = inp.lower()
        return inp

    def reward_quest(self, ans, inputs):
        if self.NOT_COMP == False:
            if self.ANS_NON_ORDER == True:
                mrs = tuple(max(round(self.compare(s, i), 1) for a in ans for s in a) for i in inputs)
            else:
                mrs = tuple(max(round(self.compare(a, i), 1) for a in als) for i, als in zip(inputs, ans))

        else:
            if self.ANS_NON_ORDER == True:
                mrs = []
                t = [list(a) for a in ans]
                for i in inputs:
                    for k in range(len(t)):
                        try:
                            del (t[k])
                            mrs.append(True)
                            break
                        except ValueError:
                            pass
                    else:
                        mrs.append(False)
                mrs = tuple(mrs)

            else:
                mrs = tuple(any(i == a for a in als) for i, als in zip(inputs, ans))

        if not self.NOT_COMP:
            if min(mrs) > 0.92:
                print("정답! : {}".format(";".join(map(str, mrs))))
                self.score += 1
            else:
                print("오답! : {}".format(";".join(map(str, mrs))))
        else:
            if all(mrs):
                print("정답!")
                self.score += 1
            else:
                print("오답!")

        return mrs

    def closing_routine(self):
        fin_time = time() - self.start_time
        if self.anw["detail"][0] == 0:
            return
        print("\n" * 24)
        print("RESULT :")
        print("정답률: {0:>3.2f}%".format(self.score / self.anw["detail"][0] * 100))
        print("걸린 시간: {0:<.4f}s".format(fin_time))
        print("걸린 시간/문항: {0:<.4f}s".format(fin_time / self.anw["detail"][0]))
        print()
        print()
        qc = 1  # questcount
        for r, i in zip(self.result, self.samples):
            for ii, mr in enumerate(r):
                if self.RESULT_QUEST_DISPLAY:
                    print("\n>".join(self.Aqs[i][0][2][ii]))
                print("({0})-{1} : ({2:.2f}){3} / {4}".format(qc, ii, mr[0], mr[1], self.Aqs[i][0][1][ii]))
            print()
            qc += 1
        print()

    def reset_routine(self):
        self.score = 0

    def reset_init_routine(self, pref):
        self.anw = self._reader(self.file_anw, self.file_opt, pref)

        print("==| {} |==================".format(self.anw['name']))
        print(self.anw['description'])
        print("=" * 30)
        if len(self.anw['stages'].keys()) == 1:
            select = "all"
        else:
            print("stage를 선택해 주십시오.")

            for item in self.anw['stages']:
                print(" : {}".format(item))
            print()
            select = input(" : ")

        if select.lower().strip() == "all":
            self.target_stages = list(self.anw['stages'].keys())
        else:
            if not select.strip():
                self.target_stages = ["main"]
            else:
                self.target_stages = [s.strip() for s in select.split(";")]

            for i in self.target_stages:
                if i not in self.anw['stages']:
                    raise

        self.Aqs = tuple((aq, stage)
                         for stage in self.target_stages
                         for aq in self.anw['stages'][stage]
                         )

    def exit_process(self):
        print("AnwCli 종료중...")
        sleep(0.1)
        print("AnwCli 종료 완료.")
        return "EC00"

    def sampling(self):
        ### recent check
        recent = 0

        if self.anw['detailMode'] in (2, 5):
            recent = self.anw['detail'][1]
            if recent >= len(self.Aqs):
                raise
        elif self.anw['detailMode'] in (3, 6):
            recent = int(len(self.Aqs) * self.anw['detail'][2])
        else:
            pass

        self.history = []

        for i in range(recent):
            r = randrange(0, len(self.Aqs))
            while r in self.history:
                r = randrange(0, len(self.Aqs))

            yield r
            self.history.append(r)

        for i in range(recent, self.anw["detail"][0]):
            r = randrange(0, len(self.Aqs))
            while r in self.history[i - recent:i]:
                r = randrange(0, len(self.Aqs))
            yield r
            self.history.append(r)

    def compare(self, a: str, b: str) -> float:
        return SequenceMatcher(None, a, b).ratio()

    def command_dispatch(self, cmd):
        mname = "command_" + str(cmd)
        if hasattr(self, mname):
            method = getattr(self, mname)
            return method()
        else:
            print("[NoGotPleaseNo!] : 그딴거 없어요!")

    def command_cut(self):
        return self.exit_process()

    def command_run(self):
        self.starting_routine()
        self.closing_routine()
        self.reset_routine()
        return "RN00"

    def command_set(self):
        self.file_opt.seek(0)
        self.file_anw.seek(0)
        self.reset_init_routine()
        return "RS00"


### 필수
MainABM = AnwMainCliModule()
