import re
import json
from enum import Enum, auto
from typing import List, Tuple

PATTERN_IS_LETTER = re.compile(r"[a-z= ]")

"""
antanswer에 대한 EBNF


<Filter> ::= SubSub

<StageSSKeyword> ::= "##@"
<CommandSSKeyword> ::= "##!"
<LetSSKeyword> ::= "##$"
<InlineCommentSSKeyword> ::= "###"

<LineBreak> ::= "\n"
<L3Sep> ::= ";"
<L2Sep> ::= "|"
<L1Sep> ::= ":"

<Void> ::= ' '
<CommentCell> ::= <InlineCommentSSKeyword><InlineExpressCell><LineBreak>


<ExpressLetter> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | " "


<InlineExpressCell> ::= <ExpressLetter>*
<ExpressCell> ::= <ExpressLetter>*
    | "{" <ExpressLetter>* {<ExpressLetter>*[CommentCell]{<LineBreak>}} "}"

<SubSub> ::= <ExpressCell>{<L3Sep><ExpressCell>}[<L3Sep>]
    | "{" LineBreak* <ExpressCell>[{Void}<CommentCell>]{<LineBreak>}{<L3Sep>[{Void}<CommentCell>]{<LineBreak>}<ExpressCell>[{Void}<CommentCell>]{<LineBreak>}}[<L3Sep>] LineBreak* "}"

<Sub> ::= <SubSub>{<L2Sep><SubSub>}[<L2Sep>]
    | "{" LineBreak* <SubSub>{<L2Sep><SubSub>}[<L2Sep>] LineBreak* "}"

<Element> ::= <Sub>{<L1Sep><Sub>}[<L1Sep>]<LineBreak>
    | "{" LineBreak* <Sub>{<L1Sep><Sub>}[<L1Sep>] LineBreak* "}"

<Stage> ::= <StageSSKeyword><InlineExpressCell><LineBreak>{<Element>{<LineBreak>}}
    | <StageSSKeyword><InlineExpressCell> "{" {<Element>{<LineBreak>}} "}" {LineBreak}

"""

"""
Antanswer Reader converts anw file to ADS through the following process:

`Tokenization` -> `CommentProcessing` -> `Parsing` -> `ValidChecking&Modifying` -> `DataProcessing`


`Tokenization` : tokenize given data

`CommentProcessing` : pre-process comment from given data

`Parsing` : Checking & Parsing given data most of Exception is checked in Parsing routine.

`ValidChecking&Modifying` : check if parsed data is valid. if parsed data is invalid, raise Exception or modifying data.

`DataProcessing` : process data with processed value from given data.

"""


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


# tokenize function

def nextToken(string: str) -> Tuple[str, Token]:
    text = ''
    c = 0
    s = string[c]
    if s == '#':
        c += 1
        s = string[c]
        text += s
        if s == '#':
            c += 1
            s = string[c]
            text += s
            if s == '@':
                return string[c + 1:], Token(TokenType.StageSSKeyword, '##@')
            elif s == '!':
                return string[c + 1:], Token(TokenType.CommandSSKeyword, '##!')
            elif s == '$':
                return string[c + 1:], Token(TokenType.LetSSKeyword, '##$')
            elif s == '#':
                return string[c + 1:], Token(TokenType.InlineCommentKeyword, '###')



    elif s == '{':
        return string[c + 1:], Token(TokenType.Opener, '{')

    elif s == '}':
        return string[c + 1:], Token(TokenType.Closer, '}')

    elif s == '\n':
        return string[c + 1:], Token(TokenType.LineBreak, '\n')

    elif PATTERN_IS_LETTER.match(s):  # start of letters loop
        text += s
        c += 1
        s = string[c]
        while PATTERN_IS_LETTER.match(s):
            text += s
            c += 1
            s = string[c]
        return string[c:], Token(TokenType.ExpressionLetter, text)

    elif s == ':':
        return string[c + 1:], Token(TokenType.L1Sep, ':')

    elif s == '|':
        return string[c + 1:], Token(TokenType.L2Sep, "|")

    elif s == ';':
        return string[c + 1:], Token(TokenType.L3Sep, ";")
    else:
        raise Exception("unexpected character")


