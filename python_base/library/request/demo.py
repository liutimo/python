import requests
import time, re


#?pageSize=90&beginTime=2018-03-01&endTime=&pageNo=10&_=1583074641302
if __name__ == '__main__':
    url = 'http://reportapi.eastmoney.com/report/list'
    # 构建URL参数
    
    # 固定参数
    fixed_params = { 
        'cb' : 'datatable7508781',
        'industryCode' : '*',
        'industry' : '*',
        'rating' : '*', 
        'ratingChange' : '*', 
        'qType' : '1',
        }

    begin_time = '2018-03-01'
    end_time = '2020-03-01'
    page_size = 50
    page_no = 1
    current_timestamp = int(time.time())

    unfixed_params = {
        'beginTime' : begin_time,
        'endTime' : end_time,
        'pageSize' : page_size,
        'pageNo' : page_no,
        '_' : current_timestamp,
    }


    payload = dict(fixed_params, **unfixed_params);

    r = requests.get(url, params=payload)

    print(r.url)
    print(r.status_code)
    print(r.encoding)
    text = r.text
    #返回一个list
    print(re.findall(r'datatable\d*\((.*)\)', text)[0])

    #解析json
    """
    {
		"title": "非银金融行业周报：新证券法落地开启资本市场新篇章，积极关注券商板块",
		"orgCode": "80000031",
		"orgName": "东吴证券股份有限公司",
		"orgSName": "东吴证券",
		"publishDate": "2020-03-01 00:00:00",
		"infoCode": "AP202003011375670959",
		"industryCode": "738",
		"industryName": "多元金融",
		"author": ["11000210450.胡翔", "11000284032.朱洁羽"],
		"indvIsNew": "",
		"researcher": "胡翔,朱洁羽",
		"attachType": "0",
		"attachSize": 1127,
		"attachPages": 12,
		"encodeUrl": "z9yDxjkOZ7oWPJ8dhFQAvvmkhcLHJaT2kAs18COc6js="
	}
    """

class IndustryReport:
    def __init__(self):
        self.title = ''
        self.org_name = ''
        self.pub_date = ''
        self.author = []
        self.encode_url = ''

    

    
