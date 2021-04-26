#mycipher
import sys
key=int(sys.argv[1])
text_array=sys.stdin.readlines()
text="".join(ele for ele in text_array)

def ceasar_cipher(key,text):
  count=0
  new_text=""
  words=0
  for ele in text:
    if ele.isalpha():
      a=ord(ele.upper())+(key%26)
      if a>ord("Z"):
        a-=26
      count+=1
      if (count)%5==0:
        new_text+=chr(a)+" "
        count=0
        words+=1
        if words%10==0:
          new_text+="\n"
      else:
        new_text+=chr(a)
  return new_text

print(ceasar_cipher(key,text))
