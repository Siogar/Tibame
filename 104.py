import requests
import json
import pandas as pd

df = pd.DataFrame(columns = ["公司名稱", "職缺", "工作內容"])

for j in range(2,3):
    url = "https://www.104.com.tw/jobs/search/list?ro=0&jobcat=2007000000&kwop=7&keyword=%E6%99%BA%E6%85%A7%E9%86%AB%E7%99%82&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&order=15&asc=0&page=" + str(j) + "&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    headers = {
        "Referer" : "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=%E6%99%BA%E6%85%A7%E9%86%AB%E7%99%82&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&order=15&asc=0&page=" + str(j-1) + "&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    }

    response = requests.get(url, headers=headers)
    jsons = json.loads(response.text)

    for i in jsons["data"]['list']:
        job = i['jobName']
        cust = i["custName"]
        description = i['descSnippet']
        s = pd.Series([job, cust, description], index =  ["公司名稱", "職缺", "工作內容"])
        df = df._append(s, ignore_index = True)
df.to_excel("104.xlsx", index = False)