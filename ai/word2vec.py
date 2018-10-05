import tensorflow as tf
import numpy as np
import teel
import csv

from gensim.models import Word2Vec

def make_dict_all_cut(dict, content):
    
    for idx , token in enumerate( content.split() ):
        #print( token )

        if (len(dict) == 0):    #처음
            dict.append((token, [token]))

        else :

            flag = 0
            for i in range (len(dict)) :
                if( token == dict[i][0] ) :
                    flag = 1            #   단어 같음 넣을필요없음
                    break

            if( flag == 0 ) :   #   단어 다름 안에 있나 봐야함

                new_token = []
                for char in token:
                    if ord(char) < 12593 or ord(char) > 12643:
                        new_token.append(char)


                pp = -1
                index = - 1
                for j in range ( len( dict) ) :
                    old_token = []
                    for char in dict[j][0] :
                        if ord(char) < 12593 or ord( char ) > 12643 :
                            old_token.append( char )

                    cnt = 0
                    for k in range( min( len(new_token) , len(old_token))) :

                        if( new_token[k] == old_token[k]) :
                            cnt += 1
                        else :
                            break

                        if (cnt == 2):
                            pp = 2
                            index = j

                if( pp >= 2 ) :

                    confirm = 0
                    for pwpw in dict[index][1] :
                        if( pwpw == token ) :
                            confirm = 1

                    if( confirm == 0 ) :
                        dict[index][1].append(token)

                else :

                    #print( "2개이상겹치지는 않아서 새단어")
                    dict.append((token, [token]))
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def run():
    data_path = './newsdata.csv'

    category ,contents = teel.loading_data( data_path , eng=False, num=False, punc=False)

    dict = []
    for content in contents :
        make_dict_all_cut( dict, content )

    print( dict )

    noun_token = []
    for i in range(len(contents)) :
        tokens = contents[i].split()
        noun_token.append( tokens )
    print( noun_token )


    model = Word2Vec( noun_token , size = 100 , min_count = 1 , iter = 1000  , sg = 1  , window= 3)


    for i in range ( len( dict)) :

        if (len(dict[i][1]) == 1):
            break

        sum = []
        for j in range(100):
            sum.append(0)

        for word in dict[i][1] :

            for j in range ( 100 ) :
                sum[j] += model.wv.vectors[model.wv.vocab[word].index][j]



        for j in range( 100 ) :
            sum[j] = sum[j] / len(dict[i][1])


        for word in dict[i][1] :
            for index in range(100):
                model.wv.vectors[model.wv.vocab[word].index][index] = sum[index]



    sumPolitics = 0
    sumPt_sp = 0
    sumPt_enter = 0
    sumSports = 0
    sumSp_enter= 0
    sumEntertainment = 0

    cntPolitics = 0
    cntPt_sp = 0
    cntPt_enter = 0
    cntSports= 0
    cntSp_enter = 0
    cntEntertainment = 0


    docSum = []
    for i in range(60):
        docSum.append(0)

    index = ['politics', 'economy', 'life', 'sports', 'entertainment']

    f = open("output0623.txt", 'w')
    g = open("output0623.csv", 'w')
    wr = csv.writer(g)

    for i in range( len( contents) ) :
        field1 = category[i]

        for j in range( i+1 , len(contents) ):

            field2 = category[j]
            first = model.wv.wmdistance(contents[i], contents[j]) * 10
            temp = first * first * first / 10
            docSum[i] = docSum[i] + temp
            docSum[j] = docSum[j] + temp
            print( i , " , " , j , " " , temp )
            wr.writerow([i, j, temp])
            wr.writerow([j, i, temp])


            if( field1 == index[0] and field2 == index[0] ):
                sumPolitics += temp
                cntPolitics += 1

            elif( ( field1 == index[0] and field2 == index[3] ) or ( field1 == index[3] and field2 == index[0]) ):
                sumPt_sp += temp
                cntPt_sp += 1

            elif( ( field1 == index[0] and field2 == index[4] ) or ( field1 == index[4] and field2 == index[0]) ):
                sumPt_enter += temp
                cntPt_enter += 1

            elif( field1 == index[3] and field2 == index[3] ):
                sumSports += temp
                cntSports += 1

            elif( (field1 == index[3] and field2 == index[4] ) or ( field1 == index[4] and field2 == index[3]) ):
                sumSp_enter += temp
                cntSp_enter += 1

            elif( field1 == index[4] and field2 == index[4] ):
                sumEntertainment += temp
                cntEntertainment += 1


    avgPolitics = sumPolitics / cntPolitics
    avgPt_sp = sumPt_sp / cntPt_sp
    avgPt_enter = sumPt_enter / cntPt_enter
    avgSports = sumSports / cntSports
    avgSp_enter = sumSp_enter / cntSp_enter
    avgEntertainment = sumEntertainment / cntEntertainment

    print( "avgPolitics " , avgPolitics)
    print( "avgPt_sp " , avgPt_sp)
    print( "avgPt_enter " , avgPt_enter)
    print( "avgSports " , avgSports)
    print( "avgSp_enter " , avgSp_enter)
    print( "avgEntertainment " , avgEntertainment)


    f.write( "avgPolitics " + str(avgPolitics) + "\n")
    f.write( "avgPt_sp " + str(avgPt_sp) + "\n")
    f.write( "avgPt_enter " + str (avgPt_enter) + "\n")
    f.write( "avgSports " + str(avgSports) + "\n")
    f.write( "avgSp_enter " + str(avgSp_enter) + "\n")
    f.write( "avgEntertainment " + str(avgEntertainment) + "\n")
    f.write( "------------------------------------\n")


    for i in range(len(docSum)):
        print(i, " : ", docSum[i]/59)


    for i in range(len(docSum)):
        f.write(str(i)+" : " + str(docSum[i]/59) + '\n')
    f.close()
    g.close()