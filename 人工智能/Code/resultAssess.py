# -*- coding:utf-8 -*-

def Binary(labelFilePath, resFilePath):

    labelFile = open(labelFilePath, 'r')
    resFile = open(resFilePath, 'r')

    label = []
    result = []

    lines = resFile.readlines()
    for line in lines:
        if line.strip('\n').strip('\r').strip(' ') == '':
            continue

        y = float(line.strip('\n').strip('\r').strip(' ').strip('[').strip(']'))
        if y >= 0.5:
            result.append(1)
        else:
            result.append(0)

    lines = labelFile.readlines()
    for line in lines:
        label.append(int(line.strip('\n').strip('\r').strip(' ')))

    TP = 0
    TN = 0
    FN = 0
    FP = 0

    # for i in range(len(label)):
    #
    #     if(label[i] == 1 and result[i] == 1):
    #         TP +=1
    #     if(label[i] ==1 and  result[i] == 0):
    #         FN += 1
    #     if(label[i] == 0 and result[i] ==0):
    #         TN += 1
    #     if(label[i] == 0 and result[i]== 1):
    #         FP += 1
    white_sum = 0
    for i in range(len(label)):

        if(label[i] != 0 and result[i] == 1):
            TP +=1
        if(label[i] != 0 and  result[i] == 0):
            FN += 1
        if(label[i] == 0 and result[i] ==0):
            TN += 1
        if(label[i] == 0 and result[i]== 1):
            FP += 1

    P = (float)(TP)/(TP+FP)
    R = (float)(TP)/(TP+FN)

    score = 100*2*P*R/(P+R)

    print('P: '+str(P))
    print('R: '+str(R))
    print('Score: '+str(score))
    print('wu bao lv: ' + str((float)(FP)/(FP + TN)))
    print('lou bao lv: ' + str((float)(FN) / (TP + FN)))




# 对二分类结果进行多分类评估的合理方式
def Binary_normal(classesFilePath, resFilePath):

    res_file = open('Binary_result.csv', 'w')
    res_file.write('Domain Type, right_num , wrong_num , P' + '\n')

    #每个元素是一个数组 [right,wrong]
    feed_id = {}
    feed_count = {}
    feed_id['Alexa'] = 0
    feed_count[0] = [0,0]

    feedFile = open('./data/black/feeds.txt', 'r')
    lines = feedFile.readlines()
    i = 1
    for line in lines:
        feed = line.split(' ')[0]
        feed_id[feed] = i
        feed_count[i] = [0,0]
        i += 1
    feedFile.close()

    print (str(len(feed_id.keys())))

    classesFile = open(classesFilePath, 'r')
    resFile = open(resFilePath, 'r')

    classes = []
    result = []

    lines = resFile.readlines()
    for line in lines:
        y = float(line.strip('\n').strip('\r').strip(' ').strip('[').strip(']'))
        if y >= 0.5:
            result.append(1)
        else:
            result.append(0)

    lines = classesFile.readlines()
    for line in lines:
        classes.append(int(line.strip('\n').strip('\r').strip(' ')))

    for i in range(len(result)):
        if result[i] == 1:
            if classes[i] != 0:
                feed_count[classes[i]][0] += 1
            else:
                feed_count[classes[i]][1] += 1

        else:
            if classes[i] != 0:
                feed_count[classes[i]][1] += 1
            else:
                feed_count[classes[i]][0] += 1

    P_sum = 0.0
    num = 0
    for feed in feed_id.keys():
        id = feed_id[feed]
        right_num = feed_count[id][0]
        wrong_num = feed_count[id][1]
        P = float(right_num) / (right_num + wrong_num)
        num += 1
        P_sum +=  P
        res_file.write(feed + ',' + str(right_num) + ',' + str(wrong_num) + ',' + str(P) + '\n')

    res_file.write('average' + ',,,' + str(P_sum/num) + '\n')




#Binary_normal('/home/audr/chc/DGA/data/Binary/360/test_classes.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_360_8_b.txt')



#Binary_normal('/home/audr/chc/DGA/data/Binary/360/test_classes.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_360_8_b.txt')




# Binary('/home/audr/chc/DGA/data/Binary/360/test_label.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_360_8_b.txt')
# Binary('/home/audr/chc/DGA/data/Binary/osint/test_label.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_osint_10_b.txt')



Binary('/home/audr/chc/DGA/data/Binary/360/test_label.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_360_8_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/osint/test_label.txt', '/home/audr/chc/DGA/result/CNN_2/test_result_osint_10_b.txt')


Binary('/home/audr/chc/DGA/data/Binary/360/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_360_128_5_1_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/360/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_360_128_5_2_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/360/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_360_128_5_3_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/osint/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_osint_128_4_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/osint/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_osint_128_5_2_b.txt')
Binary('/home/audr/chc/DGA/data/Binary/osint/test_label.txt', '/home/audr/chc/DGA/result/LSTM_ATTENTION/test_result_osint_128_5_3_b.txt')
