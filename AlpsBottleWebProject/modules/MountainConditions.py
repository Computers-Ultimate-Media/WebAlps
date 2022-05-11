from AlpsBottleWebProject.modules.mountain import MountainCondition


def get_mountain_conditions():
    return [
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