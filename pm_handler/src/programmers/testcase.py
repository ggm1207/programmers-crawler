"""
>>> python

solution("")...

>>> cpp

int main(void){
    solution("")...
    return 0;
}

"""


class TestCase:
    def __init__(self):
        self.testcase = list()
        self.language = None
        self.parameter_len = None
        self.text = ""

    def parsing(self, driver):
        self.parameter_len = (
            len(driver.find_elements_by_class_name("control-label")) - 1
        )
        testcase = driver.find_elements_by_css_selector(
            "#testcase-input-list > tbody > tr > td > input"
        )

        for tc in testcase:
            self.testcase.append(tc.get_attribute("value"))

        print(self.testcase)

    def select_language(self, language):
        self.language = language

    def write(self):
        pass

    def write_cpp(self):
        pass
