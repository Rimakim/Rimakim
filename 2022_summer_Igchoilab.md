## 2022 Summer URAP - 김하림(생공18)




# 1주차(7/4~7/8)

## lab meeting 논문요약발표(7/5(화))

논문제목: An expanding arsenal of immune systems that protect bacteria from phages 

<요약>

=> 새로운 microbal defense system 탐색

1. 박테리아의 defense system gene을 computational method 활용해서 어떻게 예측하였는지...? (at dry lab)

   1) MMseq 이용하여 protein big data를 sequence homology를 비교하여 clustering    
   2) 각 cluster를 known defense protein family의 domain들과 비교하여 prediction score 도출   
   3) defense gene들이 서로 co-localization 하는 특성 이용하여 prediction score를 assessing   
   

2. Experimental vallidation (at wet lab)
   
   1) Plaque assay: 예측된 gene 들을 균주에 cloning 후, phage 감염시켜 plaque 수를 집계하여 감염정도 측정   
   2) Mutation test: 확실한 검증을 위해, plaque assay에서 면역반응을 보인 gene을 mutation 시켜봄   
   

<느낀점>

논문을 읽으며 Biological한 부분은 이해가 잘 되어 전체적인 실험의 flow를 이해할 수 있었지만, computational tool에 대한 기초지식이 부족하여 prediction 실험에 관한 이해가 부족했던 것 같다. MMseq라는 프로그램을 다루는 내용을 처음 접해보았기 때문에, 세부적인 parameter의 사용까지는 이해할 수 없었지만, 이전에 k-clustering이라는 머신러닝 알고리즘을 공부해본 적이 있어 대체적인 틀은 이해할 수 있었다.


## MMseq 설치후 clustering module 사용해보기

Github 메뉴얼 참고하여 학교 서버에 설치한 후, 발표한 논문에 언급되었던 MMseq2의 'cluster' option을 사용해보았다.
lynux를 이용해서 파일을 다루고 무언가를 설치해보는 것이 이번이 처음이었기 때문에, 설치과정부터 많은 어려움들이 있었지만, 조교님과 대학원생 분들의 조언을 받아 겨우 설치할 수 있었다. program에 자체적으로 있는 example file로 clustering을 실행해보았지만, 결과를 해석하는 방법을 모르기 때문에 이 부분을 더 알아보아야 할 것 같다. 또한 lynux 환경에서의 파일 작업과 명령어 사용에 빨리 익숙해질 필요가 있다는 생각이 많이 들었다. (처음이라 정말 어려웠다...)

## Biopython 사용하여 Rosalind 문제 풀기

seq motif 분석 관련된 몇 가지 쉬운 문제들을 풀어보았다. 처음에 python 문법만을 가지고 문제를 접근하려고 시도하다가, 너무 복잡해지고 반복문을 많이 사용하게 되어 코드가 과도하게 길어지는 상황들이 발생했다. 조교님께서 Biopython 의 함수들을 사용하여 문제를 접근하면 훨씬 쉬울 것이라고 하셔서 Biopython을 설치하여 sequence를 다루는 몇 가지 method와 문법들을 공부하고, 바로 Rosalind 문제에 적용해 보았더니 비교적 쉽게 풀 수 있었던 것 같다. 앞으로 fasta나 genbank 파일을 parsing 하여 실제 seq data를 다루는 방법들도 공부해볼 예정이다.







# 2주차(7/11~7/15)


## 7/11(월)

   <MMseq 의 Search 옵션 사용하여 예시파일의 homology 비교해보기>

   지난 주에 MMseq를 학교 서버에 설치한 후, 발표논문에서 언급되었던 clustering 기능을 사용하여 예시 파일에 있는 Sequence를 돌려보았다.   
   결과 파일을 바로 추출할 수 있었지만, 지난 주에 했을 때는 결과 해석이 잘 되지 않았는데, 논문에서 언급된 내용들을 참조하여 다시 살펴보았더니,   
   각 cluster의 Representive Sequence와 그 cluster 내에 포함된 sequence들이 함께 출력됨을 알 수 있었다.   
   
   오늘은 cluster 옵션에 이어 search 옵션을 사용해 보았다. search 옵션은 unknown seq들을 이미 알고 있는 seq와 모두 일일히 비교하여 얼마나 homology를 가지고 있는지를   
   출력해주는 옵션이다. 예시파일로 돌려본 결과 두 파일에 있는 seq들을 matching하여 서로 일치하는 seq의 비율과 mismatch AA의 개수가 함께 출력됨을 알 수 있었다.   
   수많은 단백질 서열들을 간단하게 한번에 비교할 수 있기 때문에 연구에 있어 상당히 편한 옵션인 것 같다.   
   
   

