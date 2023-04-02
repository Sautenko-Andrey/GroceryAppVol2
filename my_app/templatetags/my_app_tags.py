from django import template
from my_app.models import *

# оздадим экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
register = template.Library()


@register.simple_tag()
def get_obolon_premium():
    '''Тэг, возвращающий информацию о пиве "Оболонь Прмиум 1,1 л из БД"'''
    return ItemsPicsFromNet.objects.get(pk=2)



@register.simple_tag()
def get_hetman_ICE():
    '''Тэг, возвращающий информацию о водке "Гетьман ICE из БД"'''
    return ItemsPicsFromNet.objects.get(pk=1)


@register.simple_tag()
def coffe_aroma_gold_classic_100gr():
    '''Тэг, возвращающий информацию о кофе "Aroma Gold Classic 100 g"'''
    return ItemsPicsFromNet.objects.get(pk=3)


@register.simple_tag()
def get_oil_shedriy_dar_085l():
    '''Тэг, возвращающий информацию о подсолнечном масле "Щедрый Дар" 0,85 л'''
    return ItemsPicsFromNet.objects.get(pk=4)


@register.simple_tag()
def get_apple_golden():
    '''Тэг, возвращающий информацию о яблоке сорта Голден, 1 кг'''
    return ItemsPicsFromNet.objects.get(pk=5)


@register.simple_tag()
def get_coca_cola_2l():
    '''Тэг, возвращающий информацию о напитке Кока-Кола, 2 л'''
    return ItemsPicsFromNet.objects.get(pk=6)


@register.simple_tag()
def get_sigarets_kent_8():
    '''Тэг, возвращающий информацию о сигаретах Кент 8'''
    return ItemsPicsFromNet.objects.get(pk=7)


@register.simple_tag()
def get_KOMO_paprikash():
    '''Тэг, возвращающий информацию о сырке плавленном "КОМО Паприкаш"'''
    return ItemsPicsFromNet.objects.get(pk=8)


@register.simple_tag()
def get_garlik():
    '''Тэг,возвращающий информацию о чесноке'''
    return ItemsPicsFromNet.objects.get(pk=9)


@register.simple_tag()
def get_tea_minutka_black_40_b():
    '''Тэг,возвращающий информацию о чае "Минутка", 40 пакетиков, черный.'''
    return ItemsPicsFromNet.objects.get(pk=10)


@register.simple_tag()
def get_fairy_500_lime():
    '''Тэг,возвращающий информацию о моющем средстве Fairy лимон, 500 г'''
    return ItemsPicsFromNet.objects.get(pk=11)


@register.simple_tag()
def get_onion():
    '''Тэг,возвращающий информацию о луке'''
    return ItemsPicsFromNet.objects.get(pk=12)


@register.simple_tag()
def get_apple_black_prince():
    '''Тэг,возвращающий информацию о яблоке "Черный принц"'''
    return ItemsPicsFromNet.objects.get(pk=13)


@register.simple_tag()
def get_smetana_stolica_smaky_20_400gr():
    '''Тэг,возвращающий информацию о сметане "Смачни традиции 20 % 400 гр"'''
    return ItemsPicsFromNet.objects.get(pk=14)


@register.simple_tag()
def get_gorchica_kolos():
    '''Тэг,возвращающий информацию о горчице "Колос"'''
    return ItemsPicsFromNet.objects.get(pk=15)


@register.simple_tag()
def get_limon():
    '''Тэг,возвращающий информацию о лимоне'''
    return ItemsPicsFromNet.objects.get(pk=16)


@register.simple_tag()
def get_oil_oleyna_neraf_850():
    '''Тэг,возвращающий информацию о масле "Оленйа" нерафинированное, 850 г'''
    return ItemsPicsFromNet.objects.get(pk=17)


@register.simple_tag()
def get_drojji_hark():
    '''Тэг,возвращающий информацию о харьковских дрожжах 100 гр'''
    return ItemsPicsFromNet.objects.get(pk=18)


@register.simple_tag()
def get_tea_monomah_kenya():
    '''Тэг,возвращающий информацию о чае "Мономах Кения", 90 гр'''
    return ItemsPicsFromNet.objects.get(pk=19)


