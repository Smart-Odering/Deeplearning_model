from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# 모델 로드
loaded_model = KeyedVectors.load_word2vec_format("cafe_data") 

model_result = loaded_model.most_similar("아메리카노")
print(model_result)