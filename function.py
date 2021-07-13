import jpholiday
import datetime as d
from dateutil.relativedelta import relativedelta
from datetime import date

class TypingList:
    def __init__(self, category):
        self.list = []
        self.category = category
    def displayList(self):
        if len(self.list) == 0:
            print("現在、" + self.category + "のリストには何も入っていません。")
        else:
            print("現在の" + self.category + "のリストは以下の通りです。")
            for i, x in enumerate(self.list):
                print(str(i) + ". " + x)
                
    def deleteItem(self):
        self.displayList()
        while True:
            try:
                number = input("何番目の" + self.category + "を削除しますか？削除しない場合は'z'を入力：")
                if number == "z":
                    break
                elif int(number) < 1:
                    raise IndexError
                temp = self.list.pop(int(number) - 1)
                print(number + "番目の" + self.category + "（" + temp + "）" "を削除しました。")
                self.displayList()
                break
            except ValueError:
                print("数値で入力してください")
            except IndexError:
                print("リストに存在する数字を入力してください")
    
    def makeList(self):
        print("（終了したら'fin'を入力）")
        print("（削除するものがある場合は'del'を入力）")
        print("（現在のリストを表示する場合は'disp'を入力）")
        while True:
            item = input()
            if item == "":
                pass
            elif item == "fin":
                break
            elif item == "del" and len(self.list) == 0:
                print(self.category + "のリストに何も入っていないため削除できません。入力を続けてください。")
            elif item == "del":
                self.deleteItem()
                print(self.category + "の入力を続けてください。")
            elif item == "disp":
                self.displayList()
                print(self.category + "の入力を続けてください。")
            else:
                self.list.append(item)
        return self.list

start = input("開始日を入力してください。（例：'2021/6/28'）：")
finish = input("終了日を入力してください。（例：'2021/7/18'）：")

time_weekday = TypingList("時間帯")
time_weekend = TypingList("時間帯")
line = "の練習時間帯を1つずつ入力してください。（例：'19:00-'）"
print("\n①平日" + line)
time_weekday = time_weekday.makeList()
print("\n②土日祝" + line)
time_weekend = time_weekend.makeList()


#time1とtime2にそれぞれ入れた個数
num1 = len(time_weekday)  
num2 = len(time_weekend)  
count = 0 #祝日のカウント

week_name = {    
    0: "月"
  , 1: "火"
  , 2: "水"
  , 3: "木"
  , 4: "金"
  , 5: "土"
  , 6: "日"
}

datetime = d.datetime.strptime(start, "%Y/%m/%d")#クラスをdatetimeにする
datetime_f = d.datetime.strptime(finish, "%Y/%m/%d")#クラスをdatetimeにする

datetime = datetime - relativedelta(days=1)#1日前にする

for i in range(100): #100日間以上の場合は要変更
  datetime = datetime + relativedelta(days=1)#1日後にする
  b = week_name[datetime.weekday()]#曜日取得(str)
  c = "{0:%m/%d}".format(datetime)#日付取得(str)
  result = jpholiday.is_holiday(datetime)
  if result == True:
    for i in range(num2):      #祝日なら
      print(c + '(' + b + ')' + time_weekend[i])
    count = count + 1
  elif datetime.weekday() < 5: #平日なら
    for i in range(num1):
      print(c + '(' + b + ')' + time_weekday[i])
  else:                        #土日なら
    for i in range(num2): 
      print(c + '(' + b + ')' + time_weekend[i])
  if datetime == datetime_f:
    break

print("")
print("祝日が" + str(count) + "件検出されました")#祝日を検出した場合お知らせ
#print("メールアドレス")
#print(address)
print("伝助の新規イベント作成ページのURL")
print("https://www.densuke.biz/event")