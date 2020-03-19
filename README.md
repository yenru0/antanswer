Antanswer Python
===

[![Python 3.6 or later Required](https://img.shields.io/badge/python-3.6%20or%20higher-blue.svg)](https://python.org)

Antanswer Python는 문제 풀이를 위한 **어떤 것**입니다. 기본적으로 파이썬과 의존성 라이브러리만 설치하고 이용 방법을 숙지하시면 
충분히 쉽게 사용할 수 있습니다.

### 목차


## 시작
### 환경 구성
Antanswer Python은 그 이름대로 파이썬을 기반으로 동작합니다. 기본적으로 Python 3.6 또는 그 이상 버전에서도 동작할 것으로 예상하지만
Python 3.7까지 테스트해보았습니다.

파이썬 설치는 [이곳](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)에서 바로 다운로드 하실 수 있습니다. (Python 3.7.4)
※ 설치할 떄 `Add Python 3.7.4 to PATH` 옵션에 체크해주셔야 합니다.

또한 Antanswer Python에는 PySide2 라이브러리가 필요합니다.
lxml 라이브러리 설치는 cmd 창에다 `pip install pyside2`을 입력하시면 알아서 설치됩니다.

### 설치/실행
Antanswer Python은 높은 자유도를 가지게됩니다.

근데 그냥 쓰실 분은 다운로드 받고 `main.py`그냥 실행하시면 됩니다.
다운로드 받는 곳은 [여기](https://github.com/yenru0/antanswer/releases)입니다.

<!--             
### 실행
아 삽질;;
## 문제 만들기
### AnwOld를 사용하여 만들기 <곧 사라져야 할 것이지만 사실 많이 쓰일거 같습니다...>
#### 기본적인 문제
#### detail 변수 선언
#### 특수 명령
#### 주석
#### 예시
#### anw 파일로 변환하기

## anw 파일 구조
사실상 xml 파일인 anw 파일 구조는 간단합니다.-->

## 기본 condition

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