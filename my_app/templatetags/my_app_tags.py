from django import template
from my_app.models import *

# оздадим экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
register = template.Library()

class SimpleTagMaker:
    '''Класс для формирования шаблонных тегов для товаров'''
    @register.simple_tag()
    def create_tag(self,pk):
        '''Формирование самой функции для тега'''
        return ItemsPicsFromNet.objects.get(pk=pk)


#создаем объект класса для создания тегов для продуктов
tag = SimpleTagMaker()
# создадим тэги:
'''Тэг, возвращающий информацию о пиве "Оболонь Прмиум 1,1 л из БД"'''
get_obolon_premium = tag.create_tag(2)

'''Тэг, возвращающий информацию о кофе "Aroma Gold Classic 100 g"'''
get_hetman_ICE = tag.create_tag(1)

'''Тэг, возвращающий информацию о кофе "Aroma Gold Classic 100 g"'''
coffe_aroma_gold_classic_100gr=tag.create_tag(3)

'''Тэг, возвращающий информацию о подсолнечном масле "Щедрый Дар" 0,85 л'''
get_oil_shedriy_dar_085l=tag.create_tag(4)

'''Тэг, возвращающий информацию о яблоке сорта Голден, 1 кг'''
get_apple_golden=tag.create_tag(5)

'''Тэг, возвращающий информацию о напитке Кока-Кола, 2 л'''
get_coca_cola_2l = tag.create_tag(6)

'''Тэг, возвращающий информацию о сигаретах Кент 8'''
get_sigarets_kent_8 = tag.create_tag(7)

'''Тэг, возвращающий информацию о сырке плавленном "КОМО Паприкаш"'''
get_KOMO_paprikash = tag.create_tag(8)

'''Тэг,возвращающий информацию о чесноке'''
get_garlik = tag.create_tag(9)

'''Тэг,возвращающий информацию о чае "Минутка", 40 пакетиков, черный.'''
get_tea_minutka_black_40_b=tag.create_tag(10)

'''Тэг,возвращающий информацию о моющем средстве Fairy лимон, 500 г'''
get_fairy_500_lime=tag.create_tag(11)

'''Тэг,возвращающий информацию о луке'''
get_onion=tag.create_tag(12)

'''Тэг,возвращающий информацию о яблоке "Черный принц"'''
get_apple_black_prince = tag.create_tag(13)

'''Тэг,возвращающий информацию о сметане "Смачни традиции 20 % 400 гр"'''
get_smetana_stolica_smaky_20_400gr=tag.create_tag(14)

'''Тэг,возвращающий информацию о горчице "Колос"'''
get_gorchica_kolos = tag.create_tag(15)

'''Тэг,возвращающий информацию о лимоне'''
get_limon=tag.create_tag(16)

'''Тэг,возвращающий информацию о масле "Оленйа" нерафинированное, 850 г'''
get_oil_oleyna_neraf_850 = tag.create_tag(17)

'''Тэг,возвращающий информацию о харьковских дрожжах 100 гр'''
get_drojji_hark=tag.create_tag(18)

'''Тэг,возвращающий информацию о чае "Мономах Кения", 90 гр'''
get_tea_monomah_kenya = tag.create_tag(19)

'''Тэг,возвращающий информацию о капусте'''
get_cabbage = tag.create_tag(20)

'''Тэг,возвращающий информацию о моркови'''
get_carrot = tag.create_tag(21)

'''Тэг,возвращающий информацию о пене для бритья "Arko Cool 300 гр +100 бонус"'''
get_arko_cool_300_100 = tag.create_tag(22)

'''Тэг,возвращающий информацию о пене для бритья "Arko Sensitive 300 гр +100 бонус"'''
get_arko_sensitive_300_100 =tag.create_tag(23)

'''Тэг,возвращающий информацию о куринных яйцах'''
get_chicken_eggs=tag.create_tag(24)

