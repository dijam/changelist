import StringIO
from colorama import init, Fore


class ConsoleFormatter(object):

    def __init__(self):
        init()

    def format(self, files):
        stream = StringIO.StringIO()

        for filename, date in files.iteritems():
            stream.write("%s%s: %s%s\n" %
                         (Fore.GREEN, filename, Fore.RESET, date))

        output = stream.getvalue()
        stream.close()

        return output
