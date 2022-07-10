from Bio import Entrez, SeqIO
from pathlib import Path
import sys

Entrez.email = "A.N.Other@example.com" # 必須使用email參數，並且如果遇到問題，NCBI可以透過郵件聯繫。

# path = Path(__file__).parent # 取得檔案所在資料夾之位置
path = Path(sys.argv[0]).parent         
path_download = path/'download'# 設定在同目錄下的download資料夾

def download(genuses, path_download):
    rettypes = ["gb", "fasta"]
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
            yield(f"{i}.{rettype} completed")
    yield("all completed")

        
if __name__ == '__main__':   
    genuses = ["Culter", "Ancherythroculter", "Chanodichthys"]
    rettypes = ["gb", "fasta"]
    download(genuses, path_download)