'''Тэг,возвращающий информацию о майонезе домашнем детском "Щедро" 67%'''
get_mayonez_dom_detsk_shedro_67 = tag.create_tag(25)

'''Тэг,возвращающий информацию о пене для дезодаратнта "Rexona Aloe Vera" женский'''
get_reksona_aloe_vera_w = tag.create_tag(26)

'''Тэг,возвращающий информацию о туалетной бумаге "Киев" 63м '''
get_toilet_papir_kiev_63m=tag.create_tag(27)

'''Тэг,возвращающий информацию о сигаретах "Мальборо" красные '''
get_marlboro_red = tag.create_tag(28)

'''Тэг,возвращающий информацию о пиве "Львовское светлое" 2,4 л '''
get_pivo_lvivske_svitle = tag.create_tag(29)

'''Тэг,возвращающий информацию о сметане "Столиця Смаку 400 гр 15% жирности"'''
get_smetana_stol_smaku_400_15=tag.create_tag(30)

'''Тэг,возвращающий информацию о дезодоранте "Garnier Magniy мужской"'''
get_dezodorant_garnier_magniy_m = tag.create_tag(31)

'''Тэг,возвращающий информацию о чае "Мономах черный Цейлон"'''
get_tea_monomah_ceylon_black=tag.create_tag(32)

'''Тэг,возвращающий информацию о кофе "Арома Голд freeze dried 70 грамм"'''
get_coffee_aroma_gold_freeze_dried_70=tag.create_tag(33)

'''Тэг,возвращающий информацию о горчице "Верес мицна украинская 120 грамм"'''
get_gorchica_veres_micna_ukr_120g=tag.create_tag(34)

'''Тэг,возвращающий информацию о чае "Мономах оригинал 100% цейлон 90 грамм"'''
get_tea_monomah_original_ceylon_90g = tag.create_tag(35)

'''Тэг,возвращающий информацию о дезодоранте "Garnier весенняя сежесть"'''
get_desodorant_garnier_spring_spirit = tag.create_tag(36)

'''Тэг,возвращающий информацию о яблоках Гала'''
get_apple_gala = tag.create_tag(37)

'''Тэг,возвращающий информацию о сметане "Галичанська 15% 370 грамм"'''
get_smetana_galichanska_15_370gr=tag.create_tag(38)

'''Тэг,возвращающий информацию о чипсах "Lays с солью 30 гр" большая пачка'''
get_chips_lays_salt_big_pack_30g=tag.create_tag(39)

'''Тэг,возвращающий информацию о напитке "Sprite 2 литра"'''
get_sprite_2l=tag.create_tag(40)

'''Тэг,возвращающий информацию о напитке "Fanta 2 литра"'''
get_fanta_2l=tag.create_tag(41)

'''Тэг,возвращающий информацию о сигаретах "BOND STREET BLUE SELECTION"'''
get_bond_street_blue_selection = tag.create_tag(42)

'''Тэг,возвращающий информацию о сигаретах "CAMEL BLUE"'''
get_camel_blue=tag.create_tag(43)

'''Тэг,возвращающий информацию о сигаретах "LD RED"'''
get_ld_red = tag.create_tag(44)

'''Тэг,возвращающий информацию о сигаретах "MARLBORO GOLD"'''
get_marlboro_gold = tag.create_tag(45)

'''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI BLUE EXCLUSIVE"'''
get_rothmans_demi_blue_exclusive=tag.create_tag(46)

'''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI CLICK PURPLE"'''
get_rothmans_demi_click_purple=tag.create_tag(47)

'''Тэг,возвращающий информацию о сигаретах "WINSTON CASTER"'''
get_winston_caster = tag.create_tag(48)

'''Тэг,возвращающий информацию о сигаретах "PARLAMENT AQUA BLUE"'''
get_parlament_aqua_blue = tag.create_tag(49)

