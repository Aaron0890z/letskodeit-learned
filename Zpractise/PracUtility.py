import traceback
import time
import string, random


class Util():

    def sleep(self, sec, info=""):
        if info is not None:
            print("Wait :: '" + str(sec) + "' seconds for the " + info)
            try:
                time.sleep(sec)
            except InterruptedError:
                traceback.print_stack()

    def getAlphanumeric(self, lenght, type="letters"):
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        elif type == "digits":
            case = string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(lenght))

    def getUniqueName(self, charCount=10):
        return self.getAlphanumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        print(nameList)

    def verifyTextContains(self, actualtext, expectedtext):
        print("Actual text is " + actualtext)
        print("Expected text is " + expectedtext)
        if actualtext.lower() in expectedtext.lower():
            print(" Verification contains")
            return True
        else:
            print("Verification failed")
            return False

    def verifyTextMatch(self, actualtext, expectedtext):
        print("Actual text is " + actualtext)
        print("Expected text is " + expectedtext)
        if actualtext.lower() == expectedtext.lower:
            print(" Verification contains")
            return True
        else:
            print("Verification failed")
            return False

    def verifyListMatch(self, expectedList, actualList):
        a = set(expectedList)
        print(a)
        b = set(expectedList) == set(actualList)
        print(b)

    def verifyListContains(self, expectedList, actualList):

        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                print(False)
        else:
            print(True)


u = Util()
u.verifyListContains([1, 2, 0, 4, 5], [1, 2, 3, 4, 5])
u.verifyListMatch([1, 2, 3, 4, 5], [7, 6, 5, 4, 3])
u.verifyTextMatch("remo", "rome")
u.verifyTextContains("terry", "terry")
u.getUniqueNameList(4, [2, 3, 6, 5])
u.getUniqueName(5)
# u.getAlphanumeric(7, "mix")
u.sleep(4, "you have to")
