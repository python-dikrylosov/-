### Добро пожаловать на кейс МЧС "Прогнозирование опасностей и рисков Пермского края"!
*** 
В представленном архиве вы можете увидеть файлы и папки следующего содержания.

1. Файл **Данные по метеостанциям.csv** - набор погодных замеров различных метеостанций Пермского края.
2. Файл **Данные по метеостанциям. Соответствие МО.csv** - соответствие метеостанций и муниципальных округов.
3. Файл **Данные по метеостанциям. Описания столбцов.txt** - описания столбцов файла **Данные по метеостанциям.csv**
4. **ДТП.csv** - список ДТП различных категорий 2013-2022 гг.
5. **Износ сетей по МО ПК.csv**
6. **ОЯ и НЯ.csv** - список погодных предсказаний и их подтверждений различных категорий 2013-2022 гг. Можно считать, что информация о прогнозе известна за 10 дней до непосредственной даты. 
7. **Пожары.csv** - список пожаров различных категорий 2013-2022 гг.
8. **Происшествия.csv** - список происшествий различных категорий 2013-2022 гг.
9. **Температурная статистика.csv** - температурная статистика по Пермскому краю по дням различных годов.

***

##### Вашей задачей будет разработка модели и интерфейса для прогнозирования рисков происшествий по Пермскому краю.

Модель представляет собой прогностический инструмент, который предсказывает вероятность происшествия, для формирования целевой переменной обязательно использовать файл **Происшествия.csv**. Прогноз осуществляется на основе информации, имеющейся на заданный день (историческая информация о погодных условиях/прогнозы/произвольные открытые данные, которые вы найдете и обоснуете/информация о происшествиях в прошлые моменты времени по файлам "пожары", "дтп", "НЯ и ОЯ"), на 10 дней вперед, прогноз необходим для каждого дня горизонта в виде вероятности заданного типа. 

Базово необходимо осуществлять прогнозы по следующим типам:
1. Аварии на транспорте,
2. Аварии с выбросом опасных/токсичных веществ,
3. Опасные природные явления,
4. ЖКХ,
5. Взрывы/пожары/разрушения,
6. Прочие опасности.

Дополнительными баллами оценивается построение модели по расширенному списку рисков:
1. Аварии на железнодорожном транспорте,
2. Аварии на автомобильном транспорте,
3. Аварии на водном транспорте,
4. Аварии на воздушном транспорте,
5. Взрывы (в том числе с последующим горением) и/или разрушения (обрушения) в зданиях и сооружениях,
6. Аварии на системах жизнеобеспечения,
7. Аварии с выбросом, сбросом опасных химических веществ,
8. Аварии с розливом (выбросом) нефти, нефтепродуктов,
9. Аварии с выбросом (проливом, просыпом) патогенных для человека микроорганизмов,
10. Гидродинамические аварии,
11. Опасные геологические явления, 
12. Опасные метеорологические явления, 
13. Опасные гидрологические явления,
14. Опасные явления в лесах,
15. Космические опасности,
16. Биологическая опасность.

Автоматическая проверка в данном кейсе отсутствует. Для решения задачи необходимо формализовать метрику качества (например, усредненный ROC AUC по типам рисков), особосновать ее выбор и осуществить контроль за ее стабильностью с помощью валидации и тестирования. 

# ЖЕЛАЕМ УДАЧИ!

P.S. Не забудьте посетить экспертные сессии и не стесняйтесь задавать вопросы)