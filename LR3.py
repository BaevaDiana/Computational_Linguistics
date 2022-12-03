from natasha import (
    # разбить предложение на токены
    Segmenter,
    # кодировка слов
    NewsEmbedding,
    # морфологический анализатор
    NewsMorphTagger,
    # синтаксический анализатор
    NewsSyntaxParser,
    Doc
)

path = "DataSet.txt"
# импортирование пакета для разделения текста на предложения
from nltk import sent_tokenize
# импортирование пакета для разделения предложений на слова
from nltk import word_tokenize
# импортирование пакета для морфологического разбора слова
from pymorphy2 import MorphAnalyzer

file = open(path, "r", encoding="utf8")
text = file.readlines()
words = []
file.close()

# создаем объект класса Segmenter
segmenter = Segmenter()
# создаём объект класса NewsEmbedding для кодировки слов
emb = NewsEmbedding()
# создаём объект класса NewsMorphTagger для морф.разбора слов
morph_tagger = NewsMorphTagger(emb)
# создаём объект класса NewsSyntaxParser для синтаксического разбора слов
syntax_parser = NewsSyntaxParser(emb)


for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        doc = Doc(sent)
        doc.segment(segmenter)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        print(doc.tokens[:5])
        doc.sents[0].syntax.print()
