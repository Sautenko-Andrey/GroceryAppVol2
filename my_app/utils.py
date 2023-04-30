import json
from .templatetags.my_app_tags import *
from .items_full_names import *

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
    clear_list = tuple(x for x in prices_array if type(x[1]) == float)
    # определяем лучшую цену
    # проверяем пуст списо с ценами или нет
    value_only=[]
    for i in clear_list:
        value_only.append(i[1])

    if len(value_only)>0:
        best_price = min(value_only)
    else:
        best_price = 0

    respond = '---'
    for index,value in enumerate(prices_array):

        if value[1] == best_price:
            respond = f'{value[0]} {best_price} грн'

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

class ContextSupervisor:

    '''Класс, благодаря которму убирается дублирование кода в context_dict
    для отвтеов по фото и тексту.'''

    ATB_WARNING_MESSAGE = 'Цена в АТБ отсутствует в БД.'
    EKO_WARNING_MESSAGE = 'Цена в EKO отсутствует в БД.'
    VARUS_WARNING_MESSAGE = 'Цена в Varus отсутствует в БД.'
    SILPO_WARNING_MESSAGE = 'Цена в Сильпо отсутствует в БД.'
    ASHAN_WARNING_MESSAGE = 'Цена в Ашане отсутствует в БД.'
    NOVUS_WARNING_MESSAGE = 'Цена в Novus отсутствует в БД.'
    METRO_WARNING_MESSAGE = 'Цена в Metro отсутствует в БД.'
    NK_WARNING_MESSAGE = 'Цена в Наш Край отсутствует в БД.'
    FOZZY_WARNING_MESSAGE = 'Цена в Fozzy отсутствует в БД.'

    def getting_prices(self,item_sample_DB:str):
        '''Метод, который пытается взять цену из БД. Возвращаемые значения уже передаются в метод
        products_context_maker для дальнейшей обработки.'''

        #инициализируем переменные с ценами
        atb_price, eko_price, varus_price, silpo_price, ashan_price,novus_price,\
        metro_price,nk_price,fozzy_price = 0,0,0,0,0,0,0,0,0

        #пробуем вытянуть цену в АТБ из БД
        try:
            atb_price = store[item_sample_DB]['atb']
        except Exception:
            print(self.ATB_WARNING_MESSAGE)

        # пробуем вытянуть цену в ЭКО из БД
        try:
            eko_price = store[item_sample_DB]['eko']
        except Exception:
            print(self.EKO_WARNING_MESSAGE)

        # пробуем вытянуть цену в Варусе из БД
        try:
            varus_price = store[item_sample_DB]['varus']
        except Exception:
            print(self.VARUS_WARNING_MESSAGE)

        # пробуем вытянуть цену в Сильпо из БД
        try:
            silpo_price = store[item_sample_DB]['silpo']
        except Exception:
            print(self.SILPO_WARNING_MESSAGE)

        # пробуем вытянуть цену в Ашане из БД
        try:
            ashan_price = store[item_sample_DB]['ashan']
        except Exception:
            print(self.ASHAN_WARNING_MESSAGE)

        # пробуем вытянуть цену в Novus из БД
        try:
            novus_price = store[item_sample_DB]['novus']
        except Exception:
            print(self.NOVUS_WARNING_MESSAGE)

        # пробуем вытянуть цену в Metro из БД
        try:
            metro_price = store[item_sample_DB]['metro']
        except Exception:
            print(self.METRO_WARNING_MESSAGE)

        # пробуем вытянуть цену в Нашем Крае из БД
        try:
            nk_price = store[item_sample_DB]['nash_kray']
        except Exception:
            print(self.NK_WARNING_MESSAGE)

        # пробуем вытянуть цену в Fozzy из БД
        try:
            fozzy_price = store[item_sample_DB]['fozzy']
        except Exception:
            print(self.FOZZY_WARNING_MESSAGE)

        return atb_price,eko_price,varus_price, silpo_price, ashan_price,\
               novus_price, metro_price, nk_price,fozzy_price


    def __init__(self,nn_respond):
        '''Сразу же формируем цены при инициализации объекта класса'''
        self.atb_price, self.eko_price, self.varus_price,\
        self.silpo_price, self.ashan_price, self.novus_price,\
        self.metro_price, self.nk_price, self.fozzy_price = self.products_context_maker(nn_respond)


    def products_context_maker(self,nn_respond):
        '''Функия, в которой для каждого продукта собираются цены из БД,
        в зависимости от ответаа НС(ответ НС является аргументом этого метода).
        Для продуктов, у которых пока что нет цены, результат возвращается
        в виде кортежа с нулями для всех магазинов.'''

        result = ''
        no_prices = (0,0,0,0,0,0,0,0,0)
        if nn_respond == BEER_OBOLON_PREMIUM_EXTRA_1_1_L:
            result = self.getting_prices('obolon_premium_1.1_l')
        elif nn_respond == VODKA_HETMAN_ICE_07_L:
            result = self.getting_prices('vodka_hetman_ice_07')
        elif nn_respond == COFFEE_AROMA_GOLD_CLASSIC_100_GR:
            result = self.getting_prices('coffee_aroma_gold')
        elif nn_respond == COCA_COLA_2_L:
            result = self.getting_prices('coca_cola_2l')
        elif nn_respond == SIROK_PLAVLENIY_KOMO_PAPRIKASH:
            result = self.getting_prices('sir_plavlenniy_komo_paprikash')
        elif nn_respond == GARLIK:
            result = self.getting_prices('garlik')
        elif nn_respond == KENT_8:
            result = self.getting_prices('sigarets_kent_8')
        elif nn_respond == TEA_MINUTKA_40_BAGS:
            result = self.getting_prices('tea_minutka')
        elif nn_respond == SUN_OIL_SHEDRIY_DAR_RAFINIR_580_GR:
            result = self.getting_prices('oil_shedriy_dar_raf_850')
        elif nn_respond == ONION:
            result = self.getting_prices('onion')
        elif nn_respond == FAIRY_LIMON_500_GR:
            result = self.getting_prices('fairy_limon_500')
        elif nn_respond == APPLE_BLACK_PRINCE:
            result = self.getting_prices('apple_black_prince')
        elif nn_respond == MUSTARD_KOLOS:
            result = no_prices


        return result








