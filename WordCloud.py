import Asin

def wc():
    import matplotlib as mpl
    import matplotlib.pyplot as plt1
    from subprocess import check_output
    from wordcloud import WordCloud, STOPWORDS

    #mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
    mpl.rcParams['font.size']=12                #10
    mpl.rcParams['savefig.dpi']=100             #72
    mpl.rcParams['figure.subplot.bottom']=.1

    stopwords = set(STOPWORDS)
    data = Asin.getWordCloud()
    # print(data)

    wordcloud = WordCloud(    collocations=False,
                              background_color='white',
                              height=300, width=400,
                              relative_scaling = 0.5,
                              random_state=2,
                              stopwords=stopwords,
                              max_words=200,
                              max_font_size=75,
                              min_font_size=5
                             ).generate(data)

    # print(wordcloud)
    plt1.cla()
    fig = plt1.figure()
    plt1.imshow(wordcloud)
    plt1.axis('off')
    #plt.show()
    asin=Asin.getAsinValue()
    fig.savefig('images/'+asin+'_wc.png', bbox_inches='tight')
    plt1.close()
