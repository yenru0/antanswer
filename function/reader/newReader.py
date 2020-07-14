import re
import json
from enum import Enum, auto
from typing import List, Tuple

PATTERN_IS_LETTER = re.compile(r"[a-z]")

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
    def __init__(self, tknType, value):
        self.tknType = tknType
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.tknType in [TokenType.ExpressionLetter, TokenType.Letter]:
            return "{}({})".format(self.tknType.name, self.value)
        else:
            return "{}".format(self.tknType.name)


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


def parse_expressCell(tokens: List[Token]) -> Tuple[List[Token], int]:
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
                return False
    else:
        return False
    return cell, c


def parse_subsub(tokens: List[Token]):
    cell = []
    c = 0

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
                c += t[1]
                cell.append(t[0])
            else:
                break

    elif tokens[c].tknType is TokenType.Opener:
        text = ""
        c += 1
        tkn = tokens[c]
        while tkn.tknType is TokenType.LineBreak:
            c += 1
            text += tkn.value
            tkn = tokens[c]
        t = parse_expressCell(tokens[c:])
        if t:
            c += t[1]
            text += t[0]
            tkn = tokens[c]

        if tkn.tknType is TokenType.L3Sep:
            c += 1
            if text.strip():
                cell.append(text)
                text = ""
            tkn = tokens[c]

        while tkn.tknType is TokenType.LineBreak:
            c += 1
            text += tkn.value
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
                c += t[1]
                text += t[0]
                tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text.strip():
                    cell.append(text)
                    text = ""
                tkn = tokens[c]
                break
            else:
                return False

            while tkn.tknType is TokenType.LineBreak:
                c += 1
                text += tkn.value
                tkn = tokens[c]
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
                c += t[1]
                cell.append(t[0])
            else:
                break

    elif tokens[c].tknType is TokenType.Opener:
        text = []
        c += 1
        tkn = tokens[c]
        while tkn.tknType is TokenType.LineBreak:
            c += 1
            #text += tkn.value
            tkn = tokens[c]
        t = parse_subsub(tokens[c:])
        if t:
            c += t[1]
            text.extend(t[0])
            tkn = tokens[c]

        if tkn.tknType is TokenType.L2Sep:
            c += 1
            if text:
                cell.append(text)
                text = []
            tkn = tokens[c]

        while tkn.tknType is TokenType.LineBreak:
            c += 1
            #text += tkn.value
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
                c += t[1]
                text.extend(t[0])
                tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                tkn = tokens[c]
                break
            else:
                return False

            while tkn.tknType is TokenType.LineBreak:
                c += 1
                tkn = tokens[c]
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

    t = parse_sub(tokens[c:])
    if t or tokens[c].tknType is TokenType.L1Sep:
        if t:
            c += t[1]
            cell.append(t[0])
        elif tokens[c].tknType is TokenType.L1Sep:
            c += 1

        while True:
            t = parse_sub(tokens[c:])
            if tokens[c].tknType is TokenType.L1Sep:
                c += 1
            elif t:
                c += t[1]
                cell.append(t[0])
            else:
                break

    elif tokens[c].tknType is TokenType.Opener:
        text = []
        c += 1
        tkn = tokens[c]
        while tkn.tknType is TokenType.LineBreak:
            c += 1
            tkn = tokens[c]
        t = parse_sub(tokens[c:])
        if t:
            c += t[1]
            text.extend(t[0])
            tkn = tokens[c]

        if tkn.tknType is TokenType.L1Sep:
            c += 1
            if text:
                cell.append(text)
                text = []
            tkn = tokens[c]

        while tkn.tknType is TokenType.LineBreak:
            c += 1
            #text += tkn.value
            tkn = tokens[c]
        while True:
            t = parse_sub(tokens[c:])
            if tkn.tknType is TokenType.L1Sep:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                tkn = tokens[c]
            elif t:
                c += t[1]
                text.extend(t[0])
                tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                if text:
                    cell.append(text)
                    text = []
                tkn = tokens[c]
                break
            else:
                return False

            while tkn.tknType is TokenType.LineBreak:
                c += 1
                tkn = tokens[c]

    else:
        return False

    return cell, c


def parse_stage(tokens: List[Token]):
    """

    :param tokens:
    :return:
    """
    cell = []
    c = 0
    tkn = tokens[c]
    if tkn.tknType is TokenType.StageSSKeyword:
        c += 1
        tkn = tokens[c]
    else:
        return False

    if tkn.tknType is TokenType.ExpressionLetter:
        c += 1
        tkn = tokens[c]
    else:
        return False

    while tkn.tknType is TokenType.LineBreak:
        c += 1
        tkn = tokens[c]

    t = parse_element(tokens[c:])
    if t:

        while True:
            t = parse_element(tokens[c:])
            if t:
                c += t[1]
                cell.append(t[0])
                tkn = tokens[c]
            else:
                break
            try:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    tkn = tokens[c]
            except IndexError:
                break



    elif tokens[c].tknType is TokenType.Opener:
        c += 1
        tkn = tokens[c]

        while True:

            t = parse_element(tokens[c:])
            if t:
                c += t[1]
                cell.append(t[0])
                tkn = tokens[c]
            elif tkn.tknType is TokenType.Closer:
                c += 1
                tkn = tokens[c]
                break
            else:
                return False
            try:
                while tkn.tknType is TokenType.LineBreak:
                    c += 1
                    tkn = tokens[c]
            except IndexError:
                break

    else:
        return False

    return cell, c


if __name__ == '__main__':
    import pprint
    """
    ##@ stage
    {{333}:{333}}
    ->
    ---tokenized
    <StageSSKeyword> <ExpressionLetter>*5 <LineBreak>
    <Opener> <Opener> <EL> <Closer> <L1Sep> <Opener> <EL> <Closer> <Closer>
    ---parsed
    [[[[333],],], [[]]]
    """
    src = \
"""a:q:demd"""
    src1 =\
"""##@stage{
a:b:element
a;b:q:demostrork
}







"""

    print(tokenize(src1))
    # print(parse_expressCell(tokenize(src)))

    pprint.pprint(parse_stage(tokenize(src1)), indent=2, width=5)
    # print(tokenize("{}}"))
