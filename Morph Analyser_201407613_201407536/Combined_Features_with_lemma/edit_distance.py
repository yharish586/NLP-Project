def edit_distance():
    word1=raw_input('Enter word 1:')
    word2=raw_input('Enter word2')

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
    print 'The minimum edit distance is', x[i][j]
    print x
    print path
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
    print list_n
    return list_n

edit_distance()

