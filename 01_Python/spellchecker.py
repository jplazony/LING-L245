#ANSWER


import sys

freq = [] # list to store frequency list


x = sys.stdin.read() # reads the users original string they entered into the spell checker.
#Writes out the original string the user put in
#sys.stdout.write(x)

fd = open('words.txt', 'r') # reads my words.txt file created which is the list of tokenized words. 


for line in fd.readlines(): # reads each line in the words.txt file 

    line = line.strip('\n') # strips each line in txt file by '\n'. 
    freq.append(line) # appends each line to my freq list.

reader = x.strip('\n') # strips each line by '\n' in the orignial user string to spell check.
if '.' in x:
    period = x[:-2]
    newx = period.split(' ')
else:
    newx  = reader.split(' ') # splits each word into a list by spaces for the user entered string.


placeHolder=[] # set a place holder to re-add the user string with the spell checked words.
for i in newx: # for loop to loop through each word in a users string.
    if i in freq: # if statement to check if the user words are in the frequency list. 
        placeHolder.append(i) # if word in the list it appends the word to my place holder list.
        stringList= ' '.join(placeHolder) # join to put sentence back together with spaces. 
    elif i not in freq: # otherwise if word not in frequency list.
            placeHolder.append("*"+i) # append the '*' symbol to the word and add it to the place holder list.
            stringList= ' '.join(placeHolder) # join to put sentence back together with spaces. 
print(stringList+'.') # prints the spell checked string back to the user.