## 7/12(화) 

   405개 유전체 데이터가 담긴 9개 genus의 Probiotics 정보를 받아, MMseq에 default option으로 한번 돌려보았다.   
   MMseqs는 하나의 fasta 파일에 대해서만 작업을 수행하고, directory를 input으로 받지 못하기 때문에,    
   파이썬을 이용하여 받은 directory 안에 있는 405개 파일들을 genus 별로 묶고, 전체 파일을 하나로 합치는 작업을 먼저 수행했다.   
   각각 새로 합쳐진 파일들을 모두 mmseq 이용하여 clustering하고, 어떻게 분류되었는지 직접 눈으로 확인해보았다.   

     
## 7/14(목)

   기초적인 pfam과 COG, Ncbi database의 구성과 사용 방법에 대해서 알아보았다.   
   protein의 domain 정보를 담고 있는 Pfam과 Ncbi database 에서 clustering이 실제로 잘 되었는지 확인해 보기 위해, 몇 가지 cluster의 protein seq를 database에 검색해보았다.   
   대체적으로 같은 cluster에 있는 protein들은 같은 domain을 포함하고 있음을 알 수 있었다.   
   
   이번에 MMseq와 기존의 Orthofinder 프로그램의 clustering 성능을 비교하는 pipeline을 제작해보는 프로젝트에 참여할 것이라고 교수님께서 말씀해주셔서, orthofinder라는
   프로그램에 대해 알아보는 시간을 가졌다.   
   espeon 서버에 이미 설치가 되어있어서, 간단한 사용방법과 어떤 식으로 clustering이 되는지에 대해 간단한 개념을 알아보았다.   
   
   <대표적인 차이점..?>
   
   1. Output 차이: MMseqs는 sequence homology에 의해 분류된 cluster의 정보만 출력하지만, orthofinder는 cluster들의 진화적 연관성 (Gene tree)도 함께 제시한다.   
   2. Input 차이: MMseqs는 fasta 파일 하나만 받을 수 있지만, orthofinder는 여러 genus의 유전체 정보가 담긴 directory를 받는다.   
   

## 7/15(금)

   이번 하계 학부연구생 프로그램 동안 내가 맡아 진행하게 될 구체적인 프로젝트 내용이 정해졌다.
   
   ### Project Main 주제: MMseqs2와 Orthofinder의 clustering 성능을 비교하는 Pipeline 설계
   
   <내가 맡은 parts>
   
   1. 받은 405개의 probiotics Protein seq들을  MMseqs2와 Orthofinder에 다양한 option으로 돌려 보고, 결과 비교분석
      
      비교해볼 수치들 => cluster의 특성을 잘 나타내주는 수치들이어야 할 것
      
      1) 전체 cluster의 수   
      2) 전체 protein 수와 orphan(단일 cluster)으로 분류된 protein 수   
      3) 등등..더 생각해보고 추가하자... (여러 paper 자료 참고 예정)   
    
    
   2. 받은 자료를 참고하여, Protein name(Locus tag)에 분류된 database 정보를 한눈에 볼 수 있도록 하는 python tool 만들기
   
           >Protein 1 - Pfam - domain 1 ....   
                     - Pfam - domain 2 ....   
                     - COG  - domain 3 ....   이런 식으로 표기되게끔 만들어보는게 목표   

   

# 3주차 (7/18~7/22)

## 7/18(월)~7/19(화)

   
   1. 결과 파일을 쉽게 보기 위해 fasta file의 headline을 locus tag로 치환하는 코드 작성 
   
   2. 405개 probiotics data를 mmseqs 와 orthofinder를 이용하여 default option으로 clustering 한 데이터를 얻었고, 각각의
      
      전체 protein 수,     
      전체 cluster 수(mmseqs2: representative seq 개수, orthofinder: orthogroup 수+orphan 수),    
      orphan cluster(cluster 내에 seq가 1개만 있는 것) 수,    
      2개 이상의 data를 가지는 Cluster 수를 집계하였다.   
      
      (orthofinder 에서는 orphan으로 분류된 cluster가 결과파일에 출력되지 않음. => 전체 data수 - 결과파일에 표시된 data개수로 구하였음.)    
      (MMseqs2는 python 이용하여 orphan 개수 집계하였음)   
      
  
  
