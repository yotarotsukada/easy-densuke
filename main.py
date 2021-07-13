# coding: utf-8

from flask import Flask, render_template, request
import datetime as d
import jpholiday

app = Flask(__name__)

@app.route('/')
def generate():
    today = d.date.today()
    start = today.isoformat()
    end = (today + d.timedelta(days=7)).isoformat()
    return render_template('generate.html', title='日程登録 - 伝助時短プログラム', start_value=start, end_value=end)

@app.route('/help')
def view_help():
    return render_template('help.html', title='ヘルプ - 伝助時短プログラム')

@app.route('/contact', methods = ['GET', 'POST'])
def view_contact():
    return render_template('contact.html', title='お問い合わせ - 伝助時短プログラム')

@app.route('/result', methods = ['GET', 'POST'])
def make_list():
    if request.method == 'GET':
        return generate()
    
    start = request.form['start']
    end = request.form['end']
    dt_start = d.date.fromisoformat(start)
    dt_end = d.date.fromisoformat(end)
    num = (dt_end - dt_start).days + 1
    
    list_weekday = request.form['weekday'].strip().split('\r\n')
    list_weekend = request.form['weekend'].strip().split('\r\n')
    list_weekday = [s for s in list_weekday if s != ''] #空の要素を除く
    list_weekend = [s for s in list_weekend if s != ''] #空の要素を除く
    len_wd = len(list_weekday)
    len_we = len(list_weekend)
    if len_wd == 0: #候補時間帯がなかった場合の処理
        list_weekday.append('')
        len_wd = 1
    if len_we == 0: #候補時間帯がなかった場合の処理
        list_weekend.append('')
        len_we = 1
    
    result = []
    dt_date = dt_start
    dic_day = {
        0: "月",
        1: "火",
        2: "水",
        3: "木",
        4: "金",
        5: "土",
        6: "日"
        }
    
    for i in range(num):
        date = str(dt_date.month) + '/' + str(dt_date.day) #日付取得(str)
        daynum = dt_date.weekday() #曜日番号取得(int)
        day = dic_day[daynum] #曜日番号取得(str)
        is_hol = jpholiday.is_holiday(dt_date)
        if is_hol: #祝日なら
            for i in range(len_we):
                result.append(date + '(' + day + '・祝)' + list_weekend[i])
        elif daynum >= 5: #土日なら
            for i in range(len_we):
                result.append(date + '(' + day + ')' + list_weekend[i])
        else: #平日なら
            for i in range(len_wd):
                result.append(date + '(' + day + ')' + list_weekday[i])
        dt_date += d.timedelta(days=1) #最後にdt_dateを1日後にする
    
    return render_template('result.html', title='実行結果 - 伝助時短プログラム', result=result, num=num)


if __name__ == '__main__':
    app.run(debug=True)