def tokenize(source: str) -> List[Token]:
    source += "\n"

    consumed = source[:]

    tokens = []

    while consumed or consumed.strip():
        consumed, tkn = nextToken(consumed)
        tokens.append(tkn)

    return tokens


# pre-process comment functions
# Mostly remove

def process_inlineComment(tokens: List[Token]) -> List[Token]:
    pass


def process_multlineComment(tokens: List[Token]) -> List[Token]:
    pass


# parse functions
def parse_command(tokens: List[Token]):
    cargs = []
    c = 0
    tkn = tokens[c]
    if tkn.tknType is TokenType.CommandSSKeyword:
        c += 1
        tkn = tokens[c]

        if tkn.tknType is TokenType.ExpressionLetter:
            cargs = [i.strip() for i in tkn.value.split()
                     if i.strip()
                     ]
            c += 1
            tkn = tokens[c]
            if tkn.tknType is TokenType.LineBreak:
                c += 1

            else:
                raise Exception
        elif tkn.tknType is TokenType.LineBreak:
            c += 1
        else:
            raise Exception
    else:
        return False
    return cargs, c


def parse_let(tokens: List[Token]):
    cell = []
    c = 0
    tkn = tokens[c]
    if tkn.tknType is TokenType.LetSSKeyword:
        c += 1
        tkn = tokens[c]
        t = parse_subsub(tokens[c:])
        if t:
            c += t[1]
            for i in t[0]:
                kvpair = i.split("=")
                if len(kvpair) != 2:
                    raise Exception
                else:
                    cell.append(kvpair)
            tkn = tokens[c]
        if tkn.tknType is TokenType.LineBreak:
            c += 1
        else:
            raise Exception

    else:
        return False
    return cell, c


def parse_expressCell(tokens: List[Token]) -> [Tuple[List[Token], int], bool]:
    cell = ""
    c = 0
    tkn = tokens[c]
    if tkn.tknType is TokenType.ExpressionLetter:
        cell += tkn.value
        c += 1
    elif tkn.tknType is TokenType.Opener:
        c += 1
        tkn = tokens[c]
        while True:
            if tkn.tknType is TokenType.ExpressionLetter:
                cell += tkn.value
                c += 1
                tkn = tokens[c]
            elif tkn.tknType is TokenType.LineBreak:
                cell += tkn.value
                c += 1
                tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                break
            else:
                if tkn.tknType in [TokenType.L3Sep, TokenType.L2Sep, TokenType.L1Sep]:
                    return False
                else:
                    raise Exception
    else:
        return False
    return cell, c


def parse_subsub(tokens: List[Token]):
    """

    :param tokens:
    :return:
    """
    cell = []
    c = 0
    backward = False  # for preventing continuous 'expressCell'
    t = parse_expressCell(tokens[c:])
    if t or tokens[c].tknType is TokenType.L3Sep:
        if t:
            c += t[1]
            cell.append(t[0])
        elif tokens[c].tknType is TokenType.L3Sep:
            c += 1

        while True:
            t = parse_expressCell(tokens[c:])
            if tokens[c].tknType is TokenType.L3Sep:
                c += 1
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                cell.append(t[0])
            else:
                break
            backward = False


    elif tokens[c].tknType is TokenType.Opener:
        text = ""
        c += 1
        tkn = tokens[c]
        while True:
            t = parse_expressCell(tokens[c:])
            if tkn.tknType is TokenType.L3Sep:
                c += 1
                if text.strip():
                    cell.append(text)
                    text = ""
                tkn = tokens[c]
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                text += t[0]
                tkn = tokens[c]
                backward = True
                continue
            elif tkn.tknType is TokenType.LineBreak:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    text += tkn.value
                    tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text.strip():
                    cell.append(text)
                    text = ""
                tkn = tokens[c]
                break
            else:
                if tkn.tknType in [TokenType.L2Sep, TokenType.L1Sep]:
                    return False
                else:
                    raise Exception
            backward = False
    else:
        return False

    return cell, c


