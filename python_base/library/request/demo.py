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
    