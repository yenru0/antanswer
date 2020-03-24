Antanswer Python
===

## 
```
##$ name=exmaple.1
##$ wil=10; recentValue=0.91
##$ {
    REVERSE_AQ=True
    COMP_IGNORE_SPACE=1
    COMP_IGNORE_CASE=yes
}

question\: what is name of this program?: antanswer
question\: what language is used in this program?: python; py3; python3; py
```

## condition(anw0.91)

```python
COND = { # string: bool
        # Anw ReaderMain
        "COMP_IGNORE_SPACE": None,  # ignoring space, blank like '\t' won't be replaced
        "COMP_IGNORE_CASE": None,  # ignoring case, replace upper to lower
        "ANSWER_WITHOUT_ORDER": None,  # when answering quest, order don't interrupt you
        "COMP_NOT": None,  # ignoring sequence matcher(compare) method
        "RESULT_DISPLAY_QUEST": None,  # not displaying Quest
        "COMP_IGNORE_LAST_PERIOD": None,  # ignoring the last period
        "RESULT_MANUAL_POST_CORRECTION": None,  # post correction at result time GUI main cond
        "REVERSE_AQ": None  # reverse AQ in element
    }
```