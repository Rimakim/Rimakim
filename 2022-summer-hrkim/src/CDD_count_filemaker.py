# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 18:46:05 2022

@author: user
"""
# usage: mmseqs 에서 각 cluster의 1~4번째로 많이 보이는 domain을 가지는 seq 개수를 counting

# 클러스터 딕셔너리 만들기
# ex) cluster_dic = {rep1:[clu1data], rep2:[clu2data]...rep(n):[clu(n)data]} 이런식으로
from tqdm import tqdm
f = open('..//Clustered_data//C1_clu_cluster.tsv', 'r')

lines = f.readlines()
cluster_dic = {}

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic[L[0]] = []

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic[L[0]].append(L[1].rstrip('\n'))

        
f.close()
print()
print('cluster parsing complete')

#orphan cluster 제거하기
cluster_dic = {key: value for key, value in cluster_dic.items() if len(value) != 1}


# Pfam domain_dic 만들기

f1 = open('..//domaindata//Whole_CDD_domaindata1.tsv', 'r')

lines = f1.readlines()
protein_Pfam_dic = {}

for line in tqdm(lines):
    L = line.split(' ')
    protein_Pfam_dic[L[0]] = []

for line in tqdm(lines):
    L = line.split(' ')
    protein_Pfam_dic[L[0]].append(L[2]+L[3])

print()   
print('domaindata parsing complete')

f1.close()


# cluster name(representative seq) column 만들기
Representative_seq = [key for key in cluster_dic]


# Cluster number column 만들기
cluster_number = [len(v) for v in cluster_dic.values()]


# 각 cluster 별 domain 개수를 센 dictionary 만들기 
import collections

clu_domain_dic = {repseq:clu_members for repseq, clu_members in cluster_dic.items()} 

for rep, clu_members in tqdm(clu_domain_dic.items()):
    for i in range(len(clu_members)):
        if clu_members[i] in protein_Pfam_dic.keys():
            clu_members[i] = protein_Pfam_dic[clu_members[i]]
            
        else:
            clu_members[i] = []
    
    clu_domain_dic[rep] = sorted(list(dict(collections.Counter(sum(clu_members,[]))).values()),reverse=True)
    
    if len(clu_domain_dic[rep]) > 4:
        clu_domain_dic[rep] = clu_domain_dic[rep][:4]
        
    elif len(clu_domain_dic[rep]) == 3:
        clu_domain_dic[rep].append('-')
        
    elif len(clu_domain_dic[rep]) == 2:
        clu_domain_dic[rep] = clu_domain_dic[rep]+['-', '-']
        
    elif len(clu_domain_dic[rep]) == 1:
        clu_domain_dic[rep] = clu_domain_dic[rep]+['-', '-', '-']
    
    elif len(clu_domain_dic[rep]) == 0:
        clu_domain_dic[rep] = clu_domain_dic[rep]+['-', '-', '-', '-']
        
print()
print('exchanging cluster (protein -> domain number) complete') 

#Cluster number, pf domain 개수 합친 딕셔너리 만들기
import pandas as pd

df = pd.DataFrame(clu_domain_dic)
df1 = df.transpose()
df1['Cluster number'] = cluster_number
df1.columns = ['P1', 'P2' ,'P3' ,'P4','Cluster number']

df1.to_csv('CDD_P1-4_domain_counted_table1.csv')
print('making file complete')
