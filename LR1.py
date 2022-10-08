import nltk
from nltk import download #скачивание списка стоп-слов
download('stopwords')
nltk.download('punkt')
from nltk import sent_tokenize  #разделение входного текста на предложения
from nltk import word_tokenize  #разделение вводного текста предложений на слова
from nltk.corpus import stopwords

file = open("DataSet.txt","r",encoding="utf8")
text = file.readlines()
count = 1 #переменная для нумерации предложений

st_words = set(stopwords.words('russian')) #список русских стоп-слов

# каждую строчку текста разбиваем на предложения(слова), потом выводим
for el in text:
    sentences = sent_tokenize(el) #строку разбиваем на предложения
    for i in range(len(sentences)):#идём по строке
        print("Предложение номер " + " " + str(count) + ": " + str(sentences[i]))
        sent = sentences[i]
        count += 1
        words = word_tokenize(sent) #предложение разбиваем на слова
        without_stop_words = [word for word in words if not word in st_words] #удаляем из предложения стоп-слова
        print("Слова из этого предложения: ", sep="")
        print(without_stop_words, sep=" ")
        print()
