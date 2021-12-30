from enum import Enum


class ToolsVar(Enum):
    """ Constanta name of tools"""
    NAME = "mytools"


class TypeFileVar(Enum):
    """ Constanta type of file """
    JSON_VAR = "json"
    TEXT_VAR = "text"


class FlagVar(Enum):
    """ Constanta name of flag """
    HELP_COMMAND = "-h"
    TYPE_FILE_COMMAND = "-t"
    OUTPUT_FILE_COMMAND = "-o"

    def list():
        return list(map(lambda s: s.value, FlagVar))
