import json
from .templatetags.my_app_tags import *
from .items_full_names import *

try:
    with open('/home/andrey/GroceryAppVol2/FBApp/my_app/prices_store.json') as f:
        store = json.load(f)
except Exception:
    print("I can't open data base with prices. Check path:"
          " '/home/andrey/GroceryAppVol2/FBApp/my_app/prices_store.json'")


class MutualContext:
    def get_user_context(self, **kwargs)->dict:
        context = kwargs
        return context


def make_list(count:int, pos:int) -> list:
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    #проверяем аргументы на принадлежность к типу int:
    if type(count) != int or type(pos) != int:
        raise TypeError("Arguments count and pos for function 'make_list' must be int!")
    #создаем вложенный список:
    res = [[0 for x in range(count)]]
    res[0][pos] = 1
    return res


def price_updating_data(price:float) -> float:
    '''Функция для корректировки отображения нестандартных записей цен на сайтах'''

    #делаем проверку, что аргумент price является вещественным числом
    if type(price) != float:
        raise TypeError("Argument price for function 'price_updating_data' must be float")

    price = price[:5]
    try:
        price = float(price.replace(',', '.'))
    except Exception:
        print('Короткая цена!')
        price = float(price[:2])
    return price


def best_price_identify(prices_array:list) -> str:
    '''В prices_array нам поступают все цены из БД.А нам надо определить
    минимальную из тех маркетов, которые выбрал пользователь.'''

    #проверяем, что на вход функция получает список:
    if type(prices_array) != list:
        raise TypeError("Argument for function 'best_price_identify' must be list!")

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


