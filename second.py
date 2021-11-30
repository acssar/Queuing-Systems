import numpy as np
import random


def alg(lambda_day, n_packets):
    # Количество концентраторов
    k = 2
    # Инициализация генеротора случайных чисел
    np.random.seed(100)
    # Вероятность блокировки
    p_refuse = 0
    # Количество повторов в методе Монте-Карло
    n_rep = 50
    # Имитационное моделирование
    # Интенсивность выходного потока
    mu = 2
    for i in range(n_rep):

        # Текущее время
        t = 0
        # текущий размер очереди
        queue = 0
        # Максимальный размер очереди
        m = 6
        # время, когда прибор освободится
        t_free = []
        for j in range(k):
            t_free.append(0)
        # Количество потярянных пактеов
        n_lost = 0
        for f in range(n_packets):
            # время поступления нового пакета
            t += np.random.exponential(scale=1 / lambda_day)
            # проверяем, свободен ли концентратор
            n = 0
            if queue > 0:
                for j in range(k):
                    while t_free[j] < t and queue > 0:
                        t_free[j] += np.random.exponential(scale=1 / mu)
                        queue -= 1
            for h in range(k):
                if t_free[h] < t:
                    t_free[h] = t + np.random.exponential(scale=1 / mu)
                    break
                else:
                    n += 1
            if n == k:
                if queue < m:
                    queue += 1
                else:
                    n_lost += 1
        p_refuse += n_lost / n_packets
    return p_refuse


# Оценка вероятности блокировки
# Количество повторов в методе Монте-Карло
n_rep = 50
# Количество пакетов (3600 секунд в часе, интенсивность)
p_refuse1 = alg(2, 16 * 3600 * 2) / n_rep
p_refuse2 = alg(0.5, 4 * 3600) / n_rep
print('Вероятность отказа днём: ' + str(p_refuse1))
print('Вероятность отказа ночью: ' + str(p_refuse2))
