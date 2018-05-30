import os
import nltk
import csv
import re

def crawl(x):
    parse='python amazon_crawler.py -d '+ x + '_files ' + x+' -o Datasets/'+x+'_folder/'+x+'_parser'
    os.system(parse)
    os.system('python amazon_parser.py -d Datasets/'+x+'_folder/'+x+'_parser -o Datasets/'+x+'_folder/'+ x + '.csv')

def convert(x):
    ipFile = open("Datasets/"+x+"_folder/"+x+".csv", "r")
    opFile = open("Datasets/"+x+"_folder/"+x+".txt", "w+")
    csv_f = csv.reader(ipFile)
    for row in csv_f:
        row[3] = re.sub("<br />", " ", row[3])
        opFile.write("\n[t]" + row[3] + "\n")
        row[4] = re.sub("<br />", " ", row[4])
        row[4]=re.sub(r'^https?:\/\/.*[\r\n]*', '', row[4], flags=re.MULTILINE)
        review = row[4].lower()
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        opFile.write('##' + '\n##'.join(tokenizer.tokenize(review)))
    opFile.close()

def pos_neg(x):
    ipFile = open("Datasets/"+x+"_folder/"+x+".csv", "r")
    posFile = open("Datasets/"+x+"_folder/"+x+"_pos.txt", "w+")
    negFile = open("Datasets/"+x+"_folder/"+x+"_neg.txt", "w+")
    csv_f = csv.reader(ipFile)
    for row in csv_f:
        if(row[6] == "negative"):
            row[4] = re.sub("<br />", " ", row[4])
            review = row[4].lower()
            negFile.write(review)
            negFile.write('\n')
        if (row[6] == "positive"):
            row[4] = re.sub("<br />", " ", row[4])
            review = row[4].lower()
            posFile.write(review)
            posFile.write('\n')
