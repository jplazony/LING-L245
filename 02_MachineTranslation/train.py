#I created the Matrix for the Dictionary Lookup of Spanish and English. I need to count the Bigrams and Add the pairs
#to a probabilistic dictionary. I also, didn't finish the translate.py file where I would have read from a dictionary 
#the most probable outcomes for each inputted words. Then I would have translated the words in unix from English to Spanish.  
import sys
englishFile = sys.argv[1]
spanishFile= sys.argv[2]
list1=[]
list2=[]
newlist1=[]
newlist2=[]
bigrams={}

file1 = open(englishFile,'r')
for line in file1:
	line.strip('\n')
	list1.append(line)

newy = ' '.join(list1[10:100])
f = open('eng.txt',"w")
f.write(newy)
f.close()

test1 = open('eng.txt','r')
teLine=test1.readline()
print(teLine)
ney =teLine.split('.\n')
ney = list(filter(None,ney))
print(ney)

file2 = open(spanishFile,'r')
for line2 in file2:
	line2.strip('.\n')
	list2.append(line2)
newy2 = ' '.join(list2[10:100])
f = open("spanish.txt","w")
f.write(newy2)
f.close()

test2 = open('spanish.txt','r')
teLine2 = test2.readline()
print(teLine2)
ney2 =teLine2.split('.\n')
ney2 = list(filter(None,ney2))
print(ney2)


vocabulary = ['#']
# Join the list with a space and then split 
#vocabulary +=newOneString
#vocabulary+=newTwoString
vocabulary +=' '.join(ney).split(' ')
vocabulary +=' '.join(ney2).split(' ')
#print(vocabulary)

vocabularyNew = set(vocabulary)
print(vocabularyNew)

for token1 in vocabularyNew:
	for token2 in vocabularyNew:
		if token1 not in bigrams:
			bigrams[token1]={}
		if token2 not in bigrams[token1]:
			bigrams[token1][token2]=0

print(bigrams)
print('\t' + '\t'.join(bigrams.keys()))
for w1 in bigrams:
        print('%s\t' % (w1), end='')
        for w2 in bigrams[w1]:
                print('%d\t' % (bigrams[w1][w2]), end='')
        print('')
