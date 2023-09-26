import requests
import os
import json
import datetime

start_time = datetime.datetime.now()
Work_path = os.getcwd()
ID = input('请输入画师ID：')
o_path = input('请输入保存路径：')
if not os.path.exists(o_path):
    print('路径不存在，正在创建...', end='')
    os.mkdir(o_path)
    print('完成')
os.chdir(o_path)

#       Init

print('正在初始化，请等待片刻... \n')

headers = {
    'cookie': 'first_visit_datetime_pc=2023-08-05+12%3A50%3A06; p_ab_id=1; p_ab_id_2=4; p_ab_d_id=62976449; yuid_b=UTeIAhA; __utmz=235335808.1691207414.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1691207418857.1491705339; __utmc=235335808; PHPSESSID=49343042_j0WRJL8M6Ta1RyZpcsMRCkyqWcQ2XxWH; device_token=40fda467a69354363f4e35f69dac6c46; c_type=26; privacy_policy_notification=0; a_type=0; b_type=1; _ga_MZ1NL4PHH0=GS1.1.1692679042.1.1.1692679123.0.0.0; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=male=1^6=user_id=49343042=1^9=p_ab_id=1=1^10=p_ab_id_2=4=1^11=lang=zh=1; privacy_policy_agreement=6; _gid=GA1.2.1859355025.1692679138; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __utma=235335808.436314191.1691207414.1692678957.1692683690.3; cf_clearance=wkga56cprxfwxk.9y1FY74CWhSy7M0jfFUhk2rYKGms-1692688058-0-1-fc1bb2d3.3d986202.ab1aed33-0.2.1692688058; _ga_75BBYNYN9J=GS1.1.1692683692.4.1.1692688207.0.0.0; _ga=GA1.2.459216914.1691207414; __cf_bm=5tHeTrfzhtYkxQ4syxobBuY0_BB85l5lsX9IoAEhDCA-1692690427-0-AWMFJfr/ZcBRgFXHXWs0ovqo4jfAwJ8E22e4nUJ/tiLxaCXjlFFiMjv8+OJt3Cdj0l/iu72GqDZ50dEnBcowZQMNJjvDpKNfGpWWN7m1Wes5',
    # 这是默认账号，你也可以用你的cookie
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'referer': 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/top'
}
headers2 = headers
headers2['referer'] = 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/top?lang=zh'
if os.path.exists(o_path + 'ids.txt'):
    os.remove(o_path + 'ids.txt')
else:
    pass
URL_1 = 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/all'
os.system('node ' + Work_path + '\\wood_man.js ' + URL_1 + ' > ids.txt')
URL_2 = 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/top'
In = open('ids.txt', 'r')
strr = In.read()
In.close()
JSON = json.loads(strr)
# print(JSON)
name = JSON['body']['illusts']


#       Beginning


def Geturl(_id):
    return 'https://www.pixiv.net/ajax/illust/' + str(_id) + '/pages?lang=zh'


def download(pid, file_path):
    if os.path.exists(file_path):
        pass
    else:
        os.mkdir(file_path)
    os.chdir(file_path)
    file_path = file_path + '\\' + str(pid)
    print('1')
    if os.path.exists(file_path):
        print('作品 {} 早就下好了'.format(pid))
    else:
        urlsum = Geturl(pid)
        hhd = headers
        hhd['referer'] = str(urlsum)
        count = requests.get(urlsum, headers=hhd)
        JSON = json.loads(count.content)['body']
        print(urlsum, '\n', count.content, '\n', len(JSON))
        cnt = 0
        for no_use in JSON:
            img_url = no_use['urls']['original']
            filepath = '{}{}'.format(file_path, img_url[-7:])
            print('原图地址：', img_url, '\n下载中......', end='')
            hhd = headers
            hhd['referer'] = img_url
            with open(filepath, 'wb') as f:
                f.write(requests.get(img_url, headers=hhd).content)
                print('完成!')
            ++cnt


file_path = o_path
i = q = 0
JSON = requests.get(URL_2, headers=headers).json()
print('该画师一共有', len(name), '个插画, 开始下载 \n')
print(JSON)
#       Definition

Name = str(ID)
for q in name:
    try:
        userName = JSON['body']['illusts'][str(q)]['userName']
        Name = userName
        break
    except:
        pass
for q in name:
    id_1 = str(q)
    try:
        title = JSON['body']['illusts'][id_1]['title']
        userName = JSON['body']['illusts'][id_1]['userName']
        information = '作品名称：' + title, '作品ID：' + \
            str(id_1), '作者姓名和ID：' + userName, str(ID)
        print(information)
        print('当前第', i + 1, '个, ')
    except KeyError:
        print('当前第', i + 1, '个，省略详细信息，')
    file_path = '{}\\{}'.format(o_path, Name)
    if os.path.exists(o_path + '\\' + Name):
        pass
    else:
        os.mkdir(file_path)
    os.chdir(file_path)
    filepath = '{}\\{}\\{}'.format(o_path, Name, q)
    download(q, filepath)
    i += 1

end_time = datetime.datetime.now()
print('用时：{}'.format(end_time - start_time))
os.system('pause')

#       Working