@register.simple_tag()
def get_cabbage():
    '''Тэг,возвращающий информацию о капусте'''
    return ItemsPicsFromNet.objects.get(pk=20)


@register.simple_tag()
def get_carrot():
    '''Тэг,возвращающий информацию о моркови'''
    return ItemsPicsFromNet.objects.get(pk=21)


@register.simple_tag()
def get_arko_cool_300_100():
    '''Тэг,возвращающий информацию о пене для бритья "Arko Cool 300 гр +100 бонус"'''
    return ItemsPicsFromNet.objects.get(pk=22)


@register.simple_tag()
def get_arko_sensitive_300_100():
    '''Тэг,возвращающий информацию о пене для бритья "Arko Sensitive 300 гр +100 бонус"'''
    return ItemsPicsFromNet.objects.get(pk=23)


def get_chicken_eggs():
    '''Тэг,возвращающий информацию о куринных яйцах'''
    return ItemsPicsFromNet.objects.get(pk=24)


@register.simple_tag()
def get_mayonez_dom_detsk_shedro_67():
    '''Тэг,возвращающий информацию о майонезе домашнем детском "Щедро" 67%'''
    return ItemsPicsFromNet.objects.get(pk=25)


@register.simple_tag()
def get_reksona_aloe_vera_w():
    '''Тэг,возвращающий информацию о пене для дезодаратнта "Rexona Aloe Vera" женский'''
    return ItemsPicsFromNet.objects.get(pk=26)


@register.simple_tag()
def get_toilet_papir_kiev_63m():
    '''Тэг,возвращающий информацию о туалетной бумаге "Киев" 63м '''
    return ItemsPicsFromNet.objects.get(pk=27)

@register.simple_tag()
def get_marlboro_red():
    '''Тэг,возвращающий информацию о сигаретах "Мальборо" красные '''
    return ItemsPicsFromNet.objects.get(pk=28)

@register.simple_tag()
def get_pivo_lvivske_svitle():
    '''Тэг,возвращающий информацию о пиве "Львовское светлое" 2,4 л '''
    return ItemsPicsFromNet.objects.get(pk=29)

@register.simple_tag()
def get_smetana_stol_smaku_400_15():
    '''Тэг,возвращающий информацию о сметане "Столиця Смаку 400 гр 15% жирности"'''
    return ItemsPicsFromNet.objects.get(pk=30)

@register.simple_tag()
def get_dezodorant_garnier_magniy_m():
    '''Тэг,возвращающий информацию о дезодоранте "Garnier Magniy мужской"'''
    return ItemsPicsFromNet.objects.get(pk=31)

@register.simple_tag()
def get_tea_monomah_ceylon_black():
    '''Тэг,возвращающий информацию о чае "Мономах черный Цейлон"'''
    return ItemsPicsFromNet.objects.get(pk=32)

@register.simple_tag()
def get_coffee_aroma_gold_freeze_dried_70():
    '''Тэг,возвращающий информацию о кофе "Арома Голд freeze dried 70 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=33)

@register.simple_tag()
def get_gorchica_veres_micna_ukr_120g():
    '''Тэг,возвращающий информацию о горчице "Верес мицна украинская 120 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=34)

@register.simple_tag()
def get_tea_monomah_original_ceylon_90g():
    '''Тэг,возвращающий информацию о чае "Мономах оригинал 100% цейлон 90 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=35)

@register.simple_tag()
def get_desodorant_garnier_spring_spirit():
    '''Тэг,возвращающий информацию о дезодоранте "Garnier весенняя сежесть"'''
    return ItemsPicsFromNet.objects.get(pk=36)

@register.simple_tag()
def get_apple_gala():
    '''Тэг,возвращающий информацию о яблоках Гала'''
    return ItemsPicsFromNet.objects.get(pk=37)

@register.simple_tag()
def get_smetana_galichanska_15_370gr():
    '''Тэг,возвращающий информацию о сметане "Галичанська 15% 370 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=38)

@register.simple_tag()
def get_chips_lays_salt_big_pack_30g():
    '''Тэг,возвращающий информацию о чипсах "Lays с солью 30 гр" большая пачка'''
    return ItemsPicsFromNet.objects.get(pk=39)

@register.simple_tag()
def get_sprite_2l():
    '''Тэг,возвращающий информацию о напитке "Sprite 2 литра"'''
    return ItemsPicsFromNet.objects.get(pk=40)

