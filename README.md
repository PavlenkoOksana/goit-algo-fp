# goit-algo-fp

# Завдання 7: Використання методу Монте-Карло

## Опис завдання

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином:

| Сума      | Ймовірність |Ймовірність |
|:-----:|:-----:|:-----:|
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

![Figure_7](https://github.com/PavlenkoOksana/goit-algo-fp/assets/107678761/53f829a7-b805-45f3-becc-2c838c8eb5f6)

## Результати виконання методу Монте-Карло

Результати виконання наведені в таблицях:

| Сума      | Ймовірність |
|:-----:|:-----:|
|2 | 2.82 % |
|3 |  5.47 % |
|4  | 8.30 % |
|5  | 11.07 % |
|6  | 13.85 % |
|7  |  16.76 % |
|8  | 13.86 % |
|9  | 11.20 % |
|10  | 8.33 % |
|11  | 5.56 % |
|12  | 2.77 % |


## Похибка методу Монте-Карло::

Порівняємо отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, розрахувавши похибку методу Монте-Карло:

| Сума      | Похибка |
|:-----:|:-----:|
|2 | -1.402878 %|
|3 |  1.600719 % |
|4  | 0.372149 % |
|5  |  0.351035 % |
|6  | 0.295176 %|
|7  |   -0.563887 % |
|8  | 0.244780 % |
|9  | -0.837084 % |
|10  |  -0.036014 %|
|11  |-0.035971 %  |
|12  | 0.251799 % |

Похибки, виникають через випадковий характер симуляції методом Монте-Карло. Чим більше кидків кубиків буде змодельовано, тим точніше отримані ймовірності будуть відповідати аналітичним значенням. 
Наприклад, при кількості кидків num_rolls = 100 000, максимальна похибка становить 1.6% 

## Висновки

В цілому, можна зробити висновок, що Метод Монте-Карло є потужним інструментом, особливо в області моделювання та оцінювання ймовірностей. Однак важливо враховувати, що його надійність залежить від кількості повторів експериментів та характеру випадкових подій. У деяких ситуаціях, де аналітичні методи не ефективні, метод Монте-Карло може бути дуже цінним інструментом для отримання наближених результатів.
