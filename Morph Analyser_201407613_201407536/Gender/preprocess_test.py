##0-Suffix,1-Previous Gender,2-Next Gender ,3-Previous wordform,4-next wordform, 5-post position,6-present word form,7-POS####


def gender_root_feature(f ,features,gender_test,root):
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
                features[j][1]=gender_test[j-1]
                features[j][2]=gender_test[j+1]
                features[j][3]=root[j-1][8 :]
                features[j][4]=root[j+1][8 :]
            features[start][1]="none"
            features[start][2]=gender_test[start+1]
            features[start][3]="none"
            features[start][4]=root[start+1][8 :]
            features[end][1]=gender_test[end-1]
            features[end][2]="none"
            features[end][3]=root[end-1][8 :]
            features[end][4]="none"
            start=end+1
            i=-1
    return features
  
f=open('trial.txt').readlines()
features_test= [[x for x in range(8)] for y in range(11)]
i=-1
gender_test=[]
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
                gender_test.append("none")
            else:
                gender_test.append(g)
            if (r=='0' or r==''):
                root.append("none")
            else:
                root.append(r)
            suffix=(str((word.split(","))[7]).split()[0])[: -1]
            if suffix=='0' or suffix=='':
                features_test[i][0]="none"
            else:   
                features_test[i][0]=suffix
            if p=='0' or p=='':
                features_test[i][5]="none"
            else:
                features_test[i][5]=p
            if wform=='0' or wform=='':
                features_test[i][6]="none"
            else:
                features_test[i][6]=wform
            if POS=='0' or POS=='':
                features_test[i][7]="none"
            else:
                features_test[i][7]=POS
features_test=gender_root_feature(f,features_test,gender_test,root)
for line in features_test:
        for word in line:
                print word,'\t',
        print ''