@register.simple_tag()
def get_fanta_2l():
    '''Тэг,возвращающий информацию о напитке "Fanta 2 литра"'''
    return ItemsPicsFromNet.objects.get(pk=41)

@register.simple_tag()
def get_bond_street_blue_selection():
    '''Тэг,возвращающий информацию о сигаретах "BOND STREET BLUE SELECTION"'''
    return ItemsPicsFromNet.objects.get(pk=42)

@register.simple_tag()
def get_camel_blue():
    '''Тэг,возвращающий информацию о сигаретах "CAMEL BLUE"'''
    return ItemsPicsFromNet.objects.get(pk=43)

@register.simple_tag()
def get_ld_red():
    '''Тэг,возвращающий информацию о сигаретах "LD RED"'''
    return ItemsPicsFromNet.objects.get(pk=44)

@register.simple_tag()
def get_marlboro_gold():
    '''Тэг,возвращающий информацию о сигаретах "MARLBORO GOLD"'''
    return ItemsPicsFromNet.objects.get(pk=45)

@register.simple_tag()
def get_rothmans_demi_blue_exclusive():
    '''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI BLUE EXCLUSIVE"'''
    return ItemsPicsFromNet.objects.get(pk=46)

@register.simple_tag()
def get_rothmans_demi_click_purple():
    '''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI CLICK PURPLE"'''
    return ItemsPicsFromNet.objects.get(pk=47)

@register.simple_tag()
def get_winston_caster():
    '''Тэг,возвращающий информацию о сигаретах "WINSTON CASTER"'''
    return ItemsPicsFromNet.objects.get(pk=48)

@register.simple_tag()
def get_parlament_aqua_blue():
    '''Тэг,возвращающий информацию о сигаретах "PARLAMENT AQUA BLUE"'''
    return ItemsPicsFromNet.objects.get(pk=49)

@register.simple_tag()
def get_winston_blue():
    '''Тэг,возвращающий информацию о сигаретах "WINSTON BLUE"'''
    return ItemsPicsFromNet.objects.get(pk=50)

@register.simple_tag()
def get_bond_street_red_selection():
    '''Тэг,возвращающий информацию о сигаретах "BOND STREET RED SELECTION"'''
    return ItemsPicsFromNet.objects.get(pk=51)

@register.simple_tag()
def get_ld_blue():
    '''Тэг,возвращающий информацию о сигаретах "LD BLUE"'''
    return ItemsPicsFromNet.objects.get(pk=52)

@register.simple_tag()
def get_kent_silver():
    '''Тэг,возвращающий информацию о сигаретах "KENT SILVER"'''
    return ItemsPicsFromNet.objects.get(pk=53)

@register.simple_tag()
def get_kent_navi_blue_new():
    '''Тэг,возвращающий информацию о сигаретах "KENT NAVI BLUE NEW"'''
    return ItemsPicsFromNet.objects.get(pk=54)

@register.simple_tag()
def get_beer_chernigivske_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Черниговское Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=55)

@register.simple_tag()
def get_beer_stella_artois_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Stella Artois 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=56)

@register.simple_tag()
def get_beer_obolon_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Оболонь Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=57)


@register.simple_tag()
def get_beer_jigulivsle_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Жигулевское Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=58)

@register.simple_tag()
def get_beer_rogan_tradiciyne_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Рогань традиционное Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=59)

