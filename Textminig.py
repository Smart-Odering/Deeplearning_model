#===========================작업중==================================
# 형태소를 분석하여 명사형태의 단어를 추출한다
#===================================================================

# !pip install konlpy
# !pip install nltk


# 주문해줘, 추천해줘, 알려줘, 보여줘, 등등 명령어에 따른 알고리즘 추천함수 필요
# 연관검색, 비슷한 텍스트 찾아주는 추천함수 필요

from konlpy.tag import Okt
okt = Okt()


class Textmining():

    def __init__(self):
        self.text1= "아이스 아메리카노 하나 그리고 따뜻한 아메리카노 추천 주문해줘 더운 뜨거운 핫"
        self.text = '형태소분석으로 문장을 분해해보자'
        self.tagging = okt.pos(self.text1)    #형태소 품사 부착
        self.sy=[]
        self.recommend = "추천"or"추천해줘"
        self.supply = "주문"
        return

    def TextClassification(self):
        for i in self.tagging:
            if i == 'EOS' : continue    #문장이 끝나면 건너뛰기 
            self.sy.append(i[0])
        print(self.sy)

        if self.recommend in self.sy:
            print('추천메뉴list 제공')

        if self.supply in self.sy:
            print('메뉴list 제공')
        #print(self.sy)
        


if __name__ == '__main__':
    Tm=Textmining()
    Tm.TextClassification()
