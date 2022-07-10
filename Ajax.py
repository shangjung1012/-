import requests
from bs4 import BeautifulSoup


url = 'https://www.ncbi.nlm.nih.gov/nuccore'
genus = 'Chanodichthys'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cookie': "ncbi_sid=CE8D8D2B268AB331_0825SID; entrezSort=nuccore:; WebEnv=1bCrlD5txs90SsxYzVoSQOegHj6GGeRSL4FvwRMLGfnQW%40CE8D8D2B268AB331_0825SID; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgMIFEAcAnAMwBsADOQEz4AsAgqQOzECMlHn5p+lV5AOgC2cVrRAAaEAGMANsmkBrAHZQAHgBdMocpnABDAObJl+jcgD2yieY2yocfctQIjUCBOlWNUZRs8WshIAzrC+cF6ykiCsekL6Jl5+vv64ftAAXgBiFhBC0cSEeqz4AKxU0bS6WExUVLFStOJYcgoq6lqNpXq6jaR6AGb6sqGVTHr4VMSV+HpUhOKNRVj60uYwUBJgbnDyyooSqprRpdUgiBoaYMEYAPS3AO5PAsrSAEbIL7JCL8iIAoYLDBbsoAK7SLzQADEJ1iWDSGkyAGUAJ7BHxCKgCAAKCMyAgAcuDIVABEioABHUG+aQOABKUGCoNkGmC2KcUFkAjxUAycHZhncOLcJwqWAJHQABAA+EAAXykoOUsgs+lQRy0GFAxGmWCGIygBWaIER1IKsywBWWMXwpAaICqelqxF6DuNSpVao1lW6WHtpX6WFdpXGQeidr0tCI4gVMgsQiEVm9WpAYpAKUyBT0YIhuUNjT0qAs0iZ+SkvpA4cLxdL0VD5w0QiiUgtqdd1tQUCGzM6MThMWirF1MSYrHGUjEem2goiiCcgsHgZAw2bI8Gw1GE9b+s3bb0eCIZD4dEYLHYXE4PD4ghEk6k9T0Gd5GBzJIwRZLoKEGAJAHkCbg0R1HoTwPC87yfMqPzKH8AJAkB1qsDQrouhMlAFP2SG8AUaajtMjTDoIxClAIwbDlhwbGqwPDynKQA===",
    }

data = {
    'term': f'{genus}',
    'EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Sequence_DisplayBar.PageSize': '200',
    'EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Entrez_Pager.CurrPage': '1',
    'EntrezSystem2.PEntrez.DbConnector.LastQueryKey': '1',
    'EntrezSystem2.PEntrez.DbConnector.Cmd': 'PageChanged',
    }
timeout = 25
idlist = []
page = '1'
count = 10
while(1):
	data['EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Entrez_Pager.CurrPage'] = page
	response = requests.post(url, headers=headers, data=data, timeout=timeout) # 取得html
	soup = BeautifulSoup(response.text, "html.parser")
	titles = soup.find_all('dd')
	cnt=0
	for title in titles:
		if(str(title.string)=="None"):
			continue
		if(cnt%2==0):
			idlist.append(str(title.string))
		cnt+=1
	page = str(int(page)+1)
	count -= 1 
	if(count == 0):
			break
print(idlist)