|Program|Option|parameter|Whole Protein Number|Whole Cluster Number|Orphan Number|2개 이상 data를 갖는 Cluster Number|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|MMseq2|easy-cluster|default|873,905|84,164|52,616|31,548|
|MMseq2|linclust|default|873,905|589,486|475,762|113,724|
|Orthofinder|-|default|873,905|45,881|21,695|24,186|
      



-daily comment-
      
실제로 프로그램을 돌려 clustering 하고 집계하는 것 보다, data를 정리하고 count 하는 코드를 짜는 데 훨씬 많은 시간이 들었다.   
통계를 내는 데 도움이 될 수 있는 소스코드를 따로 만들어 놓았으므로, 앞으로 더 빠르게 clustered data를 분석할 수 있을 것이다.   



## 7/20(수)~7/22(금)

### 생각해본 Clustering scoring 방법 

발표 논문에서 사용했던 scoring 방법을 참고하여, clustering이 잘 되었는지 검증해볼 수 있는 간단한 방법을 고안해 보았다.   

clustering이 잘 되었다는 것은, cluster마다 최대한 특정 domain 정보를 갖는 seq들로만 묶였다는 것을 의미한다.

각 cluster 마다, 가장 높은 빈도를 보이는 domain이 존재할 것이고, 각각의 cluster에서 최대빈도를 갖는 domain의 비율이 높다는 것은 clustering이 잘 되었음을 의미.

따라서, 다음과 같이 대략적으로 score를 구할 수 있을 것으로 생각되는 공식을 만들어 보았다.   


![image](https://user-images.githubusercontent.com/108413012/180389874-6d31403f-15a9-4345-bde3-2cc6d7b8e6c2.png)

여기서 S = score, W = 전체 data 수, Ci = 각 cluster의 data 수,    
Pi = 각 cluster에서 최대 빈도를 갖는 domain의 비율(최대빈도 domain 수/Ci)

따라서, 405개 genome data를 여러 옵션으로 프로그램을 돌려, 각 cluster 마다 이 Pi값과, 두 번째로 많은 빈도를 보이는 P'i 값도 함께 구해볼 예정 
 






### Clustering에 영향을 줄 수 있는 결정적인 parameter들.  

### MMseqs2

#### 1) --cluster-mode [0,1,2]
  다음과 같이 3개의 모드 존재      
  
  (그래프에서 각 seq를 잇는 edge는 mmseqs2의 clustering criteria (ex. --min-seq-id, -c, -e) 를 만족시키는 seq들 끼리 이은 것임)
   
  mode 0: Greedy 기반, 제일 connection이 많은 seq vertex를 고르고, 그 vertex에 인접한 node들을 묶어나가는 방식   
  ![mmseqs_clumode0](https://user-images.githubusercontent.com/108413012/180352650-4152171d-8100-4af9-ba4b-81baabac78fc.PNG)   
  
  mode 1: 연결된 node들을 모두 같은 cluster로 보는 방식   
  ![mmseqs_clumode1](https://user-images.githubusercontent.com/108413012/180352679-3a40dd4d-88a9-457f-af7b-7649e2157993.PNG)
  
  mode 2: 이것도 Greedy 기반, clusterdp 포함되지 않은 vertex 중 가장 길이가 긴 seq를 중심으로 인접한 node들을 묶어나가는 방식       
  ![mmseqs_clumode2](https://user-images.githubusercontent.com/108413012/180352724-9af44a30-93d6-4b39-ac6d-538c9661f0d1.PNG)   

#### 2) --cov-mode (coverage mode) [0,1,2,3]    
  다음과 같이 4개의 모드 존재  [default = 0] 
 
![mmseqs_covmode](https://user-images.githubusercontent.com/108413012/180352119-ef1b6816-447e-4bba-8dc9-4989a86e63ae.PNG)


#### 3) -c [0,1]: coverage 퍼센트 값

#### 4) --min-seq-id: minimum sequence identity, seq homology의 정도를 나타낸다. 

#### 5) -s [0,1]: sensitivity, 이 값이 주어지지 않으면, --min-seq-id 값으로 sensitivity를 대체한다. [default = 5.7] 
             running time에 핵심적인 영향을 끼친다.
             
   MMseqs2 에서는--min-seq-id를 다음과 같이 -s 값으로 환산한다.
   
   |Minimum Sequence Identitiy(--min-seq-id)|Sensitivity(-s)|
   |:---:|:---:|
   |0.3 이하|6.0|
   |0.3 초과  0.8 이하|1.0 + (1.0 * (0.7 - MinSeqId) * 10)|
   |0.8 초과|1.0|
   
   
   
   최종적으로 변화시켜볼 parameter
   => 발표논문에서 수행했던 5단계 clustering 방식을 그대로 따를 것.
      5단계 process 다시한번 정리해보면,    
      1) cluster option을 default로 한번 돌림 (C1 cluster)    
      2) clusthash option을 --min-seq-id = 0.95로 돌려 redundancy 없앰       
      3) c1 cluster의 representative seq만을 이용하여 한번 더 돌림 ('--add-self-matches'parameter 사용, -s = 0.75)       
      4) 3에서 돌린 representative seq로 반복,         
      5) 마지막으로, '--cluster-mode 1' parameter 사용하여 돌림. (C2 cluster)             
      
      2~5단계에서는 1단계에서 나온 representative seq들 한번 더 선별하는 과정이므로, 이 과정에서는 parameter를 변화시키지 않고,
      1단계에서 parameter들을 조정해가면서 돌려볼 예정이다.
      
      우선, sensitivity를 변화시켜 가며 clustering 해볼 예정      
      -s: 4.7, 5.7(default), 6.7, 7.7     
      
      
    
     

