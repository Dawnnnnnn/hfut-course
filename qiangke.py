import requests
import time
import hashlib
import json


# 这是课程代码,你只需要修改这里
lessonAssoc = [246862, 246865]


username = input("快输入你的学号:")
password = input("再输入你的密码我就能盗号了:")


# 这是一个非固定值，看起来像是选课轮次，或许明年一轮直接用163就能必中课程了吧
courseSelectTurnAssoc = '163'
# 这也是一个固定值，看起来像照搬的别的系统，没有删干净
virtualCost = '0'


def Add_course(username,password):
    salt_url = 'http://jxglstu.hfut.edu.cn/eams5-student/login-salt'
    s = requests.Session()
    response = s.get(salt_url)
    while response.status_code == 404:
        s = requests.Session()
        response = s.get(salt_url)
    temp = response.text
    password = temp + "-" +password
    hash = hashlib.sha1()
    hash.update(password.encode('utf-8'))
    password = hash.hexdigest()
    data = {'username': username, 'password': password, 'captcha': ''}
    data = json.dumps(data, separators=(',', ':')).encode(encoding='utf-8')
    header = {'Content-Type': 'application/json'}
    login_url = "http://jxglstu.hfut.edu.cn/eams5-student/login"
    s.post(login_url,data=data,headers=header)
    url = 'http://jxglstu.hfut.edu.cn/eams5-student/ws/for-std/course-select/add-request'
    url1 = 'http://jxglstu.hfut.edu.cn/eams5-student/ws/for-std/course-select/add-drop-response'
    url2 = 'http://jxglstu.hfut.edu.cn/eams5-student/ws/for-std/course-select/std-count'
    s.get('http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-select')
    info_url = 'http://jxglstu.hfut.edu.cn/eams5-student/for-std/student-info'
    res = s.get(info_url)
    id = res.url[-5:]
    for i in lessonAssoc:
        while 1:
            data = {'studentAssoc': id, 'lessonAssoc': i,
                'courseSelectTurnAssoc': courseSelectTurnAssoc, 'scheduleGroupAssoc': '', 'virtualCost': virtualCost}
            response = s.post(url, data=data)
            temp = response.text
            data1 = {'studentId': id, 'requestId': temp}
            response1 = s.post(url1, data=data1)
            data2 = {'lessonIds[]':i}
            response2 = s.post(url2,data=data2)
            print("选课状态:",response1.json())
            temp = response2.json()
            value = list(temp.values())
            print("当前课程选课人数:",value)
            time.sleep(0.5)


Add_course(username,password)


