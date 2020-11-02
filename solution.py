class Solution:
    def __init__(self):
        self.content = None

    def parsing(self, content):
        self.content = content
        self.content = "\n".join(
            filter(lambda x: not x.strip().isdecimal(), content.split("\n"))
        )

    def write(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.content)
