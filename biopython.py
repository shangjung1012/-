import Bio
from Bio import Entrez, SeqIO
from pathlib import Path
import os, stat
import shutil
from bs4 import BeautifulSoup
import requests
import sys

Entrez.email = "david103132881@gmail.com"
genuses = ["Culter", "Ancherythroculter", "Chanodichthys", "Megalobrama", "Parabramis", "Sinibrama"]
rettypes = ["gb", "fasta"]
filetypes = [["CO1", "COI", "COX1", "coxI"], ["CYTB", "cyt b"], ["D-loop"], ["ND4", "ND4L"]]
filelist = [filetype[0] for filetype in filetypes]
filelist.append("except")
cnt=1
check = []
for i in filetypes:
    for j in i:
        check.append(j)

path = Path(sys.argv[0]).parent
path_download = path/'download'# 設定在同目錄下的download資料夾

def download(genuses, path_download):
    if(path_download.is_dir() == False):
        Path.mkdir(path_download)
    for i in genuses:
        idlist = []
        with Entrez.esearch(db="nuccore", term=i, retmax=10**9) as search:
            idlist = Entrez.read(search)["IdList"]
        for rettype in rettypes:
            with open(f"{path_download}/{i}.{rettype}", 'w') as f:
                with Entrez.efetch(db="nucleotide", id=idlist, rettype=rettype, retmode='text') as handle:
                    for seq in SeqIO.parse(handle, rettype):
                        SeqIO.write(seq, f, rettype)
                        f.write('\n')
            print(f"{i}.{rettype} completed")
  
def inspect():
    def reallen(genus):
        url=f"https://www.ncbi.nlm.nih.gov/nuccore/?term={genus}"
        headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find(class_="result_count")
        result = titles.string
        count = result.split(" ")[-1]
        # print(f"{genus} : {count}")
        return count
    error = []
    for genus in genuses:
        gblist = []
        fastalist = []
        for seq in SeqIO.parse(f"{path_download}/{genus}.gb", "gb"):
            gblist.append(seq.id)
        for seq in SeqIO.parse(f"{path_download}/{genus}.fasta", "fasta"):
            fastalist.append(seq.id)
        
        if(len(gblist) != len(fastalist)):
            print(f"{genus}  gb:{len(gblist)}  fasta:{len(fastalist)} ncbi:{reallen(genus)}")
            if(len(gblist) > len(fastalist)):
                error.append([genus, "fasta"])
            else:
                error.append([genus, "gb"])
        else:
            if(str(len(gblist)) == str(reallen(genus))):
                print(f"{genus} : {len(gblist)} {True}")
            else:
                print(f"{genus} : {len(gblist)} {reallen(genus)}")
        print()



def copy(exceptgenus):
    for genus in genuses:
        for filetype in filelist:
            try:
                shutil.copyfile(f"{path}/align/sort_by_genus/{genus}/{genus}_{filetype}.fasta", f"{path}/align/sort_by_marker/{filetype}/{genus}_{filetype}.fasta")
            except FileNotFoundError:
                flag = True
                for e in exceptgenus:
                    if(f"{genus}_{filetype}.fasta" == e):
                        flag = False
                        break
                if(flag):
                    print(f"No such file or directory: {genus}_{filetype}.fasta")

def del_genus():
    for i in os.listdir(f"{path}/align/sort_by_genus"):
        try :
            for j in os.listdir(f"{path}/align/sort_by_genus/{i}"):
                os.remove(f"{path}/align/sort_by_genus/{i}/{j}")
        except NotADirectoryError:
            pass
    for i in os.listdir(f"{path}/align/sort_by_marker"):
        try:
            for j in os.listdir(f"{path}/align/sort_by_marker/{i}"):
                os.remove(f"{path}/align/sort_by_marker/{i}/{j}")
        except NotADirectoryError:
            pass
    

def del_empty():
    exceptgenus = []
    for genus in genuses:
        for filetype in filelist:
            idlist = []
            for seq in SeqIO.parse(f"{path}/align/sort_by_genus/{genus}/{genus}_{filetype}.fasta", "fasta"):
                idlist.append(seq.id)
            if(len(idlist) == 0):
                os.remove(f"{path}/align/sort_by_genus/{genus}/{genus}_{filetype}.fasta")
                exceptgenus.append(f"{genus}_{filetype}.fasta")
                print(f"{genus}_{filetype}.fasta is deleted")
    return exceptgenus

def backup():
    def remove_readonly(func, path, _): # https://stackoverflow.com/questions/1889597/deleting-read-only-directory-in-python
        "Clear the readonly bit and reattempt the removal"
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(f"{path}/align/backup/1", onerror=remove_readonly)
    for i in range(2,6):
        os.rename(f"{path}/align/backup/{i}", f"{path}/align/backup/{i-1}")
    shutil.copytree(f"{path}/align/sort_by_genus", f"{path}/align/backup/5/sort_by_genus")
    shutil.copytree(f"{path}/align/sort_by_marker", f"{path}/align/backup/5/sort_by_marker")

    shutil.rmtree(f"{path}/download", onerror=remove_readonly)
    shutil.copytree(f"{path}/download backup", f"{path}/download")
    

def build():
    backup()
    del_genus()
    for genus in genuses: 
        if(os.path.isdir(f"{path}/align/sort_by_genus/{genus}") == False):
            os.mkdir(f"{path}/align/sort_by_genus/{genus}")
            print(f"mkdir:{genus}")
    for filetype in filelist:
        if(os.path.isdir(f"{path}/align/sort_by_marker/{filetype}") == False):
            os.mkdir(f"{path}/align/sort_by_marker/{filetype}")
            print(f"mkdir:{filetype}")
    def gene():
        try:
            SeqIO.write(seq,file,"fasta")
            file.write('\n')
        except Bio.Seq.UndefinedSequenceError:
            file.write(f">{seq.id} {seq.description}\n")
            file.write(f"")
            file.write(f"Sequence content is undefined\n\n")
    global cnt
    
    for genus in genuses:
        for filetype in filetypes:
            with open(f"{path}/align/sort_by_genus/{genus}/{genus}_{filetype[0]}.fasta", 'w') as file:
                for seq in SeqIO.parse(f"{path}/download/{genus}.gb", "gb"):
                    for t in filetype:
                        if(str(seq.description).upper().find(t.upper()) !=-1):
                            # print(f"{cnt} {description}")
                            gene()
                            cnt+=1
                            break
            print(f"{genus}_{filetype[0]}.fasta completed")
        with open(f"{path}/align/sort_by_genus/{genus}/{genus}_except.fasta", 'w') as file:
            for seq in SeqIO.parse(f"{path}/download/{genus}.gb", "gb"):
                flag = False
                for filetype in check:
                    if(str(seq.description).upper().find(str(filetype).upper()) != -1):
                        flag = True
                        break
                if(flag == False):
                    gene()
        print(f"{genus}_except.fasta completed\n")
    print()
    exceptgenus = del_empty()
    copy(exceptgenus)
    print("\nall-done")
