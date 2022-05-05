from io import StringIO


class Logger:

    def __init__(self):
        self.builder = StringIO()

    def log(self, string: str):
        self.builder.write(str(string) + "\n")
        return string

    def __str__(self):
        return self.builder.getvalue()


logger = Logger()
log = logger.log
