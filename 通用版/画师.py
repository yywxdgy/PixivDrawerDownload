import requests
import json
from time import sleep
import os
import datetime
from pathlib import Path

start_time = datetime.datetime.now()
print('欢迎使用Bug非常多的PixivDrawerDownload, 如发现Bug, 可以和qq：2421594879联系（虽然就几个同学用用')
print('仅供私人使用，因为我也不知道如果某人传到了网上会发生什么 \n')
sleep(1)
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
    'cookie': '__cfduid=d577fc02e8bfc3b7a913dffa292912e521600175914; first_visit_datetime_pc=2020-09-15+22%3A18%3A35; p_ab_id=6; p_ab_id_2=2; p_ab_d_id=1548350158; yuid_b=NJkxZUA; __utmz=235335808.1600175901.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1600175901889.1381699109; _ga=GA1.2.1294526804.1600175901; _gid=GA1.2.324411859.1600214533; device_token=6771f0047f0206ac76b0d887ad6f8154; a_type=0; b_type=0; ki_r=; limited_ads=%7B%22responsive%22%3A%22%22%7D; p_b_type=2; login_ever=yes; ki_s=210251%3A0.0.0.0.2; categorized_tags=6sZKldb07K~BU9SQkS-zU~DN6RDM1CuJ~EGefOqA6KB~IVwLyT8B6k~Mt5-5Xt_R_~NqnXOnazer~O2wfZxfonb~OEXgaiEbRa~OT-C6ubi9i~PHQDP-ccQD~RcahSSzeRf~b8b4-hqot7~sr5scJlaNv~tMaqyr0fI5~y8GNntYHsi; tags_sended=1; ki_t=1600214550602%3B1600477733055%3B1600477733055%3B5%3B54; __utma=235335808.1294526804.1600175901.1600480150.1600482622.15; __utmc=235335808; __utmt=1; PHPSESSID=40191193_g19mGLIdW5eRJbaz9qxwV8YV89KQTSz6; c_type=21; privacy_policy_agreement=0; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^6=user_id=40191193=1^9=p_ab_id=6=1^10=p_ab_id_2=2=1^11=lang=en=1; _gat_UA-1830249-3=1; tag_view_ranking=Lt-oEicbBr~eVxus64GZU~ahqc2_Z8SY~RTJMXD26Ak~7dr5yDiiNE~yvN_bfBdr-~afkK5n8h7Y~fLVJtGGhWk~0-sOOtqkAh~6RcLf9BQ-w~NxCKECN-a3~5uR0C2H1G-~88CzNsCQ-T~sr5scJlaNv~O2wfZxfonb~PHQDP-ccQD~02XYWZUIFd~MSNRmMUDgC~kGYw4gQ11Z~0xsDLqCEW6~A7hSoqw-5Z~ETjPkL0e6r~HY55MqmzzQ~OGMdJys38W~k3AcsamkCa~nBTsmJOROI~1HuE7w0nKg~ePN3h1AXKX~4ZJCd8OsPC~fIMPtFR8GH~RcahSSzeRf~CrFcrMFJzz~pYlUxeIoeg~K8esoIs2eW~dkvvzKpAOm~FqVQndhufZ~MHugbgF9Xo~FFz0M9z5uL~kUbnfdh8c_~TPdzb_n7qh~p1FQfxQRtJ~70wHD0F49f~eNdHeRUOQ3~OIoyEaauWk~vNapp9tuHK~2z4S7nphJy~tAvX8S-RSe~l-Y6C2rjLn~4DWYEq_Arj~CAJC_jOheS~BQFWWhxtER~jH0uD88V6F~F5CBR92p_Q~Mt5-5Xt_R_~X189mzByda~-zk8AVVQ-j~yLh4ENOaur~9PHNivVcYr~8_wOYu6BZ5~HLWLeyYOUF~lH5YZxnbfC~tMaqyr0fI5~VN7cgWyMmg~wKl4cqK7Gl~dFqfRYFNxQ~BU9SQkS-zU~hrkSAnsIgX~y8GNntYHsi~2h8ZfJVouI; __utmb=235335808.13.9.1600482650948',
    # 这是默认账号，你也可以用你的cookie
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'referer': 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/top'
}
headers2 = headers
headers2['referer'] = 'https://pixiv.net/ajax/user/' + \
    str(ID) + '/profile/top?lang=zh'
URL_1 = 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/all'
URL_2 = 'https://pixiv.net/ajax/user/' + str(ID) + '/profile/top'
JSON = requests.get(URL_1, headers=headers).json()
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
    my1 = Path(file_path + '_0.jpg')
    my2 = Path(file_path + '_0.png')
    if my1.is_file() or my2.is_file():
        print('作品 {} 早就下好了'.format(pid))
    else:
        page_url = 'https://www.pixiv.net/artworks/{}'.format(pid)
        urlsum = Geturl(pid)
        count = requests.get(urlsum, headers={'referer': str(urlsum), 'path': '/ajax/illust/' + str(pid) + '/pages?lang=zh'})
        JSON = json.loads(count.text)['body']
        cnt = 0
        for no_use in JSON:
            img_url = no_use['urls']['original']
            filepath = '{}{}'.format(file_path, img_url[-7:])
            print('原图地址：', img_url, '\n下载中......', end='')
            with open(filepath, 'wb') as f:
                f.write(requests.get(img_url, headers={
                        'referer': page_url, 'Sec-Fetch-Dest': 'image'}).content)
                print('完成!')
            ++cnt
            sleep(1)


file_path = o_path
i = q = 0
JSON = requests.get(URL_2, headers=headers).json()
print('该画师一共有', len(name), '个插画, 开始下载 \n')

#       Definition

Name = ''
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
        pass
    file_path = '{}\\{}'.format(o_path, userName)
    if os.path.exists(o_path + '\\' + userName):
        pass
    else:
        os.mkdir(file_path)
    os.chdir(file_path)
    filepath = '{}\\{}\\{}'.format(o_path, userName, q)
    download(q, filepath)
    i += 1

end_time = datetime.datetime.now()
print('用时：{}'.format(end_time - start_time))

#       Working
