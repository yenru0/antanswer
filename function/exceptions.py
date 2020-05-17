class AnwMainError(Exception):
    pass


class AnwXmlParseError(AnwMainError):
    pass


class AnwMultipleStageError(AnwMainError):
    pass


class AnwNotFoundError(AnwXmlParseError):
    pass


class AnwRootNotFoundError(AnwNotFoundError):
    pass


class AnwAQNotFoundError(AnwNotFoundError):
    pass


class AnwInvalidError(AnwXmlParseError):
    pass


class AnwEModeInvalidError(AnwInvalidError):
    pass


class AnwOrderOverError(AnwXmlParseError):
    pass


if __name__ == '__main__':
    raise AnwMainError
