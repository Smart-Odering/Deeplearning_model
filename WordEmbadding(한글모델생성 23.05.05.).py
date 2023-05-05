import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt


df_Wordembbading = pd.read_excel("230505 리뷰데이터 테스트.xlsx")
wordembadding_df = pd.DataFrame(df_Wordembbading)
#print(wordembadding_df)

# 상위 5개 출력
print(wordembadding_df[:5]) 
# 리뷰 개수 출력
print(len(wordembadding_df))

# NULL 값 존재 유무
print('NULL 값 존재 확인:',wordembadding_df.isnull().values.any())

 # Null 값이 존재하는 행 제거
train_data = wordembadding_df['content'].dropna(how = 'any')

# Null 값이 존재하는지 확인
print(' Null 값이 존재하는지 확인:',wordembadding_df.isnull().values.any()) 

# 리뷰 개수 출력   
print('리뷰개수:',len(wordembadding_df)) 


wordembadding_df['content'] = wordembadding_df['content'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

# 불용어 정의
stopwords = ['더욱','등','에도','또한','에는','가격','향','넣다','을','이다','수','있다','곳','것','의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소 분석기 OKT를 사용한 토큰화 작업 (다소 시간 소요)
okt = Okt()
tokenized_data = []
for sentence in wordembadding_df['content']:
     # 토큰화
     # 형태소로 분류
    #temp_X = okt.morphs(sentence, stem=True)
    # 명사로 분류
    temp_X = okt.nouns(sentence)
    #nouns : 명사 추출
    #morphs : 형태소 추출
    #pos : 품사 부착

     # 불용어 제거
    temp_X = [word for word in temp_X if not word in stopwords]
    tokenized_data.append(temp_X)


# 상위 5개 출력
print(tokenized_data[:5]) 


# Word2Vec 훈련
from gensim.models import Word2Vec
model = Word2Vec(sentences = tokenized_data, size = 100, window = 3, min_count = 3, workers = 4, sg = 1)
#sg : 알고리즘을 지정한다. 0(기본값)이면 CBOW, 1이면 skip-gram
#size : 벡터의 차원 수
#window : 현재 단어와 예측 단어 간의 거리
#min_count : 빈도수가 이 값보다 낮으면 그 단어를 제거한다
#workers : 모델 학습 시 멀티 작업자 스레드 지정

# 완성된 임베딩 매트릭스의 크기 확인
print(model.wv.vectors.shape)
print(model.wv.vectors)
print(model.wv.most_similar("아이스")) #단어를 여러개 넣어도 됨
#print(model.wv.most_similar(positive=['따뜻','커피'])) #단어를 여러개 넣어도 됨



#trained_model.most_similar(positive=['woman', 'king'], negative=['man'])

#각 메뉴에 대한 설명을 구글링하여 최대한 많은 데이터를 넣어서 학습시켜보자?
#모델을 2개이상 만들어서 비슷한 단어를 가져오기?


#국어사전까지 학습시켜서 유의어를 추천

# 모델 저장
model.wv.save_word2vec_format('cafe_data')