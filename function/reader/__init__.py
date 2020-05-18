"""
"reader" is READER and TRANSLATOR python function set of 'Antanswer'

SUPPORT Formats VERSION:
    AFD: AFD 1half
    ANW: ANW 0.9a


ROLE:
    reader has 4 main function

    - 'AFD Translator' translate AFD to ANW.
        * FileObject -> Anw_String
    - 'AFD Straight Reader' read AFD and translate ADS.
        * FileObject -> ADS
    - 'AFD Error Checker' check if AFD file has no error.
        * FileObject -> Exception or True

    - 'ANW Reader' read ANW and translate ADS.
        * FileObject -> ADS

* It is Embedded in Antanswer Python 0.5

- Made by 'Yenru0'
"""
# Anw Reader for Python Bind
__version__ = "0.91"
__anw_std__ = "0.91"
__anw_compatibles__ = ["0.9"]

__anw_supports__ = {}