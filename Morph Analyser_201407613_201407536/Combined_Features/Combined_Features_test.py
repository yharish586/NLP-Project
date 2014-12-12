###0-suffix ,1-prev gender, 2-next gender, 3-prev person, 4 next person,5-prev number ,6-next number,7-prev category ,8-next category,9-prev root,10-next root,
###11-current root ,12-postposition ,13-POS##
def gender_root_feature(f ,features,gender_test,person_test,number_test,category_test,root):
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
                features[j][1]=gender_test[j-1]
                features[j][2]=gender_test[j+1]
                ##person
                features[j][3]=person_test[j-1]
                features[j][4]=person_test[j+1]
                ##number
                features[j][5]=number_test[j-1]
                features[j][6]=number_test[j+1]
                ##category
                features[j][7]=category_test[j-1]
                features[j][8]=category_test[j+1]
                ##root
                features[j][9]=root[j-1][8 :]
                features[j][10]=root[j+1][8 :]
            features[start][1]="none"
            features[start][2]=gender_test[start+1]
            features[start][3]="none"
            features[start][4]=person_test[start+1]
            features[start][5]="none"
            features[start][6]=number_test[start+1]
            features[start][7]="none"
            features[start][8]=category_test[start+1]
            features[start][9]="none"
            features[start][10]=root[start+1][8 :]
            features[end][1]=gender_test[end-1]
            features[end][2]="none"
            features[end][3]=person_test[end-1]
            features[end][4]="none"
            features[end][5]=number_test[end-1]
            features[end][6]="none"
            features[end][7]=category_test[end-1]
            features[end][8]="none"
            features[end][9]=root[end-1][8 :]
            features[end][10]="none"
            start=end+1
            i=-1
    return features
  
f=open('trial.txt').readlines()
features_test= [[x for x in range(14)] for y in range(11)]
i=-1
person_test=[]
number_test=[]
gender_test=[]
category_test=[]
root=[]
wordform=[]
for l in f:
    lines=l.rstrip('\n')
    if  not(lines.startswith('<Sentence ')or  lines.startswith('</Sentence>')or lines==(   '\t))')or lines==""):
        word=lines.split('\t')[3]
        if word.startswith("<fs af="):
            i+=1
            POS=lines.split()[2]##postag
            g=word.split(",")[2]#gender
            per=word.split(",")[4]#person
            n=word.split(",")[3]#number
            c=word.split(",")[5]#category
            r=word.split(",")[0]#root
            p=word.split(",")[1]#postposition
            wform=(((word.split(",")[7]).split("="))[2])[1:-2]#wordform

            #####making of gender_test####
            if (g=='0' or g==''):
                gender_test.append("none")
            else:
                gender_test.append(g)
                
            ####making of person_test#####
            if (per=='0' or per==''):
                person_test.append("none")
            else:
                person_test.append(per)

            #####making of number_test###
            if (n=='0' or n==''):
                number_test.append("none")
            else:
                number_test.append(n)

            #####making of category_test###
            if (c=='0' or c==''):
                category_test.append("none")
            else:
                category_test.append(c)

            ####appending root to a list###
            if (r=='0' or r==''):
                root.append("none")
            else:
                root.append(r)

            #####appending suffix#####
            suffix=(str((word.split(","))[7]).split()[0])[: -1]
            if suffix=='0' or suffix=='':
                features_test[i][0]="none"
            else:   
                features_test[i][0]=suffix

            ####appending Postposition####
            if p=='0' or p=='':
                features_test[i][12]="none"
            else:
                features_test[i][12]=p

            #####appending present wordform####
            if wform=='0' or wform=='':
                features_test[i][11]="none"
            else:
                features_test[i][11]=wform

            ####appending POS####
            if POS=='0' or POS=='':
                features_test[i][13]="none"
            else:
                features_test[i][13]=POS

                
features_test=gender_root_feature(f,features_test,gender_test,person_test,number_test,category_test,root)
print features_test