'''Тэг,возвращающий информацию о сигаретах "WINSTON BLUE"'''
get_winston_blue = tag.create_tag(50)

'''Тэг,возвращающий информацию о сигаретах "BOND STREET RED SELECTION"'''
get_bond_street_red_selection = tag.create_tag(51)

'''Тэг,возвращающий информацию о сигаретах "LD BLUE"'''
get_ld_blue = tag.create_tag(52)

'''Тэг,возвращающий информацию о сигаретах "KENT SILVER"'''
get_kent_silver = tag.create_tag(53)

'''Тэг,возвращающий информацию о сигаретах "KENT NAVI BLUE NEW"'''
get_kent_navi_blue_new = tag.create_tag(54)

'''Тэг,возвращающий информацию о пиве "Черниговское Светлое 0,5 в стеклянной бутылке"'''
get_beer_chernigivske_svitle_05_l_glass = tag.create_tag(55)

'''Тэг,возвращающий информацию о пиве "Stella Artois 0,5 в стеклянной бутылке"'''
get_beer_stella_artois_05_l_glass = tag.create_tag(56)

'''Тэг,возвращающий информацию о пиве "Оболонь Светлое 0,5 в стеклянной бутылке"'''
get_beer_obolon_svitle_05_l_glass = tag.create_tag(57)

'''Тэг,возвращающий информацию о пиве "Жигулевское Светлое 0,5 в стеклянной бутылке"'''
get_beer_jigulivsle_svitle_05_l_glass = tag.create_tag(58)

'''Тэг,возвращающий информацию о пиве "Рогань традиционное Светлое 0,5 в стеклянной бутылке"'''
get_beer_rogan_tradiciyne_svitle_05_l_glass = tag.create_tag(59)

'''Тэг,возвращающий информацию о пиве "Corona Extra светлое 0,33 в стеклянной бутылке"'''
get_beer_corona_extra_svitle_033_l_glass = tag.create_tag(60)

'''Тэг,возвращающий информацию о пиве "Черниговоское Белое нефильтрованное 0,5 в стеклянной бутылке"'''
get_beer_chernigivske_bile_nefilter_05_l_glass = tag.create_tag(61)

'''Тэг,возвращающий информацию о пиве "Янтарь Светлое 0,5 в стеклянной бутылке"'''
get_beer_yantar_svitle_05_l_glass=tag.create_tag(62)

'''Тэг,возвращающий информацию о пиве "Zibert Светлое 0,5 в стеклянной бутылке"'''
get_beer_zibert_svitle_05_l_glass = tag.create_tag(63)

'''Тэг,возвращающий информацию о пиве "Арсенал мицне 0,5 в стеклянной бутылке"'''
get_beer_arsenal_micne_05_l_glass = tag.create_tag(64)

'''Тэг,возвращающий информацию о пиве "Перша Броварня Закарпатське 0,5 в стеклянной бутылке"'''
get_beer_persha_brovarna_zakarpatske_05_l_glass = tag.create_tag(65)

'''Тэг,возвращающий информацию о пиве "Львовское Светлое 0,5 в стеклянной бутылке"'''
get_beer_lvivske_svitle_05_l_glass = tag.create_tag(66)

'''Тэг,возвращающий информацию о пиве "Львовское 1715 0,5 в стеклянной бутылке"'''
get_beer_lvivske_1715_05_l_glass = tag.create_tag(67)

'''Тэг,возвращающий информацию о пиве "Zlata Praha 0,5 в стеклянной бутылке"'''
get_beer_zlata_praha_05_l_glass = tag.create_tag(68)

'''Тэг,возвращающий информацию о пиве "Tuborg Green 0,5 в стеклянной бутылке"'''
get_beer_tuborg_green_05_l_glass = tag.create_tag(69)

'''Тэг,возвращающий информацию о пиве "Славутич ICE MIX Lime 0,5 в стеклянной бутылке"'''
get_beer_slavutich_ice_mix_lime_05_l_glass = tag.create_tag(70)

