"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

class MountainCondition:
    name: str
    description: str
    image_link: str

    def __init__(self, name: str, description: str, image_link: str):
        self.name = name
        self.description = description
        self.image_link = image_link

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        mountain_condition=[
            MountainCondition(
                'Эверест',
                'Эверест, известный также как Джомолунгма, является самой высокой точкой нашей планеты.',
                'https://i.imgur.com/CwxmBW3.png'
            ),
            MountainCondition(
                'Гималаи',
                'Гималаи — высочайшая горная система Земли, расположенная между Тибетским нагорьем на севере и Индо-Гангской равниной на юге.',
                'https://imgur.com/NwHmNir.png'
            ),            
            MountainCondition(
                'Канченджанга',
                'Канченджанга — горный массив в Гималаях, главная вершина которого, высотой 8586 м над уровнем моря, является третьим по высоте восьмитысячником мира.',
                'https://i.imgur.com/r3X1hLo.png'
            ),            
            MountainCondition(
                'Макалу',
                'Макалу – пятая по высоте гора мира, она расположена в 22 км к востоку от горы Эверест.',
                'https://imgur.com/mdrvXaR.png'
            ),
            MountainCondition(
                'Аннапурна',
                'Аннапурна — горный массив в Гималаях, где находятся высочайшие вершины — Аннапурна и Дхаулагири, разделенные самой глубокой на планете долиной Калигандаки.',
                'https://i.imgur.com/0FdHZ42.jpg'
            ),
        ]
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/mnt/<name>')
@view('mountain')
def preview(name):
    """Renders the about page."""

    #d1 = dict(
    #    head = "",
    #    description = "",
    #    climb_h = "",
    #    climb_text = "",
    #    img1 = "",
    #    location_text = "",
    #    more_text = "",
    #    last_text = "",
    #    title='Mountain paradise',
    #    year = datetime.now().year
    #    )
    d1 = dict(
        val = "everest",
        head = "Высочайшая вершина мира.",
        description = "Эверест (Джомолунгма) — самая высокая гора на планете. Ее официально признанная высота — 8848,86 метров над уровнем моря. Координаты высочайшей точки Земли 27°59’23″N 86°55’37″E, она находится на Евразийском континенте.",
        climb_h = "Сколько времени нужно, чтобы подняться на Эверест!",
        climb_text = "Экспедиция на гору Эверест занимает в среднем около 2 месяцев. До двух недель уйдет на подъём из столицы Непала — города Катманду до базового лагеря. Есть вариант сократить путь, добравшись воздушным транспортом до аэропорта в Лукле.",
        img1 = "https://alpagama.org/wp-content/uploads/2018/12/everkhumbu.jpg",
        location_text = "Джомолунгма расположена в горной системе Гималаев, а именно в хребте Махалангур-Химал, что находится на границе Республики Непал и Тибетского автономного района КНР.",
        more_text = "Высота её северной вершины, расположенной на территории Китая и считающейся главной, составляет 8848 метров. Это абсолютный рекорд среди высочайших гор Земли, которых насчитывается 117 (все они сосредоточены в регионе Центральной и Южной Азии). Южная вершина чуть ниже, 8760 метров, и ее можно назвать «интернациональной»: она находится на границе двух стран. Гора похожа на трехгранную пирамиду. Склон и ребра с юга настолько крутые, что снег и ледники на них не удерживаются. Не имеет снежного покрытия и скальная стена. Остальные ребра, начиная примерно с 5-километровой высоты, покрыты ледниками. Часть Эвереста, расположенная со стороны Непала, входит в состав национального парка «Сагарматха». Именно так – Сагарматха – называется высочайшая вершина мира на непальском языке (в переводе – «Небесная вершина»). С этой стороны она заслонена горами Нупцзе (7879 м) и Лхоцзе (8516 м). Красивые виды на нее открываются с окрестных гор Кала-Патхар и Гокио-Ри.",
        last_text = "Джомолунгма – это название переводится с тибетского как «Повелительница ветров» – одна из десяти горных вершин, так называемых восьмитысячников, расположенных в Гималаях (в мире их всего 14). Несомненно, она остается самой привлекательной целью для альпинистов всего мира.",
        title='Mountain paradise',
        year = datetime.now().year
        )

    d2 = dict(
        val = "elbrus",
        head = "Эльбрус",
        description = "Эльбру́с (карач.-балк. Минги-Тау, кабард.-черк. Iуащхьэмахуэ) — стратовулкан на Кавказе (5642 метра над уровнем моря) — самая высокая горная вершина России и Европы при условии проведения границы между Европой и Азией по Главному Кавказскому хребту или южнее (в иных случаях высочайшей вершиной Европы считается альпийская гора Монблан). Эльбрус включён в список высочайших вершин частей света «Семь вершин».",
        climb_h = "История восхождений",
        climb_text = "Первое успешное восхождение на одну из вершин Эльбруса было совершено в рамках научной экспедиции, организованной Российской Академией наук по предложению и под общим руководством начальника Кавказской укреплённой линии генерала Георгия Арсеньевича Эммануэля, в которой принимали участие выдающиеся учёные XIX века профессор Адольф Купфер — основатель Главной геофизической обсерватории Петербурга, физик Эмилий Ленц, зоолог Эдуард Минетрие — основатель Русского энтомологического общества, ботаник Карл Мейер (впоследствии ставший академиком и директором ботанического сада Российской Академии наук), художник-архитектор Иосиф (Джузеппе-Марко) Бернардацци (сделавший первое изображение Эльбруса), венгерский путешественник Янош Бессе. Восхождение осуществлялось с северной стороны Эльбруса от верховий реки Малка через «чёрные горы, среди крутых и скалистых утёсов». В полдень 22 июля 1829 года на Восточную вершину поднялся один из проводников экспедиции К. Хаширов (Хачиров), который принёс с неё чёрный с зеленоватыми прожилками кусок базальта (одну часть которого отослали в Петербург, а вторую Эммануэль вручил Бессе для хранения в национальном музее Будапешта). Остальные восходители смогли достичь лишь высоты примерно 5300 метров. Первое восхождение на Эльбрус приветствовали тремя ружейными залпами. В память об экспедиции её руководитель приказал вырезать на скале рядом с базовым лагерем надпись.",
        img1 = "https://i.imgur.com/gaI1geo.png",
        location_text = "Эльбрус находится в Боковом хребте Большого Кавказа в 10 км к северу от Главного Кавказского хребта на границе республик Кабардино-Балкария и Карачаево-Черкесия и представляет собой горный массив вулканического происхождения с диаметром основания 15 км и ярко выраженными Восточной (5621 м) и Западной вершинами (5642 м), разделённых протяжённой пологой седловиной (перевал Седловина Эльбруса, 5416 м). Расстояние между вершинами 1500 м. Абсолютные высоты цоколя 3200—3800 м. Средняя крутизна склонов 35°. Впервые высота Эльбруса была определена в 1813 году академиком В. К. Вишневским и, по его оценке, составила 5421 м. Со склонов Эльбруса стекают 23 ледника, общая площадь которых 134 км². Наибольшие из них Большой и Малый Азау, Терскол, Кюкюртлю (возможны варианты названия), Ирик. Максимальная длина эльбрусских ледников 6—9 км, что почти в два раза короче крупнейших ледников Кавказа Дыхсу и Безенгийского. За последние 100 лет общая площадь ледников сократилась на 18 %, а стекающих в долину Кубани — на 33 %. Ледники Эльбруса питают три наиболее крупные реки Кавказа и Ставрополья: Баксан, Малку и Кубань.",
        more_text = "Проведённые в последние десятилетия комплексные геологические исследования позволили уверенно отнести Эльбрус к категории потенциально активных вулканов, что стимулировало повышенный интерес к расшифровке истории и закономерностей развития магматизма в этом регионе, изучению происхождения магматических расплавов, поиску следов природных палеокатастроф, связанных с вулканическими извержениями.",
        last_text = "Примерно 250 тыс. лет назад началось формирование современного вулкана Эльбрус. Двухконусный стратовулкан Эльбрус, извергавший лавы дацитового состава, в настоящее время представляет собой округлую в плане вершину со средним диаметром основания около 18 км. Фундамент вулканической постройки вскрыт вплоть до абсолютных отметок 3000-3900 м и сложен палеозойскими метаморфическими породами и гранитоидами. Таким образом, относительная высота вулкана Эльбрус составляет 2000—2500 м.",
        title='Mountain paradise',
        year = datetime.now().year
        )

    dicts = [d1, d2]

    for x in dicts:
        if(x["val"]==name):
            return x;
    
    return "No pages found!!!!"


    return dict(
        title='Mountain paradise',
        year=datetime.now().year,
    )

