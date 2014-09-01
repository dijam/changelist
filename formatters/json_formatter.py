import json


class JsonFormatter(object):

    def format(self, files):
        return json.dumps(files)