### Orthofinder    

#### 1) -I: <int> MCL inflation parameter [Default = 1.5]  [1.0, 9.0]    

MCL clustering algorithm에서, Clustering이 얼마나 tight하게, 또는 rough하게 될 것인지를 결정하는 parameter        
Orthofinder에서는 이 한가지 option만 변화시켜가면서 clustering 해볼 예정

-I = 1.5, 2.5, 3.5, 4.5 이렇게 4가지 값으로 돌리고 통계내볼 예정. 

# 4주차(7/25~7/29)

3주차는 우선 MMseqs 위주로 진행해볼 예정이다.

## 7/25(월)

논문에 나온 대로, 5단계 process를 이용하여 405개 genome을 mmseqs2를 활용하여 돌려보았다.     
다음 표는 5단계 과정을 거치고 남은 representative seq들을 나타낸 것이다.   

|총 seq 수|남은 representative seq(cluster) 수|single cluster로 남은 representative seq 수|2개 이상 clusrter로 묶인 repseq 수|
|:---:|:---:|:---:|:---:|
|873905|83908|83893|7|

다시 확인해보니, 데이터 처리 미숙으로 중간에 누락된 데이터가 있어 정정하고 추가로 다시 프로그램을 돌려 볼 예정이다.    
   
## 7/26(화)    

### 4주차 랩미팅 Feedback
   
   1. 굳이 여러 옵션으로 돌릴 필요 없음. 딱 3가지만 보자     
   
     1) 논문에서 나온 메뉴얼 그대로, 이미 자체적으로 검증된 순서와 parameter들일 것이므로 그대로 갖다 쓰자       
     2) MMseqs 자체의 디폴트 옵션으로 돌린 결과      
     3) Orthofinder를 디폴트로 돌렸을 떄 나오는 결과를 Reference로 하여 mmseqs 결과 2개와 비교      


## 7/27(수)

1. 데이터를 수정하고 논문에 나온 옵션으로 5단계 프로세스를 다시 실행한 결과를 정리하였다.
   
C1 => default로 clustering 해주는 easy-cluster 옵션 사용              
clusthash => C1 cluster의 representative seq들을 --min-seq-id 0.95로 잡고 돌림. 추가적인 cluster가 형성되지 않았음                
cycle 2 => clusthash 옵션으로 처리한 C1 cluster의 representative seq들로 clustering. (--add-self-matches, -s 0.75)         
cycle 3 => cycle 2와 같은 방법으로 반복        
C2(cycle 4) => --cluster-mode 1 을 추가하여 반복        
   

