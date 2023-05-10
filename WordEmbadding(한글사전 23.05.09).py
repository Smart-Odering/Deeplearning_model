import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
from gensim.models import KeyedVectors 


model = Word2Vec.load('ko.bin')

## 학습모델 저장
#model.wv.save_word2vec_format('korean_w2v')

model_result = model.wv.most_similar("따뜻")
print(model_result)

#뜨거운, 따뜻한을 왜 인식못하는 거지??
#한글모델에서 비슷한 단어 검색해서 word2vec 모델에서 실행하는 것 testㄱㄱ