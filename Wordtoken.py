import re
with open('./the-verdict.txt','r',encoding='utf-8') as f:
    file=f.read()

arr=" <|endoftext|>"," <|unk|>"
file+="".join(arr)
print(len(file))
result = re.split(r'([,.:;?_!"()\']|--|\s)', file)
processed=list(set(result))
processed.remove("")
# print(processed[:50])
# "hello word motherfucker"
tokendict={}
tokenids=[]
class Word2token:
    def __init__(self,text):
        self.text=text
    def createToken(self):
        for index,value in enumerate(self.text):
        #  print((index,value))
        #  if index==50:
        #      break
         tokendict[value]=index
         tokenids.append(index)
        print(len(tokenids))
        
    def encode(self,words):
        words=re.split(r'([,.:;?_!"()\']|--|\s)', words)
        words=list(set(words))
        words.remove(' ')
        print(words)
        ids=[]
        for word in words:
            if word in tokendict:
                # print(tokendict[word])
                ids.append(tokendict[word])
                
        
            else:
                print('word does not exist')
        print(ids)
        return ids
    def decode(self,example):
     ids=self.encode(example)
     wordarr = []
     for id in ids:
        for word, token_id in tokendict.items():
            if id == token_id:
                wordarr.append(word)
                

     print(wordarr)
example="I HAD always thought "
word=Word2token(processed) 
word.createToken()
word.encode(example)
word.decode(example)



# settext=set(file)

