from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

#часть речи
dictPos = {
    'NOUN': 'существительное',
    'ADJF': 'полное прилагательное',
    'ADJS': 'краткое прилагательное',
    'COMP': 'компаратив',
    'VERB': 'глагол (личная форма)',
    'INFN': 'глагол (инфинитив)',
    'PRTF': 'полное причастие',
    'PRTS': 'краткое причастие',
    'GRND': 'деепричастие',
    'NUMR': 'числительное',
    'ADVB': 'наречие',
    'NPRO': 'местоимение-существительное',
    'PRED': 'предикатив',
    'PREP': 'предлог',
    'CONJ': 'союз',
    'PRCL': 'частица',
    'INTJ': 'междометие',
    None: 'не определено'
}

#вид(глагола)
dictAspect = {
    'perf': 'совершенный',
    'impf': 'несовершенный',
    None: 'не определено'
}

#падеж
dictCase = {
    'nomn': 'именительный',
    'gent': 'родительный',
    'datv': 'дательный',
    'accs': 'винительный',
    'ablt': 'творительный',
    'loct': 'предложный',
    'voct': 'звательный',
    'gen2': 'второй родительный (частичный)',
    'acc2': 'второй винительный',
    'loc2': 'второй предложный (местный)',
    None: 'не определено'
}

#род
dictGender = {
    'masc': 'мужской',
    'femn': 'женский',
    'neut': 'средний',
    'ms-f': 'общий',
    None: 'не определено'
}

#наклонение
dictMood = {
    'indc': 'изъявительное',
    'impr': 'повелительное',
    None: 'не определено'
}

#число
dictNumber = {
    'sing': 'единственное',
    'plur': 'множественное',
    None: 'не определено'
}

#лицо
dictPerson = {
    '1per': 1,
    '2per': 2,
    '3per': 3,
    None: 'не определено'
}

#время
dictTense = {
    'pres': 'настоящее',
    'past': 'прошедшее',
    'futr': 'будущее',
    None: 'не определено'
}

#морфологический анализатор
def morphAnalyzer(text):
    p = morph.parse(text)[0]
    print("- - - - -  МОРФОЛОГИЧЕСКИЙ АНАЛИЗ - - - - -")
    print("Нормальная форма слова:", p.normal_form)
    print('Часть речи:', dictPos[p.tag.POS])
    print('Наклонение:', dictMood[p.tag.mood])
    print('Падеж:', dictCase[p.tag.case])
    print('Число:', dictNumber[p.tag.number])
    print('Вид:', dictAspect[p.tag.aspect])
    print('Род: ', dictGender[p.tag.gender])
    print('Лицо:', dictPerson[p.tag.person])
    print('Время:', dictTense[p.tag.tense])

#функция для склонения слова/получения лексемы
def morphInflect(text):
    print("Выберите из списка:")
    print('''\t1. Склонение;
\t2. Лексема слова. ''')
    act = int(input())
    if act == 1:
        print("Характеристики склоняемого слова.")
        case = input("Введите падеж:(Выберите из списка: nomn(им.п.),gent(род.п),datv(дат.п.),accs(вин.п.),ablt(твор.п.),loct(предл.п.)   ")
        number = input("Введите число:(Выберите из списка: sing(един.ч.), plur(множ.ч.)   ")
        gender = input("Введите род:(Выберите из списка: masc(муж.р.), femn(жен.р.), neut(сред.р.)   ")
        a = {case, number, gender}
        p = morph.parse(text)[0]
        if p.inflect(a) != None:
            print(p.inflect(a).word)
        else:
            print("None")

    elif act == 2:
        p = morph.parse(text)[0]
        for i in p.lexeme:
            print(i.word, end='; ')
        print()

#функция согласования слова с числительным
def morphNumber(text):
    n = int(input("Введите числительное:   "))
    p = morph.parse(text)[0]
    print(str(n) + " " + str(p.make_agree_with_number(n).word))

#взаимодействие с пользователем,обращение к другим функциям
def menu():
    print(" Выберите пункт из  меню: ")
    print('''\t1 - Морфологический анализ;
\t2 - Просклонять слово;
\t3 - Согласование слова с числительным;
\t4 - Выйти.''')
    print("Введите команду: ")
    actions = int(input())
    if actions != 4:
        name_file = "DataSet"
        g = open(name_file + ".txt", "r", encoding='utf-8')
        text = g.read()
        word = input("Введите слово: ")
        if actions == 1:
            morphAnalyzer(word)
        elif actions == 2:
            morphInflect(word)
        elif actions == 3:
            morphNumber(word)

        print(" - - - - - - - - - - - - - - - \n")
        menu()
    else:
        return

menu()