'''Тэг,возвращающий информацию о пиве "Тетерев светлое 0,5 в стеклянной бутылке"'''
get_beer_teteriv_svitle_05_l_glass = tag.create_tag(71)

'''Тэг,возвращающий информацию о пиве "Krusovice сетлое 0,5 в стеклянной бутылке"'''
get_beer_krusovice_svitle_05_l_glass = tag.create_tag(72)

'''Тэг,возвращающий информацию о пиве "Heineken светлое 0,5 в стеклянной бутылке"'''
get_beer_heineken_svitle_05_l_glass = tag.create_tag(73)

'''Тэг,возвращающий информацию о пиве "Amstel светлое 0,5 в стеклянной бутылке"'''
get_beer_amstel_svitle_05_l_glass = tag.create_tag(74)

'''Тэг,возвращающий информацию о пиве "Hike premium 0,5 в стеклянной бутылке"'''
get_beer_hike_premium_05_l_glass = tag.create_tag(75)

'''Тэг,возвращающий информацию о пиве "Бочкове светлое 0,5 в стеклянной бутылке"'''
get_beer_bochkove_svitle_05_l_glass = tag.create_tag(76)

'''Тэг,возвращающий информацию о пиве "Kronenbourg 1664 Blanc светлое 0,5 в стеклянной бутылке"'''
get_beer_kronenbourg_1664_blanc_svitle_05_l_glass = tag.create_tag(77)

'''Тэг,возвращающий информацию о пиве "Опилля непастеризоване  светлое 0,5 в стеклянной бутылке"'''
get_beer_opilla_nepasterizovane_svitle_05_l_glass = tag.create_tag(78)

'''Тэг,возвращающий информацию о пиве "Ячменный Колос светлое 0,5 в стеклянной бутылке"'''
get_beer_yachmenniy_kolos_svitle_05_l_glass = tag.create_tag(79)

'''Тэг,возвращающий информацию о пиве "Опилля Корифей светлое 0,5 в стеклянной бутылке"'''
get_beer_opilla_korifey_svitle_05_l_glass = tag.create_tag(80)

'''Тэг,возвращающий информацию о пиве "Чайка Днепроская светлое 0,5 в стеклянной бутылке"'''
get_beer_chaika_dneprovskaya_svitle_05_l_glass = tag.create_tag(81)

'''Тэг,возвращающий информацию о пиве "Чайка Черноморская светлое 0,5 в стеклянной бутылке"'''
get_beer_chaika_chernomorskaya_svitle_05_l_glass = tag.create_tag(82)

'''Тэг,возвращающий информацию о пиве "Умань пиво Waissburg светлое 1 л в пластиковой бутылке"'''
get_beer_uman_waissburg_svitle_1_l_plastic = tag.create_tag(83)

'''Тэг,возвращающий информацию о пиве "Умань пиво пшеничное светлое 1 л в пластиковой бутылке"'''
get_beer_uman_pshenichnoe_svitle_1_l_plastic = tag.create_tag(84)

'''Тэг,возвращающий информацию о пиве "Бердичевское хмельное пиво светлое 1 л в пластиковой бутылке"'''
get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic = tag.create_tag(85)

'''Тэг,возвращающий информацию о пиве "Бердичевское лагер светлое 1 л в пластиковой бутылке"'''
get_beer_berdichevskoe_lager_svitle_1_l_plastic = tag.create_tag(86)

'''Тэг,возвращающий информацию о пиве "Опилля Корифей 1.1 л в пластиковой бутылке"'''
get_beer_opilla_korifey_11_l_plastic = tag.create_tag(87)

'''Тэг,возвращающий информацию о пиве "Оболонь жигулевское экспортное 1,5 л в пластиковой бутылке"'''
get_beer_obolon_jigulivske_eksport_15_l_plastic = tag.create_tag(88)