|Process|전체 data 수|cluster 수(representative seq 수)|1개의 data만 포함된 cluster 수|2개 이상 data 포함된 cluster 수|2개 이상 data 포함된 Cluster의 평균 data 수|
|:---:|:---:|:---:|:---:|:---:|:---:|
|C1(default)|874,200|84,357|52,832|31,525|26.05|
|clusthash|84,357|84,357|84,357|0|-|
|cycle 2|84,357|84,101|83,892|209|2.22|
|cycle 3|84,101|84,090|84,079|11|2.0|
|C2(cycle 4)|84,090|84,088|84,086|2|2.0|          
   
각 cycle에서 나온 cluster 결과 이용하여 C1과 C2 cluster를 연결시켜 최종적인 cluster를 얻을 예정
 
2. Orthfinder도 현재 백그라운드로 실행 중, 결과 나오면 분석 시작할 것이다.
   
3. 논문에 나온 parameter값이 아닌 MMseq 자체의 default 값들로도 5단계 process를 돌려볼 예정


## 7/28(목)

mmseqs를 default parameter 만으로 5단계 process로 Clustering 한 결과를 정리하였다. (cycle 2~4에서 모두 easy-cluster 옵션만 사용)        


|Process|전체 data 수|cluster 수(representative seq 수)|1개의 data만 포함된 cluster 수|2개 이상 data 포함된 cluster 수|2개 이상 data 포함된 Cluster의 평균 data 수|
|:---:|:---:|:---:|:---:|:---:|:---:|
|C1(default)|874,200|84,357|52,832|31,525|26.05|
|clusthash|84,357|84,357|84,357|0|-|
|cycle 2|84,357|83,852|83,434|418|2.21|
|cycle 3|83,852|83,820|83,789|31|2.03|
|C2(cycle 4)|83,820|83,808|83,796|12|2.0|

   
논문의 방법대로 돌린 수치와 비교하여 볼 때, clusthash 단계까지는 수치적인 변화가 없었다.         
그러나, cycle 2~4 에서 2개 이상 data가 포함된 cluster가 더 많이 나온 것으로 보아,         
C1의 representative seq 들이 default로 돌렸을 때 더 rough 하게 clustered 되었다고 말할 수 있다. 


## 7/29(금)

1) Pfam, CDD database에서 405개 genome의 874,200개 protein의 domain 정보를 검색하였다. (Domain number, IPR number만 이용)
   
   |Database|총 domain data 수|domain data 존재하는 protein 수|
   |:---:|:---:|:---:|
   |Pfam|1,054,782|737,316|
   |CDD|424,613|359,504|
   
2) MMseq의 cluster 정보와, Pfam database 정보를 매칭시켜 cluster data 수, 가장 빈도가 높은 domain 수부터 4번째로 빈도가 높은 domain 수 까지 출력하고,   
   Excel 표로 만드는 python 코드를 작성하였다. 
   
   작성한 프로그램을 시험삼아 실행시켜보기 위해, easy_cluster 로 돌린 cluster를 input으로 사용하였다.

   P1, P2, P3, P4는 각각 cluster에서 1~4번째로 빈도가 높은 domain의 수를 의미한다. 첫째 열에는 각 cluster의 representative seq를 기록하였다.       
   Pfam database에 정보가 나타나지 않는 sequence는 제외하였고, cluster 당 나타나는 Pfam domain 종류가 3개 이하인 경우 남은 칸을 '-' 로 표시하였다.   

   [P1-4_domain_counted_table.xlsx](https://github.com/choilab/compbio-urap/files/9220068/P1-4_domain_counted_table.xlsx)

   다음은 CDD database를 parsing 하여 똑같이 표로 만든 것이다.

   [CDD_P1-4_domain_counted_table1.xlsx](https://github.com/choilab/compbio-urap/files/9226043/CDD_P1-4_domain_counted_table1.xlsx)

   
3) 5단계 process에서 나온 결과파일들을 각각의 Representative seq로 연결하여 하나의 cluster로 만들고, 통계 결과를 나타내었다.
   
   |총 data 수|총 cluster 수|orphan 수|2개 이상 있는 cluster 수|2개 이상 cluster 당 평균 data 수|
   |:---:|:---:|:---:|:---:|:---:|
   |874,200|84,088|52,695|31,393|26.17|
   
   Pfam database 던져본 결과
   
   [ObeyPaper_Pfam_counted_table1.csv](https://github.com/choilab/compbio-urap/files/9226526/ObeyPaper_Pfam_counted_table1.csv)
