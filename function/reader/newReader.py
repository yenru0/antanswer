"""
antanswer에 대한 EBNF


<Filter> ::= <Stage>*

<StageSSKeyword> ::= "##@"
<CommandSSKeyword> ::= "##!"
<LetSSKeyword> ::= "##$"
<InlineCommentSSKeyword> "###"

<LineBreak> ::= "\n"
<L3Sep> ::= ";"
<L2Sep> ::= "|"
<L1Sep> ::= ":"

<expressLetter> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | " "
<InlineexpressCell> ::= <expressLetter>*
<expressCell> ::= <expressLetter>* | "{" <expressLetter>* { <expressLetter>* <LineBreak> } "}"

<SubSub> ::= <expressCell>{<L3Sep><expressCell>}[<L3Sep>] | "{" LineBreak* <expressCell>{<L3Sep><expressCell>}[<L3Sep>] LineBreak* "}"

<Sub> ::= <SubSub>{<L2Sep><SubSub>}[<L2Sep>] | "{" LineBreak* <SubSub>{<L2Sep><SubSub>}[<L2Sep>] LineBreak* "}"

<Element> ::= <Sub>{<L1Sep><Sub>}[<L1Sep>] LineBreak | "{" LineBreak* <Sub>{<L1Sep><Sub>}[<L1Sep>] LineBreak* "}"

<Stage> ::= <StageSSKeyword><InlineexpressCell><LineBreak>{<Element>{<LineBreak>}}
    | <StageSSKeyword><InlineexpressCell><expressLetter> "{" {<Element>{<LineBreak>}} "}" {LineBreak}






"""
