import random
import time


def search_elem_list(numerical_limit: int):
    lista = [i for i in range(numerical_limit)]
    time_begin_list = time.time()
    result = None
    for index in lista:
        if lista[index] == random.randint(0, numerical_limit):
            result = lista[index]
            break
    time_finish_list = time.time()
    temporal_dif_list = 1e6 * (time_finish_list - time_begin_list)
    print('The list has wasted {} microsecs searching an element'.format(temporal_dif_list))
    return result


def search_elem_set(numerical_limit: int):
    set = {i for i in range(numerical_limit)}
    set_target = random.randint(0, numerical_limit) in set
    time_begin_set = time.time()
    set_value = set_target
    time_finish_set = time.time()
    dif_temporal_set = 1e6 * (time_finish_set - time_begin_set)
    print('The set has wasted {} microsecs searching an element'.format(dif_temporal_set))


def search_elem_dicc(numerical_limit: int):
    values = ['value1']
    mydict = {"key " + str(i): values[0] for i in range(numerical_limit)}
    for i in range(numerical_limit):
        mydict['key' + str(i)] = random.randrange(numerical_limit)
    key_target = 'key {}'.format(random.randint(0, numerical_limit))
    time_begin_dict = time.time()
    dicc_value = mydict.get(key_target)
    time_finish_dict = time.time()
    dif_temporal_dict = 1e6 * (time_finish_dict - time_begin_dict)
    print('The dict has wasted {} microsecs searching an element'.format(dif_temporal_dict))
