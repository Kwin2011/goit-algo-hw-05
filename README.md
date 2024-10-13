## Порівняння алгоритмів пошуку 

### Часова складність (Time Complexity, TC) алгоритмів пошуку
#### Алгоритм Кнута-Морріса-Пратта (kmp_search), Алгоритм Бойєра-Мура (boyer_moore_search) та Алгоритм Рабіна-Карпа (rabin_karp_search)

| Алгоритм   | TC найкращого випадку | TC найгіршого випадку |
|------------|-----------------------|-----------------------|
| kmp_search | O(n+m)                | O(n+m)                |
| boyer_moore| O(n/m)                | O(m*n)                |
| rabin_karp | O(n+m)                | O(m*n)                |

### Результати тестування

| Патерн             | Область   | kmp_search, сек | boyer_moore, сек | rabin_karp, сек |
|--------------------|-----------|-----------------|------------------|-----------------|
| Знайдений          | текст1    | 0.0010666658    | 0.0002949704     | 0.0022057829    |
| Не знайдений       | текст1    | 0.0008389979    | 0.0005403129     | 0.0024201321    |
|--------------------|-----------|-----------------|------------------|-----------------|
| Знайдений          | текст2    | 0.0012876400    | 0.0004319704     | 0.0030851467    |
| Не знайдений       | текст2    | 0.0012428283    | 0.0007878279     | 0.0035636058    |

### Висновки:

#### Для тексту 1: 
Для знайденого та не знайденого патерна найшвидшим у цьому випадку виявився алгоритм Бойєра-Мура.

#### Для тексту 2: 
Аналогічно, для знайденого та не знайденого патерна найшвидшим виявився алгоритм Бойєра-Мура.

#### Загальний висновок
Найшвидшим алгоритмом для пошуку підрядка у рядку в даних тестах став алгоритм Бойєра-Мура. Втім, важливо зазначити, що результати базуються на тестуванні за типовим сценарієм. У найгірших випадках алгоритм Бойєра-Мура може бути менш ефективним через теоретичну часову складність. Згідно з нею, найкращі показники у найгіршому випадку демонструє алгоритм Кнута-Морріса-Пратта. Для глибшого аналізу поведінки алгоритмів у найгірших умовах слід провести тести на спеціально підібраних текстах та патернах, які створюють складні умови для кожного з алгоритмів.