'''Тэг,возвращающий информацию о пиве "Янтарь светлое 1,2 л в пластиковой бутылке"'''
get_beer_yantar_svitle_12_l_plastic = tag.create_tag(89)

'''Тэг,возвращающий информацию о пиве "Жашковское пшеничное нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic = tag.create_tag(90)

'''Тэг,возвращающий информацию о пиве "Жашковское светлое нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_svitle_nefilter_1_l_plastic = tag.create_tag(91)

'''Тэг,возвращающий информацию о пиве "Жашковское жигулевское нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic = tag.create_tag(92)

'''Тэг,возвращающий информацию о пиве "Перша приватна броварня бочкове 1 л в пластиковой бутылке"'''
get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic = tag.create_tag(93)

'''Тэг,возвращающий информацию о пиве "Чайка днипровська 1 л в пластиковой бутылке"'''
get_beer_chayka_dniprovska_1_l_plastic = tag.create_tag(94)

'''Тэг,возвращающий информацию о "Кетчуп Торчин с чесноком 270 гр"'''
get_ketchup_torchin_s_chesnokom = tag.create_tag(95)

'''Тэг,возвращающий информацию о "Майонез Королевский смак королевский 300 гр"'''
get_mayonez_korolivkiy_smak_korolivskiy_67_300gr = tag.create_tag(96)

'''Тэг,возвращающий информацию о "Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг"'''
get_muka_zolote_zernyatko_pshenichne_2kg = tag.create_tag(97)

'''Тэг,возвращающий информацию о "Пиво Черниговское Белое 1 литр в пластике"'''
get_beer_chernigivske_bile_1l_plastic = tag.create_tag(98)

'''Тэг,возвращающий информацию о "Пиво Оболонь светлое 1 литр в пластике"'''
get_beer_obolon_svitle_1l_plastic = tag.create_tag(99)

'''Тэг,возвращающий информацию о "Пиво Рогань традиционное светлое 1 литр в пластике"'''
get_beer_rogan_tradiciyne_svitle_1l_plastic = tag.create_tag(100)

'''Тэг,возвращающий информацию о "Соус Торчин чесночный 200 грамм"'''
get_sous_torchin_chesnochniy_200gr = tag.create_tag(101)

'''Тэг,возвращающий информацию о "Орбит клубника-банан"'''
get_jvachka_orbit_clubnika_banan = tag.create_tag(102)

'''Тэг,возвращающий информацию о "Сигареты LM красные"'''
get_sigarets_LM_red = tag.create_tag(103)

'''Тэг,возвращающий информацию о "Пиво Жигулевское 2л в пластике"'''
get_beer_jigulivske_2l_plastic = tag.create_tag(104)

'''Тэг,возвращающий информацию о "Пиво Чайка днипровская 2л в пластике"'''
get_beer_chayka_dniprovskaya_2l_plastic = tag.create_tag(105)

'''Тэг,возвращающий информацию о "Пиво Piwny Kubek  2л в пластике"'''
get_beer_piwny_kubek_2l_plastic = tag.create_tag(106)

'''Тэг,возвращающий информацию о "Кетчуп Торчин до шашлику 270 грамм"'''
get_ketchup_torchin_do_shasliky_270gr = tag.create_tag(107)

'''Тэг,возвращающий информацию о "Майонез Чумак аппетитный 50% 300 грамм"'''
get_mayonez_chumak_appetitniy_50_300gr = tag.create_tag(108)

'''Тэг,возвращающий информацию о "Колбаса Перша Столиця Салями Фирменная высший сорт"'''
get_kolbasa_persha_stolica_salyami_firmova_vs = tag.create_tag(109)

'''Тэг,возвращающий информацию о "Кофе Чорна Карта GOLD 50 грамм"'''
get_cofee_chorna_karta_gold_50gr = tag.create_tag(110)

'''Тэг,возвращающий информацию о "Пиво Арсенал "Міцне" світле, 2л"'''
get_beer_arsenal_micne_svitle_2l_plastic = tag.create_tag(111)

'''Тэг,возвращающий информацию о "Пиво "ППБ Бочкове" світле, 2л"'''
get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic = tag.create_tag(112)

'''Тэг,возвращающий информацию о "Пиво "ППБ Закарпатське оригінальне" світле, 2л"'''
get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic = tag.create_tag(113)

'''Тэг,возвращающий информацию о "Пиво Zibert сетлое 0,5 л в банке"'''
get_beer_zibert_svitle_05_l_banochnoe = tag.create_tag(114)

'''Тэг,возвращающий информацию о "Йогурт Фанни лесные ягоды 1,5% 240 грамм"'''
get_yogurt_fanni_lisovi_yagodi_1_5_240gr = tag.create_tag(115)

'''Тэг,возвращающий информацию о "Кефир Славия 2,5 % 850 грамм"'''
get_kefir_slaviya_2_5_850gr = tag.create_tag(116)

'''Тэг,возвращающий информацию о "Пиво Оболонь Киевское разливное светлое 1,95 л в пластике"'''
get_beer_obolon_kievskoe_razlivnoe_svetloe_195l_plastic = tag.create_tag(117)

'''Тэг,возвращающий информацию о "Пиво Черниговское light светлое 2,0 л в пластике"'''
get_beer_chernigivske_light_svitle_2l_plastic = tag.create_tag(118)

'''Тэг,возвращающий информацию о "Пиво Опилля Корифей светлое 2,0 л в пластике"'''
get_beer_opilla_korifey_svitle_2l_plastic = tag.create_tag(119)

'''Тэг,возвращающий информацию о "Пиво Янтарь светлое 2,0 л в пластике"'''
get_beer_yantar_svitle_2l_plastic = tag.create_tag(120)

'''Тэг,возвращающий информацию о "Пиво Tuborg Green 4 банки х 0,5 л"'''
get_beer_tuborg_green_svitle_4_banki_05l = tag.create_tag(121)

'''Тэг,возвращающий информацию о "Пиво ППБ Закарпатське 4 банки х 0,5 л"'''
get_beer_ppb_zakarpatske_svitle_4_banki_05l = tag.create_tag(122)

'''Тэг,возвращающий информацию о "Пиво ППБ Бочкове 4 банки х 0,5 л"'''
get_beer_ppb_bochkove_svitle_4_banki_05l = tag.create_tag(123)

'''Тэг,возвращающий информацию о "Пиво Budweiser Budvar светлое 0,5 л в стекле"'''
get_beer_budweiser_budvar_05l_glass = tag.create_tag(124)

'''Тэг,возвращающий информацию о "Пиво Pilsner Urquell светлое 0,5 л в стекле"'''
get_beer_pilsner_urquell_05l_glass = tag.create_tag(125)

'''Тэг,возвращающий информацию о "Пиво Robert Doms бельгийский светлое нефильтрованное 0,5 л в стекле"'''
get_beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass = tag.create_tag(126)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Чернігівське світле жб"'''
get_beer_chernigivske_svitle_05l_jb = tag.create_tag(127)

