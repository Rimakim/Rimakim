# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:34:05 2022

@author: user
"""
# mmseqs 결과 파일 중 cluster tsv 파일을 받아 기초적인 통계치를 파악해주는 

from tqdm import tqdm 
import pandas as pd

df = pd.read_csv('..//Merged Cluster.tsv', 
                 sep='\t', 
                 header=None,
                 names=['RepSeq', 'In cluster']
)




Repli = df['RepSeq']

#총 data 수
whole_data_number = len(Repli)

#cluster 개수
rep_list = list(set(Repli))
count_cluster = len(rep_list)

#orphan cluster 개수
count_orphan = 0

if Repli[0] != Repli[1]:
    count_orphan = count_orphan + 1
 
for i in tqdm(range(1, whole_data_number-1)):
    if Repli[i-1] != Repli[i] != Repli[i+1]:
        count_orphan = count_orphan + 1
        

        
if Repli[whole_data_number-2] != Repli[whole_data_number-1]:
    count_orphan = count_orphan + 1

#2개 이상 있는 cluster 수
not_orphan = count_cluster - count_orphan
 
#2개 이상 cluster 당 평균 data 수

average_not_orphan = (whole_data_number - count_orphan) / not_orphan


#최대 크기의 cluster
'''
cluster_number = [0 for i in range(len(rep_list))]

from tqdm import tqdm
j = 0 
for repseq in tqdm(list(Repli)):
    
    j = j+1
    
    cluster_number[rep_list.index(repseq)] = cluster_number[rep_list.index(repseq)] + 1
    
max_clu_number = max(cluster_number)    
'''

print()
print('총 data 수:', whole_data_number)
print('총 cluster 수:', count_cluster)        
print('orphan cluster 수:', count_orphan)

print('2개 이상 있는 cluster 수:', not_orphan)

print('2개 이상 cluster 당 평균 data수:', average_not_orphan)

'''
print('최대 크기의 cluster:', max_clu_number)
'''











