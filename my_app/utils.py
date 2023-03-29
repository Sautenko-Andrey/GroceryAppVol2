import json

with open('/home/andrey/GroceryAppVol2/FBApp/my_app/prices_store.json') as f:
    store = json.load(f)


class MutualContext:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context


def make_list(count, pos):
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    res = [[0 for x in range(count)]]
    res[0][pos] = 1
    return res


def price_updating_data(price):
    price = price[:5]
    try:
        price = float(price.replace(',', '.'))
    except Exception:
        print('Короткая цена!')
        price = float(price[:2])
    return price


def get_prices_for_set(names_list: list):
    '''Метод, формирующий списки цен для продуктовых наборов,
    которые собирает пользователь.'''
    out_of_stoke='нет'
    atb_list = []
    eko_list = []
    varus_list = []
    silpo_list = []
    ashan_list = []
    novus_list = []
    metro_list = []
    nash_kray_list = []
    fozzy_list = []
    for name in names_list:
        if name == 'Пиво "Оболонь Премиум Экстра 1,1 л"':
            # atb = store['eggs']['atb']
            atb_list.append(store['obolon_premium_1.1_l']['atb'])
            # eko = store['eggs']['eko']
            eko_list.append(store['obolon_premium_1.1_l']['eko'])
            varus_list.append(out_of_stoke)
            silpo_list.append(out_of_stoke)
            ashan_list.append(out_of_stoke)
            novus_list.append(out_of_stoke)
            metro_list.append(out_of_stoke)
            nash_kray_list.append(out_of_stoke)
            fozzy_list.append(out_of_stoke)

        elif name=='Водка "Гетьман ICE 0,7 л"':
            atb_list.append(store['vodka_hetman_ice_07']['atb'])
            eko_list.append(out_of_stoke)
            varus_list.append(out_of_stoke)
            silpo_list.append(out_of_stoke)
            ashan_list.append(out_of_stoke)
            novus_list.append(out_of_stoke)
            metro_list.append(out_of_stoke)
            nash_kray_list.append(out_of_stoke)
            fozzy_list.append(out_of_stoke)

        elif name == 'Напиток Sprite 2 литра':
            atb_list.append(out_of_stoke)
            eko_list.append(store['sprite_2l']['eko'])
            varus_list.append(store['sprite_2l']['varus'])
            silpo_list.append(store['sprite_2l']['silpo'])
            ashan_list.append(store['sprite_2l']['ashan'])
            novus_list.append(store['sprite_2l']['novus'])
            metro_list.append(store['sprite_2l']['metro'])
            nash_kray_list.append(store['sprite_2l']['nash_kray'])
            fozzy_list.append(store['sprite_2l']['fozzy'])

        elif name == 'Сигареты Kent Silver':
            atb_list.append(store['kent_silver']['atb'])
            eko_list.append(store['kent_silver']['eko'])
            varus_list.append(store['kent_silver']['varus'])
            silpo_list.append(out_of_stoke)
            ashan_list.append(store['kent_silver']['ashan'])
            novus_list.append(store['kent_silver']['novus'])
            metro_list.append(out_of_stoke)
            nash_kray_list.append(out_of_stoke)
            fozzy_list.append(store['kent_silver']['fozzy'])


        elif name == 'Кофе "Арома Голд Классик 100 гр"':
            atb_list.append(out_of_stoke)
            eko_list.append(store['coffee_aroma_gold']['eko'])
            varus_list.append(out_of_stoke)
            silpo_list.append(out_of_stoke)
            ashan_list.append(out_of_stoke)
            novus_list.append(out_of_stoke)
            metro_list.append(out_of_stoke)
            nash_kray_list.append(out_of_stoke)
            fozzy_list.append(store['coffee_aroma_gold']['fozzy'])

    return atb_list,eko_list,varus_list,silpo_list,ashan_list,\
           novus_list,metro_list,nash_kray_list,fozzy_list






def define_markets_names(collection: list):
    new_collection = []
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
