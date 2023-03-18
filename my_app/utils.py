class MutualContext:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

def make_list(count,pos):
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    res=[[0 for x in range(count)]]
    res[0][pos]=1
    return res


def price_updating_data(price):
    price = price[:5]
    try:
        price = float(price.replace(',', '.'))
    except Exception:
        print('Короткая цена!')
        price=float(price[:2])
    return price


def define_markets_names(collection: list):
    new_collection=[]
    for index, value in enumerate(collection):
        if collection[index] == True and index == 0:
            collection[index] = 'ATB'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 1:
            collection[index] = 'EKO'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 2:
            collection[index] = 'Varus'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 3:
            collection[index] = 'Silpo'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 4:
            collection[index] = 'Ashan'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 5:
            collection[index] = 'Novus'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 6:
            collection[index] = 'Metro'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 7:
            collection[index] = 'Nash Kray'
            new_collection.append(collection[index])
        elif collection[index] == True and index == 8:
            collection[index] = 'Fozzy'
            new_collection.append(collection[index])
    print(new_collection)
    return new_collection