@register.simple_tag()
def get_beer_corona_extra_svitle_033_l_glass():
    '''Тэг,возвращающий информацию о пиве "Corona Extra светлое 0,33 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=60)

@register.simple_tag()
def get_beer_chernigivske_bile_nefilter_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Черниговоское Белое нефильтрованное 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=61)

@register.simple_tag()
def get_beer_yantar_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Янтарь Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=62)

@register.simple_tag()
def get_beer_zibert_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Zibert Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=63)

@register.simple_tag()
def get_beer_arsenal_micne_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Арсенал мицне 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=64)

@register.simple_tag()
def get_beer_persha_brovarna_zakarpatske_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Перша Броварня Закарпатське 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=65)

@register.simple_tag()
def get_beer_lvivske_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Львовское Светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=66)

@register.simple_tag()
def get_beer_lvivske_1715_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Львовское 1715 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=67)

@register.simple_tag()
def get_beer_zlata_praha_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Zlata Praha 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=68)

@register.simple_tag()
def get_beer_tuborg_green_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Tuborg Green 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=69)

@register.simple_tag()
def get_beer_slavutich_ice_mix_lime_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Славутич ICE MIX Lime 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=70)

@register.simple_tag()
def get_beer_teteriv_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Тетерев светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=71)

@register.simple_tag()
def get_beer_krusovice_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Krusovice сетлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=72)

@register.simple_tag()
def get_beer_heineken_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Heineken светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=73)

@register.simple_tag()
def get_beer_amstel_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Amstel светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=74)

@register.simple_tag()
def get_beer_hike_premium_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Hike premium 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=75)

@register.simple_tag()
def get_beer_bochkove_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Бочкове светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=76)

@register.simple_tag()
def get_beer_kronenbourg_1664_blanc_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Kronenbourg 1664 Blanc светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=77)

@register.simple_tag()
def get_beer_opilla_nepasterizovane_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Опилля непастеризоване  светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=78)

@register.simple_tag()
def get_beer_yachmenniy_kolos_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Ячменный Колос светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=79)

@register.simple_tag()
def get_beer_opilla_korifey_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Опилля Корифей светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=80)

@register.simple_tag()
def get_beer_chaika_dneprovskaya_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Чайка Днепроская светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=81)

@register.simple_tag()
def get_beer_chaika_chernomorskaya_svitle_05_l_glass():
    '''Тэг,возвращающий информацию о пиве "Чайка Черноморская светлое 0,5 в стеклянной бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=82)

@register.simple_tag()
def get_beer_uman_waissburg_svitle_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Умань пиво Waissburg светлое 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=83)

@register.simple_tag()
def get_beer_uman_pshenichnoe_svitle_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Умань пиво пшеничное светлое 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=84)

@register.simple_tag()
def get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Бердичевское хмельное пиво светлое 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=85)

@register.simple_tag()
def get_beer_berdichevskoe_lager_svitle_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Бердичевское лагер светлое 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=86)

@register.simple_tag()
def get_beer_opilla_korifey_11_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Опилля Корифей 1.1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=87)

@register.simple_tag()
def get_beer_obolon_jigulivske_eksport_15_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Оболонь жигулевское экспортное 1,5 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=88)

@register.simple_tag()
def get_beer_yantar_svitle_12_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Янтарь светлое 1,2 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=89)

@register.simple_tag()
def get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Жашковское пшеничное нефильтрованное 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=90)

@register.simple_tag()
def get_beer_jashkovskoe_svitle_nefilter_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Жашковское светлое нефильтрованное 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=91)

@register.simple_tag()
def get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Жашковское жигулевское нефильтрованное 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=92)

@register.simple_tag()
def get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Перша приватна броварня бочкове 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=93)

@register.simple_tag()
def get_beer_chayka_dniprovska_1_l_plastic():
    '''Тэг,возвращающий информацию о пиве "Чайка днипровська 1 л в пластиковой бутылке"'''
    return ItemsPicsFromNet.objects.get(pk=94)

@register.simple_tag()
def get_ketchup_torchin_s_chesnokom():
    '''Тэг,возвращающий информацию о "Кетчуп Торчин с чесноком 270 гр"'''
    return ItemsPicsFromNet.objects.get(pk=95)

@register.simple_tag()
def get_mayonez_korolivkiy_smak_korolivskiy_67_300gr():
    '''Тэг,возвращающий информацию о "Майонез Королевский смак королевский 300 гр"'''
    return ItemsPicsFromNet.objects.get(pk=96)

@register.simple_tag()
def get_muka_zolote_zernyatko_pshenichne_2kg():
    '''Тэг,возвращающий информацию о "Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг"'''
    return ItemsPicsFromNet.objects.get(pk=97)

@register.simple_tag()
def get_beer_chernigivske_bile_1l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Черниговское Белое 1 литр в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=98)

@register.simple_tag()
def get_beer_obolon_svitle_1l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Оболонь светлое 1 литр в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=99)

@register.simple_tag()
def get_beer_rogan_tradiciyne_svitle_1l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Рогань традиционное светлое 1 литр в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=100)

