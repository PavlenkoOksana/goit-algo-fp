# goit-algo-fp

# Завдання 7: Використання методу Монте-Карло

## Опис завдання

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином:

| Сума      | Імовірність |Імовірність |
|:-----:|:-----:|
|2 | 2.78% |1/36|
|3 |  5.56%|2/36|
|4  |8.33%  |3/36|
|5  | 11.11% |4/36|
|6  | 13.89% |5/36|
|7  | 16.67%  |6/36|
|8  | 13.89% |5/36|
|9  | 11.11% |4/36|
|10  |  8.33%|3/36|
|11  | 5.56% |2/36|
|12  | 2.78% |1/36|

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

## Графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло



## Результати тестування алгоритмів

Для порівняння ефективності алгоритмів, були проведені тести, з різними параметрами виклику функцій (основну увагу було приділено сумі, яку потрібно видати покупцеві). Результати тестування наведені в таблицях:


| сума      | 113 | 100 | 1 056 | 1 130 053 | 11 300 537 |
| --------------    |:-----:|:-----:|:-----:|:-----:|:-----:|
| кіл-ть монет | 3 | 6 | 6 | 6 | 6 |
| жадібний |4.49997e-06|6.39999e-06|5.200039e-06|7.90000e-06|5.60000e-06|
| динамічний|5.98999e-05|7.17000e-05|0.00125|0.88265|8.81887|


Як можна побачити у результатах тестування, ефективність жадібного алгоритму не дуже відрізняється від параметрів виклику функції find_coins_greedy, в той час, як для алгоритму динамічного програмування, вочевидь, є пропорційна залежність від параметрів виклику find_min_coins.

### Жадібний алгоритм (find_coins_greedy):

Жадібний алгоритм вибирає найбільшу доступну монету на кожному кроці, намагаючись максимізувати кількість виданих монет.
Ефективний для швидкого розрахунку видачі решти.
Недолік: не завжди дає оптимальний результат.

### Алгоритм динамічного програмування (find_min_coins):

Алгоритм динамічного програмування розв'язує задачу оптимального розподілу монет для кожної суми.
Ефективний для знаходження мінімальної кількості монет для будь-якої суми.


### Для невеликих сум:

Обидва алгоритми працюють добре, і час виконання буде приблизно однаковим. В проведених тестах при сумах 100 та 113 час виконання обох алгоритмів був незначним, однак слід зазначити, що жадібний алгоритм працював приблизно у 10 разів швидше.

### Для великих сум:

Як підтвердили тести, жадібний алгоритм працює швидше через свою простоту і відсутність необхідності робити розрахунки для всіх можливих комбінацій.
Алгоритм динамічного програмування може вимагати більше обчислювальних ресурсів, оскільки розрахунки здійснюються для всіх сум від 0 до заданої суми. Наприклад розрахунку для суми 11 300 537, жадібному алгоритму потрібно 5.6000001222855644e-06 сек, в той час, як алгоритму динамічного програмування потрібно 8,82 сек. 

## Результати роботи алгоритмів

Загалом, обираючи між жадібним алгоритмом та алгоритмом динамічного програмування, слід враховувати конкретні обставини та вимоги задачі. Жадібний алгоритм може бути швидшим та працювати добре для певних сценаріїв, але алгоритм динамічного програмування гарантує оптимальність відповіді.

## Часова скаладність

Жадібний алгоритм (find_coins_greedy):

Часова складність цього алгоритму є лінійною O(n), де n - кількість різних номіналів монет.
Оскільки алгоритм просто вибирає найбільший доступний номінал, кількість операцій зазвичай лінійно залежить від кількості різних номіналів.

Алгоритм динамічного програмування (find_min_coins):

Часова складність алгоритму динамічного програмування для цієї задачі при побудові таблиці dp_table залежить від обраної суми для видачі та кількості різних номіналів монет. Часова складність дорівнює O(s * n), де s - сума, n - кількість різних номіналів монет. При побудові результату, часова складність мінша за O(s * n), тому можемо її ігнорувати.

## Висновки

Результати тестів ефективності жадібного алгоритму та алгоритму динамічного програмування показали, що жадібний алгоритм є більш ефективним за часом виконання, оскільки він не виконує складних обчислень, в той час, як алгоритм динамічного програмування гарантує оптимальність, але він вимагає більше обчислювальних ресурсів, особливо при роботі з великими діапазонами сум.

