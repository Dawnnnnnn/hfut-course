import requests
import time
# cookies值失效时间暂时不确定，应该在一天之内
cookies = ''
# 这是每个人的固定 studentId
studentAssoc = ''
# 这是一个固定值，暂不知道干嘛用的
courseSelectTurnAssoc = '161'
# 这也是一个固定值，暂不知道干嘛用的
virtualCost = '0'

# 这是课程代码
lessonAssoc = []

headers = {
    'Cookie': cookies,
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}


def Add_course(headers):
    url = 'http://jxglstu.hfut.edu.cn/eams5-student/ws/for-std/course-select/add-request'
    url1 = 'http://jxglstu.hfut.edu.cn/eams5-student/ws/for-std/course-select/add-drop-response'
    for i in lessonAssoc:
        data = {'studentAssoc': studentAssoc, 'lessonAssoc': i,
                'courseSelectTurnAssoc': courseSelectTurnAssoc, 'scheduleGroupAssoc': '', 'virtualCost': virtualCost}
        response = requests.post(url, data=data, headers=headers)
        temp = response.text
        data1 = {'studentId': studentAssoc, 'requestId': temp}
        response1 = requests.post(url1, data=data1, headers=headers)
        try:
            print(response1.json())
        except:
            print(response1.text)
        time.sleep(0.01)


Add_course(headers)
