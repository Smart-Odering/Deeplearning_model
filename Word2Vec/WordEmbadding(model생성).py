# !pip install konlpy
# !pip install nltk

from konlpy.tag import Okt
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
from gensim.models import Word2Vec
okt = Okt()

class Textmining():

    def __init__(self):
        
        # 학습데이터 불러오기
        self.df_Wordembbading = pd.read_excel("F 카페(7,859)_new.xlsx")
        self.wordembadding_df = pd.DataFrame(self.df_Wordembbading)

        # Null 값이 존재하는 행 제거
        self.train_data = self.wordembadding_df['SENTENCE'].dropna(how = 'any')
        self.wordembadding_df['SENTENCE'] = self.wordembadding_df['SENTENCE'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
        
        # 불용어 정의
        self.stopwords = ['더욱','등','에도','또한','에는','가격','향','넣다','을','이다','수','있다','곳','것','의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
        self.tokenized_data = []

        # text토큰화 알고리즘 실행
        # 형태소, 명사 분류 선택
        for sentence in self.wordembadding_df['SENTENCE']:

            # 형태소로 분류
            temp_X = okt.morphs(sentence, stem=True)

            # 명사로 분류
            #temp_X = okt.nouns(sentence)
            #nouns : 명사 추출
            #morphs : 형태소 추출
            #pos : 품사 부착

            # 불용어 제거
            temp_X = [word for word in temp_X if not word in self.stopwords]
            self.tokenized_data.append(temp_X)

        ## 형태소 분리된 문장 전부출력
        #print(self.tokenized_data[:])

        ## 형태소 분리된 문장 일부출력 
        #print(self.tokenized_data[:5])

        # Word2Vec 훈련
        model = Word2Vec(sentences = self.tokenized_data, size = 100, window = 3, min_count = 3, workers = 4, sg = 1)
        self.model=model
        return




    # 모델 저장
    def save_model(self):
        self.model.wv.save_word2vec_format('cafe_data')
        print(self.model.wv.most_similar("따뜻하다")) #단어를 여러개 넣어도 됨
        return



if __name__ == '__main__':
    Tm=Textmining()
    #Tm.TextClassification()
    #Tm.create_model()
    Tm.save_model()