@register.simple_tag()
def get_sous_torchin_chesnochniy_200gr():
    '''Тэг,возвращающий информацию о "Соус Торчин чесночный 200 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=101)

@register.simple_tag()
def get_jvachka_orbit_clubnika_banan():
    '''Тэг,возвращающий информацию о "Орбит клубника-банан"'''
    return ItemsPicsFromNet.objects.get(pk=102)

@register.simple_tag()
def get_sigarets_LM_red():
    '''Тэг,возвращающий информацию о "Сигареты LM красные"'''
    return ItemsPicsFromNet.objects.get(pk=103)

@register.simple_tag()
def get_beer_jigulivske_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Жигулевское 2л в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=104)

@register.simple_tag()
def get_beer_chayka_dniprovskaya_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Чайка днипровская 2л в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=105)

@register.simple_tag()
def get_beer_piwny_kubek_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Piwny Kubek  2л в пластике"'''
    return ItemsPicsFromNet.objects.get(pk=106)

@register.simple_tag()
def get_ketchup_torchin_do_shasliky_270gr():
    '''Тэг,возвращающий информацию о "Кетчуп Торчин до шашлику 270 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=107)

@register.simple_tag()
def get_mayonez_chumak_appetitniy_50_300gr():
    '''Тэг,возвращающий информацию о "Майонез Чумак аппетитный 50% 300 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=108)

@register.simple_tag()
def get_kolbasa_persha_stolica_salyami_firmova_vs():
    '''Тэг,возвращающий информацию о "Колбаса Перша Столиця Салями Фирменная высший сорт"'''
    return ItemsPicsFromNet.objects.get(pk=109)

@register.simple_tag()
def get_cofee_chorna_karta_gold_50gr():
    '''Тэг,возвращающий информацию о "Кофе Чорна Карта GOLD 50 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=110)

@register.simple_tag()
def get_beer_arsenal_micne_svitle_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Арсенал "Міцне" світле, 2л"'''
    return ItemsPicsFromNet.objects.get(pk=111)

@register.simple_tag()
def get_beer_arsenal_micne_svitle_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво Арсенал "Міцне" світле, 2л"'''
    return ItemsPicsFromNet.objects.get(pk=112)

@register.simple_tag()
def get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво "ППБ Бочкове" світле, 2л"'''
    return ItemsPicsFromNet.objects.get(pk=112)

@register.simple_tag()
def get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic():
    '''Тэг,возвращающий информацию о "Пиво "ППБ Закарпатське оригінальне" світле, 2л"'''
    return ItemsPicsFromNet.objects.get(pk=113)

@register.simple_tag()
def get_beer_zibert_svitle_05_l_banochnoe():
    '''Тэг,возвращающий информацию о "Пиво Zibert сетлое 0,5 л в банке"'''
    return ItemsPicsFromNet.objects.get(pk=114)

@register.simple_tag()
def get_yogurt_fanni_lisovi_yagodi_1_5_240gr():
    '''Тэг,возвращающий информацию о "Йогурт Фанни лесные ягоды 1,5% 240 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=115)

@register.simple_tag()
def get_kefir_slaviya_2_5_850gr():
    '''Тэг,возвращающий информацию о "Кефир Славия 2,5 % 850 грамм"'''
    return ItemsPicsFromNet.objects.get(pk=116)




# ТЕГИ ДЛЯ БЛЮД

@register.simple_tag()
def get_borsh_ukr_info():
    '''Тег , возвращающий информацю о борще украинском'''
    return InfoAboutDishes.objects.get(pk=1)


@register.simple_tag()
def get_vareniki_s_kartoshkoy_info():
    '''Тег , возвращающий информацю о варениках с картошкой'''
    return InfoAboutDishes.objects.get(pk=2)


#ТЕГ ДЛЯ ПРОДУКТОВОГО НАБОРА
@register.simple_tag()
def get_product_set_from_data_base():
    '''Возьмем все продукты,что есть в наборе пользователя'''
    return SetOfProducts.objects.all()

#ТЕГ ДЛЯ ДОСУТПА КО ВСЕМ СУПЕРМАРКЕТАМ
@register.simple_tag()
def get_all_markets():
    '''С помощбю этого тега получаем доступ ко всем названиям досутпных супермаркетов'''
    return RelevantMarkets.objects.all()
