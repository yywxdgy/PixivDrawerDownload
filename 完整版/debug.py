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
    'cookie': '__cfduid=d577fc02e8bfc3b7a913dffa292912e521600175914; first_visit_datetime_pc=2020-09-15+22%3A18%3A35; p_ab_id=6; p_ab_id_2=2; p_ab_d_id=1548350158; yuid_b=NJkxZUA; _fbp=fb.1.1600175901889.1381699109; _ga=GA1.2.1294526804.1600175901; _gid=GA1.2.324411859.1600214533; device_token=6771f0047f0206ac76b0d887ad6f8154; a_type=0; ki_r=; limited_ads=%7B%22responsive%22%3A%22%22%7D; p_b_type=2; login_ever=yes; ki_s=210251%3A0.0.0.0.2; categorized_tags=6sZKldb07K~BU9SQkS-zU~DN6RDM1CuJ~EGefOqA6KB~IVwLyT8B6k~Mt5-5Xt_R_~NqnXOnazer~O2wfZxfonb~OEXgaiEbRa~OT-C6ubi9i~PHQDP-ccQD~RcahSSzeRf~b8b4-hqot7~sr5scJlaNv~tMaqyr0fI5~y8GNntYHsi; ki_t=1600214550602%3B1600477733055%3B1600477733055%3B5%3B54; tag_view_ranking=Lt-oEicbBr~eVxus64GZU~ahqc2_Z8SY~RTJMXD26Ak~7dr5yDiiNE~yvN_bfBdr-~afkK5n8h7Y~fLVJtGGhWk~0-sOOtqkAh~6RcLf9BQ-w~NxCKECN-a3~5uR0C2H1G-~88CzNsCQ-T~sr5scJlaNv~O2wfZxfonb~PHQDP-ccQD~02XYWZUIFd~MSNRmMUDgC~kGYw4gQ11Z~0xsDLqCEW6~A7hSoqw-5Z~ETjPkL0e6r~HY55MqmzzQ~OGMdJys38W~k3AcsamkCa~nBTsmJOROI~1HuE7w0nKg~ePN3h1AXKX~4ZJCd8OsPC~fIMPtFR8GH~RcahSSzeRf~CrFcrMFJzz~pYlUxeIoeg~K8esoIs2eW~dkvvzKpAOm~FqVQndhufZ~MHugbgF9Xo~FFz0M9z5uL~kUbnfdh8c_~TPdzb_n7qh~p1FQfxQRtJ~70wHD0F49f~eNdHeRUOQ3~OIoyEaauWk~vNapp9tuHK~2z4S7nphJy~tAvX8S-RSe~l-Y6C2rjLn~4DWYEq_Arj~CAJC_jOheS~BQFWWhxtER~jH0uD88V6F~F5CBR92p_Q~Mt5-5Xt_R_~X189mzByda~-zk8AVVQ-j~yLh4ENOaur~9PHNivVcYr~8_wOYu6BZ5~HLWLeyYOUF~lH5YZxnbfC~tMaqyr0fI5~VN7cgWyMmg~wKl4cqK7Gl~dFqfRYFNxQ~BU9SQkS-zU~hrkSAnsIgX~y8GNntYHsi~2h8ZfJVouI; __utmt=1; tags_sended=1; c_type=23; PHPSESSID=54167627_vgNLoMtwbkByNqG382ZHOSbzgfGkboVF; privacy_policy_agreement=2; b_type=0; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=54167627=1^9=p_ab_id=6=1^10=p_ab_id_2=2=1^11=lang=zh=1; __utma=235335808.1294526804.1600175901.1600497761.1600498137.19; __utmz=235335808.1600498137.19.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=235335808; __utmb=235335808.2.10.1600498137',
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
    file_path = file_path + '\\' + pid
    if os.path.exists(file_path + '_p0.png') or os.path.exists(file_path + '_p0.jpg') or os.path.exists(file_path + '\\' + str(pid) + '_p0.jpg') or os.path.exists(file_path + '\\' + str(pid) + '_p0.png'):
        print('作品 {} 早就下好了'.format(pid))
    else:
        urlsum = Geturl(pid)
        hhd = headers
        hhd['referer'] = str(urlsum)
        count = requests.get(urlsum, headers=hhd)
        JSON = json.loads(count.text)['body']
        if len(JSON) > 1:
            if os.path.exists(file_path):
                pass
            else:
                os.mkdir(file_path)
            file_path = file_path + '\\' + str(pid)
            cnt = 0
            for no_use in JSON:
                img_url = no_use['urls']['original']
                filepath = '{}{}'.format(file_path, img_url[-7:])
                print('原图地址：', img_url, '\n下载中......', end='')
                os.system('curl "' + img_url + '" >' + filepath + ' ^ -H "Upgrade-Insecure-Requests: 1" ^ -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" ^ -H "Referer: https://www.pixiv.net/" ^ --compressed')
                ++cnt
                # sleep(3)
        else:
            img_url = JSON[0]['urls']['original']
            filepath = '{}{}'.format(file_path, img_url[-7:])
            print('原图地址：', img_url, '\n下载中......', end='')
            os.system('curl "' + img_url + '" >' + filepath + ' ^ -H "Upgrade-Insecure-Requests: 1" ^ -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" ^ -H "Referer: https://www.pixiv.net/" ^ --compressed')


file_path = o_path
i = q = 0
JSON = requests.get(URL_2, headers=headers).json()
print('该画师一共有', len(name), '个插画, 开始下载 \n')

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
        title = JSON['body']['illusts'][id_1]['illustTitle']
        userName = JSON['body']['illusts'][id_1]['userName']
        information = '作品名称：' + title, '作品ID：' + \
            str(id_1), '作者姓名和ID：' + userName, str(ID)
        print(information)
        print('当前第', i + 1, '个, ')
    except KeyError:
        print('当前第', i + 1, '个，省略详细信息，')
    file_path = '{}\\{}'.format(o_path, str(ID))
    if os.path.exists(o_path + '\\' + str(ID)):
        pass
    else:
        os.mkdir(file_path)
    os.chdir(file_path)
    filepath = '{}\\{}'.format(o_path, str(ID))
    download(q, filepath)
    i += 1

end_time = datetime.datetime.now()
print('用时：{}'.format(end_time - start_time))
os.system('pause')

#       Working
