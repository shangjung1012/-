import requests
import bs4

url="https://www.ncbi.nlm.nih.gov/nuccore/?term=culter"
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("dd")

idlist = []

cnt=0
for title in titles:
        if(str(title.string)=="None"):
                continue
        if(cnt%2==0):
                idlist.append(str(title.string))
        cnt+=1

print(idlist)

# 利用 Biopython 抓出序列
# from Bio import Entrez
# from Bio import SeqIO
# Entrez.email="david103132881@gmail.com"
# for n in idlist:
#         handle=Entrez.efetch(db="nuccore",id=n,rettype="fasta")
#         print(handle.read())
