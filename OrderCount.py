#===========================작업중==================================
# 주문 빈도를 저장하여 추천알고리즘에 적용할 수 있음.
#===================================================================

class OrderCount():
    
    def __init__(self):
        self.tag_sentence_list = ["민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동",
                                "민주","영찬","동용","지혜","동찬","명동"]
        self.word_frequency = {}    # 단어와 빈도를 쌍으로 저장할 딕셔너리를 생성합니다.

    def Count(self):
        for tag_sentence in self.tag_sentence_list:
            words = tag_sentence.split()
            for word in words:
                # 단어가 word_frequency의 키(key)값에 존재하는 경우 값(value)만 1을 더하고,
                # 없는 경우에는 1로 초기화합니다.
                if word in self.word_frequency.keys():
                    self.word_frequency[word] += 1
                else:
                    self.word_frequency[word] = 1
                    
        # word_frequency에 저장된 단어의 빈도를 리스트에 저장하고 정렬합니다.
        word_count = []
        for word, freq in self.word_frequency.items():
            word_count.append([word, freq])
        word_count.sort(key=lambda elem: elem[1], reverse=True)

        # 단어의 빈도 상위 N개를 출력합니다.
        for word, freq in word_count[:20]:
            print(word + "\t" + str(freq))


if __name__ == '__main__':
    Oc=OrderCount()
    Oc.Count()

