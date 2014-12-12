#0-suffix ,1-prev gender, 2-next gender, 3-prev person, 4 next person,5-prev number ,6-next number,7-prev category ,8-next category,9-prev root,10-next root,
#11-current root ,12-POS##
#import edit_distance

def edit_distance(word1,word2):

##    word1=raw_input('Enter word 1:')
##    word2=raw_input('Enter word2')

    len_1=len(word1)

    len_2=len(word2)

    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element is the edit distance
    path =[[0]*(len_2+1) for _ in range(len_1+1)]
    for i in range(0,len_1+1): #initialization of base case values

        x[i][0]=i
    for j in range(0,len_2+1):

        x[0][j]=j
    for i in range (1,len_1+1):

        for j in range(1,len_2+1):

            temp=x[i][j]
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1]
            else :
                
                if x[i-1][j]==min(x[i][j-1],x[i-1][j],x[i-1][j-1]):
                    path[i][j]='delete'
                elif x[i][j-1]==min(x[i][j-1],x[i-1][j],x[i-1][j-1]):
                    path[i][j]='insert'
                elif x[i-1][j-1]==min(x[i][j-1],x[i-1][j],x[i-1][j-1]):
                    path[i][j]='interchange'
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
    ##print 'The minimum edit distance is', x[i][j]
##    print x
##    print path
    a=path[i][j]
    mylist=[]
    list_n=[]
    while not(a==0):
        if a=='delete':
            #print a
            mylist.append(a)
            i=i-1
            a=path[i][j]
        elif a=='insert':
            #print a
            mylist.append(a)
            j=j-1
            a=path[i][j]
            #print x
        elif a=='interchange':
            #print a
            mylist.append(a)
            i=i-1
            j=j-1
            a=path[i][j]

    for i in range(len(mylist)-1,-1,-1):
        list_n.append(mylist[i])
    #print list_n
    return list_n




def gender_root_feature(f ,features,gender,person,number,category,root):
    i=-1
    start=0
    for l in f:
        lines=l.rstrip('\n')
        if  not(lines.startswith('<Sentence ')or  lines.startswith('</Sentence>')or lines==(   '\t))')or lines==""):
            word=lines.split('\t')[3]
            if word.startswith("<fs af="):
                i+=1
        elif  lines.startswith('</Sentence'):
            end=start+i
            for j in range(start+1,end):
                ##gender
                features[j][1]=gender[j-1]
                features[j][2]=gender[j+1]
                ##person
                features[j][3]=person[j-1]
                features[j][4]=person[j+1]
                ##number
                features[j][5]=number[j-1]
                features[j][6]=number[j+1]
                ##category
                features[j][7]=category[j-1]
                features[j][8]=category[j+1]
                ##root
                features[j][9]=root[j-1]
                features[j][10]=root[j+1]
            features[start][1]="none"
            features[start][2]=gender[start+1]
            features[start][3]="none"
            features[start][4]=person[start+1]
            features[start][5]="none"
            features[start][6]=number[start+1]
            features[start][7]="none"
            features[start][8]=category[start+1]
            features[start][9]="none"
            features[start][10]=root[start+1]
            features[end][1]=gender[end-1]
            features[end][2]="none"
            features[end][3]=person[end-1]
            features[end][4]="none"
            features[end][5]=number[end-1]
            features[end][6]="none"
            features[end][7]=category[end-1]
            features[end][8]="none"
            features[end][9]=root[end-1]
            features[end][10]="none"
            start=end+1
            i=-1
    return features
  
f=open('1070425029_2.txt').readlines()
features= [[x for x in range(13)] for y in range(357)]
i=-1
lemma_labels=[]
person=[]
number=[]
gender=[]
category=[]
root=[]
wordform=[]
for l in f:
    lines=l.rstrip('\n')
    if  not(lines.startswith('<Sentence ')or  lines.startswith('</Sentence>')or lines==(   '\t))')or lines==""):
        word=lines.split('\t')[3]
        if word.startswith("<fs af="):
            i+=1
            g=word.split(",")[2]#gender
            per=word.split(",")[4]#person
            n=word.split(",")[3]#number
            c=word.split(",")[5]#category
            r=(word.split(",")[0])[8 :]#root
            #print "The root  is",r
            p=word.split(",")[1]#pos
            wform=(((word.split(",")[7]).split("="))[2])[1:-2]#wordform
            #print 'wform is',wform
            wform1=lines.split()[1]
            #print "The wordform 1 is",wform1
            
            list_n=edit_distance(r,wform1)####the labels
            
            #print list_n
            lemma_labels.append(list_n)
            #####making of gender_test####
            if (g=='0' or g==''):
                gender.append("none")
            else:
                gender.append(g)
                
            ####making of person_test#####
            if (per=='0' or per==''):
                person.append("none")
            else:
                person.append(per)

            #####making of number_test###
            if (n=='0' or n==''):
                number.append("none")
            else:
                number.append(n)

            #####making of category_test###
            if (c=='0' or c==''):
                category.append("none")
            else:
                category.append(c)

            ####appending root to a list###
            if (r=='0' or r==''):
                root.append("none")
            else:
                root.append(r)

            #####appending suffix#####
            suffix=(str((word.split(","))[7]).split()[0])[: -1]
            if suffix=='0' or suffix=='':
                features[i][0]="none"
            else:   
                features[i][0]=suffix

            ####appending POS-TAGS####
            if p=='0' or p=='':
                features[i][12]="none"
            else:
                features[i][12]=p

            #####appending present wordform####
            if wform=='0' or wform=='':
                features[i][11]="none"
            else:
                features[i][11]=wform

                
features=gender_root_feature(f,features,gender,person,number,category,root)
print features

print lemma_labels
