# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 22:23:51 2022

@author: hrkim
"""

# 5단계 프로세스에서 나온 cluster data pasing 하기

from tqdm import tqdm

f1 = open('Clustered_data//mmseqs_obey_paper//C1_cluster.tsv', 'r')  # C1 cluster tsv 파일 받기

lines1 = f1.readlines()
cluster_dic_C1 = {}

for line in tqdm(lines1):
    L = line.split('\t')
    cluster_dic_C1[L[0]] = []

for line in tqdm(lines1):
    L = line.split('\t')
    cluster_dic_C1[L[0]].append(L[1].rstrip('\n'))

f1.close()


f2 = open('Clustered_data//mmseqs_obey_paper//C1-2_cluster.tsv', 'r') # 2단계 process cluster tsv 파일 받기

lines2 = f2.readlines()
cluster_dic_C1_2 = {}

for line in tqdm(lines2):
    L = line.split('\t')
    cluster_dic_C1_2[L[0]] = []

for line in tqdm(lines2):
    L = line.split('\t')
    cluster_dic_C1_2[L[0]].append(L[1].rstrip('\n'))

f2.close()


f3 = open('Clustered_data//mmseqs_obey_paper//C1-3clu.tsv', 'r')  # 3단계 tsv 파일 받기

lines3 = f3.readlines()
cluster_dic_C1_3 = {}

for line in tqdm(lines3):
    L = line.split('\t')
    cluster_dic_C1_3[L[0]] = []

for line in tqdm(lines3):
    L = line.split('\t')
    cluster_dic_C1_3[L[0]].append(L[1].rstrip('\n'))
    
  
f3.close()


f4 = open('Clustered_data//mmseqs_obey_paper//C1-4clu.tsv', 'r') # 4단계 tsv 파일 받기

lines = f4.readlines()
cluster_dic_C1_4 = {}

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic_C1_4[L[0]] = []

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic_C1_4[L[0]].append(L[1].rstrip('\n'))    
    
f4.close()


f5 = open('Clustered_data//mmseqs_obey_paper//C2clu.tsv', 'r') # C2 cluster tsv 파일 받기

lines = f5.readlines()
cluster_dic_C2 = {}

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic_C2[L[0]] = []

for line in tqdm(lines):
    L = line.split('\t')
    cluster_dic_C2[L[0]].append(L[1].rstrip('\n'))

print()
print('Cluster data parsing complete')


# 각 cluster 들을 representative seq로 연결하여 묶기
def Cluster_merge(Rep_clu_dict, Cluster_dict):
    
    Merged_cluster = Rep_clu_dict
    
    for rep_seq, clu_members in tqdm(Merged_cluster.items()):
        
        for i in range(len(clu_members)):
            if clu_members[i] in Cluster_dict.keys():
                clu_members[i] = Cluster_dict[clu_members[i]]
                
            else:
                clu_members[i] = []
        
        Merged_cluster[rep_seq] = sum(clu_members,[])
        
    return Merged_cluster



C2_C1_4 = Cluster_merge(cluster_dic_C2, cluster_dic_C1_4)    
C2__C1_3 = Cluster_merge(C2_C1_4, cluster_dic_C1_3)
C2____C1_2 = Cluster_merge(C2__C1_3, cluster_dic_C1_2)   
Merged_Cluster = Cluster_merge(C2____C1_2, cluster_dic_C1)  


for rep_seq, clu_members in Merged_Cluster.items():
    
    Merged_Cluster[rep_seq] = list(set(clu_members))

print('Merging cluster complete')        

# Merged cluster를 tsv파일로 내보내기
New_lines = []

for rep_seq, clu_members in Merged_Cluster.items():
    
    for seq in clu_members:
        
        New_lines.append(rep_seq + '\t' + seq +'\n')
        

f = open('Merged Cluster.tsv', 'w')

for line in New_lines:
    f.write(line)

f.close()

print('tsv file making complete')
