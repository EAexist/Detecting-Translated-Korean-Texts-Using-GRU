f = open("../data/google/raw/original.txt", "r")
lines = [line for line in f if '\t' in line]
f.close()

# google
# should use googletrans==3.1.0a0
from googletrans import Translator
translator = Translator()

f = open("../data/google/raw/google.txt", "w", encoding='utf-8')
f.write("translated\ttext\n")
i = 0
for line in lines:
    line_ko, line_en = line.split('\t')
    line_trans = translator.translate(line_en, src='en', dest='ko').text

    f.write("0\t"+line_ko+"\n")
    f.write("1\t"+line_trans+"\n")
    
    i+=1
    if i % 100 == 0:
        print(i)

f.close()
