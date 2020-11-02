import json

from driver import Driver
from programmers import Programmers


def config_parsing(cfg_path: str):
    cfg = json.loads(open(cfg_path, "r").read())
    cfg["language"] = cfg["language"].split(",")
    cfg["select"] = list(map(int, cfg["select"].split(",")))
    return cfg


class App:
    config = {"language": ["python", "cpp", "java"], "select": [1, 1, 0]}

    def __init__(self, cfg_path: str):
        self.cfg = self._get_config(cfg_path)
        self.problems = self._get_problems()

        self.driver = Driver()
        self.programmers = Programmers(self.driver, self.cfg)

    def _get_config(self, cfg_path: str):
        try:
            cfg = config_parsing(cfg_path)
        except FileNotFoundError:
            print("Config File Not Found.. Use Default Config")
            cfg = self.config
        return cfg

    def _get_problems(self):
        try:
            problems = [
                line.strip("\n") for line in open(self.cfg["problem_path"], "r")
            ]
        except FileNotFoundError:
            print("problem File Not Found.. Write problem number in problem")
            exit(-1)
        return problems

    def parsing(self):
        self.programmers.parsing(self.problems)


if __name__ == "__main__":
    app = App("./config.json")
    # app.parsing()
