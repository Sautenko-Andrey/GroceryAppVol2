import os, glob

import json

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from rest_framework import generics

from my_app.utils import MutualContext, get_products_prices, best_price_identify
from django.views.generic import ListView, CreateView

from .forms import *

from .serializers import MainPageSerializer, SitePoliticsSerializer, ItemsFromNetSerializer

from .tester_for_groceryappNNphoto import TesterForGroceryAppPhoto as NN
from .tester_for_groceryappNN_TEXT import TesterForGroceryAppText as NN_text

from .templatetags.my_app_tags import *

from .parsers import *

from rest_framework.pagination import PageNumberPagination
from .permissions import ReadOnlyPermission

from django.shortcuts import redirect

with open('/home/andrey/GroceryAppVol2/FBApp/my_app/prices_store.json') as f:
    store = json.load(f)


class my_appHome(MutualContext, ListView):
    """Класс-обработчик главной страницы приложения"""

    model = MainPage
    template_name = 'my_app/index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        # начало работы парсеров
        # parser = ProductParsers()
        # res_usd = parser.dollar_value_parcer()[:6]
        # context_dict['usd_value_nbu'] = res_usd

        mutual_context_dict = self.get_user_context(title='Самые выгодные предложения от супермаркетов')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class PhotoAnswerPage(MutualContext, ListView):
    '''Класс-обработчик для страницы сайта,
    на которой пользователь будет видеть результат ответа приложения.
    '''
    model = UserPhotoUploadModel_2
    template_name = 'my_app/photo_answer.html'
    context_object_name = 'data'

    def NN_works(self):
        '''Метод, загружающий фото пользователя и пропускающий его через НС'''

        user_image = '/home/andrey/GroceryAppVol2/FBApp/media/photos'
        pred = NN()
        result = pred.identify_item(user_image)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['nn_answer'] = self.NN_works()  # подключение НС:

        # подключение тэгов для отображние изображений товара:
        if context_dict['nn_answer'] == 'Пиво "Оболонь Премиум Экстра 1.1 л"':
            context_dict['item_image_for_user'] = get_obolon_premium
            # метод подключения к собственной базе данных цен
            context_dict['price_from_site_atb'] = store['obolon_premium_1.1_l']['atb']
            context_dict['price_from_site_eko'] = store['obolon_premium_1.1_l']['eko']
            # метод подключения парсеров в режиме online
            # parser = ProductParserVol2()
            # res_atb = parser.obolon_premium_parser()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.obolon_premium_parser()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.obolon_premium_parser()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Водка "Гетьман ICE 0,7 л"':
            context_dict['item_image_for_user'] = get_hetman_ICE
            context_dict['price_from_site_atb'] = store['vodka_hetman_ice_07']['atb']
            # parser = ProductParserVol2()
            # res_atb = parser.vodka_getman_ICE_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.vodka_getman_ICE_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.vodka_getman_ICE_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Кофе растворимый "Aroma Gold Classic 100 грамм"':
            context_dict['item_image_for_user'] = coffe_aroma_gold_classic_100gr
            context_dict['price_from_site_eko'] = store['coffee_aroma_gold']['eko']
            context_dict['price_from_site_fozzy'] = store['coffee_aroma_gold']['fozzy']
            # parser = ProductParserVol2()
            # res_atb=parser.coffee_aroma_gold_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.coffee_aroma_gold_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.coffee_aroma_gold_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Масло подсолнечное "Щедрый Дар" 0,85 л':
            context_dict['item_image_for_user'] = get_oil_shedriy_dar_085l
            context_dict['price_from_site_atb'] = store['oil_shedriy_dar_raf_850']['atb']
            context_dict['price_from_site_eko'] = store['oil_shedriy_dar_raf_850']['eko']
            context_dict['price_from_site_varus'] = store['oil_shedriy_dar_raf_850']['varus']
            context_dict['price_from_site_silpo'] = store['oil_shedriy_dar_raf_850']['silpo']
            context_dict['price_from_site_ashan'] = store['oil_shedriy_dar_raf_850']['ashan']
            context_dict['price_from_site_novus'] = store['oil_shedriy_dar_raf_850']['novus']
            context_dict['price_from_site_metro'] = store['oil_shedriy_dar_raf_850']['metro']
            context_dict['price_from_site_fozzy'] = store['oil_shedriy_dar_raf_850']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.oil_shedriy_dar_850_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.oil_shedriy_dar_850_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.oil_shedriy_dar_850_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.oil_shedriy_dar_850_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo
            # res_ashan = parser.oil_shedriy_dar_850_parcer()[4]
            # context_dict['price_from_site_ashan'] = res_ashan

        elif context_dict['nn_answer'] == 'Яблоко Голден, 1 кг':
            context_dict['item_image_for_user'] = get_apple_golden
            context_dict['price_from_site_atb'] = store['apple_golden']['atb']
            context_dict['price_from_site_eko'] = store['apple_golden']['eko']
            context_dict['price_from_site_varus'] = store['apple_golden']['varus']
            context_dict['price_from_site_silpo'] = store['apple_golden']['silpo']
            context_dict['price_from_site_metro'] = store['apple_golden']['metro']
            context_dict['price_from_site_nash_kray'] = store['apple_golden']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['apple_golden']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.apple_golden_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.apple_golden_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.apple_golden_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.apple_golden_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Напиток безалкогольный "Coca-Cola" 2 л':
            context_dict['item_image_for_user'] = get_coca_cola_2l
            context_dict['price_from_site_atb'] = store['coca_cola_2l']['atb']
            context_dict['price_from_site_eko'] = store['coca_cola_2l']['eko']
            context_dict['price_from_site_varus'] = store['coca_cola_2l']['varus']
            context_dict['price_from_site_silpo'] = store['coca_cola_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['coca_cola_2l']['ashan']
            context_dict['price_from_site_novus'] = store['coca_cola_2l']['novus']
            context_dict['price_from_site_metro'] = store['coca_cola_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['coca_cola_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['coca_cola_2l']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.coca_cola_2l_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.coca_cola_2l_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.coca_cola_2l_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.coca_cola_2l_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo
            # res_ashan = parser.coca_cola_2l_parcer()[4]
            # context_dict['price_from_site_ashan'] = res_ashan

        elif context_dict['nn_answer'] == 'Сырок плавленный "Комо Паприкаш"':
            context_dict['item_image_for_user'] = get_KOMO_paprikash
            context_dict['price_from_site_novus'] = store['sir_plavlenniy_komo_paprikash']['novus']
            context_dict['price_from_site_metro'] = store['sir_plavlenniy_komo_paprikash']['metro']
            context_dict['price_from_site_nash_kray'] = store['sir_plavlenniy_komo_paprikash']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['sir_plavlenniy_komo_paprikash']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты "Kent 8"':
            context_dict['item_image_for_user'] = get_sigarets_kent_8
            context_dict['price_from_site_atb'] = store['sigarets_kent_8']['atb']
            context_dict['price_from_site_eko'] = store['sigarets_kent_8']['eko']
            context_dict['price_from_site_varus'] = store['sigarets_kent_8']['varus']
            context_dict['price_from_site_silpo'] = store['sigarets_kent_8']['silpo']
            context_dict['price_from_site_ashan'] = store['sigarets_kent_8']['ashan']
            context_dict['price_from_site_novus'] = store['sigarets_kent_8']['novus']
            context_dict['price_from_site_fozzy'] = store['sigarets_kent_8']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.kent_8_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.kent_8_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.kent_8_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.kent_8_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Чеснок, кг':
            context_dict['item_image_for_user'] = get_garlik
            context_dict['price_from_site_atb'] = store['garlik']['atb']
            context_dict['price_from_site_eko'] = store['garlik']['eko']
            context_dict['price_from_site_varus'] = store['garlik']['varus']
            context_dict['price_from_site_silpo'] = store['garlik']['silpo']
            context_dict['price_from_site_novus'] = store['garlik']['novus']
            context_dict['price_from_site_nash_kray'] = store['garlik']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['garlik']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.garlik_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.garlik_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.garlik_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.garlik_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Моющее средство Fairy':
            context_dict['item_image_for_user'] = get_fairy_500_lime
            context_dict['price_from_site_atb'] = store['fairy_limon_500']['atb']
            context_dict['price_from_site_eko'] = store['fairy_limon_500']['eko']
            context_dict['price_from_site_varus'] = store['fairy_limon_500']['varus']
            context_dict['price_from_site_silpo'] = store['fairy_limon_500']['silpo']
            context_dict['price_from_site_novus'] = store['fairy_limon_500']['novus']
            context_dict['price_from_site_metro'] = store['fairy_limon_500']['metro']
            context_dict['price_from_site_fozzy'] = store['fairy_limon_500']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.fairy_limon_500_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.fairy_limon_500_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.fairy_limon_500_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.fairy_limon_500_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Лук, 1 кг':
            context_dict['item_image_for_user'] = get_onion
            context_dict['price_from_site_atb'] = store['onion']['atb']
            context_dict['price_from_site_eko'] = store['onion']['eko']
            context_dict['price_from_site_varus'] = store['onion']['varus']
            context_dict['price_from_site_silpo'] = store['onion']['silpo']
            context_dict['price_from_site_novus'] = store['onion']['novus']
            context_dict['price_from_site_metro'] = store['onion']['metro']
            context_dict['price_from_site_nash_kray'] = store['onion']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['onion']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.onion_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.onion_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.onion_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo=parser.onion_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Яблоко "Черный принц"':
            context_dict['item_image_for_user'] = get_apple_black_prince
            context_dict['price_from_site_atb'] = store['apple_black_prince']['atb']
            context_dict['price_from_site_eko'] = store['apple_black_prince']['eko']
            context_dict['price_from_site_varus'] = store['apple_black_prince']['varus']
            context_dict['price_from_site_silpo'] = store['apple_black_prince']['silpo']
            context_dict['price_from_site_metro'] = store['apple_black_prince']['metro']
            context_dict['price_from_site_fozzy'] = store['apple_black_prince']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.apple_black_prince_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.apple_black_prince_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.apple_black_prince_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.apple_black_prince_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Сметана "Столица Смаку" 20% 400 гр':
            context_dict['item_image_for_user'] = get_smetana_stolica_smaky_20_400gr
            context_dict['price_from_site_varus'] = store['smetana_stol_smaky_20%']['varus']
            # parser = ProductParserVol2()
            # res_atb = parser.smetana_stolica_smaky_400_20()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.smetana_stolica_smaky_400_20()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.smetana_stolica_smaky_400_20()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Горчица "Колос"':
            context_dict['item_image_for_user'] = get_gorchica_kolos
            # нет на сайтах

        elif context_dict['nn_answer'] == 'Лимон, кг':
            context_dict['item_image_for_user'] = get_limon
            context_dict['price_from_site_atb'] = store['limon']['atb']
            context_dict['price_from_site_eko'] = store['limon']['eko']
            context_dict['price_from_site_varus'] = store['limon']['varus']
            context_dict['price_from_site_silpo'] = store['limon']['silpo']
            context_dict['price_from_site_novus'] = store['limon']['novus']
            context_dict['price_from_site_metro'] = store['limon']['metro']
            context_dict['price_from_site_nash_kray'] = store['limon']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['limon']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.limon_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.limon_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.limon_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.limon_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Масло подсолнечное "Олейна" нерафинированное, 850 гр':
            context_dict['item_image_for_user'] = get_oil_oleyna_neraf_850
            context_dict['price_from_site_eko'] = store['oil_oleyna_neraf_850']['eko']
            context_dict['price_from_site_ashan'] = store['oil_oleyna_neraf_850']['ashan']
            # parser = ProductParserVol2()
            # res_atb = parser.oil_oleyna_neraf_850_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.oil_oleyna_neraf_850_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.oil_oleyna_neraf_850_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Дрожжи "Харьковские", 100 гр':
            context_dict['item_image_for_user'] = get_drojji_hark
            # out of stock

        elif context_dict['nn_answer'] == 'Чай черный "Мономах Кения", 90 гр':
            context_dict['item_image_for_user'] = get_tea_monomah_kenya
            context_dict['price_from_site_eko'] = store['tea_monomah_kenya_90']['eko']
            # parser = ProductParserVol2()
            # res_atb = parser.tea_monomah_black_kenya_90_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.tea_monomah_black_kenya_90_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.tea_monomah_black_kenya_90_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Пена для бритья "Arko Cool" 300 гр+100':
            context_dict['item_image_for_user'] = get_arko_cool_300_100
            context_dict['price_from_site_atb'] = store['arko_cool_200']['atb']
            context_dict['price_from_site_eko'] = store['arko_cool_200']['eko']
            context_dict['price_from_site_varus'] = store['arko_cool_200']['varus']
            context_dict['price_from_site_silpo'] = store['arko_cool_200']['silpo']
            context_dict['price_from_site_ashan'] = store['arko_cool_200']['ashan']
            context_dict['price_from_site_novus'] = store['arko_cool_200']['novus']
            context_dict['price_from_site_metro'] = store['arko_cool_200']['metro']
            context_dict['price_from_site_fozzy'] = store['arko_cool_200']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.arko_cool_200_bonus100_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.arko_cool_200_bonus100_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.arko_cool_200_bonus100_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.arko_cool_200_bonus100_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Пена для бритья "Arko Sensitive" 300 гр+100':
            context_dict['item_image_for_user'] = get_arko_sensitive_300_100
            context_dict['price_from_site_atb'] = store['arko_sensitive_200']['atb']
            context_dict['price_from_site_eko'] = store['arko_sensitive_200']['eko']
            context_dict['price_from_site_varus'] = store['arko_sensitive_200']['varus']
            context_dict['price_from_site_silpo'] = store['arko_sensitive_200']['silpo']
            context_dict['price_from_site_ashan'] = store['arko_sensitive_200']['ashan']
            context_dict['price_from_site_novus'] = store['arko_sensitive_200']['novus']
            context_dict['price_from_site_metro'] = store['arko_sensitive_200']['metro']
            context_dict['price_from_site_nash_kray'] = store['arko_sensitive_200']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['arko_sensitive_200']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.arko_sensitive_200_bonus100_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.arko_sensitive_200_bonus100_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.arko_sensitive_200_bonus100_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.arko_sensitive_200_bonus100_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == "Морковь, кг":
            context_dict['item_image_for_user'] = get_carrot
            context_dict['price_from_site_atb'] = store['carrot']['atb']
            context_dict['price_from_site_eko'] = store['carrot']['eko']
            context_dict['price_from_site_varus'] = store['carrot']['varus']
            context_dict['price_from_site_silpo'] = store['carrot']['silpo']
            context_dict['price_from_site_novus'] = store['carrot']['novus']
            context_dict['price_from_site_metro'] = store['carrot']['metro']
            context_dict['price_from_site_nash_kray'] = store['carrot']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['carrot']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.carrot_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.carrot_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.carrot_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.carrot_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Капуста белокачанная, кг':
            context_dict['item_image_for_user'] = get_cabbage
            context_dict['price_from_site_atb'] = store['cabbage']['atb']
            context_dict['price_from_site_eko'] = store['cabbage']['eko']
            context_dict['price_from_site_varus'] = store['cabbage']['varus']
            context_dict['price_from_site_silpo'] = store['cabbage']['silpo']
            context_dict['price_from_site_novus'] = store['cabbage']['novus']
            context_dict['price_from_site_metro'] = store['cabbage']['metro']
            context_dict['price_from_site_nash_kray'] = store['cabbage']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['cabbage']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.cabbage_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.cabbage_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.cabbage_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.cabbage_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Яйца куринные, 10 шт':
            context_dict['item_image_for_user'] = get_chicken_eggs
            context_dict['price_from_site_atb'] = store['eggs']['atb']
            context_dict['price_from_site_eko'] = store['eggs']['eko']
            context_dict['price_from_site_varus'] = store['eggs']['varus']
            context_dict['price_from_site_silpo'] = store['eggs']['silpo']
            context_dict['price_from_site_ashan'] = store['eggs']['ashan']
            context_dict['price_from_site_novus'] = store['eggs']['novus']
            context_dict['price_from_site_metro'] = store['eggs']['metro']
            context_dict['price_from_site_nash_kray'] = store['eggs']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['eggs']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.egg_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.egg_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.egg_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.egg_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Майонез домашний детский "Щедро" 67%':
            context_dict['item_image_for_user'] = get_mayonez_dom_detsk_shedro_67
            context_dict['price_from_site_atb'] = store['mayonez_detsk_shedro_67%']['atb']
            context_dict['price_from_site_eko'] = store['mayonez_detsk_shedro_67%']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_detsk_shedro_67%']['varus']
            context_dict['price_from_site_silpo'] = store['mayonez_detsk_shedro_67%']['silpo']
            context_dict['price_from_site_metro'] = store['mayonez_detsk_shedro_67%']['metro']
            context_dict['price_from_site_fozzy'] = store['mayonez_detsk_shedro_67%']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.mayonez_detsk_shedro_67_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.mayonez_detsk_shedro_67_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.mayonez_detsk_shedro_67_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.mayonez_detsk_shedro_67_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Дезодорант "Rexona Aloe Vera" женский':
            context_dict['item_image_for_user'] = get_reksona_aloe_vera_w
            context_dict['price_from_site_eko'] = store['rexona_aloe_vera']['eko']
            context_dict['price_from_site_ashan'] = store['rexona_aloe_vera']['ashan']
            # parser = ProductParserVol2()
            # res_atb = parser.rexona_aloe_vera_w_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.rexona_aloe_vera_w_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.rexona_aloe_vera_w_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Туалетная бумага "Киев" 63 м':
            context_dict['item_image_for_user'] = get_toilet_papir_kiev_63m
            # out of stock

        elif context_dict['nn_answer'] == 'Сигареты Marlboro red':
            context_dict['item_image_for_user'] = get_marlboro_red
            context_dict['price_from_site_atb'] = store['marlboro_red']['atb']
            context_dict['price_from_site_eko'] = store['marlboro_red']['eko']
            context_dict['price_from_site_varus'] = store['marlboro_red']['varus']
            context_dict['price_from_site_silpo'] = store['marlboro_red']['silpo']
            context_dict['price_from_site_ashan'] = store['marlboro_red']['ashan']
            context_dict['price_from_site_novus'] = store['marlboro_red']['novus']
            context_dict['price_from_site_fozzy'] = store['marlboro_red']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.marloboro_red_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.marloboro_red_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.marloboro_red_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.marloboro_red_parcer()[3]
            # context_dict['price_from_site_silpo'] = res_silpo
            # res_ashan = parser.marloboro_red_parcer()[4]
            # context_dict['price_from_site_ashan'] = res_ashan

        elif context_dict['nn_answer'] == 'Пиво "Львовское светлое", 2.4 литра':
            context_dict['item_image_for_user'] = get_pivo_lvivske_svitle
            context_dict['price_from_site_varus'] = store['beer_lvivske_svetl_2.4 l']['varus']
            context_dict['price_from_site_silpo'] = store['beer_lvivske_svetl_2.4 l']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_lvivske_svetl_2.4 l']['ashan']
            context_dict['price_from_site_fozzy'] = store['beer_lvivske_svetl_2.4 l']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.beer_lvivske_svitle_24l()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.beer_lvivske_svitle_24l()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.beer_lvivske_svitle_24l()[2]
            # context_dict['price_from_site_varus'] = res_varus
            # res_silpo = parser.beer_lvivske_svitle_24l()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Сметана Столица Смаку 400 гр 15% жирности':
            context_dict['item_image_for_user'] = get_smetana_stol_smaku_400_15
            context_dict['price_from_site_varus'] = store['smetana_stol_smaky_15%']['varus']
            # parser = ProductParserVol2()
            # res_atb = parser.smetana_stolica_smaky_400_15_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.smetana_stolica_smaky_400_15_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.smetana_stolica_smaky_400_15_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Дезодорант Garnier Магний мужской':
            context_dict['item_image_for_user'] = get_dezodorant_garnier_magniy_m
            context_dict['price_from_site_silpo'] = store['desodorant_garnier_man']['silpo']
            context_dict['price_from_site_fozzy'] = store['desodorant_garnier_man']['fozzy']
            # parser = ProductParserVol2()
            # res_silpo =parser.desodorant_garnier_magniy_man_parser()[3]
            # context_dict['price_from_site_silpo'] = res_silpo

        elif context_dict['nn_answer'] == 'Чай Мономах Цейлон черный':
            context_dict['item_image_for_user'] = get_tea_monomah_ceylon_black

        elif context_dict['nn_answer'] == 'Кофе Арома Голд Freeze Dried 70 грамм':
            context_dict['item_image_for_user'] = get_coffee_aroma_gold_freeze_dried_70
            context_dict['price_from_site_eko'] = store['cofee_aroma_gold_freeze_dried_70g']['eko']
            context_dict['price_from_site_silpo'] = store['cofee_aroma_gold_freeze_dried_70g']['silpo']
            context_dict['price_from_site_nash_kray'] = store['cofee_aroma_gold_freeze_dried_70g']['nash_kray']

        elif context_dict['nn_answer'] == 'Горчица Верес украинска мицна 120 грамм':
            context_dict['item_image_for_user'] = get_gorchica_veres_micna_ukr_120g
            context_dict['price_from_site_silpo'] = store['gorchica_veres_ukrainska_micna_120g']['silpo']
            context_dict['price_from_site_novus'] = store['gorchica_veres_ukrainska_micna_120g']['novus']
            context_dict['price_from_site_metro'] = store['gorchica_veres_ukrainska_micna_120g']['metro']

        elif context_dict['nn_answer'] == 'Чай Мономах 100% Цейлон Original черный крупнолистовой':
            context_dict['item_image_for_user'] = get_tea_monomah_original_ceylon_90g

        elif context_dict['nn_answer'] == 'Дезодорант Garnier весенняя свежесть':
            context_dict['item_image_for_user'] = get_desodorant_garnier_spring_spirit
            context_dict['price_from_site_silpo'] = store['desodorant_garnier_spring_spirit']['silpo']
            context_dict['price_from_site_novus'] = store['desodorant_garnier_spring_spirit']['novus']
            context_dict['price_from_site_metro'] = store['desodorant_garnier_spring_spirit']['metro']
            context_dict['price_from_site_fozzy'] = store['desodorant_garnier_spring_spirit']['fozzy']

        elif context_dict['nn_answer'] == 'Яблоко Гала, кг':
            context_dict['item_image_for_user'] = get_apple_gala
            context_dict['price_from_site_atb'] = store['apple_gala']['atb']
            context_dict['price_from_site_eko'] = store['apple_gala']['eko']
            context_dict['price_from_site_varus'] = store['apple_gala']['varus']
            context_dict['price_from_site_silpo'] = store['apple_gala']['silpo']
            context_dict['price_from_site_novus'] = store['apple_gala']['novus']
            context_dict['price_from_site_metro'] = store['apple_gala']['metro']
            context_dict['price_from_site_fozzy'] = store['apple_gala']['fozzy']

        elif context_dict['nn_answer'] == 'Сметана Галичанская 15% 370 грамм':
            context_dict['item_image_for_user'] = get_smetana_galichanska_15_370gr
            context_dict['price_from_site_atb'] = store['smetana_galichanska_15_370gr']['atb']
            context_dict['price_from_site_eko'] = store['smetana_galichanska_15_370gr']['eko']
            context_dict['price_from_site_novus'] = store['smetana_galichanska_15_370gr']['novus']
            context_dict['price_from_site_metro'] = store['smetana_galichanska_15_370gr']['metro']
            context_dict['price_from_site_fozzy'] = store['smetana_galichanska_15_370gr']['fozzy']

        elif context_dict['nn_answer'] == 'Чипсы Lays с солью большая пачка 30 грамм':
            context_dict['item_image_for_user'] = get_chips_lays_salt_big_pack_30g
            context_dict['price_from_site_eko'] = store['chips_lays_with_salt_big_pack']['eko']
            context_dict['price_from_site_fozzy'] = store['chips_lays_with_salt_big_pack']['fozzy']

        elif context_dict['nn_answer'] == 'Напиток Sprite 2 литра':
            context_dict['item_image_for_user'] = get_sprite_2l
            context_dict['price_from_site_eko'] = store['sprite_2l']['eko']
            context_dict['price_from_site_varus'] = store['sprite_2l']['varus']
            context_dict['price_from_site_silpo'] = store['sprite_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['sprite_2l']['ashan']
            context_dict['price_from_site_novus'] = store['sprite_2l']['novus']
            context_dict['price_from_site_metro'] = store['sprite_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['sprite_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['sprite_2l']['fozzy']

        elif context_dict['nn_answer'] == 'Напиток Fanta 2 литра':
            context_dict['item_image_for_user'] = get_fanta_2l
            context_dict['price_from_site_eko'] = store['fanta_2l']['eko']
            context_dict['price_from_site_varus'] = store['fanta_2l']['varus']
            context_dict['price_from_site_silpo'] = store['fanta_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['fanta_2l']['ashan']
            context_dict['price_from_site_novus'] = store['fanta_2l']['novus']
            context_dict['price_from_site_metro'] = store['fanta_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['fanta_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['fanta_2l']['fozzy']

        elif context_dict['nn_answer'] == 'Кетчуп Торчин с чесноком 270 гр':
            context_dict['item_image_for_user'] = get_ketchup_torchin_s_chesnokom
            context_dict['price_from_site_eko'] = store['ketchup_torchin_s_chasnikom_270gr']['eko']
            context_dict['price_from_site_varus'] = store['ketchup_torchin_s_chasnikom_270gr']['varus']
            context_dict['price_from_site_metro'] = store['ketchup_torchin_s_chasnikom_270gr']['metro']
            context_dict['price_from_site_fozzy'] = store['ketchup_torchin_s_chasnikom_270gr']['fozzy']

        elif context_dict['nn_answer'] == 'Майонез Королевский Смак королевский 67 % 300 гр':
            context_dict['item_image_for_user'] = get_mayonez_korolivkiy_smak_korolivskiy_67_300gr
            context_dict['price_from_site_atb'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['atb']
            context_dict['price_from_site_eko'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['varus']
            context_dict['price_from_site_novus'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['novus']
            context_dict['price_from_site_metro'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['metro']
            context_dict['price_from_site_fozzy'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['fozzy']

        elif context_dict['nn_answer'] == 'Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг':
            context_dict['item_image_for_user'] = get_muka_zolote_zernyatko_pshenichne_2kg

        elif context_dict['nn_answer'] == 'Соус Чумак чесночный 200 грамм':
            context_dict['item_image_for_user'] = get_sous_torchin_chesnochniy_200gr
            context_dict['price_from_site_eko'] = store['sous_chumak_chesnochniy_200gr']['eko']
            context_dict['price_from_site_varus'] = store['sous_chumak_chesnochniy_200gr']['varus']
            context_dict['price_from_site_novus'] = store['sous_chumak_chesnochniy_200gr']['novus']

        elif context_dict['nn_answer'] == 'Жвачка Orbit полуниця-банан':
            context_dict['item_image_for_user'] = get_jvachka_orbit_clubnika_banan
            context_dict['price_from_site_atb'] = store['orbit_polunica_banan']['atb']
            context_dict['price_from_site_eko'] = store['orbit_polunica_banan']['eko']
            context_dict['price_from_site_varus'] = store['orbit_polunica_banan']['varus']
            context_dict['price_from_site_ashan'] = store['orbit_polunica_banan']['ashan']
            context_dict['price_from_site_novus'] = store['orbit_polunica_banan']['novus']
            context_dict['price_from_site_metro'] = store['orbit_polunica_banan']['metro']
            context_dict['price_from_site_nash_kray'] = store['orbit_polunica_banan']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['orbit_polunica_banan']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты LM красные':
            context_dict['item_image_for_user'] = get_sigarets_LM_red
            context_dict['price_from_site_ashan'] = store['sigarets_lm_red']['ashan']
            context_dict['price_from_site_novus'] = store['sigarets_lm_red']['novus']
            context_dict['price_from_site_fozzy'] = store['sigarets_lm_red']['fozzy']

        elif context_dict['nn_answer'] == 'Кетчуп Торчин до шашлику 270 грамм':
            context_dict['item_image_for_user'] = get_ketchup_torchin_do_shasliky_270gr
            context_dict['price_from_site_eko'] = store['ketchup_torchin_do_shashliky_270gr']['eko']
            context_dict['price_from_site_varus'] = store['ketchup_torchin_do_shashliky_270gr']['varus']
            context_dict['price_from_site_silpo'] = store['ketchup_torchin_do_shashliky_270gr']['silpo']
            context_dict['price_from_site_ashan'] = store['ketchup_torchin_do_shashliky_270gr']['ashan']
            context_dict['price_from_site_novus'] = store['ketchup_torchin_do_shashliky_270gr']['novus']
            context_dict['price_from_site_fozzy'] = store['ketchup_torchin_do_shashliky_270gr']['fozzy']

        elif context_dict['nn_answer'] == 'Майонез Чумак аппетитный 50% 300 грамм':
            context_dict['item_image_for_user'] = get_mayonez_chumak_appetitniy_50_300gr
            context_dict['price_from_site_eko'] = store['mayonez_chumak_appetitniy_50_300gr']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_chumak_appetitniy_50_300gr']['varus']
            context_dict['price_from_site_silpo'] = store['mayonez_chumak_appetitniy_50_300gr']['silpo']
            context_dict['price_from_site_novus'] = store['mayonez_chumak_appetitniy_50_300gr']['novus']
            context_dict['price_from_site_metro'] = store['mayonez_chumak_appetitniy_50_300gr']['metro']

        elif context_dict['nn_answer'] == 'Колбаса Перша Столиця Салями Фирменная высший сорт':
            context_dict['item_image_for_user'] = get_kolbasa_persha_stolica_salyami_firmova_vs

        elif context_dict['nn_answer'] == 'Кофе Чорна Карта GOLD 50 грамм':
            context_dict['item_image_for_user'] = get_cofee_chorna_karta_gold_50gr
            context_dict['price_from_site_eko'] = store['coffee_chorna_karta_50gr']['eko']

        elif context_dict['nn_answer'] == 'Пиво Zibert светлое 0,5 л в банке':
            context_dict['item_image_for_user'] = get_beer_zibert_svitle_05_l_banochnoe
            context_dict['price_from_site_atb'] = store['beer_zibert_svitle_05l_v_banke']['atb']
            context_dict['price_from_site_eko'] = store['beer_zibert_svitle_05l_v_banke']['eko']
            context_dict['price_from_site_varus'] = store['beer_zibert_svitle_05l_v_banke']['varus']
            context_dict['price_from_site_novus'] = store['beer_zibert_svitle_05l_v_banke']['novus']
            context_dict['price_from_site_metro'] = store['beer_zibert_svitle_05l_v_banke']['metro']

        elif context_dict['nn_answer'] == 'Йогурт Фанни 240 грамм 1.5% лесовые ягоды':
            context_dict['item_image_for_user'] = get_yogurt_fanni_lisovi_yagodi_1_5_240gr
            context_dict['price_from_site_varus'] = store['yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan']['varus']
            context_dict['price_from_site_silpo'] = store['yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan']['silpo']

        elif context_dict['nn_answer'] == 'Кефир Славия 2,5% 850 грамм':
            context_dict['item_image_for_user'] = get_kefir_slaviya_2_5_850gr

        else:
            context_dict['item_image_for_user'] = get_tea_minutka_black_40_b
            context_dict['price_from_site_atb'] = store['tea_minutka']['atb']
            context_dict['price_from_site_eko'] = store['tea_minutka']['eko']
            context_dict['price_from_site_metro'] = store['tea_minutka']['metro']
            # parser = ProductParserVol2()
            # res_atb = parser.tea_minutka_black_40_b_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.tea_minutka_black_40_b_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.tea_minutka_black_40_b_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        mutual_context_dict = self.get_user_context(title='Результат поиска')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
                которая была добавлена самой последней'''

        return UserPhotoUploadModel_2.objects.latest('time_create')


class ItemNameAnswerPage(MutualContext, ListView):
    '''Класс-обработчик для страницы сайта,
    на которой пользователь будет видеть результат ответа приложения.
    '''
    model = UserItemNameUpload_2
    template_name = 'my_app/text_answer.html'
    context_object_name = 'data'

    def NN_works(self):
        pred = NN_text()
        user_text = self.get_queryset().user_item_name
        result = pred.identify_item(user_text)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['nn_answer'] = self.NN_works()  # работа НС

        # подключение тэгов для отображние изображений товара:
        if context_dict['nn_answer'] == 'Пиво "Оболонь Премиум Экстра 1,1 л"':
            context_dict['item_image_for_user'] = get_obolon_premium
            # метод подключения к собственной базе данных цен
            context_dict['price_from_site_atb'] = store['obolon_premium_1.1_l']['atb']
            context_dict['price_from_site_eko'] = store['obolon_premium_1.1_l']['eko']
            # parser = ProductParserVol2()
            # res_atb = parser.obolon_premium_parser()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.obolon_premium_parser()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.obolon_premium_parser()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Водка "Гетьман ICE 0,7 л"':
            context_dict['item_image_for_user'] = get_hetman_ICE
            context_dict['price_from_site_atb'] = store['vodka_hetman_ice_07']['atb']
            # parser = ProductParserVol2()
            # res_atb = parser.vodka_getman_ICE_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.vodka_getman_ICE_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.vodka_getman_ICE_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Кофе растворимый "Aroma Gold Classic 100 грамм"':
            context_dict['item_image_for_user'] = coffe_aroma_gold_classic_100gr
            context_dict['price_from_site_eko'] = store['coffee_aroma_gold']['eko']
            context_dict['price_from_site_fozzy'] = store['coffee_aroma_gold']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.coffee_aroma_gold_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.coffee_aroma_gold_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.coffee_aroma_gold_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Напиток Coca Cola 2 л':
            context_dict['item_image_for_user'] = get_coca_cola_2l
            context_dict['price_from_site_atb'] = store['coca_cola_2l']['atb']
            context_dict['price_from_site_eko'] = store['coca_cola_2l']['eko']
            context_dict['price_from_site_varus'] = store['coca_cola_2l']['varus']
            context_dict['price_from_site_silpo'] = store['coca_cola_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['coca_cola_2l']['ashan']
            context_dict['price_from_site_novus'] = store['coca_cola_2l']['novus']
            context_dict['price_from_site_metro'] = store['coca_cola_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['coca_cola_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['coca_cola_2l']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.coca_cola_2l_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.coca_cola_2l_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.coca_cola_2l_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Сырок плавленный КОМО Паприкаш':
            context_dict['item_image_for_user'] = get_KOMO_paprikash
            context_dict['price_from_site_novus'] = store['sir_plavlenniy_komo_paprikash']['novus']
            context_dict['price_from_site_metro'] = store['sir_plavlenniy_komo_paprikash']['metro']
            context_dict['price_from_site_nash_kray'] = store['sir_plavlenniy_komo_paprikash']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['sir_plavlenniy_komo_paprikash']['fozzy']

        elif context_dict['nn_answer'] == 'Чеснок':
            context_dict['item_image_for_user'] = get_garlik
            context_dict['price_from_site_atb'] = store['garlik']['atb']
            context_dict['price_from_site_eko'] = store['garlik']['eko']
            context_dict['price_from_site_varus'] = store['garlik']['varus']
            context_dict['price_from_site_silpo'] = store['garlik']['silpo']
            context_dict['price_from_site_novus'] = store['garlik']['novus']
            context_dict['price_from_site_nash_kray'] = store['garlik']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['garlik']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.garlik_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.garlik_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.garlik_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Сигареты Кент 8':
            context_dict['item_image_for_user'] = get_sigarets_kent_8
            context_dict['price_from_site_atb'] = store['sigarets_kent_8']['atb']
            context_dict['price_from_site_eko'] = store['sigarets_kent_8']['eko']
            context_dict['price_from_site_varus'] = store['sigarets_kent_8']['varus']
            context_dict['price_from_site_silpo'] = store['sigarets_kent_8']['silpo']
            context_dict['price_from_site_ashan'] = store['sigarets_kent_8']['ashan']
            context_dict['price_from_site_novus'] = store['sigarets_kent_8']['novus']
            context_dict['price_from_site_fozzy'] = store['sigarets_kent_8']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.kent_8_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.kent_8_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.kent_8_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Чай "Минутка" черный 40 пакетиков':
            context_dict['item_image_for_user'] = get_tea_minutka_black_40_b
            context_dict['price_from_site_atb'] = store['tea_minutka']['atb']
            context_dict['price_from_site_eko'] = store['tea_minutka']['eko']
            # parser = ProductParserVol2()
            # res_atb = parser.tea_minutka_black_40_b_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.tea_minutka_black_40_b_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.tea_minutka_black_40_b_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Масло подсолнечное "Щедрый Дар" 850 г рафинированное':
            context_dict['item_image_for_user'] = get_oil_shedriy_dar_085l
            context_dict['price_from_site_atb'] = store['oil_shedriy_dar_raf_850']['atb']
            context_dict['price_from_site_eko'] = store['oil_shedriy_dar_raf_850']['eko']
            context_dict['price_from_site_varus'] = store['oil_shedriy_dar_raf_850']['varus']
            context_dict['price_from_site_silpo'] = store['oil_shedriy_dar_raf_850']['silpo']
            context_dict['price_from_site_ashan'] = store['oil_shedriy_dar_raf_850']['ashan']
            context_dict['price_from_site_novus'] = store['oil_shedriy_dar_raf_850']['novus']
            context_dict['price_from_site_metro'] = store['oil_shedriy_dar_raf_850']['metro']
            context_dict['price_from_site_fozzy'] = store['oil_shedriy_dar_raf_850']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.oil_shedriy_dar_850_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.oil_shedriy_dar_850_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.oil_shedriy_dar_850_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Лук, 1 кг':
            context_dict['item_image_for_user'] = get_onion
            context_dict['price_from_site_atb'] = store['onion']['atb']
            context_dict['price_from_site_eko'] = store['onion']['eko']
            context_dict['price_from_site_varus'] = store['onion']['varus']
            context_dict['price_from_site_silpo'] = store['onion']['silpo']
            context_dict['price_from_site_novus'] = store['onion']['novus']
            context_dict['price_from_site_metro'] = store['onion']['metro']
            context_dict['price_from_site_nash_kray'] = store['onion']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['onion']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.onion_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.onion_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.onion_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Средство для мытья посуды Fairy, лимон, 500 г':
            context_dict['item_image_for_user'] = get_fairy_500_lime
            context_dict['price_from_site_atb'] = store['fairy_limon_500']['atb']
            context_dict['price_from_site_eko'] = store['fairy_limon_500']['eko']
            context_dict['price_from_site_varus'] = store['fairy_limon_500']['varus']
            context_dict['price_from_site_silpo'] = store['fairy_limon_500']['silpo']
            context_dict['price_from_site_novus'] = store['fairy_limon_500']['novus']
            context_dict['price_from_site_metro'] = store['fairy_limon_500']['metro']
            context_dict['price_from_site_fozzy'] = store['fairy_limon_500']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.fairy_limon_500_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.fairy_limon_500_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.fairy_limon_500_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Яблоко "Черный принц"':
            context_dict['item_image_for_user'] = get_apple_black_prince
            context_dict['price_from_site_atb'] = store['apple_black_prince']['atb']
            context_dict['price_from_site_eko'] = store['apple_black_prince']['eko']
            context_dict['price_from_site_varus'] = store['apple_black_prince']['varus']
            context_dict['price_from_site_silpo'] = store['apple_black_prince']['silpo']
            context_dict['price_from_site_metro'] = store['apple_black_prince']['metro']
            context_dict['price_from_site_fozzy'] = store['apple_black_prince']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.apple_black_prince_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.apple_black_prince_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.apple_black_prince_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Горчица "Колос"':
            context_dict['item_image_for_user'] = get_gorchica_kolos

        elif context_dict['nn_answer'] == 'Сметана "Столица Смаку" 20% 400 гр':
            context_dict['item_image_for_user'] = get_smetana_stolica_smaky_20_400gr
            context_dict['price_from_site_varus'] = store['smetana_stol_smaky_20%']['varus']
            # parser = ProductParserVol2()
            # res_atb = parser.smetana_stolica_smaky_400_20()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.smetana_stolica_smaky_400_20()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.smetana_stolica_smaky_400_20()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Лимон, 1 кг':
            context_dict['item_image_for_user'] = get_limon
            context_dict['price_from_site_atb'] = store['limon']['atb']
            context_dict['price_from_site_eko'] = store['limon']['eko']
            context_dict['price_from_site_varus'] = store['limon']['varus']
            context_dict['price_from_site_silpo'] = store['limon']['silpo']
            context_dict['price_from_site_novus'] = store['limon']['novus']
            context_dict['price_from_site_metro'] = store['limon']['metro']
            context_dict['price_from_site_nash_kray'] = store['limon']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['limon']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.limon_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.limon_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.limon_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Масло подсолнечное нерафинированное Олейна, 850 гр':
            context_dict['item_image_for_user'] = get_oil_oleyna_neraf_850
            context_dict['price_from_site_eko'] = store['oil_oleyna_neraf_850']['eko']
            context_dict['price_from_site_ashan'] = store['oil_oleyna_neraf_850']['ashan']
            # parser = ProductParserVol2()
            # res_atb = parser.oil_oleyna_neraf_850_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.oil_oleyna_neraf_850_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.oil_oleyna_neraf_850_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Пиво Львовское светлое 2.4 литра':
            context_dict['item_image_for_user'] = get_pivo_lvivske_svitle
            context_dict['price_from_site_varus'] = store['beer_lvivske_svetl_2.4 l']['varus']
            context_dict['price_from_site_silpo'] = store['beer_lvivske_svetl_2.4 l']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_lvivske_svetl_2.4 l']['ashan']
            context_dict['price_from_site_fozzy'] = store['beer_lvivske_svetl_2.4 l']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.beer_lvivske_svitle_24l()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.beer_lvivske_svitle_24l()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.beer_lvivske_svitle_24l()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Пена для бритья "Arko Cool 200 млг + бонус 100 млг"':
            context_dict['item_image_for_user'] = get_arko_cool_300_100
            context_dict['price_from_site_atb'] = store['arko_cool_200']['atb']
            context_dict['price_from_site_eko'] = store['arko_cool_200']['eko']
            context_dict['price_from_site_varus'] = store['arko_cool_200']['varus']
            context_dict['price_from_site_silpo'] = store['arko_cool_200']['silpo']
            context_dict['price_from_site_ashan'] = store['arko_cool_200']['ashan']
            context_dict['price_from_site_novus'] = store['arko_cool_200']['novus']
            context_dict['price_from_site_metro'] = store['arko_cool_200']['metro']
            context_dict['price_from_site_fozzy'] = store['arko_cool_200']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.arko_cool_200_bonus100_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.arko_cool_200_bonus100_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.arko_cool_200_bonus100_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Пена для бритья "Arko Sensitive 200 млг + бонус 100 млг"':
            context_dict['item_image_for_user'] = get_arko_sensitive_300_100
            context_dict['price_from_site_atb'] = store['arko_sensitive_200']['atb']
            context_dict['price_from_site_eko'] = store['arko_sensitive_200']['eko']
            context_dict['price_from_site_varus'] = store['arko_sensitive_200']['varus']
            context_dict['price_from_site_silpo'] = store['arko_sensitive_200']['silpo']
            context_dict['price_from_site_ashan'] = store['arko_sensitive_200']['ashan']
            context_dict['price_from_site_novus'] = store['arko_sensitive_200']['novus']
            context_dict['price_from_site_metro'] = store['arko_sensitive_200']['metro']
            context_dict['price_from_site_nash_kray'] = store['arko_sensitive_200']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['arko_sensitive_200']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.arko_sensitive_200_bonus100_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.arko_sensitive_200_bonus100_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.arko_sensitive_200_bonus100_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Морковь, 1 кг':
            context_dict['item_image_for_user'] = get_carrot
            context_dict['price_from_site_atb'] = store['carrot']['atb']
            context_dict['price_from_site_eko'] = store['carrot']['eko']
            context_dict['price_from_site_varus'] = store['carrot']['varus']
            context_dict['price_from_site_silpo'] = store['carrot']['silpo']
            context_dict['price_from_site_novus'] = store['carrot']['novus']
            context_dict['price_from_site_metro'] = store['carrot']['metro']
            context_dict['price_from_site_nash_kray'] = store['carrot']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['carrot']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.carrot_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.carrot_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.carrot_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Дрожжи харьковские 100 гр хлебо-пекарские пресованные':
            context_dict['item_image_for_user'] = get_drojji_hark

        elif context_dict['nn_answer'] == 'Яйца куринные, 10 штук':
            context_dict['item_image_for_user'] = get_chicken_eggs
            context_dict['price_from_site_atb'] = store['eggs']['atb']
            context_dict['price_from_site_eko'] = store['eggs']['eko']
            context_dict['price_from_site_varus'] = store['eggs']['varus']
            context_dict['price_from_site_silpo'] = store['eggs']['silpo']
            context_dict['price_from_site_ashan'] = store['eggs']['ashan']
            context_dict['price_from_site_novus'] = store['eggs']['novus']
            context_dict['price_from_site_metro'] = store['eggs']['metro']
            context_dict['price_from_site_nash_kray'] = store['eggs']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['eggs']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.egg_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.egg_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.egg_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Дезодорант Garnier Магний для мужчин':
            context_dict['item_image_for_user'] = get_dezodorant_garnier_magniy_m
            context_dict['price_from_site_silpo'] = store['desodorant_garnier_man']['silpo']
            context_dict['price_from_site_fozzy'] = store['desodorant_garnier_man']['fozzy']

        elif context_dict['nn_answer'] == 'Капуста белокачанная , 1 кг':
            context_dict['item_image_for_user'] = get_cabbage
            context_dict['price_from_site_atb'] = store['cabbage']['atb']
            context_dict['price_from_site_eko'] = store['cabbage']['eko']
            context_dict['price_from_site_varus'] = store['cabbage']['varus']
            context_dict['price_from_site_silpo'] = store['cabbage']['silpo']
            context_dict['price_from_site_novus'] = store['cabbage']['novus']
            context_dict['price_from_site_metro'] = store['cabbage']['metro']
            context_dict['price_from_site_nash_kray'] = store['cabbage']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['cabbage']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.cabbage_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.cabbage_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.cabbage_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Сигареты Marlboro Red':
            context_dict['item_image_for_user'] = get_marlboro_red
            context_dict['price_from_site_atb'] = store['marlboro_red']['atb']
            context_dict['price_from_site_eko'] = store['marlboro_red']['eko']
            context_dict['price_from_site_varus'] = store['marlboro_red']['varus']
            context_dict['price_from_site_silpo'] = store['marlboro_red']['silpo']
            context_dict['price_from_site_ashan'] = store['marlboro_red']['ashan']
            context_dict['price_from_site_novus'] = store['marlboro_red']['novus']
            context_dict['price_from_site_fozzy'] = store['marlboro_red']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.marloboro_red_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.marloboro_red_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.marloboro_red_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Майонез детский Щедро домашний 67% жирности':
            context_dict['item_image_for_user'] = get_mayonez_dom_detsk_shedro_67
            context_dict['price_from_site_atb'] = store['mayonez_detsk_shedro_67%']['atb']
            context_dict['price_from_site_eko'] = store['mayonez_detsk_shedro_67%']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_detsk_shedro_67%']['varus']
            context_dict['price_from_site_silpo'] = store['mayonez_detsk_shedro_67%']['silpo']
            context_dict['price_from_site_metro'] = store['mayonez_detsk_shedro_67%']['metro']
            context_dict['price_from_site_fozzy'] = store['mayonez_detsk_shedro_67%']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.mayonez_detsk_shedro_67_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.mayonez_detsk_shedro_67_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.mayonez_detsk_shedro_67_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Дезодорант Rexona Aloe Vera женский':
            context_dict['item_image_for_user'] = get_reksona_aloe_vera_w
            context_dict['price_from_site_eko'] = store['rexona_aloe_vera']['eko']
            context_dict['price_from_site_ashan'] = store['rexona_aloe_vera']['ashan']
            # parser = ProductParserVol2()
            # res_atb = parser.rexona_aloe_vera_w_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.rexona_aloe_vera_w_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.rexona_aloe_vera_w_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Сметана Столица Смаку 15% жирности 400 гр':
            context_dict['item_image_for_user'] = get_smetana_stol_smaku_400_15
            context_dict['price_from_site_varus'] = store['smetana_stol_smaky_15%']['varus']
            # parser = ProductParserVol2()
            # res_atb = parser.smetana_stolica_smaky_400_15_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.smetana_stolica_smaky_400_15_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.smetana_stolica_smaky_400_15_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Чай Мономах Кения черный 90 гр':
            context_dict['item_image_for_user'] = get_tea_monomah_kenya
            context_dict['price_from_site_eko'] = store['tea_monomah_kenya_90']['eko']
            # parser = ProductParserVol2()
            # res_atb = parser.tea_monomah_black_kenya_90_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.tea_monomah_black_kenya_90_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.tea_monomah_black_kenya_90_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        elif context_dict['nn_answer'] == 'Туалетная бумага Киев 63 м':
            context_dict['item_image_for_user'] = get_toilet_papir_kiev_63m

        elif context_dict['nn_answer'] == 'Чай Мономах Цейлон черный':
            context_dict['item_image_for_user'] = get_tea_monomah_ceylon_black

        elif context_dict['nn_answer'] == 'Кофе Арома Голд Freeze Dried 70 грамм':
            context_dict['item_image_for_user'] = get_coffee_aroma_gold_freeze_dried_70
            context_dict['price_from_site_eko'] = store['cofee_aroma_gold_freeze_dried_70g']['eko']
            context_dict['price_from_site_silpo'] = store['cofee_aroma_gold_freeze_dried_70g']['silpo']
            context_dict['price_from_site_nash_kray'] = store['cofee_aroma_gold_freeze_dried_70g']['nash_kray']

        elif context_dict['nn_answer'] == 'Горчица Верес украинска мицна 120 грамм':
            context_dict['item_image_for_user'] = get_gorchica_veres_micna_ukr_120g
            context_dict['price_from_site_silpo'] = store['gorchica_veres_ukrainska_micna_120g']['silpo']
            context_dict['price_from_site_novus'] = store['gorchica_veres_ukrainska_micna_120g']['novus']
            context_dict['price_from_site_metro'] = store['gorchica_veres_ukrainska_micna_120g']['metro']

        elif context_dict['nn_answer'] == 'Чай Мономах 100% Цейлон Original черный крупнолистовой':
            context_dict['item_image_for_user'] = get_tea_monomah_original_ceylon_90g

        elif context_dict['nn_answer'] == 'Дезодорант Garnier весенняя свежесть':
            context_dict['item_image_for_user'] = get_desodorant_garnier_spring_spirit
            context_dict['price_from_site_silpo'] = store['desodorant_garnier_spring_spirit']['silpo']
            context_dict['price_from_site_novus'] = store['desodorant_garnier_spring_spirit']['novus']
            context_dict['price_from_site_metro'] = store['desodorant_garnier_spring_spirit']['metro']
            context_dict['price_from_site_fozzy'] = store['desodorant_garnier_spring_spirit']['fozzy']

        elif context_dict['nn_answer'] == 'Яблоко Гала, кг':
            context_dict['item_image_for_user'] = get_apple_gala
            context_dict['price_from_site_atb'] = store['apple_gala']['atb']
            context_dict['price_from_site_eko'] = store['apple_gala']['eko']
            context_dict['price_from_site_varus'] = store['apple_gala']['varus']
            context_dict['price_from_site_silpo'] = store['apple_gala']['silpo']
            context_dict['price_from_site_novus'] = store['apple_gala']['novus']
            context_dict['price_from_site_metro'] = store['apple_gala']['metro']
            context_dict['price_from_site_fozzy'] = store['apple_gala']['fozzy']

        elif context_dict['nn_answer'] == 'Сметана Галичанская 15% 370 грамм':
            context_dict['item_image_for_user'] = get_smetana_galichanska_15_370gr
            context_dict['price_from_site_atb'] = store['smetana_galichanska_15_370gr']['atb']
            context_dict['price_from_site_eko'] = store['smetana_galichanska_15_370gr']['eko']
            context_dict['price_from_site_novus'] = store['smetana_galichanska_15_370gr']['novus']
            context_dict['price_from_site_metro'] = store['smetana_galichanska_15_370gr']['metro']
            context_dict['price_from_site_fozzy'] = store['smetana_galichanska_15_370gr']['fozzy']

        elif context_dict['nn_answer'] == 'Чипсы Lays с солью большая пачка 30 грамм':
            context_dict['item_image_for_user'] = get_chips_lays_salt_big_pack_30g
            context_dict['price_from_site_eko'] = store['chips_lays_with_salt_big_pack']['eko']
            context_dict['price_from_site_fozzy'] = store['chips_lays_with_salt_big_pack']['fozzy']

        elif context_dict['nn_answer'] == 'Напиток Sprite 2 литра':
            context_dict['item_image_for_user'] = get_sprite_2l
            context_dict['price_from_site_eko'] = store['sprite_2l']['eko']
            context_dict['price_from_site_varus'] = store['sprite_2l']['varus']
            context_dict['price_from_site_silpo'] = store['sprite_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['sprite_2l']['ashan']
            context_dict['price_from_site_novus'] = store['sprite_2l']['novus']
            context_dict['price_from_site_metro'] = store['sprite_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['sprite_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['sprite_2l']['fozzy']

        elif context_dict['nn_answer'] == 'Напиток Fanta 2 литра':
            context_dict['item_image_for_user'] = get_fanta_2l
            context_dict['price_from_site_eko'] = store['fanta_2l']['eko']
            context_dict['price_from_site_varus'] = store['fanta_2l']['varus']
            context_dict['price_from_site_silpo'] = store['fanta_2l']['silpo']
            context_dict['price_from_site_ashan'] = store['fanta_2l']['ashan']
            context_dict['price_from_site_novus'] = store['fanta_2l']['novus']
            context_dict['price_from_site_metro'] = store['fanta_2l']['metro']
            context_dict['price_from_site_nash_kray'] = store['fanta_2l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['fanta_2l']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Bond Street Blue Selection':
            context_dict['item_image_for_user'] = get_bond_street_blue_selection
            context_dict['price_from_site_atb'] = store['bond_street_blue_selection']['atb']
            context_dict['price_from_site_eko'] = store['bond_street_blue_selection']['eko']
            context_dict['price_from_site_varus'] = store['bond_street_blue_selection']['varus']
            context_dict['price_from_site_silpo'] = store['bond_street_blue_selection']['silpo']
            context_dict['price_from_site_ashan'] = store['bond_street_blue_selection']['ashan']
            context_dict['price_from_site_novus'] = store['bond_street_blue_selection']['novus']
            context_dict['price_from_site_fozzy'] = store['bond_street_blue_selection']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Camel Blue':
            context_dict['item_image_for_user'] = get_camel_blue
            context_dict['price_from_site_atb'] = store['camel_blue']['atb']
            context_dict['price_from_site_eko'] = store['camel_blue']['eko']
            context_dict['price_from_site_varus'] = store['camel_blue']['varus']
            context_dict['price_from_site_silpo'] = store['camel_blue']['silpo']
            context_dict['price_from_site_ashan'] = store['camel_blue']['ashan']
            context_dict['price_from_site_novus'] = store['camel_blue']['novus']
            context_dict['price_from_site_fozzy'] = store['camel_blue']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты LD Red':
            context_dict['item_image_for_user'] = get_ld_red
            context_dict['price_from_site_atb'] = store['ld_red']['atb']
            context_dict['price_from_site_eko'] = store['ld_red']['eko']
            context_dict['price_from_site_silpo'] = store['ld_red']['silpo']
            context_dict['price_from_site_fozzy'] = store['ld_red']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Marlboro Gold':
            context_dict['item_image_for_user'] = get_marlboro_gold
            context_dict['price_from_site_atb'] = store['marlboro_gold']['atb']
            context_dict['price_from_site_eko'] = store['marlboro_gold']['eko']
            context_dict['price_from_site_varus'] = store['marlboro_gold']['varus']
            context_dict['price_from_site_silpo'] = store['marlboro_gold']['silpo']
            context_dict['price_from_site_ashan'] = store['marlboro_gold']['ashan']
            context_dict['price_from_site_novus'] = store['marlboro_gold']['novus']
            context_dict['price_from_site_fozzy'] = store['marlboro_gold']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Rothmans Demi BLue Exclusive':
            context_dict['item_image_for_user'] = get_rothmans_demi_blue_exclusive
            context_dict['price_from_site_atb'] = store['rothmans_demi_blue_exclusive']['atb']
            context_dict['price_from_site_eko'] = store['rothmans_demi_blue_exclusive']['eko']
            context_dict['price_from_site_varus'] = store['rothmans_demi_blue_exclusive']['varus']
            context_dict['price_from_site_silpo'] = store['rothmans_demi_blue_exclusive']['silpo']
            context_dict['price_from_site_ashan'] = store['rothmans_demi_blue_exclusive']['ashan']
            context_dict['price_from_site_novus'] = store['rothmans_demi_blue_exclusive']['novus']

        elif context_dict['nn_answer'] == 'Сигареты Rothmans Demi Click Purple':
            context_dict['item_image_for_user'] = get_rothmans_demi_click_purple
            context_dict['price_from_site_atb'] = store['rothmans_demi_click_purple']['atb']
            context_dict['price_from_site_eko'] = store['rothmans_demi_click_purple']['eko']
            context_dict['price_from_site_ashan'] = store['rothmans_demi_click_purple']['ashan']


        elif context_dict['nn_answer'] == 'Сигареты Winston Caster':
            context_dict['item_image_for_user'] = get_winston_caster
            context_dict['price_from_site_atb'] = store['winston_caster']['atb']

        elif context_dict['nn_answer'] == 'Сигареты Parlament Aqua Blue':
            context_dict['item_image_for_user'] = get_parlament_aqua_blue
            context_dict['price_from_site_atb'] = store['parlament_aqua_blue']['atb']
            context_dict['price_from_site_eko'] = store['parlament_aqua_blue']['eko']
            context_dict['price_from_site_varus'] = store['parlament_aqua_blue']['varus']
            context_dict['price_from_site_silpo'] = store['parlament_aqua_blue']['silpo']
            context_dict['price_from_site_ashan'] = store['parlament_aqua_blue']['ashan']
            context_dict['price_from_site_novus'] = store['parlament_aqua_blue']['novus']
            context_dict['price_from_site_fozzy'] = store['parlament_aqua_blue']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Winston Blue':
            context_dict['item_image_for_user'] = get_winston_blue
            context_dict['price_from_site_atb'] = store['winston_blue']['atb']
            context_dict['price_from_site_eko'] = store['winston_blue']['eko']
            context_dict['price_from_site_varus'] = store['winston_blue']['varus']
            context_dict['price_from_site_silpo'] = store['winston_blue']['silpo']
            context_dict['price_from_site_ashan'] = store['winston_blue']['ashan']
            context_dict['price_from_site_novus'] = store['winston_blue']['novus']
            context_dict['price_from_site_fozzy'] = store['winston_blue']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Bond Street Red Selection':
            context_dict['item_image_for_user'] = get_bond_street_red_selection
            context_dict['price_from_site_atb'] = store['bond_street_red_selection']['atb']
            context_dict['price_from_site_varus'] = store['bond_street_red_selection']['varus']
            context_dict['price_from_site_silpo'] = store['bond_street_red_selection']['silpo']
            context_dict['price_from_site_ashan'] = store['bond_street_red_selection']['ashan']

        elif context_dict['nn_answer'] == 'Сигареты LD Blue':
            context_dict['item_image_for_user'] = get_ld_blue
            context_dict['price_from_site_atb'] = store['ld_blue']['atb']
            context_dict['price_from_site_silpo'] = store['ld_blue']['silpo']
            context_dict['price_from_site_fozzy'] = store['ld_blue']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты Kent Silver':
            context_dict['item_image_for_user'] = get_kent_silver
            context_dict['price_from_site_atb'] = store['kent_silver']['atb']
            context_dict['price_from_site_eko'] = store['kent_silver']['eko']
            context_dict['price_from_site_varus'] = store['kent_silver']['varus']
            context_dict['price_from_site_ashan'] = store['kent_silver']['ashan']
            context_dict['price_from_site_novus'] = store['kent_silver']['novus']
            context_dict['price_from_site_fozzy'] = store['kent_silver']['fozzy']

        elif context_dict['nn_answer'] == 'Kent Navy Blue New':
            context_dict['item_image_for_user'] = get_kent_navi_blue_new
            context_dict['price_from_site_atb'] = store['kent_navy_blue']['atb']
            context_dict['price_from_site_eko'] = store['kent_navy_blue']['eko']
            context_dict['price_from_site_varus'] = store['kent_navy_blue']['varus']
            context_dict['price_from_site_silpo'] = store['kent_navy_blue']['silpo']
            context_dict['price_from_site_ashan'] = store['kent_navy_blue']['ashan']
            context_dict['price_from_site_novus'] = store['kent_navy_blue']['novus']
            context_dict['price_from_site_fozzy'] = store['kent_navy_blue']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Черниговское Светлое" 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_chernigivske_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_chernigivske_svitle_05_l_glass']['atb']
            context_dict['price_from_site_silpo'] = store['beer_chernigivske_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_chernigivske_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_chernigivske_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_chernigivske_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_chernigivske_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_chernigivske_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Stella Artois" 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_stella_artois_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_stella_artois_05_l_glass']['atb']
            context_dict['price_from_site_silpo'] = store['beer_stella_artois_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_stella_artois_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_stella_artois_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_stella_artois_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_stella_artois_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Оболонь Светлое" 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_obolon_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_obolon_svitle_05_l_glass']['atb']
            context_dict['price_from_site_eko'] = store['beer_obolon_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_obolon_svitle_05_l_glass']['varus']
            context_dict['price_from_site_novus'] = store['beer_obolon_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_obolon_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_obolon_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_obolon_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Жигулевское светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_jigulivsle_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_jugulivske_svitle_05_l_glass']['atb']
            context_dict['price_from_site_eko'] = store['beer_jugulivske_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_jugulivske_svitle_05_l_glass']['varus']
            context_dict['price_from_site_novus'] = store['beer_jugulivske_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_jugulivske_svitle_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_jugulivske_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Рогань традиционное светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_rogan_tradiciyne_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['atb']
            context_dict['price_from_site_silpo'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_rogan_tradicionnoe_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Корона Экстра светлое 0,33 л в стекле':
            context_dict['item_image_for_user'] = get_beer_corona_extra_svitle_033_l_glass
            context_dict['price_from_site_atb'] = store['beer_corona_extra_svitle_033_l_glass']['atb']
            context_dict['price_from_site_eko'] = store['beer_corona_extra_svitle_033_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_corona_extra_svitle_033_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_corona_extra_svitle_033_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_corona_extra_svitle_033_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_corona_extra_svitle_033_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_corona_extra_svitle_033_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_corona_extra_svitle_033_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Черниговоское Белое нефильтрованное 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_chernigivske_bile_nefilter_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['atb']
            context_dict['price_from_site_silpo'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_chernigibske_bile_nefilter_05_l_glass']['fozzy']


        elif context_dict['nn_answer'] == 'Пиво Янтарь светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_yantar_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_yantar_svitle_05_l_glass']['atb']
            context_dict['price_from_site_ashan'] = store['beer_yantar_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_metro'] = store['beer_yantar_svitle_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_yantar_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Zibert светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_zibert_svitle_05_l_glass
            context_dict['price_from_site_atb'] = store['beer_zibert_svitle_05_l_glass']['atb']
            context_dict['price_from_site_eko'] = store['beer_zibert_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_zibert_svitle_05_l_glass']['varus']
            context_dict['price_from_site_novus'] = store['beer_zibert_svitle_05_l_glass']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_zibert_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Арсенал мицне 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_arsenal_micne_05_l_glass
            context_dict['price_from_site_novus'] = store['beer_arsenal_micne_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_arsenal_micne_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_arsenal_micne_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_arsenal_micne_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Перша Броварня Закарпатське 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_persha_brovarna_zakarpatske_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass'][
                'nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_persha_brovarna_zakarpatske_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Львовское светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_lvivske_svitle_05_l_glass
            context_dict['price_from_site_metro'] = store['beer_lvivske_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_lvivske_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_lvivske_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Львовское 1715 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_lvivske_1715_05_l_glass
            context_dict['price_from_site_varus'] = store['beer_lvivske_1715_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_lvivske_1715_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_lvivske_1715_05_l_glass']['ashan']
            context_dict['price_from_site_metro'] = store['beer_lvivske_1715_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_lvivske_1715_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_lvivske_1715_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Zlata Praha светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_zlata_praha_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_zlata_praha_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_zlata_praha_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_zlata_praha_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_zlata_praha_svitle_05_l_glass']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_zlata_praha_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Tuborg Green 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_tuborg_green_05_l_glass
            context_dict['price_from_site_varus'] = store['beer_tuborg_green_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_tuborg_green_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_tuborg_green_05_l_glass']['ashan']
            context_dict['price_from_site_metro'] = store['beer_tuborg_green_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_tuborg_green_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_tuborg_green_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Славутич ICE MIX Lime 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_slavutich_ice_mix_lime_05_l_glass
            context_dict['price_from_site_varus'] = store['beer_slavutich_ice_mix_lime_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_slavutich_ice_mix_lime_05_l_glass']['silpo']
            context_dict['price_from_site_metro'] = store['beer_slavutich_ice_mix_lime_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_slavutich_ice_mix_lime_05_l_glass']['nash_kray']

        elif context_dict['nn_answer'] == 'Пиво Тетерев 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_teteriv_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_teteriv_svitle_05_l_glass']['eko']
            context_dict['price_from_site_silpo'] = store['beer_teteriv_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_teteriv_svitle_05_l_glass']['novus']
            context_dict['price_from_site_nash_kray'] = store['beer_teteriv_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_teteriv_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Krusovice светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_krusovice_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_krusovice_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_krusovice_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_krusovice_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_krusovice_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_krusovice_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_krusovice_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_krusovice_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_krusovice_svitle_05_l_glass']['fozzy']


        elif context_dict['nn_answer'] == 'Пиво Heineken светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_heineken_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_heineken_svitle_05_l_glass']['eko']
            context_dict['price_from_site_silpo'] = store['beer_heineken_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_heineken_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_heineken_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_heineken_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_heineken_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_heineken_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Amstel светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_amstel_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_amstel_svitle_05_l_glass']['eko']
            context_dict['price_from_site_silpo'] = store['beer_amstel_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_amstel_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_amstel_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_amstel_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_amstel_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_amstel_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Hike premium светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_hike_premium_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_hike_premium_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_hike_premium_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_hike_premium_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_hike_premium_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_hike_premium_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_hike_premium_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_hike_premium_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_hike_premium_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Бочкове светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_bochkove_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_bochkove_svitle_05_l_glass']['eko']
            context_dict['price_from_site_varus'] = store['beer_bochkove_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_bochkove_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_bochkove_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_bochkove_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_bochkove_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_bochkove_svitle_05_l_glass']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_bochkove_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Kronenbourg 1664 Blanc светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_kronenbourg_1664_blanc_svitle_05_l_glass
            context_dict['price_from_site_varus'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_metro'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass'][
                'nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_kronenbourg_1664_blanc_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Опилля Фирменное непастеризоване светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_opilla_nepasterizovane_svitle_05_l_glass
            context_dict['price_from_site_ashan'] = store['beer_opilla_firmove_nepasterizovane_svitle_05_l_glass'][
                'ashan']
            context_dict['price_from_site_novus'] = store['beer_opilla_firmove_nepasterizovane_svitle_05_l_glass'][
                'novus']
            context_dict['price_from_site_metro'] = store['beer_opilla_firmove_nepasterizovane_svitle_05_l_glass'][
                'metro']
            context_dict['price_from_site_fozzy'] = store['beer_opilla_firmove_nepasterizovane_svitle_05_l_glass'][
                'fozzy']

        elif context_dict['nn_answer'] == 'Пиво Ячменный Колос светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_yachmenniy_kolos_svitle_05_l_glass
            context_dict['price_from_site_fozzy'] = store['beer_yachmenniy_kolos_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Опилля Корифей" светлое 0,5 в стекле':
            context_dict['item_image_for_user'] = get_beer_opilla_korifey_svitle_05_l_glass
            context_dict['price_from_site_varus'] = store['beer_opilla_korifey_svitle_05_l_glass']['varus']
            context_dict['price_from_site_ashan'] = store['beer_opilla_korifey_svitle_05_l_glass']['ashan']
            context_dict['price_from_site_novus'] = store['beer_opilla_korifey_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_opilla_korifey_svitle_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_opilla_korifey_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Чайка Днепровская" 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_chaika_dneprovskaya_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_chaika_dniprovska_svitle_05_l_glass']['eko']
            context_dict['price_from_site_silpo'] = store['beer_chaika_dniprovska_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chaika_dniprovska_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_chaika_dniprovska_svitle_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chaika_dniprovska_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "Чайка Черноморская" светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_chaika_chernomorskaya_svitle_05_l_glass
            context_dict['price_from_site_eko'] = store['beer_chaika_chernomorskaya_svitle_05_l_glass']['eko']
            context_dict['price_from_site_silpo'] = store['beer_chaika_chernomorskaya_svitle_05_l_glass']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chaika_chernomorskaya_svitle_05_l_glass']['novus']
            context_dict['price_from_site_metro'] = store['beer_chaika_chernomorskaya_svitle_05_l_glass']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chaika_chernomorskaya_svitle_05_l_glass']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Умань Waissburg светлое 1 литр':
            context_dict['item_image_for_user'] = get_beer_uman_waissburg_svitle_1_l_plastic
            context_dict['price_from_site_varus'] = store['beer_uman_waissburg_1_l_svitle_plastic']['varus']
            context_dict['price_from_site_ashan'] = store['beer_uman_waissburg_1_l_svitle_plastic']['ashan']
            context_dict['price_from_site_novus'] = store['beer_uman_waissburg_1_l_svitle_plastic']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_uman_waissburg_1_l_svitle_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Умань Пшеничное светлое 1 литр':
            context_dict['item_image_for_user'] = get_beer_uman_pshenichnoe_svitle_1_l_plastic
            context_dict['price_from_site_novus'] = store['beer_uman_pshenichnoe_1_l_svitle_plastic']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_uman_pshenichnoe_1_l_svitle_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Бердичевское Хмельное светлое 1 литр':
            context_dict['item_image_for_user'] = get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic
            context_dict['price_from_site_silpo'] = store['beer_berdichevske_hmilne_1_l_svitle_plastic']['silpo']
            context_dict['price_from_site_novus'] = store['beer_berdichevske_hmilne_1_l_svitle_plastic']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_berdichevske_hmilne_1_l_svitle_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Бердичевское Лагер светлое 1 литр':
            context_dict['item_image_for_user'] = get_beer_berdichevskoe_lager_svitle_1_l_plastic
            context_dict['price_from_site_silpo'] = store['beer_berdichevske_lager_1_l_svitle_plastic']['silpo']
            context_dict['price_from_site_metro'] = store['beer_berdichevske_lager_1_l_svitle_plastic']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_berdichevske_lager_1_l_svitle_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Опилля Корифей 1.1 литра':
            context_dict['item_image_for_user'] = get_beer_opilla_korifey_11_l_plastic
            context_dict['price_from_site_atb'] = store['beer_opilla_korifey_11_l_plastic']['atb']
            context_dict['price_from_site_novus'] = store['beer_opilla_korifey_11_l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_opilla_korifey_11_l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво Оболонь жигулевское экспортное 1.5 литра':
            context_dict['item_image_for_user'] = get_beer_obolon_jigulivske_eksport_15_l_plastic
            context_dict['price_from_site_atb'] = store['beer_obolon_jigulivske_eksportne_15_l_plastic']['atb']

        elif context_dict['nn_answer'] == 'Пиво Янтарь светлое 1,2 литра':
            context_dict['item_image_for_user'] = get_beer_yantar_svitle_12_l_plastic
            context_dict['price_from_site_atb'] = store['beer_yantar_svitle_12_l_plastic']['atb']
            context_dict['price_from_site_ashan'] = store['beer_yantar_svitle_12_l_plastic']['ashan']
            context_dict['price_from_site_novus'] = store['beer_yantar_svitle_12_l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_yantar_svitle_12_l_plastic']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_yantar_svitle_12_l_plastic']['fozzy']


        elif context_dict['nn_answer'] == 'Пиво Жашковское пшеничное нефильтрованное 1 литр':
            context_dict['item_image_for_user'] = get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic
            context_dict['price_from_site_eko'] = store['beer_jashkovske_pshenichne_nefiltr_1_l_plastic']['eko']
            context_dict['price_from_site_novus'] = store['beer_jashkovske_pshenichne_nefiltr_1_l_plastic']['novus']

        elif context_dict['nn_answer'] == 'Пиво Жашковское светлое нефильтрованное 1 литр':
            context_dict['item_image_for_user'] = get_beer_jashkovskoe_svitle_nefilter_1_l_plastic
            context_dict['price_from_site_eko'] = store['beer_jashkovske_svitle_nefiltr_1_l_plastic']['eko']
            context_dict['price_from_site_novus'] = store['beer_jashkovske_svitle_nefiltr_1_l_plastic']['novus']

        elif context_dict['nn_answer'] == 'Пиво Жашковское жигулевское нефильтрованное 1 литр':
            context_dict['item_image_for_user'] = get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic
            context_dict['price_from_site_eko'] = store['beer_jashkovske_jigulivske_nefiltr_1_l_plastic']['eko']
            context_dict['price_from_site_silpo'] = store['beer_jashkovske_jigulivske_nefiltr_1_l_plastic']['silpo']
            context_dict['price_from_site_novus'] = store['beer_jashkovske_jigulivske_nefiltr_1_l_plastic']['novus']

        elif context_dict['nn_answer'] == 'Пиво Перша приватна броварня бочкове 1 литр':
            context_dict['item_image_for_user'] = get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic
            context_dict['price_from_site_eko'] = store['beer_persha_privatna_brovarnya_bochkove_1_l_plastic']['eko']
            context_dict['price_from_site_novus'] = store['beer_persha_privatna_brovarnya_bochkove_1_l_plastic'][
                'novus']

        elif context_dict['nn_answer'] == 'Пиво Чайка днипровська 1 литр':
            context_dict['item_image_for_user'] = get_beer_chayka_dniprovska_1_l_plastic
            context_dict['price_from_site_eko'] = store['beer_chayka_dniprovska_1_l_plastic']['eko']
            context_dict['price_from_site_silpo'] = store['beer_chayka_dniprovska_1_l_plastic']['silpo']

        elif context_dict['nn_answer'] == 'Кетчуп Торчин с чесноком 270 гр':
            context_dict['item_image_for_user'] = get_ketchup_torchin_s_chesnokom
            context_dict['price_from_site_eko'] = store['ketchup_torchin_s_chasnikom_270gr']['eko']
            context_dict['price_from_site_varus'] = store['ketchup_torchin_s_chasnikom_270gr']['varus']
            context_dict['price_from_site_metro'] = store['ketchup_torchin_s_chasnikom_270gr']['metro']
            context_dict['price_from_site_fozzy'] = store['ketchup_torchin_s_chasnikom_270gr']['fozzy']

        elif context_dict['nn_answer'] == 'Майонез Королевский Смак королевский 67 % 300 гр':
            context_dict['item_image_for_user'] = get_mayonez_korolivkiy_smak_korolivskiy_67_300gr
            context_dict['price_from_site_atb'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['atb']
            context_dict['price_from_site_eko'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['varus']
            context_dict['price_from_site_novus'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['novus']
            context_dict['price_from_site_metro'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['metro']
            context_dict['price_from_site_fozzy'] = store['mayonez_korolivskiy_smak_korolivskiy_67_300gr']['fozzy']

        elif context_dict['nn_answer'] == 'Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг':
            context_dict['item_image_for_user'] = get_muka_zolote_zernyatko_pshenichne_2kg

        elif context_dict['nn_answer'] == 'Пиво Черниговское Белое нефильтрованное 1 л':
            context_dict['item_image_for_user'] = get_beer_chernigivske_bile_1l_plastic
            context_dict['price_from_site_novus'] = store['beer_chernigivske_bile_nefilter_1l']['novus']
            context_dict['price_from_site_metro'] = store['beer_chernigivske_bile_nefilter_1l']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chernigivske_bile_nefilter_1l']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Оболонь светлое 1 л':
            context_dict['item_image_for_user'] = get_beer_obolon_svitle_1l_plastic
            context_dict['price_from_site_varus'] = store['beer_obolon_svitle_1l']['varus']
            context_dict['price_from_site_novus'] = store['beer_obolon_svitle_1l']['novus']

        elif context_dict['nn_answer'] == 'Пиво Рогань традиционное светлое 1 л':
            context_dict['item_image_for_user'] = get_beer_rogan_tradiciyne_svitle_1l_plastic
            context_dict['price_from_site_atb'] = store['beer_rogan_tradiciyne_svitle_1l']['atb']
            context_dict['price_from_site_ashan'] = store['beer_rogan_tradiciyne_svitle_1l']['ashan']
            context_dict['price_from_site_novus'] = store['beer_rogan_tradiciyne_svitle_1l']['novus']
            context_dict['price_from_site_metro'] = store['beer_rogan_tradiciyne_svitle_1l']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_rogan_tradiciyne_svitle_1l']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_rogan_tradiciyne_svitle_1l']['fozzy']

        elif context_dict['nn_answer'] == 'Соус Чумак чесночный 200 грамм':
            context_dict['item_image_for_user'] = get_sous_torchin_chesnochniy_200gr
            context_dict['price_from_site_eko'] = store['sous_chumak_chesnochniy_200gr']['eko']
            context_dict['price_from_site_varus'] = store['sous_chumak_chesnochniy_200gr']['varus']
            context_dict['price_from_site_novus'] = store['sous_chumak_chesnochniy_200gr']['novus']

        elif context_dict['nn_answer'] == 'Жвачка Orbit полуниця-банан':
            context_dict['item_image_for_user'] = get_jvachka_orbit_clubnika_banan
            context_dict['price_from_site_atb'] = store['orbit_polunica_banan']['atb']
            context_dict['price_from_site_eko'] = store['orbit_polunica_banan']['eko']
            context_dict['price_from_site_varus'] = store['orbit_polunica_banan']['varus']
            context_dict['price_from_site_ashan'] = store['orbit_polunica_banan']['ashan']
            context_dict['price_from_site_novus'] = store['orbit_polunica_banan']['novus']
            context_dict['price_from_site_metro'] = store['orbit_polunica_banan']['metro']
            context_dict['price_from_site_nash_kray'] = store['orbit_polunica_banan']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['orbit_polunica_banan']['fozzy']

        elif context_dict['nn_answer'] == 'Сигареты LM красные':
            context_dict['item_image_for_user'] = get_sigarets_LM_red
            context_dict['price_from_site_ashan'] = store['sigarets_lm_red']['ashan']
            context_dict['price_from_site_novus'] = store['sigarets_lm_red']['novus']
            context_dict['price_from_site_fozzy'] = store['sigarets_lm_red']['fozzy']

        elif context_dict['nn_answer'] == 'Жигулевское светлое 2 литра':
            context_dict['item_image_for_user'] = get_beer_jigulivske_2l_plastic
            context_dict['price_from_site_varus'] = store['beer_jigulivske_svitle_2l_plastic']['varus']

        elif context_dict['nn_answer'] == 'Пиво Чайка Днепровская 2 литра':
            context_dict['item_image_for_user'] = get_beer_chayka_dniprovskaya_2l_plastic
            context_dict['price_from_site_silpo'] = store['beer_chayka_dniprovska_2l_plastic']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chayka_dniprovska_2l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_chayka_dniprovska_2l_plastic']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chayka_dniprovska_2l_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Piwny Kebek 2 литра':
            context_dict['item_image_for_user'] = get_beer_piwny_kubek_2l_plastic
            context_dict['price_from_site_varus'] = store['beer_piwny_kebek_svitle_2l_plastic']['varus']

        elif context_dict['nn_answer'] == 'Кетчуп Торчин до шашлику 270 грамм':
            context_dict['item_image_for_user'] = get_ketchup_torchin_do_shasliky_270gr
            context_dict['price_from_site_eko'] = store['ketchup_torchin_do_shashliky_270gr']['eko']
            context_dict['price_from_site_varus'] = store['ketchup_torchin_do_shashliky_270gr']['varus']
            context_dict['price_from_site_silpo'] = store['ketchup_torchin_do_shashliky_270gr']['silpo']
            context_dict['price_from_site_ashan'] = store['ketchup_torchin_do_shashliky_270gr']['ashan']
            context_dict['price_from_site_novus'] = store['ketchup_torchin_do_shashliky_270gr']['novus']
            context_dict['price_from_site_fozzy'] = store['ketchup_torchin_do_shashliky_270gr']['fozzy']

        elif context_dict['nn_answer'] == 'Майонез Чумак аппетитный 50% 300 грамм':
            context_dict['item_image_for_user'] = get_mayonez_chumak_appetitniy_50_300gr
            context_dict['price_from_site_eko'] = store['mayonez_chumak_appetitniy_50_300gr']['eko']
            context_dict['price_from_site_varus'] = store['mayonez_chumak_appetitniy_50_300gr']['varus']
            context_dict['price_from_site_silpo'] = store['mayonez_chumak_appetitniy_50_300gr']['silpo']
            context_dict['price_from_site_novus'] = store['mayonez_chumak_appetitniy_50_300gr']['novus']
            context_dict['price_from_site_metro'] = store['mayonez_chumak_appetitniy_50_300gr']['metro']

        elif context_dict['nn_answer'] == 'Колбаса Перша Столиця Салями Фирменная высший сорт':
            context_dict['item_image_for_user'] = get_kolbasa_persha_stolica_salyami_firmova_vs
            # нет в наличии нигде

        elif context_dict['nn_answer'] == 'Кофе Чорна Карта GOLD 50 грамм':
            context_dict['item_image_for_user'] = get_cofee_chorna_karta_gold_50gr
            context_dict['price_from_site_eko'] = store['coffee_chorna_karta_50gr']['eko']

        elif context_dict['nn_answer'] == 'Пиво Арсенал "Міцне" світле, 2л':
            context_dict['item_image_for_user'] = get_beer_arsenal_micne_svitle_2l_plastic
            context_dict['price_from_site_metro'] = store['beer_arsenal_micne_2l_plastic']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_arsenal_micne_2l_plastic']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_arsenal_micne_2l_plastic']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво "ППБ Бочкове" світле, 2л':
            context_dict['item_image_for_user'] = get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic
            context_dict['price_from_site_eko'] = store['beer_ppb_bochkove_svitle_2l_plastic']['eko']
            context_dict['price_from_site_silpo'] = store['beer_ppb_bochkove_svitle_2l_plastic']['silpo']
            context_dict['price_from_site_novus'] = store['beer_ppb_bochkove_svitle_2l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_bochkove_svitle_2l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво "ППБ Закарпатське оригінальне" світле, 2л':
            context_dict['item_image_for_user'] = get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic
            context_dict['price_from_site_silpo'] = store['beer_ppb_zakarpatske_svitle_2l_plastic']['silpo']
            context_dict['price_from_site_novus'] = store['beer_ppb_zakarpatske_svitle_2l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_zakarpatske_svitle_2l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво Zibert светлое 0,5 л в банке':
            context_dict['item_image_for_user'] = get_beer_zibert_svitle_05_l_banochnoe
            context_dict['price_from_site_atb'] = store['beer_zibert_svitle_05l_v_banke']['atb']
            context_dict['price_from_site_eko'] = store['beer_zibert_svitle_05l_v_banke']['eko']
            context_dict['price_from_site_varus'] = store['beer_zibert_svitle_05l_v_banke']['varus']
            context_dict['price_from_site_novus'] = store['beer_zibert_svitle_05l_v_banke']['novus']
            context_dict['price_from_site_metro'] = store['beer_zibert_svitle_05l_v_banke']['metro']

        elif context_dict['nn_answer'] == 'Йогурт Фанни 240 грамм 1.5% лесовые ягоды':
            context_dict['item_image_for_user'] = get_yogurt_fanni_lisovi_yagodi_1_5_240gr
            context_dict['price_from_site_varus'] = store['yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan']['varus']
            context_dict['price_from_site_silpo'] = store['yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan']['silpo']

        elif context_dict['nn_answer'] == 'Кефир Славия 2,5% 850 грамм':
            context_dict['item_image_for_user'] = get_kefir_slaviya_2_5_850gr
            #нет в наличии нигде
            
        elif context_dict['nn_answer'] == 'Пиво Оболонь Киевское розливное светлое 1,95 литра в пластике':
            context_dict['item_image_for_user'] = get_beer_obolon_kievskoe_razlivnoe_svetloe_195l_plastic
            context_dict['price_from_site_eko'] = store['beer_obolon_kievskoe_razlivnoe_svetloe_195l']['eko']
            context_dict['price_from_site_varus'] = store['beer_obolon_kievskoe_razlivnoe_svetloe_195l']['varus']
            context_dict['price_from_site_novus'] = store['beer_obolon_kievskoe_razlivnoe_svetloe_195l']['novus']
            context_dict['price_from_site_metro'] = store['beer_obolon_kievskoe_razlivnoe_svetloe_195l']['metro']

        elif context_dict['nn_answer'] == 'Пиво Черниговское light светлое 2,0 л в пластике':
            context_dict['item_image_for_user'] = get_beer_chernigivske_light_svitle_2l_plastic
            context_dict['price_from_site_atb'] = store['beer_chernigivske_light_svitle_2l_plastic']['atb']
            context_dict['price_from_site_silpo'] = store['beer_chernigivske_light_svitle_2l_plastic']['silpo']
            context_dict['price_from_site_metro'] = store['beer_chernigivske_light_svitle_2l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво Опилля Корифей светлое 2,0 л в пластике':
            context_dict['item_image_for_user'] = get_beer_opilla_korifey_svitle_2l_plastic
            context_dict['price_from_site_ashan'] = store['beer_opilla_korifey_svitle_2l_plastic']['ashan']
            context_dict['price_from_site_novus'] = store['beer_opilla_korifey_svitle_2l_plastic']['novus']
            context_dict['price_from_site_metro'] = store['beer_opilla_korifey_svitle_2l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво Янтарь светлое 2,0 л в пластике':
            context_dict['item_image_for_user'] = get_beer_yantar_svitle_2l_plastic
            context_dict['price_from_site_metro'] = store['beer_yantar_svitle_2l_plastic']['metro']

        elif context_dict['nn_answer'] == 'Пиво Tuborg Green 4 банки х 0,5 л':
            context_dict['item_image_for_user'] = get_beer_tuborg_green_svitle_4_banki_05l
            context_dict['price_from_site_silpo'] = store['beer_tuborg_green_svitle_4_banki_05l']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_tuborg_green_svitle_4_banki_05l']['ashan']
            context_dict['price_from_site_metro'] = store['beer_tuborg_green_svitle_4_banki_05l']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_tuborg_green_svitle_4_banki_05l']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво ППБ Закарпатське 4 банки х 0,5 л':
            context_dict['item_image_for_user'] = get_beer_ppb_zakarpatske_svitle_4_banki_05l
            context_dict['price_from_site_silpo'] = store['beer_ppb_zakarpatske_svitle_4_banki_05l']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_ppb_zakarpatske_svitle_4_banki_05l']['ashan']
            context_dict['price_from_site_novus'] = store['beer_ppb_zakarpatske_svitle_4_banki_05l']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_zakarpatske_svitle_4_banki_05l']['metro']


        elif context_dict['nn_answer'] == 'Пиво ППБ Бочкове 4 банки х 0,5 л':
            context_dict['item_image_for_user'] = get_beer_ppb_bochkove_svitle_4_banki_05l
            context_dict['price_from_site_silpo'] = store['beer_ppb_bochkove_svitle_4_banki_05l']['silpo']
            context_dict['price_from_site_novus'] = store['beer_ppb_bochkove_svitle_4_banki_05l']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_bochkove_svitle_4_banki_05l']['metro']

        elif context_dict['nn_answer'] == 'Пиво Budweiser Budvar светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_budweiser_budvar_05l_glass
            context_dict['price_from_site_varus'] = store['beer_budweiser_budvar_svitle_05l']['varus']
            context_dict['price_from_site_ashan'] = store['beer_budweiser_budvar_svitle_05l']['ashan']
            context_dict['price_from_site_novus'] = store['beer_budweiser_budvar_svitle_05l']['novus']
            context_dict['price_from_site_metro'] = store['beer_budweiser_budvar_svitle_05l']['metro']

        elif context_dict['nn_answer'] == 'Пиво Pilsner Urquell светлое 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_pilsner_urquell_05l_glass
            context_dict['price_from_site_varus'] = store['beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass']['varus']
            context_dict['price_from_site_silpo'] = store['beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass']['silpo']
            context_dict['price_from_site_metro'] = store['beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass']['metro']

        elif context_dict['nn_answer'] == 'Пиво Robert Doms бельгийский светлое нефильтрованное 0,5 л в стекле':
            context_dict['item_image_for_user'] = get_beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass
            context_dict['price_from_site_metro'] = store['beer_pilsner_urquell_svitle_05l']['metro']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Чернігівське світле жб':
            context_dict['item_image_for_user'] = get_beer_chernigivske_svitle_05l_jb
            context_dict['price_from_site_ashan'] = store['beer_chernigivske_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_chernigivske_svitle_05_l_jb']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_chernigivske_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пивo 0,5 л Чepнігівськe Білe жб':
            context_dict['item_image_for_user'] = get_beer_chernigivske_bile_nefilter_05l_jb
            context_dict['price_from_site_atb'] = store['beer_chernigivske_bile_nefilter_05_l_jb']['atb']
            context_dict['price_from_site_silpo'] = store['beer_chernigivske_bile_nefilter_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_chernigivske_bile_nefilter_05_l_jb']['ashan']
            context_dict['price_from_site_metro'] = store['beer_chernigivske_bile_nefilter_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chernigivske_bile_nefilter_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Velkopopovicky Kozel темне жб':
            context_dict['item_image_for_user'] = get_beer_velkopopovicky_kozel_temne_05l_jb
            context_dict['price_from_site_atb'] = store['beer_velkopopovicky_kozel_temne_05_l_jb']['atb']
            context_dict['price_from_site_ashan'] = store['beer_velkopopovicky_kozel_temne_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_velkopopovicky_kozel_temne_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_velkopopovicky_kozel_temne_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_velkopopovicky_kozel_temne_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Edelmeister Pilsner світле фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_edelmeister_pilsner_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_edelmeister_pilsner_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Faxe світле фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_faxe_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_faxe_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Livu Pilzenes світле фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_livu_pilzenes_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_livu_pilzenes_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Velkopopovicky Kozel світле жб':
            context_dict['item_image_for_user'] = get_beer_velkopopovicky_kozel_temne_05l_jb
            context_dict['price_from_site_atb'] = store['beer_velkopopovicky_kozel_svitle_05_l_jb']['atb']
            context_dict['price_from_site_silpo'] = store['beer_velkopopovicky_kozel_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_velkopopovicky_kozel_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_velkopopovicky_kozel_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_velkopopovicky_kozel_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Оболонь BeerMix Лимон жб':
            context_dict['item_image_for_user'] = get_beer_obolon_beermix_limon_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_obolon_beermix_limon_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Edelmeister Weizenbier світле нефільтроване жб':
            context_dict['item_image_for_user'] = get_beer_edelmeister_weizenbier_nefilter_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Edelmeister Schwarzbier темне фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_edelmeister_schwarzbier_temne_05l_jb
            context_dict['price_from_site_atb'] = store['beer_edelmeister_schwarzbier_temne_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пивo 0,5л Hike Blanche світлe нeфільтpoвaнe жб':
            context_dict['item_image_for_user'] = get_beer_hike_blanche_svitle_nefilter_05l_jb
            context_dict['price_from_site_atb'] = store['beer_hike_blanche_nefilter_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_hike_blanche_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_hike_blanche_nefilter_05_l_jb']['varus']
            context_dict['price_from_site_ashan'] = store['beer_hike_blanche_nefilter_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_hike_blanche_nefilter_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_hike_blanche_nefilter_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Zlata Praha світле жб':
            context_dict['item_image_for_user'] = get_beer_zlata_praha_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_zlata_praha_svitle_05_l_jb']['atb']
            context_dict['price_from_site_varus'] = store['beer_zlata_praha_svitle_05_l_jb']['varus']
            context_dict['price_from_site_ashan'] = store['beer_zlata_praha_svitle_05_l_jb']['ashan']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Thuringer Premium Beer світле фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_thuringer_premium_beer_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_thuringer_premium_beer_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Livu Sencu світле фільтроване жб':
            context_dict['item_image_for_user'] = get_beer_livu_sencu_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_livu_sencu_beer_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5 л Germanarich светлое жб':
            context_dict['item_image_for_user'] = get_beer_germanarich_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_germanarich_svitle_05_l_jb']['atb']

        elif context_dict['nn_answer'] == 'Пиво 0,5л Hike Преміум світле жб':
            context_dict['item_image_for_user'] = get_beer_hike_premium_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_hike_premium_svitle_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_hike_premium_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_hike_premium_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_hike_premium_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_hike_premium_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_hike_premium_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_hike_premium_svitle_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_hike_premium_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пивo бeзaлкoгoльнe 0,5л Обoлoнь 0 світлe нефільтроване пaстepизoвaнe жб':
            context_dict['item_image_for_user'] = get_beer_obolon_svitle_nefilter_nonalcohol_05l_jb
            context_dict['price_from_site_atb'] = store['beer_obolon_nonalcohol_nefilter_svitle_05_l_jb']['atb']
            context_dict['price_from_site_varus'] = store['beer_obolon_nonalcohol_nefilter_svitle_05_l_jb']['varus']
            context_dict['price_from_site_ashan'] = store['beer_obolon_nonalcohol_nefilter_svitle_05_l_jb']['ashan']

        elif context_dict['nn_answer'] == 'Пивo Zibert Баварское светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_bavaria_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_zibert_bavarskoe_svitle_05_l_jb']['eko']
            context_dict['price_from_site_novus'] = store['beer_zibert_bavarskoe_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_zibert_bavarskoe_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пивo Bavaria Liquid Apple безалкогольное светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_bavaria_liquid_apple_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пивo Heineken светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_heineken_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_heineken_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_heineken_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_heineken_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_heineken_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_heineken_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_heineken_svitle_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_heineken_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пивo Rychtar Grant 11 светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_rychtar_grunt_11_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_rychtar_grant_11_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пивo Amstel светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_amstel_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_amstel_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_amstel_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_amstel_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_amstel_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_amstel_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_amstel_svitle_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_amstel_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пивo Bavaria светлое 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_bavaria_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_bavaria_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_bavaria_svitle_05_l_jb']['varus']
            context_dict['price_from_site_ashan'] = store['beer_bavaria_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_metro'] = store['beer_bavaria_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пивo Bavaria светлое безалкогольное 0,5 л жб':
            context_dict['item_image_for_user'] = get_beer_bavaria_svitle_nonalcohol_05l_jb
            context_dict['price_from_site_eko'] = store['beer_bavaria_svitle_nonalcohol_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_bavaria_svitle_nonalcohol_05_l_jb']['varus']

        elif context_dict['nn_answer'] == 'Пиво Edelburg Lager світле 5,2% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_edelburg_lager_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_edelburg_lager_05_l_jb']['eko']
            context_dict['price_from_site_metro'] = store['beer_edelburg_lager_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Donner Pils світле 3,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_donner_pils_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_donner_pils_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Dutch Windmill світле 4,6% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_dutch_windmill_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_dutch_windmill_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_dutch_windmill_svitle_05_l_jb']['varus']
            context_dict['price_from_site_novus'] = store['beer_dutch_windmill_svitle_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Edelburg Hefeweizen світле нефільтроване 5,1% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_edelburg_hefeweizen_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_metro'] = store['beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Edelmeister Unfiltered світле нефільтроване 5,7% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_edelmeister_unfiltered_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Estrella Damm Barcelona світле 4,6% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_estrella_damm_barcelona_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_estrella_damm_barcelona_svitle_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_estrella_damm_barcelona_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_estrella_damm_barcelona_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_estrella_damm_barcelona_svitle_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_estrella_damm_barcelona_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Halne Jasne Pelne з/б 6% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_halne_jasne_pelne_05l_jb
            context_dict['price_from_site_eko'] = store['beer_halne_jasne_pelne_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_halne_jasne_pelne_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_halne_jasne_pelne_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Eurotour Hefeweissbier світле 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_eurotour_hefeweissbier_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_eurotour_hefeweissbier_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Hollandia Strong світле 7,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_hollandia_strong_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_hollandia_strong_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_hollandia_strong_svitle_05_l_jb']['varus']
            context_dict['price_from_site_ashan'] = store['beer_hollandia_strong_svitle_05_l_jb']['ashan']

        elif context_dict['nn_answer'] == 'Пиво Lander Brau Premium світле 4,9% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_lander_brau_premium_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_lander_brau_premium_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_lander_brau_premium_svitle_05_l_jb']['varus']
            context_dict['price_from_site_metro'] = store['beer_lander_brau_premium_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Saku Kuld 5,2% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Saku_Kuld_05l_jb
            context_dict['price_from_site_eko'] = store['beer_saku_kuld_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Saku Originaal 4,7% 0,5л л жб':
            context_dict['item_image_for_user'] = get_beer_Saku_Originaal_05l_jb
            context_dict['price_from_site_eko'] = store['beer_saku_originaal_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Stangen Lager світле 5,4% 0,5л л жб':
            context_dict['item_image_for_user'] = get_beer_Stangen_Lager_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_stangen_lager_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Van Pur Premium світле 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Van_Pur_Premium_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_van_pur_premium_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Bavaria манго-маракуйя світле безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Bavaria_mango_marakya_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Bavaria Гранат безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Bavaria_granat_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_bavaria_granat_nonalco_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Оболонь Beermix Малина світле 2,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Obolon_Beermix_malina_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_obolon_beermix_malina_svitle_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_obolon_beermix_malina_svitle_05_l_jb']['eko']
            context_dict['price_from_site_ashan'] = store['beer_obolon_beermix_malina_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_nash_kray'] = store['beer_obolon_beermix_malina_svitle_05_l_jb']['nash_kray']

        elif context_dict['nn_answer'] == 'Пиво Оболонь Beermix Вишня спеціальне світле 2,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Obolon_Beermix_vishnya_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_obolon_beermix_vishnya_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Lomza світле 5,7% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Lomza_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_lomza_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Paderborner Pilsener світле 4,8% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Paderborner_Pilsener_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_paderborner_pilsener_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_paderborner_pilsener_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_paderborner_pilsener_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_paderborner_pilsener_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_paderborner_pilsener_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Paderborner Export світле 5,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Paderborner_Export_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_paderborner_export_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_paderborner_export_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_paderborner_export_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_paderborner_export_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Clausthaler Grapefruit безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Clausthaler_Grapefruit_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_clausthaler_grapefruit_nonalco_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_clausthaler_grapefruit_nonalco_05_l_jb']['varus']
            context_dict['price_from_site_metro'] = store['beer_clausthaler_grapefruit_nonalco_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Clausthaler Original безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Clausthaler_Original_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_clausthaler_original_nonalco_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_clausthaler_original_nonalco_05_l_jb']['varus']
            context_dict['price_from_site_metro'] = store['beer_clausthaler_original_nonalco_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Clausthaler Lemon безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Clausthaler_Lemon_nonalcohol_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_clausthaler_lemon_nonalco_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_clausthaler_lemon_nonalco_05_l_jb']['varus']
            context_dict['price_from_site_novus'] = store['beer_clausthaler_lemon_nonalco_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Forever Rock & Roll світле нефільтроване 7,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Forever_Rock_N_Roll_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_forever_rock_n_roll_nefilter_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Forever Black Queen темне нефільтроване 5,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Forever_Black_Queen_temne_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_forever_black_queen_nefilter_temne_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Forever Kite Safari світле нефільтроване 7% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Forever_Kite_Safari_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_forever_kite_safari_nefilter_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Forever Crazy світле нефільтроване 6,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Forever_Crazy_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_forever_crazy_nefilter_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Hike Light світле 3,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Hike_Light_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_hike_light_svitle_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_hike_light_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_hike_light_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_hike_light_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_metro'] = store['beer_hike_light_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Hike Zero безалкогольне 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Hike_Zero_nonalco_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_hike_zero_nonalco_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_hike_zero_nonalco_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_hike_zero_nonalco_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_hike_zero_nonalco_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_hike_zero_nonalco_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_hike_zero_nonalco_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_hike_zero_nonalco_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Horn Disel Ice Pilsner світле 4,7% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Horn_Disel_Ice_Pilsner_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_horn_disel_ice_pilsner_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Horn Disel Original 5,3% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Horn_Disel_Original_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_horn_disel_original_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Horn Disel Traditional світле 6% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Horn_Disel_Traditional_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_horn_disel_traditional_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Horn Premium Diesel світле 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Horn_Disel_Premium_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_horn_disel_premium_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Krusovice Cerne темне 3,8% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Krusovice_Cerne_temne_05l_jb
            context_dict['price_from_site_eko'] = store['beer_krusovice_cerne_temne_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_krusovice_cerne_temne_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_krusovice_cerne_temne_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_krusovice_cerne_temne_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_krusovice_cerne_temne_05_l_jb']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_krusovice_cerne_temne_05_l_jb']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_krusovice_cerne_temne_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Lander Brau міцне 4,9% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Lander_Brau_micne_05l_jb
            context_dict['price_from_site_eko'] = store['beer_lander_brau_micne_05_l_jb']['eko']
            context_dict['price_from_site_metro'] = store['beer_lander_brau_micne_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Lander Brau світле нефільтроване 4,7% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Lander_Brau_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_lander_brau_svitle_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_lander_brau_svitle_nefilter_05_l_jb']['varus']
            context_dict['price_from_site_metro'] = store['beer_lander_brau_svitle_nefilter_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Paderborner Pilger світле нефільтроване пастеризоване 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Paderborner_Pilger_svitle_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_paderborner_pilger_svitle_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_paderborner_pilger_svitle_nefilter_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_paderborner_pilger_svitle_nefilter_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_paderborner_pilger_svitle_nefilter_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_paderborner_pilger_svitle_nefilter_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Platan Jedenactka 11 світле 4,6% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Platan_Jedenactka_11_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_platan_jedenactka_11_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Praga світле фільтроване 4,7% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Praga_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_praga_svitle_05_l_jb']['eko']
            context_dict['price_from_site_novus'] = store['beer_praga_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_praga_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво Saku Rock світле 5,3% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Saku_Rock_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_saku_rock_svitle_0568_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Sitnan світле 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Sitnan_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_sitnan_svitle_05_l_jb']['eko']
            context_dict['price_from_site_novus'] = store['beer_sitnan_svitle_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Vienas Premium Golden світле 5% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Vienas_Premium_Golden_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_vienas_premium_golden_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Vienas Premium Traditional світле 5,8% 0,568л жб':
            context_dict['item_image_for_user'] = get_beer_Vienas_Premium_Traditional_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_vienas_premium_traditional_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Volynski Browar Forever Sweet Wit пшеничне світле нефільтроване 4,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Volynski_Browar_Forever_Sweet_Wit_nefilter_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Zahringer Преміум світле 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Zahringer_premium_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_zahringer_premium_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Zahringer Hefeweizen світле 0,5л ж':
            context_dict['item_image_for_user'] = get_beer_Zahringer_Hefeweizen_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_zahringer_hefeweizen_svitle_05_l_jb']['eko']

        elif context_dict['nn_answer'] == 'Пиво Жашківське світле нефільтроване 4,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_jajkivske_nefilter_svitle_05l_jb
            context_dict['price_from_site_atb'] = store['beer_jajkivske_nefilter_svitle_05_l_jb']['atb']
            context_dict['price_from_site_eko'] = store['beer_jajkivske_nefilter_svitle_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_jajkivske_nefilter_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_jajkivske_nefilter_svitle_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Оболонь світле 4,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_obolon_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_obolon_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_obolon_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_obolon_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_obolon_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_obolon_svitle_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_obolon_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Pubster світле 5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Pubster_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_pubster_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_pubster_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_pubster_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_pubster_svitle_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_pubster_svitle_05_l_jb']['metro']

        elif context_dict['nn_answer'] == 'Пиво ППБ Чайка Чорноморська 4,5% 0,5л жб':
            context_dict['item_image_for_user'] = get_beer_Chaika_Chernomorska_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_chaika_chernomorskaya_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_chaika_chernomorskaya_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chaika_chernomorskaya_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_chaika_chernomorskaya_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_chaika_chernomorskaya_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво ППБ Закарпатське Оригінальне світле 4,4% 0,5л':
            context_dict['item_image_for_user'] = get_beer_PPB_Zakarpatske_origin_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_ppb_zakarpatske_origin_svitle_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_ppb_zakarpatske_origin_svitle_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_ppb_zakarpatske_origin_svitle_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_ppb_zakarpatske_origin_svitle_05_l_jb']['novus']
            context_dict['price_from_site_fozzy'] = store['beer_ppb_zakarpatske_origin_svitle_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво ППБ Бочкове Нефільтроване з/б 4,8% 0,5л':
            context_dict['item_image_for_user'] = get_beer_PPB_Bochkove_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['silpo']
            context_dict['price_from_site_ashan'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['ashan']
            context_dict['price_from_site_novus'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_ppb_bochkove_nefilter_05_l_jb']['nash_kray']


        elif context_dict['nn_answer'] == 'Пиво ППБ Нефільтроване світле безалкогольне 0,5л':
            context_dict['item_image_for_user'] = get_beer_PPB_Nefilter_svitle_nonalco_05l_jb
            context_dict['price_from_site_eko'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['varus']
            context_dict['price_from_site_silpo'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['metro']
            context_dict['price_from_site_fozzy'] = store['beer_ppb_nefilter_svitle_nonalco_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво ППБ Лимон-Лайм безалкогольне нефільтроване 0,5л':
            context_dict['item_image_for_user'] = get_beer_PPB_Limon_lime_nonalco_nefilter_05l_jb
            context_dict['price_from_site_eko'] = store['beer_ppb_limon_lime_nonalco_nefilter_05_l_jb']['eko']
            context_dict['price_from_site_varus'] = store['beer_ppb_limon_lime_nonalco_nefilter_05_l_jb']['varus']
            context_dict['price_from_site_novus'] = store['beer_ppb_limon_lime_nonalco_nefilter_05_l_jb']['novus']

        elif context_dict['nn_answer'] == 'Пиво Чайка Дніпровська світле фільтроване 4,8% 0,5л':
            context_dict['item_image_for_user'] = get_beer_Chaika_Dniprovska_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_chaika_dniprovskaya_05_l_jb']['eko']
            context_dict['price_from_site_silpo'] = store['beer_chaika_dniprovskaya_05_l_jb']['silpo']
            context_dict['price_from_site_novus'] = store['beer_chaika_dniprovskaya_05_l_jb']['novus']
            context_dict['price_from_site_metro'] = store['beer_chaika_dniprovskaya_05_l_jb']['metro']
            context_dict['price_from_site_nash_kray'] = store['beer_chaika_dniprovskaya_05_l_jb']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['beer_chaika_dniprovskaya_05_l_jb']['fozzy']

        elif context_dict['nn_answer'] == 'Пиво Brok Export світле 5,2% 0,5л':
            context_dict['item_image_for_user'] = get_beer_Brok_Export_svitle_05l_jb
            context_dict['price_from_site_eko'] = store['beer_brok_export_svitle_05_l_jb']['eko']
            context_dict['price_from_site_novus'] = store['beer_brok_export_svitle_05_l_jb']['novus']


        else:
            context_dict['item_image_for_user'] = get_apple_golden
            context_dict['price_from_site_atb'] = store['apple_golden']['atb']
            context_dict['price_from_site_eko'] = store['apple_golden']['eko']
            context_dict['price_from_site_varus'] = store['apple_golden']['varus']
            context_dict['price_from_site_silpo'] = store['apple_golden']['silpo']
            context_dict['price_from_site_metro'] = store['apple_golden']['metro']
            context_dict['price_from_site_nash_kray'] = store['apple_golden']['nash_kray']
            context_dict['price_from_site_fozzy'] = store['apple_golden']['fozzy']
            # parser = ProductParserVol2()
            # res_atb = parser.apple_golden_parcer()[0]
            # context_dict['price_from_site_atb'] = res_atb
            # res_eko = parser.apple_golden_parcer()[1]
            # context_dict['price_from_site_eko'] = res_eko
            # res_varus = parser.apple_golden_parcer()[2]
            # context_dict['price_from_site_varus'] = res_varus

        mutual_context_dict = self.get_user_context(title='Результат поиска')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
        которая была добавлена самой последней'''

        return UserItemNameUpload_2.objects.latest('time_create')


class GetItemNameFromUser(MutualContext, CreateView):
    '''Класс-обработчки в привязке с формой для получения
    изображения от пользователя, его сохранения в БД
    и последующей обработки.'''

    form_class = UploadItemNameForm
    template_name = 'my_app/upload_text_page.html'
    success_url = reverse_lazy('result_with_name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск товара по названию')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Terms_of_Use(MutualContext, ListView):
    """Класс-обработчик страницы 'Условия использования'."""

    model = SitePolitics
    template_name = 'my_app/terms_of_use.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Условия использования')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class PrivacyPolicy(MutualContext, ListView):
    """Класс-обработчик страницы 'Условия использования'."""

    model = SitePolitics
    template_name = 'my_app/privacy_policy.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Политика конфиденциальности')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class CookiePolicy(MutualContext, ListView):
    """Класс-обработчик страницы 'Политика cookie'."""

    model = SitePolitics
    template_name = 'my_app/cookie_policy.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Политика cookie')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class SearchByPhoto(MutualContext, CreateView):
    '''Класс для поиска товара по фото пользователя'''
    form_class = SearchByPhotoForm
    template_name = 'my_app/search_by_photo.html'
    success_url = reverse_lazy('result_with_photo')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск по фото')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Thanksfull(MutualContext, ListView):
    '''Класс для удаления изображения из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = UserPhotoUploadModel_2

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем изображения из БД и самого проекта.'''

        # вот тут можно удалить фото из папки
        for file in glob.glob("/home/andrey/GroceryAppVol2/FBApp/media/photos/user/*"):
            os.remove(file)

        # тут удаляем загруженное фото из БД
        user_pic = UserPhotoUploadModel_2.objects.latest('time_create')
        return user_pic.delete()


class Thanksfull_DELETE_NAME(MutualContext, ListView):
    '''Класс для удаления изображения из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = UserItemNameUpload_2

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем названия товара из БД'''

        # тут удаляем загруженное название из БД
        user_item_name = UserItemNameUpload_2.objects.latest('time_create')
        return user_item_name.delete()


class FindYouDishHere(MutualContext, CreateView):
    '''Класс-представление, который использует форму , с помощью
    которой пользователь может выбрать интересующее его блюдо
    и узнать его себестоимость в супермаркетах'''

    form_class = SearchDishesForm
    template_name = 'my_app/dishes.html'
    success_url = reverse_lazy('prices_for_dish')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск блюда')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class DishesResult(MutualContext, ListView):
    '''Класс-представление, который ответчает за
     выдачу результат пользователю после поиска блюда'''

    model = Dishes
    template_name = 'my_app/dishes_result.html'
    context_object_name = 'info'

    def calculate_dish_value(self, count_people, parser):
        '''Метод для упрощения кода.Выноисм подсчет стоимости блюда в отельную функцию.'''
        self.value_atb = round(parser * int(count_people), 2)
        self.value_eko = round(parser * int(count_people), 2)
        self.value_varus = round(parser * int(count_people), 2)
        return self.value_atb, self.value_eko, self.value_varus

    def what_dish(self):
        user_dish = self.get_queryset().dish_name
        user_count = self.get_queryset().count_persons
        dish_parser = AllDishParsersVol2()
        if user_dish == "Борщ":
            self.value_atb = dish_parser.dish_red_borsh_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_red_borsh_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_red_borsh_parser()[2] * int(user_count)
        elif user_dish == 'Вареники с картошкой':
            self.value_atb = dish_parser.dish_vareniki_s_kartoshkoy_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_vareniki_s_kartoshkoy_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_vareniki_s_kartoshkoy_parser()[2] * int(user_count)
        elif user_dish == 'Вареники с капустой':
            self.value_atb = dish_parser.dish_vareniki_s_kapustoy_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_vareniki_s_kapustoy_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_vareniki_s_kapustoy_parser()[2] * int(user_count)

        result_atb = self.value_atb
        result_eko = self.value_eko
        result_varus = self.value_varus
        return user_dish, user_count, result_atb, result_eko, result_varus

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['user_dish_name'] = self.what_dish()[0]
        # для украинского борща:
        if context_dict['user_dish_name'] == 'Борщ':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict['dish_pic'] = get_borsh_ukr_info
        # для вареников с картошкой
        elif context_dict['user_dish_name'] == 'Вареники с картошкой':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict['dish_pic'] = get_vareniki_s_kartoshkoy_info
        # для вареников с капустой
        elif context_dict['user_dish_name'] == 'Вареники с капустой':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict[
                'dish_pic'] = get_vareniki_s_kartoshkoy_info  # картинка одинакова для вареников с картошкой и капустой

        mutual_context_dict = self.get_user_context(title='Запрашиваемое блюдо')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
        которая была добавлена самой последней'''

        return Dishes.objects.latest('time_create')


class ProductsSet(MutualContext, CreateView):
    '''Класс-обработчик для страницы , на которой пользователь
    может собирать продуктовые наборы, вручную написав их в форме заполнения'''
    form_class = AssembleProductSet
    template_name = 'my_app/products_set_main.html'
    success_url = reverse_lazy('items_set')

    def compile_all_user_requests(self):
        self.product_order_info = get_product_set_from_data_base
        return self.product_order_info

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # получаем id владельца, кто собирает продуктовый набор(зарегестрированный пользователь)
        self.object.owner = self.request.user.id
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['user_item_info'] = self.compile_all_user_requests()
        context_dict['all_markets'] = get_all_markets
        mutual_context_dict = self.get_user_context(title='Продуктовый набор')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class SetResults(MutualContext, ListView):
    '''Класс для удаления пользовательских продуктовых наборов из БД и
    по совместительству страница для выбора маркетов для поиска выгодных цен.'''

    template_name = 'my_app/answer_sets.html'
    success_url = reverse_lazy('home')
    model = SetOfProducts
    context_object_name = 'user_orders'

    def NN_works(self):
        '''Подключение НС для текста, которая определяет, какой
        конкретно продукт пользователь добавил в список (название продукта)'''
        pred = NN_text()
        user_orders = self.get_queryset()
        total_product_info = []

        for order in user_orders:
            result = pred.identify_item(order.product_name)
            # добавим цены из БД цен
            atb_price, eko_price, varus_price, silpo_price,ashan_price,\
            novus_price,metro_price,nash_kray_price,fozzy_price,picture=get_products_prices(result)

            #отфильтруем цены. оставим только те цены , которые соответствуют выбранным супермаркетам!
            filtered_prices=[]
            marker=1
            if order.atb_choice==marker:               #тут какой-то баг!
                filtered_prices.append(atb_price)
            else:
                filtered_prices.append(9999999999)
            # elif order.eko_choice==marker:
            #     filtered_prices.append(eko_price)
            # elif order.varus_choice==marker:
            #     filtered_prices.append(varus_price)
            # elif order.silpo_choice==marker:
            #     filtered_prices.append(silpo_price)
            # elif order.ashan_choice==marker:
            #     filtered_prices.append(ashan_price)
            # elif order.novus_choice==marker:
            #     filtered_prices.append(novus_price)
            # elif order.metro_choice==marker:
            #     filtered_prices.append(metro_price)
            # elif order.nash_kray_choice==marker:
            #     filtered_prices.append(nash_kray_price)
            # elif order.fozzy_choice==marker:
            #     filtered_prices.append(fozzy_price)
            filtered_prices.append(picture)
            print('Отфильтрованный список цен',filtered_prices)


            #определяем лучшую цену:
            best_price=best_price_identify(filtered_prices)
            print('Best price: ',best_price)
            #best_price=best_price_identify([atb_price, eko_price, varus_price, silpo_price,ashan_price,
            #novus_price,metro_price,nash_kray_price,fozzy_price,picture]) #заносит все цены из БД

            total_product_info.append(
                {result: [
                    order.amount, order.atb_choice, order.eko_choice, order.varus_choice,
                    order.silpo_choice, order.ashan_choice, order.novus_choice, order.metro_choice,
                    order.nash_kray_choice, order.fozzy_choice, atb_price, eko_price, varus_price, silpo_price,
                    ashan_price,novus_price,metro_price,nash_kray_price,fozzy_price,picture,best_price
                ]}
            )
        return total_product_info

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['all_relevant_markets'] = get_all_markets
        # отображение списка кортежей с полной информацией по заказу
        context_dict['products_set'] = self.NN_works()
        mutual_context_dict = self.get_user_context(title='Результаты по наборам')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только те записи из БД,
         которые принадлежат текущему пользователю'''

        return super().get_queryset().filter(owner=self.request.user.id)


class Thanksfull_DELETE_SET(MutualContext, ListView):
    '''Класс для удаления продуктовых наборов из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = SetOfProducts

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем названия товара из БД'''

        # тут удаляем загруженное название из БД айдишнюку текущего пользователя
        user_id = super().get_queryset().filter(owner=self.request.user.id)
        return user_id.delete()


class UserRegistration(MutualContext, CreateView):
    '''Класс для регистрации пользователей на сайте'''
    form_class = UserRegisterForm
    template_name = 'my_app/user_registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['all_relevant_markets'] = get_all_markets
        context_dict['total'] = 150
        mutual_context_dict = self.get_user_context(title='Регистрация')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def form_valid(self, form):
        '''Автоматическая авторизация пользователя
         при его успешной регистрации'''
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    '''Класс для авторизации пользователя'''
    form_class = LoginForm
    template_name = 'my_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    '''Функция-обработчик для запросов несуществующих страниц приложения'''
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Далее идут обработчики для REST API!!!
class MainPageAPI(generics.ListAPIView):
    '''Обработчик для предоставления данных из БД по главной странице приложения.
    Работает только для GET-запросов со стороны клиента.'''

    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer


class SitePoliticsAPI(generics.ListAPIView):
    '''Обработчик для предоставления данных из БД по
    условиям пользовательских соглашений.
    Работает только для get-запросов со стороны клиента.'''

    queryset = SitePolitics.objects.all()
    serializer_class = SitePoliticsSerializer


class ItemsInfoAPIPagination(PageNumberPagination):
    '''Класс пагинации для представления ItemsInfoAPI'''

    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 50


class ItemsInfoAPI(generics.ListAPIView):
    """Обработчик для предоставлений из БД
    информации о продуктах, которые может обрабатывать
    приложение(название товара, фото и описание)"""

    queryset = ItemsPicsFromNet.objects.all()
    serializer_class = ItemsFromNetSerializer

    pagination_class = ItemsInfoAPIPagination
    permission_classes = (ReadOnlyPermission,)
