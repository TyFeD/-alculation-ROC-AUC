import numpy as np
import pandas as pd

def check_decimal_places(num):
    """
        Функция для проверки кол-ва знаков дробной части.

        :rtype: int or float
        :param num: string. Введенное с клавиатуры число - ответ/предсказание
    """
    if float(num) == 0.0:
        return num

    if float(num) % 1 == 0:  # для избежания ошибки в случае, когда дробная часть отсутствует
        return int(num)

    # взятие дробной части, как отдельного числа, и сравнение с максимально-возможным 6-ти значным числом
    if float(num.split('.')[1]) < 999999:
        return float(num)

def get_sampels(n):
    """
        Функция-загрузчик. Принимает на вход значения параметров и конвертирует их в pd.DataFrame

        :rtype: DataFrame
        :param n: int. введенное с клавиатуры число - число объектов в выборке
    """
    data = []
    for i in range(n):
        # пропущена проверка на то, что дробная часть < 6-ти знаков
        true_sample, predict_sample = map(float, input().split())
        data += [[true_sample, predict_sample]]
        # if check_decimal_places(true_sample) and check_decimal_places(predict_sample) != 0:
        #     data += [[float(true_sample), float(predict_sample)]]

    df = pd.DataFrame(data, columns=['True', 'Predict'])
    df = df.sort_values(by='True', ignore_index=True)
    df = np.array(df, dtype=float)
    # возвращение сортированного по True массива
    return df

def calculated_roc_auc(n):
    df = get_sampels(n)
    flag_1 = flag_2 = 0

    # for i in range(n):
    #     for j in range(i, n):
    #         if df['True'][i] < df['True'][j]:
    #             flag_1 += 1
    #             if df['Predict'][i] < df['Predict'][j]:
    #                 flag_2 += 1
    #             if df['Predict'][i] == df['Predict'][j]:
    #                 flag_2 += 0.5

    for i in range(n):
        for j in range(i, n):
            if df['True'][i] < df['True'][j]:
                flag_1 += 1
                if df['Predict'][i] < df['Predict'][j]:
                    flag_2 += 1
                if df['Predict'][i] == df['Predict'][j]:
                    flag_2 += 0.5

    roc_auc = flag_2/flag_1

    return roc_auc


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    n = int(input())

    if 2 <= n <= 100000:
        print(calculated_roc_auc(n))

