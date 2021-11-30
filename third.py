import numpy as np

# Инициализация генеротора случайных чисел
np.random.seed(100)


def calculations(k, lambda_, mu):
    # Количество повторов в методе Монте-Карло
    n_rep = 100
    # Вероятность блокировки
    p_refuse = 0
    # Имитационное моделирование
    m = 0
    while 1:
        for i in range(n_rep):
            # текущий размер очереди
            queue = 0
            # Количество пакетов
            n_packets = 1000
            # Текущее время
            t = 0
            # время, когда прибор освободится

            t_free = []
            for j in range(k):
                t_free.append(0)
            # Количество потярянных пактеов
            n_lost = 0
            for f in range(n_packets):
                # время поступления нового пакета
                t += np.random.exponential(scale=1 / lambda_)
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
        p_refuse /= n_rep
        if p_refuse < 0.0001:
            break
        else:
            m += 1
            p_refuse = 0

    # Оценка вероятности блокировки
    return p_refuse, m + 1


# Количество концентраторов
k_ = 2

# Интенсивность потока
mu_ = 2400 / 1200

lambda_day = 2
lambda_night = 0.5
p_day, b_day = calculations(k_, lambda_day, mu_)
p_night, b_night = calculations(k_, lambda_night, mu_)

print('Вероятность отказа днём: ' + str(p_day) + ' < 0.0001')
print('Размер буфера днём: ' + str(b_day))
print('Вероятность отказа ночью: ' + str(p_night) + ' < 0.0001')
print('Размер буфера ночью: ' + str(b_night))