'''Тэг,возвращающий информацию о "Пивo 0,5 л Чepнігівськe Білe жб"'''
get_beer_chernigivske_bile_nefilter_05l_jb = tag.create_tag(128)

'''Тэг,возвращающий информацию о "Пиво 0,5л Velkopopovicky Kozel темне жб"'''
get_beer_velkopopovicky_kozel_temne_05l_jb = tag.create_tag(129)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Pilsner світле фільтроване жб"'''
get_beer_edelmeister_pilsner_svitle_05l_jb = tag.create_tag(130)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Faxe світле фільтроване жб"'''
get_beer_faxe_svitle_05l_jb = tag.create_tag(131)

'''Тэг,возвращающий информацию о "Пиво 0,5л Livu Pilzenes світле фільтроване жб"'''
get_beer_livu_pilzenes_svitle_05l_jb=tag.create_tag(132)

'''Тэг,возвращающий информацию о "Пиво 0,5л Velkopopovicky Kozel світле жб"'''
get_beer_velkopopovicky_kozel_svitle_05l_jb = tag.create_tag(133)

'''Тэг,возвращающий информацию о "Пиво 0,5л Оболонь BeerMix Лимон жб"'''
get_beer_obolon_beermix_limon_svitle_05l_jb = tag.create_tag(134)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Weizenbier світле нефільтроване жб"'''
get_beer_edelmeister_weizenbier_nefilter_svitle_05l_jb = tag.create_tag(135)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Schwarzbier темне фільтроване жб"'''
get_beer_edelmeister_schwarzbier_temne_05l_jb = tag.create_tag(136)

