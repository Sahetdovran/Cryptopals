import binascii
from Crypto.Util.strxor import strxor_c

#decrementing whendiagraphs are found
def has_forbidden_digraphs( text ):
    local_score=0
    forbidden_digraphs = ['cj','fq','gx','hx','jf','jq','jx','jz','qb','qc','qj','qk','qx','qz','sx','vf','vj','vq','vx','wx','xj','zx']
    for digraph in forbidden_digraphs:
        if digraph in text:
            local_score-=1
    return local_score

#adding when common words are found
def has_english_words( text ):
    local_score=0;
    most_frequent_words = ['a','of','\'s','the', 'and', 'have', 'that', 'for',
    'you', 'with', 'say', 'this', 'they', 'but', 'his', 'from',
    'that', 'not', "n't", 'she', 'what', 'their', 'can', 'who',
    'get', 'would', 'her', 'make', 'about', 'know', 'will',
    'one', 'time', 'there', 'year', 'think', 'when', 'which',
    'them', 'some', 'people', 'take', 'out', 'into','just', 'see',
    'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other',
    'how', 'then', 'its', 'out', 'two', 'more ,these', 'want',
    'way', 'look', 'first', 'also', 'new', 'because', 'day',
    'more', 'use', 'man', 'find', 'here', 'thing', 'give', 'many']
    for word in most_frequent_words:
        if word in text:
            local_score+=1
    return local_score

def brute_line(cipher):
    score=[]
    for i in range(32, 128):
        #taking only printable characters
        text = strxor_c(cipher,i )
        score.append(has_english_words(text)+has_forbidden_digraphs(text))
    temp=score.index(max(score))
    return temp+32, max(score)

def conv(value):
        return binascii.unhexlify(value)

marks=[]
marks_key=[]
f = open("Ch4.txt","r")
for line in f:
    if line[-1] == '\n':
        line = line[:-1]
    cipher_line=conv(line)
    tempA, tempB = brute_line(cipher_line)
    marks_key.append(tempA)
    marks.append(tempB)
f.close()

pointer=marks.index(max(marks))
key_ascii=marks_key[pointer]
key=chr(key_ascii)
print ("The key is: "+key)
print ("The line number: "+pointer)
