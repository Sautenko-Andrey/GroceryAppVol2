import json
from .templatetags.my_app_tags import *

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

def best_price_identify(prices_array:list):
    '''В prices_array нам поступают все цены из БД.А нам надо определить
    минимальную из тех маркетов, которые выбрал пользователь.'''
    #очищаем от цен, которых нет в магазине
    clear_list=tuple(x for x in prices_array if type(x) == float)
    #определяем лучшую цену
    #проверяем пуст списо с ценами или нет
    if len(clear_list)>0:
        best_price=min(clear_list)
    else:
        best_price=0

    global respond
    for index,value in enumerate(prices_array):
        if value==best_price and index==0:
            respond=('atb',value)
        elif value == best_price and index==1:
            respond=('eko',value)
        elif value == best_price and index==2:
            respond = ('varus',value)
        elif value == best_price and index==3:
            respond = ('silpo',value)
        elif value == best_price and index==4:
            respond = ('ashan',value)
        elif value == best_price and index==5:
            respond = ('novus',value)
        elif value == best_price and index==6:
            respond = ('metro',value)
        elif value == best_price and index==7:
            respond = ('nash_kray',value)
        elif value == best_price and index==8:
            respond = ('fozzy',value)

    # print(prices_array)
    # print(clear_list)
    # print(best_price)
    # print(respond)
    return respond

def get_products_prices(respond:str):
    '''Функция, обрабатывающая результат работы НС и выдающая цены для продуктов'''
    out_of_stoke='нет'
    global atb_price,eko_price,varus_price,silpo_price,\
        ashan_price,novus_price,metro_price,nash_kray_price,fozzy_price,picture
    match respond:
        case 'Пиво "Оболонь Премиум Экстра 1,1 л"':
            picture=get_obolon_premium
            atb_price = store['obolon_premium_1.1_l']['atb']
            eko_price = store['obolon_premium_1.1_l']['eko']
            varus_price = out_of_stoke
            silpo_price = out_of_stoke
            ashan_price = out_of_stoke
            novus_price = out_of_stoke
            metro_price = out_of_stoke
            nash_kray_price = out_of_stoke
            fozzy_price = out_of_stoke

        case 'Водка "Гетьман ICE 0,7 л"':
            picture = get_hetman_ICE
            atb_price = store['vodka_hetman_ice_07']['atb']
            eko_price = out_of_stoke
            varus_price = out_of_stoke
            silpo_price = out_of_stoke
            ashan_price = out_of_stoke
            novus_price = out_of_stoke
            metro_price = out_of_stoke
            nash_kray_price = out_of_stoke
            fozzy_price = out_of_stoke

        case 'Напиток Sprite 2 литра':
            picture = get_sprite_2l
            atb_price = out_of_stoke
            eko_price = store['sprite_2l']['eko']
            varus_price = store['sprite_2l']['varus']
            silpo_price = store['sprite_2l']['silpo']
            ashan_price = store['sprite_2l']['ashan']
            novus_price = store['sprite_2l']['novus']
            metro_price = store['sprite_2l']['metro']
            nash_kray_price = store['sprite_2l']['nash_kray']
            fozzy_price = store['sprite_2l']['fozzy']

        case 'Сигареты Kent Silver':
            picture = get_kent_silver
            atb_price = store['kent_silver']['atb']
            eko_price = store['kent_silver']['eko']
            varus_price = store['kent_silver']['varus']
            silpo_price = out_of_stoke
            ashan_price = store['kent_silver']['ashan']
            novus_price = store['kent_silver']['novus']
            metro_price = out_of_stoke
            nash_kray_price = out_of_stoke
            fozzy_price = store['kent_silver']['fozzy']

        case 'Кофе "Арома Голд Классик 100 гр"':
            picture = coffe_aroma_gold_classic_100gr
            atb_price = out_of_stoke
            eko_price = store['coffee_aroma_gold']['eko']
            varus_price = out_of_stoke
            silpo_price=out_of_stoke
            ashan_price=out_of_stoke
            novus_price=out_of_stoke
            metro_price=out_of_stoke
            nash_kray_price=out_of_stoke
            fozzy_price=store['coffee_aroma_gold']['fozzy']

    return atb_price,eko_price,varus_price,silpo_price,ashan_price,\
           novus_price,metro_price,nash_kray_price,fozzy_price,picture


prices=[101.56, 35.87, 89.99]
my_test=best_price_identify(prices)