'''Тэг,возвращающий информацию о "Пивo 0,5л Hike Blanche світлe нeфільтpoвaнe жб"'''
get_beer_hike_blanche_svitle_nefilter_05l_jb = tag.create_tag(137)

'''Тэг,возвращающий информацию о "Пиво 0,5л Zlata Praha світле жб"'''
get_beer_zlata_praha_svitle_05l_jb = tag.create_tag(138)

'''Тэг,возвращающий информацию о "Пиво 0,5л Thuringer Premium Beer світле фільтроване жб"'''
get_beer_thuringer_premium_beer_svitle_05l_jb = tag.create_tag(139)

'''Тэг,возвращающий информацию о "Пиво 0,5л Livu Sencu світле фільтроване жб"'''
get_beer_livu_sencu_svitle_05l_jb = tag.create_tag(140)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Germanarich светлое жб"'''
get_beer_germanarich_svitle_05l_jb = tag.create_tag(141)

'''Тэг,возвращающий информацию о "Пиво 0,5л Hike Преміум світле жб"'''
get_beer_hike_premium_svitle_05l_jb = tag.create_tag(142)

'''Тэг,возвращающий информацию о "Пивo бeзaлкoгoльнe 0,5л Обoлoнь 0 світлe нефільтроване пaстepизoвaнe жб"'''
get_beer_obolon_svitle_nefilter_nonalcohol_05l_jb = tag.create_tag(143)


# @register.simple_tag()
# def get_obolon_premium():
#     '''Тэг, возвращающий информацию о пиве "Оболонь Прмиум 1,1 л из БД"'''
#     return ItemsPicsFromNet.objects.get(pk=2)


# ТЕГИ ДЛЯ БЛЮД
class SimpleTagMakerForDishes:
    '''Класс для формирования шаблонных тегов для блюд'''
    @register.simple_tag()
    def create_tag(self,pk):
        '''Формирование самой функции для тега'''
        return InfoAboutDishes.objects.get(pk=pk)

#Объект класса для формирования тегов для блюд
dish_tag = SimpleTagMakerForDishes()

'''Тег , возвращающий информацю о борще украинском'''
get_borsh_ukr_info = dish_tag.create_tag(1)

'''Тег , возвращающий информацю о варениках с картошкой'''
get_vareniki_s_kartoshkoy_info = dish_tag.create_tag(2)



# ТЕГ ДЛЯ ПРОДУКТОВОГО НАБОРА
@register.simple_tag()
def get_product_set_from_data_base():
    '''Возьмем все продукты,что есть в наборе пользователя'''
    return SetOfProducts.objects.all()


# ТЕГ ДЛЯ ДОСУТПА КО ВСЕМ СУПЕРМАРКЕТАМ
@register.simple_tag()
def get_all_markets():
    '''С помощбю этого тега получаем доступ ко всем названиям досутпных супермаркетов'''
    return RelevantMarkets.objects.all()
