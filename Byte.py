import tiktoken
import torch
from torch.utils.data import Dataset,DataLoader
filepath='./the-verdict.txt'
with open(filepath,'r',encoding="utf-8") as f:
    text=f.read()
tokenizer=tiktoken.get_encoding("gpt2")
ids=tokenizer.encode(text, allowed_special={"<|endoftext|>"})
# print(ids[:50])
# print(len(ids))
sample_size=4

# inputarr=[]
# outputarr=[]
# # print(inputarr)
# # print(outputarr)
# for i in range(10):
#  inputarr.append(ids[i:sample_size+i])
#  outputarr.append(ids[i+1:sample_size+i])
# print(f'input:{inputarr}')
# print(f'output:{outputarr}')

class GptByte:
   def __init__(self,ids,batch,stride,sample_size):
      self.inputarr=[]
      self.outputarr=[]
      self.batch=batch
      self.stride=stride
      self.ids=ids
      self.sample_size=sample_size
   def createloop(self):
      for i in range(len(self.ids)):
        inp = self.ids[i:self.sample_size+i]
        out = self.ids[i+self.stride:i+(self.sample_size+self.stride)]

        if len(inp) < self.sample_size:
            inp += [0] * (self.sample_size - len(inp))
        if len(out) < self.sample_size:
            out += [0] * (self.sample_size - len(out))

        self.inputarr.append(inp)
        self.outputarr.append(out)
      return self.inputarr, self.outputarr
    #   print(f'inputarr:{torch.tensor(self.inputarr)}')
    #   print(f'outputarr:{torch.tensor(self.outputarr)}')
byte=GptByte(ids,4,2,4)
dataset = list(zip(*byte.createloop()))  # list of (inp, out)
dataset = [(torch.tensor(inp), torch.tensor(out)) for inp, out in dataset] 
if __name__=="__main__":
 traindataset=DataLoader(dataset,batch_size=30,shuffle=True,num_workers=2)
 new_data=iter(traindataset)
 input,output=next(new_data)
 print(input.shape,output.shape)
 print(f'input:{input[0]}')
 print(f'output:{output[0]}')
      