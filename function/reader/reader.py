import re
import json
from enum import Enum, auto
from typing import List, Tuple, Dict


class TokenType(Enum):
    LineBreak = auto()

    # Define StartSetter
    StageSSKeyword = auto()
    LetSSKeyword = auto()
    CommandSSKeyword = auto()

    # Define Comment
    InlineCommentKeyword = auto()
    BlockCommentKeyword = auto()

    Letter = auto()  # to be exact, letter or void (e.g. ' ', '\t')
    ExpressionLetter = auto()

    L3Sep = auto()
    L2Sep = auto()
    L1Sep = auto()

    Opener = auto()
    Closer = auto()


class Token():
    def __init__(self, tknType: TokenType, value: str, pos: Tuple[int, int] = (0, 0)):
        """
        :param tknType: type of token
        :param value: its text
        :param pos: (line number, pos of its line)
        """
        self.tknType: TokenType = tknType
        self.value: str = value
        self.pos: Tuple[int, int] = pos  # line, pos

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.tknType in [TokenType.ExpressionLetter, TokenType.Letter]:
            return "{}({})".format(self.tknType.name, self.value)
        else:
            return "{}".format(self.tknType.name)


class Reader:
    PATTERN_IS_LETTER = re.compile(r"[a-z= ]")

    def __init__(self, src: str):
        self.src = src + "\n"
        self.src_size = len(src)
        self.var = {}  # used custom var
        self.tokens: List[Token] = []

    def read(self):
        pass

    def nextToken(self, cnt) -> Tuple[int, Token]:
        text = ''
        s = self.src[cnt]
        if s == '#':
            cnt += 1
            s = self.src[cnt]
            text += s
            if s == '#':
                cnt += 1
                s = self.src[cnt]
                text += s
                if s == '@':
                    return cnt + 1, Token(TokenType.StageSSKeyword, '##@')
                elif s == '!':
                    return cnt + 1, Token(TokenType.CommandSSKeyword, '##!')
                elif s == '$':
                    return cnt + 1, Token(TokenType.LetSSKeyword, '##$')
                elif s == '#':
                    return cnt + 1, Token(TokenType.InlineCommentKeyword, '###')



        elif s == '{':
            return cnt + 1, Token(TokenType.Opener, '{')

        elif s == '}':
            return cnt + 1, Token(TokenType.Closer, '}')

        elif s == '\n':
            return cnt + 1, Token(TokenType.LineBreak, '\n')

        elif Reader.PATTERN_IS_LETTER.match(s):  # start of letters loop
            text += s
            cnt += 1
            s = self.src[cnt]
            while Reader.PATTERN_IS_LETTER.match(s):
                text += s
                cnt += 1
                s = self.src[cnt]
            return cnt, Token(TokenType.ExpressionLetter, text)

        elif s == ':':
            return cnt + 1, Token(TokenType.L1Sep, ':')

        elif s == '|':
            return cnt + 1, Token(TokenType.L2Sep, "|")

        elif s == ';':
            return cnt + 1, Token(TokenType.L3Sep, ";")
        else:
            raise Exception("unexpected character")

    def tokenize(self) -> bool:
        cnt = 0

        while cnt < self.src_size:
            cnt, tkn = self.nextToken(cnt)
            self.tokens.append(tkn)
        return True

    def preprocess(self):
        pass

    def preprocess_inlineComment(self):
        pass

    def preprocess_blockComment(self):
        pass

    def parse(self):
        pass

    def parse_command(self, cnt) -> (Tuple[List, int], bool):
        cargs = []

        tkn = self.tokens[cnt]

        if tkn.tknType is TokenType.CommandSSKeyword:
            cnt += 1
            tkn = self.tokens[cnt]

            if tkn.tknType is TokenType.ExpressionLetter:
                cargs = [i.strip() for i in tkn.value.split() if i.strip()]
                cnt += 1
                tkn = self.tokens[cnt]

            if tkn.tknType is TokenType.LineBreak:
                cnt += 1
            else:
                raise Exception
        else:
            return False
        return cargs, cnt

    def parse_let(self, cnt) -> (Tuple[List, int], bool):
        cell = []

        tkn = self.tokens[cnt]
        if tkn.tknType is TokenType.LetSSKeyword:
            cnt += 1
            tkn = self.tokens[cnt]
            t = self.parse_subsub(cnt)
            if t:
                cnt = t[1]
                for i in t[0]:
                    pair = i.split("=")
                    if len(pair) != 2:
                        raise Exception("wrong pair")
                    else:
                        cell.append(pair)
                tkn = self.tokens[cnt]
            if tkn.tknType is TokenType.LineBreak:
                cnt += 1
            else:
                raise Exception
        else:
            return False
        return cell, cnt

    def parse_expressCell(self, cnt) -> [Tuple[str, int], bool]:
        cell = ""
        tkn = self.tokens[cnt]
        if tkn.tknType is TokenType.ExpressionLetter:
            cell += tkn.value
            cnt += 1
        elif tkn.tknType is TokenType.Opener:
            cnt += 1
            tkn = self.tokens[cnt]
            while True:
                if tkn.tknType is TokenType.ExpressionLetter:
                    cell += tkn.value
                    cnt += 1
                    tkn = self.tokens[cnt]
                elif tkn.tknType is TokenType.LineBreak:
                    cell += tkn.value
                    cnt += 1
                    tkn = self.tokens[cnt]
                elif tkn.tknType is TokenType.Closer:
                    cnt += 1
                    break
                else:
                    if tkn.tknType in [TokenType.L3Sep, TokenType.L2Sep, TokenType.L1Sep]:
                        return False
                    else:
                        raise Exception
        else:
            return False
        return cell, cnt

    def parse_subsub(self, cnt) -> [Tuple[List, int], bool]:
        cell = []
        backward = False

        tkn = self.tokens[cnt]
        t = self.parse_expressCell(cnt)
        if t or tkn.tknType is TokenType.L3Sep:
            if t:
                cnt = t[1]
                cell.append(t[0])
                tkn = self.tokens[cnt]
            elif tkn.tknType is TokenType.L3Sep:
                cnt += 1
                tkn = self.tokens[cnt]

            while True:
                t = self.parse_expressCell(cnt)
                if tkn.tknType is TokenType.L3Sep:
                    cnt += 1
                elif t:
                    if backward:
                        raise Exception
                    cnt = t[1]
                    cell.append(t[0])
                    backward = True
                    continue
                else:
                    break
                backward = False
        elif tkn.tknType is TokenType.Opener:
            text = ""
            cnt += 1
            tkn = self.tokens[cnt]
            while True:
                t = self.parse_expressCell(cnt)
                if tkn.tknType is TokenType.L3Sep:
                    cnt += 1
                    if text.strip():
                        cell.append(text)
                        text = ""
                    tkn = self.tokens[cnt]
                elif t:
                    if backward:
                        raise Exception
                    cnt = t[1]
                    text += t[0]
                    tkn = self.tokens[cnt]
                    backward = True
                    continue
                elif tkn.tknType is TokenType.LineBreak:
                    while tkn.tknType is TokenType.LineBreak:
                        cnt += 1
                        text += tkn.value
                        tkn = self.tokens[cnt]
                elif tkn.tknType is TokenType.Closer:
                    cnt += 1
                    if text.strip():
                        cell.append(text)
                        text = ""
                    tkn = self.tokens[cnt]
                else:
                    if tkn.tknType in [TokenType.L2Sep, TokenType.L1Sep]:
                        return False
                    else:
                        raise Exception
                backward = False
        else:
            return False

        return cell, cnt

    def parse_sub(self, cnt):
        cell = []
        backward = False

        tkn = self.tokens[cnt]
        t = self.parse_subsub(cnt)
        if t or tkn.tknType is TokenType.L2Sep:
            if t:
                cnt = t[1]
                cell.append(t[0])
                tkn = self.tokens[cnt]
            elif tkn.tknType is TokenType.L2Sep:
                cnt += 1
                tkn = self.tokens[cnt]



    def parse_element(self, cnt):
        pass

    def parse_stage(self, cnt):
        pass
