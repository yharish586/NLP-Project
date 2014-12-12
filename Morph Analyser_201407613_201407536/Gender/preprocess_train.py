##0-Suffix,1-Previous Gender,2-Next Gender ,3-Previous wordform,4-next wordform, 5-post position,6-present word form,7-POS####

def gender_root_feature(f ,features,gender,root):
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
                features[j][1]=gender[j-1]
                features[j][2]=gender[j+1]
                features[j][3]=root[j-1][8 :]
                features[j][4]=root[j+1][8 :]
            features[start][1]="none"
            features[start][2]=gender[start+1]
            features[start][3]="none"
            features[start][4]=root[start+1][8 :]
            features[end][1]=gender[end-1]
            features[end][2]="none"
            features[end][3]=root[end-1][8 :]
            features[end][4]="none"
            start=end+1
            i=-1
    return features
  
f=open('1070425029_2.txt').readlines()
features= [[x for x in range(8)] for y in range(357)]
i=-1
gender=[]
root=[]
wordform=[]
for l in f:
    lines=l.rstrip('\n')
    if  not(lines.startswith('<Sentence ')or  lines.startswith('</Sentence>')or lines==(   '\t))')or lines==""):
        word=lines.split('\t')[3]
        if word.startswith("<fs af="):
            i+=1
            POS=lines.split()[2]
            g=word.split(",")[2]
            r=word.split(",")[0]
            p=word.split(",")[1]
            wform=(((word.split(",")[7]).split("="))[2])[1:-2]
            if (g=='0' or g==''):
                gender.append("none")
            else:
                gender.append(g)
            if (r=='0' or r==''):
                root.append("none")
            else:
                root.append(r)
            suffix=(str((word.split(","))[7]).split()[0])[: -1]
            if suffix=='0' or suffix=='':
                features[i][0]="none"
            else:   
                features[i][0]=suffix
            if p=='0' or p=='':
                features[i][5]="none"
            else:
                features[i][5]=p
            if wform=='0' or wform=='':
                features[i][6]="none"
            else:
                features[i][6]=wform
            if POS=='0' or POS=='':
                features[i][7]="none"
            else:
                features[i][7]=POS
gender_root_feature(f,features,gender,root)

for line in features:
        for word in line:
                print word,'\t',
        print ''