@route('/bio/<name>')
@view('human')
def preview(name):
    """Renders the about page."""

    d1 = dict(val = "bukreev", 
              name= "Анатолий Николаевич Букреев",
              img ="https://i.imgur.com/7go85qx.jpeg", 
              disc =  "Анатолий Николаевич Букреев (16 января 1958, Коркино, Челябинская область, СССР — 25 декабря 1997, Аннапурна, Гималаи, Непал) — советский и казахстанский высотный альпинист, горный гид и писатель русского происхождения. Заслуженный мастер спорта СССР (1989), мастер спорта СССР международного класса (1989), обладатель титула «Снежный барс» (1985). Покоритель одиннадцати восьмитысячников планеты, совершивший на них в общей сложности 18 восхождений. По мнению Райнхольда Месснера, самый сильный альпинист-высотник XX века. Кавалер ордена «За личное мужество» (1989), казахстанской медали «За мужество» (1998, посмертно), высшей награды Американского альпклуба — медали Дэвида Соулса, вручаемой альпинистам, спасшим в горах людей с риском для собственной жизни (1997).",
              early = "Спортивную карьеру начал в детском возрасте с походов и восхождений на Урале. Будучи студентом Челябинского пединститута, поднимался на вершины Тянь-Шаня, а во время службы в армии покорил свои первые семитысячники на Памире. В 1989 году в составе советской гималайской экспедиции на Канченджангу взошёл на все вершины этого массива высотой выше 8000 метров. После распада СССР и сокращения государственного финансирования профессионального альпинизма работал преимущественно горным гидом — первый опыт в этом начинании получил в США, подняв клиентов на высшую точку Северной Америки вершину Мак-Кинли. В период с 1991 по 1995 год в составе различных экспедиций дважды поднимался на Эверест, Дхаулагири и Макалу, а также взошёл на К2 и Манаслу. 30 июня 1995 года на массовой альпиниаде на пик Абая (4010 м) в Заилийском Алатау являлся персональным гидом президента Казахстана Нурсултана Назарбаева. В 1997 году с выходом бестселлера «В разрежённом воздухе» Джона Кракауэра, посвящённого трагедии на Эвересте годом ранее, имя Букреева стало известно далеко за пределами узкого круга альпинистов-профессионалов, однако для англоязычных читателей книги образ Букреева как представителя другой культурной среды, к тому же не в совершенстве владевшего языком, вышел отнюдь не положительным. Не будучи профессионалом в высотном альпинизме, Кракауэр дал собственную оценку целого ряда решений и действий Букреева, вызвавшую серьёзную полемику в альпинистской среде. Хотя профессиональное реноме Букреева не пострадало, в том же году была опубликована его книга, написанная в соавторстве с Вестоном Де Уолтом «Восхождение», в которой Букреев изложил собственное видение событий на Эвересте. В 1997 году в четвёртый раз в карьере поднялся на Джомолунгму, второй раз на Лхоцзе, впервые на Броуд-Пик и Гашербрум II.",
              common = "Родился 16 января 1958 года в городе Коркино Челябинской области третьим ребёнком в многодетной семье (старшие дети Александр (1952) и Любовь (1954), младшие Ирина и Николай). Отец, Николай Васильевич, занимался ремонтом музыкальных инструментов, мать, Валентина Андреевна, работала в местном транспортном управлении, а позже в местном клубе. Учился в средней школе № 2 (ныне МБОУ «СОШ № 2» Коркинского муниципального района), которую окончил в 1975 году. Учёба давалась ему легко, по словам старшего брата, «всё схватывал на лету». Увлекался чтением, «…любил науку. Физику.». По рекомендации от школы поступил на физико-математический факультет Челябинского государственного педагогический института, который окончил в 1979 году по специальности учитель физики, а также получил диплом тренера по лыжному спорту. После окончания ВУЗа получил распределение в родную школу, но «как-то сумел договориться» и из Челябинска уехал в Алма-Ату. Там же был призван на срочную службу в армию (1979—1981). По протекции Ерванда Ильинского, главного тренера республиканского ЦСКА и сборной Казахстана по альпинизму, получил направление в спортивную роту Среднеазиатского военного округа. Во время службы в армии заболел менингитом, из-за чего был исключён из состава сборной САВО, а врачи запретили ему заниматься спортом вообще. Тем не менее, сумел полностью восстановиться. После увольнения в запас остался в Казахстане, жил неподалёку от Алма-Аты в совхозе «Горный садовод». Работал в ЦСКА тренером по лыжной подготовке в областной ДЮСШ, а также инструктором по горной подготовке, совместив работу с увлечением альпинизмом. После распада СССР остался в Казахстане и получил гражданство (двойное) этой республики. В 1990-х годах перебрался в США, как он сам говорил: «Я гражданин мира. Мне говорят: „Анатолий, ты тренируешься в Америке, живешь в Казахстане, родился на Урале“. Я отвечаю: „Да, вот так получается, а большую часть времени провожу в Непале“».",
              death = "Погиб 25 декабря в результате схода снежной лавины во время попытки зимнего восхождения на вершину Аннапурна.",
              vid1 = "https://www.youtube.com/embed/OBpubDhDJ78",
              vid2 = "https://www.youtube.com/embed/t1GeXhcEXAA",
              title='Mountain paradise',
              year = datetime.now().year)
    
    d2 = dict(val = "messner", 
              name= "Райнхольд Андреас Месснер",
              img ="https://i.imgur.com/A52FzB1.png", 
              disc =  "Райнхольд Андреас Месснер (нем. Reinhold Andreas Messner; род. 17 сентября 1944, Бриксен) — итальянский альпинист из немецкоговорящей автономной провинции Южного Тироля, Италия, первым совершивший восхождения на все 14 «восьмитысячников» мира, некоторые из них в одиночку. Месснер — один из самых знаменитых альпинистов в мировой истории, путешественник, писатель, в настоящее время депутат Европарламента и общественный деятель. Пионер спортивного подхода к альпинизму, ввел в практику скоростные одиночные восхождения, сначала в Доломитовых Альпах, а затем и в районе Монблана. Стал первым альпинистом, покорившим все 14 восьмитысячников мира, одним из первых достиг семи высочайших вершин континентов, двух полюсов. Совершил рекордные восхождения в разных регионах: по южной стене Аконкагуа, Брич Уолл на Килиманджаро, по юго-западной стене на Мак-Кинли и др. Но главным образом он стал известен своими восхождениями в Гималаях. 9 апреля 2010 года Райнхольду Месснеру вручён почётный Lifetime Achievement Piolet d’Or (Золотой ледоруб — самая престижная награда в альпинизме, вручаемая за выдающиеся достижения), второй в истории после Вальтера Бонатти (2009). Лауреат премии принцессы Астурийской (2018, совместно с Кшиштофом Велицким).",
              early = "Райнхольд Месснер родился 17 сентября 1944 г. в Южном Тироле. Родным языком Райнхольда был немецкий. Он с детства привык жить в условиях Альп. Окончил университет Падуи по специальности «архитектура». Первые восхождения совершил в студенчестве со своим братом в доломитовых Альпах.",
              common = "Первое гималайское восхождение Месснер совершил в 1970 году на вершину Нанга-Парбат. И хотя формально оно было успешным, его омрачила трагедия — во время спуска погиб в лавине его родной брат Гюнтер, а у самого Райнхольда в результате обморожения были ампутированы семь пальцев на ногах. Тело Гюнтера Месснера было найдено 17 июля 2005 года тремя пакистанскими альпинистами. Было омрачено трагедией и второе восхождение Месснера на восьмитысячник: в 1972 году при восхождении на Манаслу (8136 м) погиб его напарник по связке. В 1975 году Месснер совершил восхождение на Хидден-пик (8068 м) в Каракоруме, а в мае 1978 года вместе с Петером Хабелером поднялся без использования кислорода на Джомолунгму по классическому маршруту (с Южного седла по Юго-восточному гребню). Летом этого же года Месснер совершил одиночное бескислородное восхождение на вершину Нанга Парбат по западной (Диамирской) стене. В 1979 году Месснер в альпийском стиле совершил восхождение на К2 по классическому маршруту (юго-восточное ребро Абруцци), а летом 1980 года одиночное бескислородное восхождение на Джомолунгму во время сезона муссонов (со стороны Тибета через перевал Северное седло и Северо-восточный гребень с выходом на вершину по кулуару Нортона). Об этом восхождении он написал книгу «Хрустальный горизонт» (переведена на русский в 1990 году, перевод Матвеенко В. А.).",
              death = "Он еще жив!",
              vid1 = "https://www.youtube.com/embed/WkS-cjwCOl8",
              vid2 = "https://www.youtube.com/embed/p7k4wSHF1yg",
              title='Mountain paradise',
              year = datetime.now().year)



    dicts = [d1, d2];

    for x in dicts:
        if(x["val"]==name):
            return x;
    
    return "No pages found!!!!"

#class Bio
#    name: str
#    img: str
#    description: str
#    early_life: str
#    death: str
#    vid1: str
#    vid2: str

#    def __init__(self, name: str, img: str, description: str,early_life: str,  death: str,  vid1: str,  vid2: str):
#        self.name = name
#        self.img = img
#        self.description = description
#        self.early_life = early_life
#        self.death = death
#        self.vid1 = vid1        
#        self.vid2 = vid2


