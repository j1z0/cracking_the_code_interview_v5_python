
class StringBuffer(object):

    def __init__(self):
        self.strings = []

    def append(self, val):
        self.strings.append(val)

    def toString(self):
        return "".join(self.strings)

    def __str__(self):
        return self.toString()


if __name__ == "__main__":
    sb = StringBuffer()
    sb.append("some")
    sb.append("young")
    sb.append("guy")
    print(sb)
