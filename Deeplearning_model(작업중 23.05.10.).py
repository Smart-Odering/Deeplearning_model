import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
from gensim.models import KeyedVectors 

from WordEmbadding import Textmining


class MatchingSystem(Textmining):
    def __init__(self):
        self.model_1 = Textmining.model()
        # 완성된 임베딩 매트릭스의 크기 확인
        print(self.model_1.wv.vectors.shape)
        print(self.model_1.wv.vectors)
        print(self.model_1.wv.most_similar("달콤")) #단어를 여러개 넣어도 됨

    # def Find_menu():
    #     # 완성된 임베딩 매트릭스의 크기 확인
    #     print(self.model_1.wv.vectors.shape)
    #     print(model.wv.vectors)
    #     print(model.wv.most_similar("달콤")) #단어를 여러개 넣어도 됨



if __name__ == '__main__':
    Ms=MatchingSystem()