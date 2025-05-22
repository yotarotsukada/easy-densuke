# coding: utf-8

from flask import Flask, send_from_directory, render_template, request
import os
import datetime as d
import function
import jpholiday
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

class ScheduleForm(FlaskForm):
    pass

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'), 'favicon.ico', )

@app.route('/')
def generate():
    form = ScheduleForm()
    today = d.date.today()
    start = today.isoformat()
    end = (today + d.timedelta(days=7)).isoformat()
    return render_template('generate.html', title='日程登録 - 伝助時短プログラム', start_value=start, end_value=end, form=form)

@app.route('/help')
def view_help():
    return render_template('help.html', title='ヘルプ - 伝助時短プログラム')

@app.route('/contact', methods = ['GET', 'POST'])
def view_contact():
    return render_template('contact.html', title='お問い合わせ - 伝助時短プログラム')

@app.route('/result', methods = ['GET', 'POST'])
def get_result():
    if request.method == 'GET':
        return generate()
    
    start = request.form['start']
    end = request.form['end']
    dt_start = d.date.fromisoformat(start)
    dt_end = d.date.fromisoformat(end)
    num = (dt_end - dt_start).days + 1

    MAX_TEXTAREA_LENGTH = 2000

    raw_list_weekday = request.form['list-weekday']
    raw_list_weekend = request.form['list-weekend']

    if len(raw_list_weekday) > MAX_TEXTAREA_LENGTH:
        raw_list_weekday = raw_list_weekday[:MAX_TEXTAREA_LENGTH] # Truncate
        # TODO: Consider sending an error message back to the user instead of truncating.
    
    if len(raw_list_weekend) > MAX_TEXTAREA_LENGTH:
        raw_list_weekend = raw_list_weekend[:MAX_TEXTAREA_LENGTH] # Truncate
        # TODO: Consider sending an error message back to the user instead of truncating.

    check_data = request.form.getlist('check')
    print(check_data)
    flag_weekday = 'weekday' in check_data
    flag_weekend = 'weekend' in check_data
    list_weekday = function.make_list(flag_weekday, raw_list_weekday)
    list_weekend = function.make_list(flag_weekend, raw_list_weekend)
    len_wd = len(list_weekday)
    len_we = len(list_weekend)

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

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://unpkg.com; style-src 'self' https://unpkg.com; object-src 'none'; frame-ancestors 'none';"
    return response

if __name__ == '__main__':
    app.run(debug=False)