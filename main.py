from Header import Bus
from stylef import Marquee
import os, time, json

def selectStyle(marquee, styleNum):
    if styleNum == 1: marquee.verticalStyle()
    if styleNum == 4: marquee.classicStyle("classic")
    if styleNum == 5: marquee.rollStyle()
    if styleNum == 6: marquee.classicStyle("custom")
    if styleNum == 8: marquee.stayStyle("before")
    if styleNum == 9: marquee.stayStyle("after")
    if styleNum == 10: marquee.rollStyle(25)


def main():
    with open('setting.json', encoding='utf-8') as f:
        data_file = json.load(f)
    routeNum = input("請輸入路線名稱: ")
    bus = Bus(data_file['AppID'], data_file['AppKey'], routeNum)
    bus.url_req(f"https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung/{routeNum}?&$format=JSON")
    get_operators = bus.busDict(['RouteName', 'Zh_tw'], ['Operators', 0, 'OperatorName', 'Zh_tw'])[routeNum]
    get_headsign = bus.busDict(['RouteName', 'Zh_tw'], ['SubRoutes', 0, 'Headsign'])[routeNum]
    bus.url_req(f"https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taichung/{routeNum}?$format=JSON")
    get_plate = bus.busDict(['PlateNumb'], ['StopName', 'Zh_tw'])
    for row in get_plate:
        print(row, end=', ')
    plate = input("\n請輸入車牌: ").upper()
    print("輸入客運樣式           VerB.5.S0\n" +
          "--------------通用--------------\n\n" +
          "(1)垂直輪播 (X)垂直輪播(置中) \n\n" +
          "(X)垂直輪播(停滯)\n\n" +
          "(4)經典 (5)普通 (6)自創 \n\n" +
          "(8)前停滯 (9)後停滯 \n\n" +
          "--------------其他--------------\n\n" +
          "(10)豐原客運 (X)豐原客運(BYD)  \n\n" +
          "(X)北市公車 (X)首都北花線\n"
          )
    styleNum = int(input("輸入: "))
    os.system("cls")
    location = {0: ""}
    while 1:
        bus.url_req(f"https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taichung/{routeNum}?$&format=JSON")
        chinese = bus.busDict(['PlateNumb'], ['StopName', 'Zh_tw'])[plate]
        english = bus.busDict(['PlateNumb'], ['StopName', 'En'])[plate]
        marquee = Marquee()
        if location != chinese:
            maq = marquee.Alert(chinese, english)
            selectStyle(maq, styleNum)
        else:
            maq = marquee.Is_rest(routeNum, get_operators, get_headsign)
            selectStyle(maq, styleNum)
        location = bus.busDict(['PlateNumb'], ['StopName', 'Zh_tw'])[plate]
        time.sleep(1.5)

if __name__ == "__main__":
    main()