def parse_sub(tokens: List[Token]):
    """
    333|333
    :param tokens:
    :return:
    """
    cell = []
    c = 0
    backward = False  # subsub의 중복 방지용

    t = parse_subsub(tokens[c:])
    if t or tokens[c].tknType is TokenType.L2Sep:
        if t:
            c += t[1]
            cell.append(t[0])
        elif tokens[c].tknType is TokenType.L2Sep:
            c += 1

        while True:
            t = parse_subsub(tokens[c:])
            if tokens[c].tknType is TokenType.L2Sep:
                c += 1
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                cell.append(t[0])
                backward = True
                continue
            else:
                break
            backward = False

    elif tokens[c].tknType is TokenType.Opener:
        text = []
        c += 1
        tkn = tokens[c]
        while True:
            t = parse_subsub(tokens[c:])
            if tkn.tknType is TokenType.L2Sep:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                tkn = tokens[c]
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                text.extend(t[0])
                tkn = tokens[c]
                backward = True
                continue
            elif tkn.tknType is TokenType.LineBreak:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    # text += tkn.value
                    tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                tkn = tokens[c]
                break
            else:
                if tkn.tknType in [TokenType.L1Sep]:
                    return False
                else:
                    raise Exception
            backward = False
    else:
        return False

    return cell, c


def parse_element(tokens: List[Token]):
    """
    333|333
    :param tokens:
    :return:
    """
    cell = []
    c = 0

    backward = False  # for preventing continuous 'sub'
    t = parse_sub(tokens[c:])
    if t or tokens[c].tknType is TokenType.L1Sep:
        if t:
            c += t[1]
            cell.append(t[0])
        elif tokens[c].tknType is TokenType.L1Sep:
            cell.append([['']])  # Because L1Sep is so Big Impact on this anw
            c += 1

        while True:
            t = parse_sub(tokens[c:])
            if tokens[c].tknType is TokenType.L1Sep:
                c += 1
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                cell.append(t[0])
                backward = True
                continue
            else:
                break
            backward = False
        if tokens[c].tknType is TokenType.LineBreak:
            c += 1
            pass
        else:
            raise Exception

    elif tokens[c].tknType is TokenType.Opener:
        text = []
        c += 1
        tkn = tokens[c]
        while True:
            t = parse_sub(tokens[c:])
            if tkn.tknType is TokenType.L1Sep:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                else:
                    cell.append([['']])  # only in element
                tkn = tokens[c]
            elif t:
                if backward:
                    raise Exception
                c += t[1]
                text.extend(t[0])
                tkn = tokens[c]
                backward = True
                continue
            elif tkn.tknType is TokenType.LineBreak:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    # text += tkn.value
                    tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                else:
                    cell.append([['']])
                tkn = tokens[c]
                break
            else:
                raise Exception  # meeting strange token in bracket is incorrect
            backward = False

        if tkn.tknType is TokenType.LineBreak:
            c += 1
            pass
        else:
            raise Exception

    else:
        return False

    return cell, c


def parse_stage(tokens: List[Token]):
    """
    parse stage
    :param tokens:
    :return:
    """
    stageName = ""
    cell = []
    c = 0
    tkn = tokens[c]
    if tkn.tknType is TokenType.StageSSKeyword:
        c += 1
        tkn = tokens[c]
    else:
        return False

    if tkn.tknType is TokenType.ExpressionLetter:
        stageName = tkn.value
        c += 1
        tkn = tokens[c]
    else:
        raise Exception("NO HEADER OF STAGE")

    while True:
        t = parse_element(tokens[c:])
        if tkn.tknType is TokenType.LineBreak:
            try:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    tkn = tokens[c]
            except IndexError:
                break
        elif t:
            c += t[1]
            cell.append(t[0])
            try:
                tkn = tokens[c]
            except IndexError:
                break

        else:
            t1 = parse_command(tokens[c:])
            t2 = parse_let(tokens[c:])
            if t1:
                # dispatch
                c += t1[1]
                tkn = tokens[c]
                pass
            elif t2:
                # dispatch
                c += t2[1]
                tkn = tokens[c]
                pass
            else:
                break



    return {stageName: cell}, c


def parse_complete(tokens: List[Token]):
    pass


# valid check & modify


if __name__ == '__main__':
    import pprint


    def test(ts):
        try:
            test_tokens = tokenize(ts)
            print(test_tokens)
            print(parse_let(test_tokens))
            print("Conje" + "=" * 25)
        except Exception as e:
            print(e)
            print("False" + "=" * 25)


    test_sources = ["##$str=aaa;{u=d}"]

    test(test_sources[0])
    # test(test_sources[1])
