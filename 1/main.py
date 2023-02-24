def task_1(geo_logs):
    # Дан список с визитами по городам и странам.
    # Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."

    result = []
    for visit in geo_logs:
        for key, value in visit.items():
            if value[1].lower() == 'россия':
                result.append({key: value})

    return result


def task_2(ids):
    # Выведите на экран все уникальные гео-ID из значений словаря ids.
    # Т.е. список вида [213, 15, 54, 119, 98, 35]
    
    all_ids = []

    for id, value in ids.items():
        all_ids += value

    unique_ids = list(set(all_ids))
    return unique_ids


def task_3(queries):
    # Дан список поисковых запросов.
    # Получить распределение количества слов в них.
    # Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

    count_queries = len(queries)
    count = dict()

    for query in queries:
        words_key = query.count(' ') + 1
        count.setdefault(words_key, 0)
        count[words_key] += 1

    result = {}
    for key, value in count.items():
        percent = round(value / count_queries * 100, 2)
        result[key] = percent

    return result


if __name__ == '__main__':
    pass
