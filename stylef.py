import time


def marquee(showMsg, length, splitLen = 30):
    for i in range(len(length) + 1):
        print(showMsg[i: i + splitLen], end = '  \r')
        time.sleep(0.08)


class Marquee():
    class Alert():
        def __init__(self, chinese, english):
            self.chinese = chinese
            self.english = english
            self.spaceRepeat = ' ' * (30 - len(self.chinese))

        def rest(self, showMsg):
            marquee(' ' * 30 + showMsg, ' ' * 30 + showMsg)

        def classicStyle(self, style):
            print(" " * 12 + "下一站", end = '\r')
            time.sleep(1.5)
            if style == "custom":
                print("\r" + self.chinese + self.spaceRepeat, end = '\r')
                time.sleep(1.5)
                setMsg = self.chinese + self.spaceRepeat + self.english + self.spaceRepeat
            elif style == "classic":
                setMsg = " " * 12 + "下一站" + ' ' * 16 + self.chinese + ' ' * 12 + self.english + self.spaceRepeat
            showMsg = setMsg + self.chinese
            marquee(showMsg, setMsg)
            time.sleep(1.5)
            marquee(self.chinese, self.chinese)

        def rollStyle(self, split = 100):
            self.rest(f"下一站: {self.chinese} Next: {self.english[:split]}")

        def verticalStyle(self):
            print(" " * 12 + "下一站", end = '\r')
            time.sleep(1.5)
            if len(self.chinese) < 10:
                print("\r" + self.chinese + self.spaceRepeat, end = '\r')
                time.sleep(1.5)
                if len(self.english) < 10:
                    print("\r" + self.english + self.spaceRepeat, end = '\r')
                else:
                    self.rest(self.english)
                time.sleep(1.5)
                print("\r" + self.chinese + self.spaceRepeat, end = '\r')
            else:
                time.sleep(1.5)
                self.rest(self.chinese)
                self.rest(self.english)
                self.rest(self.chinese)

        def stayStyle(self, style):
            stayStr = f"下一站: {self.chinese} Next: {self.english}"
            if style == "before":
                stayStr = f"{' ' * 30}下一站: {self.chinese} Next: {self.english}"
                marquee(stayStr, stayStr[:len(stayStr) - 30])
            elif style == "after":
                print("\r" + stayStr[:30], end = '\r')
                time.sleep(1.5)
                marquee(stayStr, stayStr)

    class Is_rest():
        def __init__(self, routeNum, get_operators, get_headsign):
            self.routeNum = routeNum
            self.get_operators = get_operators
            self.get_headsign = get_headsign

        def verticalStyle(self):
            setMsg = f"{' ' * 30}歡迎搭乘台中市公車"
            marquee(setMsg, setMsg)

        def classicStyle(self, style):
            if style == "classic":
                setMsg = f"{' ' * 30}歡迎搭乘台中市公車"
                marquee(setMsg, setMsg)
                print(' '*13 + time.strftime("%H:%M", time.localtime()), end = '\r')
            elif style == "custom":
                setMsg = f"{' ' * 30}歡迎搭乘 {self.get_operators} {self.routeNum} 路線 {self.get_headsign} " + \
                         time.strftime("%H:%M:%S", time.localtime())
                marquee(setMsg, setMsg)

        def rollStyle(self, split):
            setMsg = f"{' ' * 30}歡迎搭乘  {self.get_operators}  {self.routeNum}  路線  " + \
                     time.strftime("%H:%M:%S", time.localtime())
            marquee(setMsg, setMsg)

        def stayStyle(self, style):
            stayStr = f"歡迎搭乘{self.get_operators}，{self.routeNum} 路線，經{self.get_headsign}"
            if style == "before":
                stayStr = " "*30 + stayStr
                marquee(stayStr, stayStr[:len(stayStr) - 19])
            elif style == "after":
                print("\r" + stayStr[:19], end = '\r')
                time.sleep(1.5)
                marquee(stayStr, stayStr, 19)