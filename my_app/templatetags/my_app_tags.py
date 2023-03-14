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