class ContextSupervisor:
    '''Класс, благодаря которму убирается дублирование кода в context_dict
    для отвтеов по фото и тексту.'''

    #сообщения об отсутствии цены в БД.
    ATB_WARNING_MESSAGE = 'Цена в АТБ отсутствует в БД.'
    EKO_WARNING_MESSAGE = 'Цена в EKO отсутствует в БД.'
    VARUS_WARNING_MESSAGE = 'Цена в Varus отсутствует в БД.'
    SILPO_WARNING_MESSAGE = 'Цена в Сильпо отсутствует в БД.'
    ASHAN_WARNING_MESSAGE = 'Цена в Ашане отсутствует в БД.'
    NOVUS_WARNING_MESSAGE = 'Цена в Novus отсутствует в БД.'
    METRO_WARNING_MESSAGE = 'Цена в Metro отсутствует в БД.'
    NK_WARNING_MESSAGE = 'Цена в Наш Край отсутствует в БД.'
    FOZZY_WARNING_MESSAGE = 'Цена в Fozzy отсутствует в БД.'

    #переменные-ключи для маркетов
    __ATB_KEY = 'atb'
    __EKO_KEY = 'eko'
    __VARUS_KEY = 'varus'
    __SILPO_KEY = 'silpo'
    __ASHAN_KEY = 'ashan'
    __NOVUS_KEY = 'novus'
    __METRO_KEY = 'metro'
    __NK_KEY = 'nash_kray'
    __FOZZY_KEY = 'fozzy'

    #флаг, означающий, что для товара нет парсеров и цен в БД
    NO_PRICES = 'absent'

    #минимальная длина строки метки из БД
    __MIN_SAMPLE_LENGTH = 3

    #флаг для проверки существования тэга
    __NO_TAG = True

    @classmethod
    def __verify_sample(cls, sample):
        """Метод, выполняющий проверку корректности метки продукта в БД."""
        if type(sample) != str:
            raise TypeError("Sample has to be str type!")
        if len(sample) < cls.__MIN_SAMPLE_LENGTH:
            raise TypeError("Product's sample length is suspicious short!")

    @classmethod
    def __verify_tag(cls, tag):
        '''Метод проверяющий корректность тэга (его существование)'''
        if not cls.__NO_TAG:
            raise AttributeError("Tag absents!")

    def getting_prices(self,item_sample_DB, item_tag):
        '''Метод, который пытается взять цену из БД.
        Также подключается тег продукта (тег , который берет изображение и текст описания товара из БД).
        Возвращаемые значения уже передаются в метод
        products_context_maker для дальнейшей обработки.'''

        #совершаем проверку метки из БД как аргумента
        self.__verify_sample(item_sample_DB)

        #сделаем проверку существования тэга
        self.__verify_tag(item_tag)

        # делаем проверку, что если цены отсутствуют(не имееются парсеры на цены),то мы возвращаем нули
        if item_sample_DB == self.NO_PRICES:
            #инициализируем переменные с ценами
            atb_price, eko_price, varus_price, silpo_price, ashan_price,novus_price,\
            metro_price,nk_price,fozzy_price = 0, 0, 0, 0, 0, 0, 0, 0, 0

        else:
            atb_price, eko_price, varus_price, silpo_price, ashan_price, novus_price, \
            metro_price, nk_price, fozzy_price = 0, 0, 0, 0, 0, 0, 0, 0, 0
            #пробуем вытянуть цену в АТБ из БД
            try:
                atb_price = store[item_sample_DB][self.__ATB_KEY]
            except Exception:
                print(self.ATB_WARNING_MESSAGE)

            # пробуем вытянуть цену в ЭКО из БД
            try:
                eko_price = store[item_sample_DB][self.__EKO_KEY]
            except Exception:
                print(self.EKO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Варусе из БД
            try:
                varus_price = store[item_sample_DB][self.__VARUS_KEY]
            except Exception:
                print(self.VARUS_WARNING_MESSAGE)

            # пробуем вытянуть цену в Сильпо из БД
            try:
                silpo_price = store[item_sample_DB][self.__SILPO_KEY]
            except Exception:
                print(self.SILPO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Ашане из БД
            try:
                ashan_price = store[item_sample_DB][self.__ASHAN_KEY]
            except Exception:
                print(self.ASHAN_WARNING_MESSAGE)

            # пробуем вытянуть цену в Novus из БД
            try:
                novus_price = store[item_sample_DB][self.__NOVUS_KEY]
            except Exception:
                print(self.NOVUS_WARNING_MESSAGE)

            # пробуем вытянуть цену в Metro из БД
            try:
                metro_price = store[item_sample_DB][self.__METRO_KEY]
            except Exception:
                print(self.METRO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Нашем Крае из БД
            try:
                nk_price = store[item_sample_DB][self.__NK_KEY]
            except Exception:
                print(self.NK_WARNING_MESSAGE)

            # пробуем вытянуть цену в Fozzy из БД
            try:
                fozzy_price = store[item_sample_DB][self.__FOZZY_KEY]
            except Exception:
                print(self.FOZZY_WARNING_MESSAGE)

        #подключение тега для продукта
        info = item_tag

        return atb_price,eko_price,varus_price, silpo_price, ashan_price,\
               novus_price, metro_price, nk_price,fozzy_price, info


    def __init__(self,nn_respond):
        '''Сразу же формируем цены и инфо продукта при инициализации объекта класса'''
        self.atb_price, self.eko_price, self.varus_price,\
        self.silpo_price, self.ashan_price, self.novus_price,\
        self.metro_price, self.nk_price, self.fozzy_price, self.info= self.products_context_maker(nn_respond)


    def products_context_maker(self,nn_respond):
        '''Функия, в которой для каждого продукта собираются цены из БД,
        в зависимости от ответа НС(ответ НС является аргументом этого метода).
        Для продуктов, у которых пока что нет цены, результат возвращается
        в виде кортежа с нулями для всех магазинов.'''

        #проверяем на корректность ответ НС
        self.__verify_sample(nn_respond)

        if nn_respond == BEER_OBOLON_PREMIUM_EXTRA_1_1_L:
            result = self.getting_prices('obolon_premium_1.1_l',get_obolon_premium)
        elif nn_respond == VODKA_HETMAN_ICE_07_L:
            result = self.getting_prices('vodka_hetman_ice_07',get_hetman_ICE)
        elif nn_respond == COFFEE_AROMA_GOLD_CLASSIC_100_GR:
            result = self.getting_prices('coffee_aroma_gold',coffe_aroma_gold_classic_100gr)
        elif nn_respond == COCA_COLA_2_L:
            result = self.getting_prices('coca_cola_2l',get_coca_cola_2l)
        elif nn_respond == SIROK_PLAVLENIY_KOMO_PAPRIKASH:
            result = self.getting_prices('sir_plavlenniy_komo_paprikash',get_KOMO_paprikash)
        elif nn_respond == GARLIK:
            result = self.getting_prices('garlik',get_garlik)
        elif nn_respond == KENT_8:
            result = self.getting_prices('sigarets_kent_8',get_sigarets_kent_8)
        elif nn_respond == TEA_MINUTKA_40_BAGS:
            result = self.getting_prices('tea_minutka',get_tea_minutka_black_40_b)
        elif nn_respond == SUN_OIL_SHEDRIY_DAR_RAFINIR_580_GR:
            result = self.getting_prices('oil_shedriy_dar_raf_850',get_oil_shedriy_dar_085l)
        elif nn_respond == ONION:
            result = self.getting_prices('onion',get_onion)
        elif nn_respond == FAIRY_LIMON_500_GR:
            result = self.getting_prices('fairy_limon_500',get_fairy_500_lime)
        elif nn_respond == APPLE_BLACK_PRINCE:
            result = self.getting_prices('apple_black_prince',get_apple_black_prince)
        elif nn_respond == MUSTARD_KOLOS:
            result = self.getting_prices(self.NO_PRICES,get_gorchica_kolos)
        elif nn_respond == SMETANA_STOLICA_SMAKY_20PER_400_GR:
            result = self.getting_prices('smetana_stol_smaky_20%',get_smetana_stolica_smaky_20_400gr)
        elif nn_respond == LEMON:
            result = self.getting_prices('limon',get_limon)
        elif nn_respond == SUN_OIL_OLEYNA_NERAF_850_GR:
            result = self.getting_prices('oil_oleyna_neraf_850',get_oil_oleyna_neraf_850)
        elif nn_respond == BEER_LVIVSKE_SVITLE_2_4_L:
            result = self.getting_prices('beer_lvivske_svetl_2.4 l',get_pivo_lvivske_svitle)
        elif nn_respond == SHAVING_FOAM_ARKO_COOL_200_MLG:
            result = self.getting_prices('arko_cool_200',get_arko_cool_300_100)
        elif nn_respond == SHAVING_FOAM_ARKO_SENSITIVE_200_MLG:
            result = self.getting_prices('arko_sensitive_200',get_arko_sensitive_300_100)
        elif nn_respond == CARROT:
            result = self.getting_prices('carrot',get_carrot)
        elif nn_respond == DROJJI_HARKOV_100_GR:
            result = self.getting_prices(self.NO_PRICES,get_drojji_hark)
        elif nn_respond == EGGS:
            result = self.getting_prices('eggs',get_chicken_eggs)
        elif nn_respond == DESODORANT_GARNIER_MAGNIY_MEN:
            result = self.getting_prices('desodorant_garnier_man',get_dezodorant_garnier_magniy_m)
        elif nn_respond == CABBAGE:
            result = self.getting_prices('cabbage',get_cabbage)
        elif nn_respond == MARLBORO_RED:
            result = self.getting_prices('marlboro_red',get_marlboro_red)
        elif nn_respond == MAYONES_DETSKIY_SHEDRO_67:
            result = self.getting_prices('mayonez_detsk_shedro_67%',get_mayonez_dom_detsk_shedro_67)
        elif nn_respond == DESODORANT_REXONA_ALOE_VERA_WOMEN:
            result = self.getting_prices('rexona_aloe_vera',get_reksona_aloe_vera_w)
        elif nn_respond == SMETANA_STOLICA_SMAKY_15_400_GR:
            result = self.getting_prices('smetana_stol_smaky_15%',get_smetana_stol_smaku_400_15)
        elif nn_respond == TEA_MONOMAH_KENYA_BLACK_90_GR:
            result = self.getting_prices('tea_monomah_kenya_90',get_tea_monomah_kenya)
        elif nn_respond == TOILET_PAPER_KIEV_63_M:
            result = self.getting_prices(self.NO_PRICES,get_toilet_papir_kiev_63m)
        elif nn_respond == TEA_MONOMAH_CEYLON_BLACK:
            result = self.getting_prices(self.NO_PRICES,get_tea_monomah_ceylon_black)
        elif nn_respond == COFFEE_AROMA_GOLD_FREEZE_FRIED_70_GR:
            result = self.getting_prices('cofee_aroma_gold_freeze_dried_70g',get_coffee_aroma_gold_freeze_dried_70)
        elif nn_respond == MUSTARD_VERES_UKRAINSKA_MICNA_120_GR:
            result = self.getting_prices('gorchica_veres_ukrainska_micna_120g',get_gorchica_veres_micna_ukr_120g)
        elif nn_respond == TEA_MONOMAH_100_CEYLON_ORIGINAL_BLACK_KRUPNOLIST:
            result = self.getting_prices(self.NO_PRICES,get_tea_monomah_original_ceylon_90g)
        elif nn_respond == DESODORANT_GARNIER_VESENNYA_SVEJEST:
            result = self.getting_prices('desodorant_garnier_spring_spirit',get_desodorant_garnier_spring_spirit)
        elif nn_respond == APPLE_GALA:
            result = self.getting_prices('apple_gala',get_apple_gala)
        elif nn_respond == SMETANA_GALICHANSKAYA_15_370_GR:
            result = self.getting_prices('smetana_galichanska_15_370gr',get_smetana_galichanska_15_370gr)
        elif nn_respond == CHIPS_SALT_BIG_PACK_30_GR:
            result = self.getting_prices('chips_lays_with_salt_big_pack',get_chips_lays_salt_big_pack_30g)
        elif nn_respond == SPRITE_2L:
            result = self.getting_prices('sprite_2l',get_sprite_2l)
        elif nn_respond == FANTA_2L:
            result = self.getting_prices('fanta_2l',get_fanta_2l)
        elif nn_respond == BOND_STREET_BLUE_SELECTION:
            result = self.getting_prices('bond_street_blue_selection',get_bond_street_blue_selection)
        elif nn_respond == CAMEL_BLUE:
            result = self.getting_prices('camel_blue',get_camel_blue)
        elif nn_respond == LD_RED:
            result = self.getting_prices('ld_red',get_ld_red)
        elif nn_respond == MARLBORO_GOLD:
            result = self.getting_prices('marlboro_gold',get_marlboro_gold)
        elif nn_respond == ROTHMANS_DEMI_BLUE_EXCLUSIVE:
            result = self.getting_prices('rothmans_demi_blue_exclusive',get_rothmans_demi_blue_exclusive)
        elif nn_respond == ROTHMANS_DEMI_CLICK_PURPLE:
            result = self.getting_prices('rothmans_demi_click_purple',get_rothmans_demi_click_purple)
        elif nn_respond == WINSTON_CASTER:
            result = self.getting_prices('winston_caster',get_winston_caster)
        elif nn_respond == PARLAMENT_AQUA_BLUE:
            result = self.getting_prices('parlament_aqua_blue',get_parlament_aqua_blue)
        elif nn_respond == WINSTON_BLUE:
            result = self.getting_prices('winston_blue',get_winston_blue)
        elif nn_respond == BOND_STREET_RED_SELECTION:
            result = self.getting_prices('bond_street_red_selection',get_bond_street_red_selection)
        elif nn_respond == LD_BLUE:
            result = self.getting_prices('ld_blue',get_ld_blue)
        elif nn_respond == KENT_SILVER:
            result = self.getting_prices('kent_silver',get_kent_silver)
        elif nn_respond == KENT_NAVY_BLUE_NEW:
            result = self.getting_prices('kent_navy_blue',get_kent_navi_blue_new)
        elif nn_respond == BEER_CHERNIGOVSKOE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_chernigivske_svitle_05_l_glass',get_beer_chernigivske_svitle_05_l_glass)
        elif nn_respond == BEER_STELLA_ARTOIS_05_L_GLASS:
            result = self.getting_prices('beer_stella_artois_05_l_glass',get_beer_stella_artois_05_l_glass)
        elif nn_respond == BEER_OBOLON_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_obolon_svitle_05_l_glass',get_beer_obolon_svitle_05_l_glass)
        elif nn_respond == BEER_JIGULIVSKE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_jugulivske_svitle_05_l_glass',get_beer_jigulivsle_svitle_05_l_glass)
        elif nn_respond == BEER_ROGAN_TRADICIYNE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_rogan_tradicionnoe_svitle_05_l_glass',get_beer_rogan_tradiciyne_svitle_05_l_glass)
        elif nn_respond == BEER_CORONA_EXTRA_SVITLE_033_L_GLASS:
            result = self.getting_prices('beer_corona_extra_svitle_033_l_glass',get_beer_corona_extra_svitle_033_l_glass)
        elif nn_respond == BEER_CHERNIGIVSKE_BILE_NEFILTER_05_L_GLASS:
            result = self.getting_prices('beer_chernigibske_bile_nefilter_05_l_glass',get_beer_chernigivske_bile_nefilter_05_l_glass)
        elif nn_respond == BEER_YANTAR_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_yantar_svitle_05_l_glass',get_beer_yantar_svitle_05_l_glass)
        elif nn_respond == BEER_ZIBERT_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_zibert_svitle_05_l_glass',get_beer_zibert_svitle_05_l_glass)
        elif nn_respond == BEER_ARSENAL_MICNE_05_L_GLASS:
            result = self.getting_prices('beer_arsenal_micne_05_l_glass',get_beer_arsenal_micne_05_l_glass)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_05_L_GLASS:
            result = self.getting_prices('beer_persha_brovarna_zakarpatske_svitle_05_l_glass',get_beer_persha_brovarna_zakarpatske_05_l_glass)
        elif nn_respond == BEER_LVIVSKE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_lvivske_svitle_05_l_glass',get_beer_lvivske_svitle_05_l_glass)
        elif nn_respond == BEER_LVIVSKE_1715_05_L_GLASS:
            result = self.getting_prices('beer_lvivske_1715_05_l_glass',get_beer_lvivske_1715_05_l_glass)
        elif nn_respond == BEER_ZLATA_PRAHA_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_zlata_praha_svitle_05_l_glass',get_beer_zlata_praha_05_l_glass)
        elif nn_respond == BEER_TUBORG_GREEN_05_L_GLASS:
            result = self.getting_prices('beer_tuborg_green_05_l_glass',get_beer_tuborg_green_05_l_glass)
        elif nn_respond == BEER_SLAVUTICH_ICE_MIX_LIME_05_L_GLASS:
            result = self.getting_prices('beer_slavutich_ice_mix_lime_05_l_glass',get_beer_slavutich_ice_mix_lime_05_l_glass)
        elif nn_respond == BEER_TETEREV_05_L_GLASS:
            result = self.getting_prices('beer_teteriv_svitle_05_l_glass',get_beer_teteriv_svitle_05_l_glass)
        elif nn_respond == BEER_KRUSOVICE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_krusovice_svitle_05_l_glass',get_beer_krusovice_svitle_05_l_glass)
        elif nn_respond == BEER_HEINEKEN_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_heineken_svitle_05_l_glass',get_beer_heineken_svitle_05_l_glass)
        elif nn_respond == BEER_AMSTEL_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_amstel_svitle_05_l_glass',get_beer_amstel_svitle_05_l_glass)
        elif nn_respond == BEER_HIKE_PREMIUM_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_hike_premium_svitle_05_l_glass',get_beer_hike_premium_05_l_glass)
        elif nn_respond == BEER_BOCHKOVE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_bochkove_svitle_05_l_glass',get_beer_bochkove_svitle_05_l_glass)
        elif nn_respond == BEER_KRONENBOURG_1664_BLANC_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_kronenbourg_1664_blanc_svitle_05_l_glass',get_beer_kronenbourg_1664_blanc_svitle_05_l_glass)
        elif nn_respond == BEER_OPILLYA_FIRMENNOE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_opilla_firmove_nepasterizovane_svitle_05_l_glass',get_beer_opilla_nepasterizovane_svitle_05_l_glass)
        elif nn_respond == BEER_YACHMENNIY_KOLOS_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_yachmenniy_kolos_svitle_05_l_glass',get_beer_yachmenniy_kolos_svitle_05_l_glass)
        elif nn_respond == BEER_OPILLYA_KORIFEY_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_opilla_korifey_svitle_05_l_glass',get_beer_opilla_korifey_svitle_05_l_glass)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_05_L_GLASS:
            result = self.getting_prices('beer_chaika_dniprovska_svitle_05_l_glass',get_beer_chaika_dneprovskaya_svitle_05_l_glass)
        elif nn_respond == BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_chaika_chernomorskaya_svitle_05_l_glass',get_beer_chaika_chernomorskaya_svitle_05_l_glass)
        elif nn_respond == BEER_UMAN_WAISSBURG_SVITLE_1_L:
            result = self.getting_prices('beer_uman_waissburg_1_l_svitle_plastic',get_beer_uman_waissburg_svitle_1_l_plastic)
        elif nn_respond == BEER_UMAN_PSHENICHNOE_SVITLE_1_L:
            result = self.getting_prices('beer_uman_pshenichnoe_1_l_svitle_plastic',get_beer_uman_pshenichnoe_svitle_1_l_plastic)
        elif nn_respond == BEER_BERDICHEVSKOE_HMELNOE_SVITLE_1_L:
            result = self.getting_prices('beer_berdichevske_hmilne_1_l_svitle_plastic',get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic)
        elif nn_respond == BEER_BERDICHEVSKOE_LAGER_SVITLE_1_L:
            result = self.getting_prices('beer_berdichevske_lager_1_l_svitle_plastic',get_beer_berdichevskoe_lager_svitle_1_l_plastic)
        elif nn_respond == BEER_OPILLYA_KORIFEY_11_L:
            result = self.getting_prices('beer_opilla_korifey_11_l_plastic',get_beer_opilla_korifey_11_l_plastic)
        elif nn_respond == BEER_OBOLON_JIGULIVSKE_EXPORTNE_15_L:
            result = self.getting_prices('beer_obolon_jigulivske_eksportne_15_l_plastic',get_beer_obolon_jigulivske_eksport_15_l_plastic)
        elif nn_respond == BEER_YANTAR_SVITLE_12_L:
            result = self.getting_prices('beer_yantar_svitle_12_l_plastic',get_beer_yantar_svitle_12_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_PSHENICHNOE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_pshenichne_nefiltr_1_l_plastic',get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_SVITLE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_svitle_nefiltr_1_l_plastic',get_beer_jashkovskoe_svitle_nefilter_1_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_JIGULIVSKE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_jigulivske_nefiltr_1_l_plastic',get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic)
        elif nn_respond == BEER_PPB_BOCHKOVE_1_L:
            result = self.getting_prices('beer_persha_privatna_brovarnya_bochkove_1_l_plastic',get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_1_L:
            result = self.getting_prices('beer_chayka_dniprovska_1_l_plastic',get_beer_chayka_dniprovska_1_l_plastic)
        elif nn_respond == KETCHUP_TORCHIN_CHESNOK_270_GR:
            result = self.getting_prices('ketchup_torchin_s_chasnikom_270gr',get_ketchup_torchin_s_chesnokom)
        elif nn_respond == MAYONES_KOROLIVSKIY_SMAK_KOROLIVSKIY_67_300_GR:
            result = self.getting_prices('mayonez_korolivskiy_smak_korolivskiy_67_300gr',get_mayonez_korolivkiy_smak_korolivskiy_67_300gr)
        elif nn_respond == MUKA_ZOLOTE_ZERNYATKO_PSHENICHNE_2_KG:
            result = self.getting_prices(self.NO_PRICES,get_muka_zolote_zernyatko_pshenichne_2kg)
        elif nn_respond == BEER_CHERNIGOVSKOE_BELOE_NEFILTER_1_L:
            result = self.getting_prices('beer_chernigivske_bile_nefilter_1l',get_beer_chernigivske_bile_1l_plastic)
        elif nn_respond == BEER_OBOLON_SVITLE_1_L:
            result = self.getting_prices('beer_obolon_svitle_1l',get_beer_obolon_svitle_1l_plastic)
        elif nn_respond == BEER_ROGAN_TRADICIYNE_SVITLE_1_L:
            result = self.getting_prices('beer_rogan_tradiciyne_svitle_1l',get_beer_rogan_tradiciyne_svitle_1l_plastic)
        elif nn_respond == SOUS_CHUMAK_CHESNOCHNIY_200_GR:
            result = self.getting_prices('sous_chumak_chesnochniy_200gr',get_sous_chumak_chesnochniy_200gr)
        elif nn_respond == ORBIT_POLYNICA_BANAN:
            result = self.getting_prices('orbit_polunica_banan',get_jvachka_orbit_clubnika_banan)
        elif nn_respond == LM_RED:
            result = self.getting_prices('sigarets_lm_red',get_sigarets_LM_red)
        elif nn_respond == BEER_JIGULIVSKE_SVITLE_2_L:
            result = self.getting_prices('beer_jigulivske_svitle_2l_plastic',get_beer_jigulivske_2l_plastic)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_2_L:
            result = self.getting_prices('beer_chayka_dniprovska_2l_plastic',get_beer_chayka_dniprovskaya_2l_plastic)
        elif nn_respond == BEER_PIWNY_KEBEK_2_L:
            result = self.getting_prices('beer_piwny_kebek_svitle_2l_plastic',get_beer_piwny_kubek_2l_plastic)
        elif nn_respond == KETCHUP_TORCHIN_DO_SHASHLIKY_270_GR:
            result = self.getting_prices('ketchup_torchin_do_shashliky_270gr',get_ketchup_torchin_do_shasliky_270gr)
        elif nn_respond == MAYONES_CHUMAK_APPETITNIY_50_300_GR:
            result = self.getting_prices('mayonez_chumak_appetitniy_50_300gr',get_mayonez_chumak_appetitniy_50_300gr)
        elif nn_respond == KOLBASA_PERSHA_STOLICA_SALYAMI_FIRMENNAYA_VS:
            result = self.getting_prices(self.NO_PRICES,get_kolbasa_persha_stolica_salyami_firmova_vs)
        elif nn_respond == COFFEE_CHERNA_KARTA_GOLD_50_GR:
            result = self.getting_prices('coffee_chorna_karta_50gr',get_cofee_chorna_karta_gold_50gr)
        elif nn_respond == BEER_ARSENAL_MICNE_SVITLE_2_L:
            result = self.getting_prices('beer_arsenal_micne_2l_plastic',get_beer_arsenal_micne_svitle_2l_plastic)
        elif nn_respond == BEER_PPB_BOCHKOVE_SVITLE_2_L:
            result = self.getting_prices('beer_ppb_bochkove_svitle_2l_plastic',get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_2_L:
            result = self.getting_prices('beer_ppb_zakarpatske_svitle_2l_plastic',get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic)
        elif nn_respond == BEER_ZIBERT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zibert_svitle_05l_v_banke',get_beer_zibert_svitle_05_l_banochnoe)
        elif nn_respond == YOGURT_FANNI_240_GR_1_5_LESNIE_YAGODI:
            result = self.getting_prices('yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan',get_yogurt_fanni_lisovi_yagodi_1_5_240gr)
        elif nn_respond == KEFIR_SLAVIYA_2_5_850_GR:
            result = self.getting_prices(self.NO_PRICES, get_kefir_slaviya_2_5_850gr)
        elif nn_respond == BEER_OBOLON_KIEVSKOE_ROZLIVNOE_SVITLE_195_L:
            result = self.getting_prices('beer_obolon_kievskoe_razlivnoe_svetloe_195l',get_beer_obolon_kievskoe_razlivnoe_svetloe_195l_plastic)
        elif nn_respond == BEER_CHERNIGOVSKOE_LIGHT_SVITLE_2_L:
            result = self.getting_prices('beer_chernigivske_light_svitle_2l_plastic',get_beer_chernigivske_light_svitle_2l_plastic)
        elif nn_respond == BEER_OPILLYA_KORIFEY_2_L:
            result = self.getting_prices('beer_opilla_korifey_svitle_2l_plastic',get_beer_opilla_korifey_svitle_2l_plastic)
        elif nn_respond == BEER_YANTAR_SVITLE_2_L:
            result = self.getting_prices('beer_yantar_svitle_2l_plastic',get_beer_yantar_svitle_2l_plastic)
        elif nn_respond == BEER_TUBORG_GREEN_4_X_05_L:
            result = self.getting_prices('beer_tuborg_green_svitle_4_banki_05l',get_beer_tuborg_green_svitle_4_banki_05l)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_4_X_05_L:
            result = self.getting_prices('beer_ppb_zakarpatske_svitle_4_banki_05l',get_beer_ppb_zakarpatske_svitle_4_banki_05l)
        elif nn_respond == BEER_PPB_BOCHKOVE_4_X_05_L:
            result = self.getting_prices('beer_ppb_bochkove_svitle_4_banki_05l',get_beer_ppb_bochkove_svitle_4_banki_05l)
        elif nn_respond == BEER_BUDWEISER_BUDVAR_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_budweiser_budvar_svitle_05l',get_beer_budweiser_budvar_05l_glass)
        elif nn_respond == BEER_PILSNER_URQUELL_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_pilsner_urquell_svitle_05l',get_beer_pilsner_urquell_05l_glass)
        elif nn_respond == BEER_ROBERT_DOMS_BELGIYSKIY_SVITLE_NEFILTER_05_L_GLASS:
            result = self.getting_prices('beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass',get_beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass)
        elif nn_respond == BEER_CHERNIGOVSKOE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_chernigivske_svitle_05_l_jb',get_beer_chernigivske_svitle_05l_jb)
        elif nn_respond == BEER_CHERNIGOVSKOE_BELOE_05_L_JB:
            result = self.getting_prices('beer_chernigivske_bile_nefilter_05_l_jb',get_beer_chernigivske_bile_nefilter_05l_jb)
        elif nn_respond == BEER_VELKOPOPOVICKY_KOZEL_TEMNE_05_L_JB:
            result = self.getting_prices('beer_velkopopovicky_kozel_temne_05_l_jb',get_beer_velkopopovicky_kozel_temne_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_PILSNER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_edelmeister_pilsner_svitle_05_l_jb',get_beer_edelmeister_pilsner_svitle_05l_jb)
        elif nn_respond == BEER_FAXE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_faxe_svitle_05_l_jb',get_beer_faxe_svitle_05l_jb)
        elif nn_respond == BEER_LIVU_PILZENES_SVITLE_05_L_JB:
            result = self.getting_prices('beer_livu_pilzenes_svitle_05_l_jb',get_beer_livu_pilzenes_svitle_05l_jb)
        elif nn_respond == BEER_VELKOPOPOVICKY_KOZEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_velkopopovicky_kozel_svitle_05_l_jb',get_beer_velkopopovicky_kozel_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_LIMON_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_limon_svitle_05_l_jb',get_beer_obolon_beermix_limon_svitle_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_WEIZENBIER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb',get_beer_edelmeister_weizenbier_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_SCHWARZBIER_TEMNE_05_L_JB:
            result = self.getting_prices('beer_edelmeister_schwarzbier_temne_05_l_jb',get_beer_edelmeister_schwarzbier_temne_05l_jb)
        elif nn_respond == BEER_HIKE_BLANCHE_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_hike_blanche_nefilter_05_l_jb',get_beer_hike_blanche_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_ZLATA_PRAHA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zlata_praha_svitle_05_l_jb',get_beer_zlata_praha_svitle_05l_jb)
        elif nn_respond == BEER_THURINGER_PREMIUM_BEER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_thuringer_premium_beer_svitle_05_l_jb',get_beer_thuringer_premium_beer_svitle_05l_jb)
        elif nn_respond == BEER_LIVU_SENCU_SVITLE_05_L_JB:
            result = self.getting_prices('beer_livu_sencu_beer_svitle_05_l_jb',get_beer_livu_sencu_svitle_05l_jb)
        elif nn_respond == BEER_GERMANARICH_SVITLE_05_L_JB:
            result = self.getting_prices('beer_germanarich_svitle_05_l_jb',get_beer_germanarich_svitle_05l_jb)
        elif nn_respond == BEER_HIKE_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hike_premium_svitle_05_l_jb',get_beer_hike_premium_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_0_NONALCO_NEFILTER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_nonalcohol_nefilter_svitle_05_l_jb',get_beer_obolon_svitle_nefilter_nonalcohol_05l_jb)
        elif nn_respond == BEER_ZIBERT_BAVARSKOE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zibert_bavarskoe_svitle_05_l_jb',get_beer_zibrert_bavarske_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIYA_LIQUID_APPLE_NONALCO_SVITLE_05_L_JB:
            result = self.getting_prices('beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb',get_beer_bavaria_liquid_apple_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_HEINEKEN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_heineken_svitle_05_l_jb',get_beer_heineken_svitle_05l_jb)
        elif nn_respond == BEER_RYCHTAR_GRANT_11_SVITLE_05_L_JB:
            result = self.getting_prices('beer_rychtar_grant_11_svitle_05_l_jb',get_beer_rychtar_grunt_11_svitle_05l_jb)
        elif nn_respond == BEER_AMSTEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_amstel_svitle_05_l_jb',get_beer_amstel_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_bavaria_svitle_05_l_jb',get_beer_bavaria_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_svitle_nonalcohol_05_l_jb',get_beer_bavaria_svitle_nonalcohol_05l_jb)
        elif nn_respond == BEER_EDELBURG_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_edelburg_lager_05_l_jb',get_beer_edelburg_lager_svitle_05l_jb)
        elif nn_respond == BEER_DONNER_PILS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_donner_pils_svitle_05_l_jb',get_beer_donner_pils_svitle_05l_jb)
        elif nn_respond == BEER_DUTCH_WINDMILL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_dutch_windmill_svitle_05_l_jb',get_beer_dutch_windmill_svitle_05l_jb)
        elif nn_respond == BEER_EDELBURG_HEFEWEIZEN_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb',get_beer_edelburg_hefeweizen_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_UNFILTERED_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb',get_beer_edelmeister_unfiltered_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_ESTRELLA_DAMM_BARCELONA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_estrella_damm_barcelona_svitle_05_l_jb',get_beer_estrella_damm_barcelona_svitle_05l_jb)
        elif nn_respond == BEER_HALNE_JASNE_PELNE_05_L_JB:
            result = self.getting_prices('beer_halne_jasne_pelne_05_l_jb',get_beer_halne_jasne_pelne_05l_jb)
        elif nn_respond == BEER_EUROTOUR_HEFEWEISSBIER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_eurotour_hefeweissbier_svitle_05_l_jb',get_beer_eurotour_hefeweissbier_svitle_05l_jb)
        elif nn_respond == BEER_HOLLANDIA_STRONG_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hollandia_strong_svitle_05_l_jb',get_beer_hollandia_strong_svitle_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_lander_brau_premium_svitle_05_l_jb',get_beer_lander_brau_premium_svitle_05l_jb)
        elif nn_respond == BEER_SAKU_KULD_05_L_JB:
            result = self.getting_prices('beer_saku_kuld_05_l_jb',get_beer_Saku_Kuld_05l_jb)
        elif nn_respond == BEER_SAKU_ORIGINAAL_05_L_JB:
            result = self.getting_prices('beer_saku_originaal_05_l_jb',get_beer_Saku_Originaal_05l_jb)
        elif nn_respond == BEER_STANGEN_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_stangen_lager_svitle_05_l_jb',get_beer_Stangen_Lager_svitle_05l_jb)
        elif nn_respond == BEER_VAN_PUR_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_van_pur_premium_svitle_05_l_jb',get_beer_Van_Pur_Premium_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_MANGO_MARAKUYA_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb',get_beer_Bavaria_mango_marakya_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_GRANAT_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_granat_nonalco_svitle_05_l_jb',get_beer_Bavaria_granat_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_MALINA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_malina_svitle_05_l_jb',get_beer_Obolon_Beermix_malina_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_VISHNYA_SPECIALNE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_vishnya_svitle_05_l_jb',get_beer_Obolon_Beermix_vishnya_svitle_05l_jb)
        elif nn_respond == BEER_LOMZA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_lomza_svitle_05_l_jb',get_beer_Lomza_svitle_05l_jb)
        elif nn_respond == BEER_PADERBORNER_PILSENER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_paderborner_pilsener_05_l_jb',get_beer_Paderborner_Pilsener_svitle_05l_jb)
        elif nn_respond == BEER_PADERBORNER_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_paderborner_export_05_l_jb',get_beer_Paderborner_Export_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_GRAPEFRUIT_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_grapefruit_nonalco_05_l_jb',get_beer_Clausthaler_Grapefruit_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_ORIGINAL_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_original_nonalco_05_l_jb',get_beer_Clausthaler_Original_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_LEMON_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_lemon_nonalco_05_l_jb',get_beer_Clausthaler_Lemon_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_FOREVER_ROCK_N_ROLL_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_rock_n_roll_nefilter_svitle_05_l_jb',get_beer_Forever_Rock_N_Roll_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_BLACK_QUEEN_TEMNE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_black_queen_nefilter_temne_05_l_jb',get_beer_Forever_Black_Queen_temne_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_KITE_SAFARI_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_kite_safari_nefilter_svitle_05_l_jb',get_beer_Forever_Kite_Safari_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_CRAZY_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_crazy_nefilter_svitle_05_l_jb',get_beer_Forever_Crazy_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_HIKE_LIGHT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hike_light_svitle_05_l_jb',get_beer_Hike_Light_svitle_05l_jb)
        elif nn_respond == BEER_HIKE_ZERO_NONALCO_05_L_JB:
            result = self.getting_prices('beer_hike_zero_nonalco_05_l_jb',get_beer_Hike_Zero_nonalco_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_ICE_PILSNER_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_ice_pilsner_svitle_05_l_jb',get_beer_Horn_Disel_Ice_Pilsner_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_ORIGINAL_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_original_svitle_05_l_jb',get_beer_Horn_Disel_Original_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_TRADITIONAL_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_traditional_svitle_05_l_jb',get_beer_Horn_Disel_Traditional_svitle_05l_jb)
        elif nn_respond == BEER_HORN_PREMIUM_DIESEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_horn_disel_premium_svitle_05_l_jb',get_beer_Horn_Disel_Premium_svitle_05l_jb)
        elif nn_respond == BEER_KRUSOVICE_CERNE_TEMNE_05_L_JB:
            result = self.getting_prices('beer_krusovice_cerne_temne_05_l_jb',get_beer_Krusovice_Cerne_temne_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_MICNE_05_L_JB:
            result = self.getting_prices('beer_lander_brau_micne_05_l_jb',get_beer_Lander_Brau_micne_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_lander_brau_svitle_nefilter_05_l_jb',get_beer_Lander_Brau_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_PADERBORNER_PILGER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_paderborner_pilger_svitle_nefilter_05_l_jb',get_beer_Paderborner_Pilger_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_PLATAN_JEDENACTKA_11_SVITLE_05_L_JB:
            result = self.getting_prices('beer_platan_jedenactka_11_svitle_05_l_jb',get_beer_Platan_Jedenactka_11_svitle_05l_jb)
        elif nn_respond == BEER_PRAGA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_praga_svitle_05_l_jb',get_beer_Praga_svitle_05l_jb)
        elif nn_respond == BEER_SAKU_ROCK_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_saku_rock_svitle_0568_l_jb',get_beer_Saku_Rock_svitle_05l_jb)
        elif nn_respond == BEER_SITNAN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_sitnan_svitle_05_l_jb',get_beer_Sitnan_svitle_05l_jb)
        elif nn_respond == BEER_VIENAS_PREMIUM_GOLDEN_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_vienas_premium_golden_svitle_05_l_jb',get_beer_Vienas_Premium_Golden_svitle_05l_jb)
        elif nn_respond == BEER_VIENAS_PREMIUM_TRADITIONAL_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_vienas_premium_traditional_svitle_05_l_jb',get_beer_Vienas_Premium_Traditional_svitle_05l_jb)
        elif nn_respond == BEER_VLYNSKI_BROWAR_FOREVER_SWEET_WIT_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb',get_beer_Volynski_Browar_Forever_Sweet_Wit_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_ZAHRINGER_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zahringer_premium_svitle_05_l_jb',get_beer_Zahringer_premium_svitle_05l_jb)
        elif nn_respond == BEER_ZAHRINGER_HEFEWEIZEN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zahringer_hefeweizen_svitle_05_l_jb',get_beer_Zahringer_Hefeweizen_svitle_05l_jb)
        elif nn_respond == BEER_JASHKOVSKOE_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_jajkivske_nefilter_svitle_05_l_jb',get_beer_jajkivske_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_svitle_05_l_jb',get_beer_obolon_svitle_05l_jb)
        elif nn_respond == BEER_PUBSTER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_pubster_svitle_05_l_jb',get_beer_Pubster_svitle_05l_jb)
        elif nn_respond == BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_chaika_chernomorskaya_05_l_jb',get_beer_Chaika_Chernomorska_svitle_05l_jb)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_ppb_zakarpatske_origin_svitle_05_l_jb',get_beer_PPB_Zakarpatske_origin_svitle_05l_jb)
        elif nn_respond == BEER_PPB_BOCHKOVE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_ppb_bochkove_nefilter_05_l_jb',get_beer_PPB_Bochkove_nefilter_05l_jb)
        elif nn_respond == BEER_PPB_NEFILTROVANE_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_ppb_nefilter_svitle_nonalco_05_l_jb',get_beer_PPB_Nefilter_svitle_nonalco_05l_jb)
        elif nn_respond == BEER_PPB_LIMON_LIME_NONALCO_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_ppb_limon_lime_nonalco_nefilter_05_l_jb',get_beer_PPB_Limon_lime_nonalco_nefilter_05l_jb)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_05_L_JB:
            result = self.getting_prices('beer_chaika_dniprovskaya_05_l_jb',get_beer_Chaika_Dniprovska_svitle_05l_jb)
        elif nn_respond == BEER_BROK_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_brok_export_svitle_05_l_jb',get_beer_Brok_Export_svitle_05l_jb)
        elif nn_respond == BEER_CARLING_SVITLE_05_L_JB:
            result = self.getting_prices('beer_carling_svitle_05_l_jb',get_beer_Carling_svitle_05l_jb)
        elif nn_respond == BEER_KETEN_BRUG_BLANCHE_ELEGANT_05_L_JB:
            result = self.getting_prices('beer_keten_brug_blanche_elegant_05_l_jb',get_beer_Keten_Brug_Blanche_Elegant_05l_jb)
        elif nn_respond == BEER_BUDWEISER_NONALCO_05_L_JB:
            result = self.getting_prices('beer_budweiser_nonalco_05_l_jb',get_beer_Budweiser_nonalco_05l_jb)
        elif nn_respond == BEER_FELDSCHLOSSCHEN_WHEAT_BEER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_feldschlosschenWheatBeer_svitle_nefilter_05_l_jb',get_beer_Feldschlosschen_Wheat_Beer_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_TETERIV_HMILNA_VISHNYA_NAPIVTEMNE_05_L_JB:
            result = self.getting_prices('beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb',get_beer_Teteriv_hmilna_vishnya_napivtemne_05l_jb)
        elif nn_respond == BEER_GROTWERG_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_grotwerg_svitle_05_l_jb',get_beer_Grotwerg_svitle_nonalco_05l_jb)
        elif nn_respond == BEER_HOLLAND_IMPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_holland_import_svitle_05_l_jb',get_beer_Holland_import_svitle_05l_jb)
        elif nn_respond == BEER_GOLDEN_CASTLE_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_golden_castle_export_svitle_05_l_jb',get_beer_Golden_castle_export_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_CRAFT_BEER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb',get_beer_5_0_original_craft_beer_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_GUINESS_DRAUGHT_TEMNE_044_L_JB:
            result = self.getting_prices('beer_guinness_draught_temne_044_l_jb',get_beer_Guinness_draught_temne_05l_jb)
        elif nn_respond == BEER_GRIMBERGEN_DOUBLE_AMBREE_NAPIVTEMNE_05_L_JB:
            result = self.getting_prices('beer_grimbergenDoubleAmbree_napivtemne_05_l_jb',get_beer_GrimbergenDoubleAmbree_napivtemne_05l_jb)
        elif nn_respond == BEER_WARSTEINER_PREMIUM_VERUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_warsteinerPremiumVerum_svitle_05_l_jb',get_beer_WarsteinerPremiumVerum_svitle_05l_jb)
        elif nn_respond == BEER_DAB_TEMNE_05_L_JB:
            result = self.getting_prices('beer_dab_temne_05_l_jb',get_beer_DAB_temne_05l_jb)
        elif nn_respond == BEER_GRIMBERGEN_BLANCHE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_grimbergenBlanche_svitle_05_l_jb',get_beer_GrimbergenBlanche_svitle_05l_jb)
        elif nn_respond == BEER_KLOSTERKELLER_WEISSBIER_CHINA_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_klosterkellerWeissbierChina_nefilter_svitle_05_l_jb',get_beer_KlosterkellerWeissbierChina_svitle_05l_jb)
        elif nn_respond == BEER_KARPACKIE_PILS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_karpackiePils_svitle_05_l_jb',get_beer_KarpackiePils_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_PILLS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_5_0_OriginalPills_svitle_05_l_jb',get_beer_5_0_OriginalPills_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_5_0_Original_lager_svitle_05_l_jb',get_beer_5_0_OriginalLager_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_WEISS_BEER_SVITLE__NEFILTER_05_L_JB:
            result = self.getting_prices('beer_5_0_Original_weiss_beer_nefilter_svitle_05_l_jb',get_beer_5_0_Original_Weiss_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_FAHNEN_BRAU_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Fahnen_Brau_svitle_05_l_jb',get_beer_Fahnen_Brau_svitle_05l_jb)
        elif nn_respond == BEER_GOSSER_LIGHT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Gosser_Light_svitle_05_l_jb',get_beer_Gosser_light_svitle_05l_jb)
        elif nn_respond == BEER_HOLLANDIA_IMPORT_SVITLE_033_L_JB:
            result = self.getting_prices('beer_Hollandia_Import_svitle_033_l_jb',get_beer_HollandiaImport_svitle_033l_jb)
        elif nn_respond == BEER_HOLSTEN_PILSENER_048_L_JB:
            result = self.getting_prices('beer_Holsten_Pilsner_048_l_jb',get_beer_Holsten_Pilsener_048l_jb)
        elif nn_respond == BEER_OBOLON_PREMIUM_EXTRA_BREW_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb',get_beer_Obolon_Premium_Extra_Brew_svitle_05l_jb)
        elif nn_respond == BEER_LVIVSKE_SVITLE_048_L_JB:
            result = self.getting_prices('beer_Lvivske_svitle_48_l_jb',get_beer_Lvivske_svitle_048l_jb)
        elif nn_respond == BEER_CARLSBERG_PREMIUM_PILSNER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb',get_beer_Carlsberg_Premium_Pilsner_svitle_05l_jb)
        elif nn_respond == BEER_CARLSBERG_PILSNER_05_L_JB:
            result = self.getting_prices('beer_Carlsberg_Pilsner_05_l_jb',get_beer_Carlsberg_Pilsner_05l_jb)
        else:
            result = self.getting_prices('apple_golden',get_apple_golden)

        return result








