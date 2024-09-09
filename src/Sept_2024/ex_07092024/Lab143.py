from abc import ABC, abstractmethod


class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass


class TestCase_1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


testcase1 = TestCase_1()
testcase1.runTc()