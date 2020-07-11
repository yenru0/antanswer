"""
antanswer에 대한 EBNF



Filter ::= <표현셀>

StageSSKeyword ::= '##@'
LineBreak ::= '\n'

<L3구분자> ::= ';'
<L2구분자> ::= '|'
<L1구분자> ::= ':'

<표현문자> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | ' '
<Inline표현셀> ::= 표현문자*
<표현셀> ::= <표현문자>* | '{' <표현문자>*{<표현문자>* LineBreak} '}'

<SubSub> ::= <표현셀>{<L3구분자><표현셀>}[<L3구분자>] | '{' LineBreak* <표현셀>{<L3구분자><표현셀>}[<L3구분자>] LineBreak* '}'
<Sub> ::= <SubSub>{<L2구분자><SubSub>}[<L2구분자>] | '{' LineBreak* <SubSub>{<L2구분자><SubSub>}[<L2구분자>] LineBreak* '}'
<Element> ::= <Sub>{<L1구분자><Sub>}[<L1구분자>] | '{' LineBreak* <Sub>{<L1구분자><Sub>}[<L1구분자>] LineBreak* '}'
<Stage> ::= <StageSSKeyword><표현문자><LineBreak>{<Element><LineBreak>}





"""