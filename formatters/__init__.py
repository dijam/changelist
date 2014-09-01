from json_formatter import JsonFormatter
from console_formatter import ConsoleFormatter

_formatters = {
    "console": ConsoleFormatter(),
    "json": JsonFormatter()
}


def Formatter(type):
    return _formatters[type]
