# Queuing-Systems
## NSU course of theoretical probability and mathematical statistics
### Все описания также есть в Jypyter Notebook файле

#### 1. Определить вероятность блокировки пакета днем и ночью, если входной и выходной поток являются пуассоновскими

Используем формулу для подсчета вероятности отказа многоканальной СМО с очередью нам даны:  
* количество концентраторов - 2  
* интенсивность днём - 2   
* и ночью - 0.5  
* максимальный размер очереди (размер буфера 7 минус 1) = 6  
* выходная интенсивность (скорость передачи, деленная на среднюю длину пакета 2400/1200) = 2  
Вероятность отказа днём: 0.0026109660574412533  
Вероятность отказа ночью: 9.271833754537287e-08

#### 2. Определить вероятность блокировки пакета в задаче 1, используя метод Монте-Карло. Сравнить результаты

Исходные данные те же, количество пакетов рассчитываем так: по условию день - 16 часов, ночь - 8 часов мы переводим это в секунды и умножаем на соответсвующую интенсивность. Повторы берем так, чтобы слишком долго не считало =), но чем больше повторов - тем больше точность  
Вероятность отказа днём: 0.002669791666666666  
Вероятность отказа ночью: 0.0  

Вероятность отказа днём сходится, а ночью метод Монте-Карло выдаёт нулевую, потому что проверок слишком мало, она стремится к нулю, надо хотя бы ~миллион проверок

#### 3. Определить оптимальный размер буфера, чтобы вероятность блокировки пакета не превышала 0.0001
В третьем пункте считается по циклу, наращивая очередь (это буфер декрементированный на единицу, т.е. B - 1) пока вероятность не станет меньше 0.0001
Можно добавить цикл к 1-му пункту или 2-му, возьмём второй за основу  
Получается, что днём надо взять буфер 12 (очередь = 11), а ночью 4 (очередь = 3)  
Вероятность отказа днём: 6e-05 < 0.0001  
Размер буфера днём: 12  
Вероятность отказа ночью: 1e-05 < 0.0001  
Размер буфера ночью: 4  