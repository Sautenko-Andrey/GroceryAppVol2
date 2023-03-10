import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

import keras
from tensorflow import keras

from keras.layers import Dense, Embedding, LSTM
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

from .utils import make_list


class GroceryAppText:
    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    def __init__(self):
        '''Инициализация модели НС и ее подготовка к обучению'''

        self.model = keras.Sequential([
            Embedding(self.MAX_WORDS, 150, input_length=self.MAX_LENGTH_TEXT),
            LSTM(150, return_sequences=True),  # 128
            LSTM(100),  # 64
            Dense(54, activation='softmax')
        ])

        self.model.compile(optimizer=Adam(0.0001), loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def training_NN(self):
        '''Метод обучения НС'''

        # загружаем подготовленные данные для обучения:
        TRAIN_DATA, TARGET_DATA, tokenizer = self.converted_data()

        # запускаем тренировку:
        history = self.model.fit(TRAIN_DATA, TARGET_DATA, batch_size=50, epochs=150)

        reverse_word_map = dict(map(reversed, self.converted_data()[2].word_index.items()))

        # сохраняем модель обученной НС:
        self.model.save('my_model_text_v56')  # сохранил не как h5!!!

        return history, reverse_word_map

    def add_new_item(self, path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'
        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def upload_data(self):
        """Функция загрузки обучающей выборки для каждой позиции товара"""

        # загрузка обучающего текста
        obolon_premium_extra_11_text = self.add_new_item('pivo_obolon_extra(1.1).txt')
        hetman_sagaydachniy_07_text = self.add_new_item('vodka_hetman(0.7).txt')
        coffee_aroma_gold_classic_100gr_text = self.add_new_item('coffee_aroma_gold_classic_100gr.txt')
        apple_golden_text = self.add_new_item('apple_golden.txt')
        coca_cola_2l_text = self.add_new_item('coca_cola.txt')
        KOMO_paprikash_text = self.add_new_item('furnaced_cheese_KOMO_paprikash.txt')
        garlik_text = self.add_new_item('garlik.txt')
        kent_8_text = self.add_new_item('kent_8.txt')
        tea_minutka_40_p_black_text = self.add_new_item('tea_minutka_40_packs_black.txt')
        oil_shedriy_dar_850_text = self.add_new_item('oil_shedriy_dar_850.txt')
        onion_text = self.add_new_item('onion.txt')
        fairy_text = self.add_new_item('fairy.txt')
        apple_black_prince_text = self.add_new_item('apple_black_prince.txt')
        gorchica_kolos_text = self.add_new_item('gorchica_kolos.txt')
        smetana_stolica_smaky_20_400_text = self.add_new_item('smetana_stolica_smaky_20jir_400g.txt')
        limon_text = self.add_new_item('limon.txt')
        oil_oleyna_neraf_850_text = self.add_new_item('oil_oleyna_neraf_850.txt')
        pivo_lvivske_svitle_24l_text = self.add_new_item('pivo_lvivske_svitle_24l.txt')
        pena_arko_cool_200_100_text = self.add_new_item('pena_arko_cool_200_bonus_100.txt')
        pena_arko_sensitive_200_100_text = self.add_new_item('pena_arko_sensitive_200_bonus_100.txt')
        carrot_text = self.add_new_item('carrot.txt')
        drojji_text = self.add_new_item('drojji.txt')
        eggs_text = self.add_new_item('eggs.txt')
        desodorant_garnier_magniy_text = self.add_new_item('desodorant_garnier_magniy_m.txt')
        cabbage_text = self.add_new_item('cabbage.txt')
        marlboro_red_text = self.add_new_item('marlboro_red.txt')
        mayonez_detsk_shedro_190_text = self.add_new_item('mayonez_dom_detsk_shedro.txt')
        rexona_aloe_vera_w_text = self.add_new_item('rexona_aloe_vera_w.txt')
        smetana_stolica_smaky_15jir_400gr_text = self.add_new_item('smetana_stolica_smaky_15jir_400g.txt')
        tea_monomah_kenya_90_text = self.add_new_item('tea_monomah-kenya_90.txt')
        toilet_papir_text = self.add_new_item('toilet_papir_kiev_63m.txt')
        coffee_aroma_gold_freeze_dried_70g_text = self.add_new_item('coffee_aroma_gold_freeze_dried_70g.txt')
        gorchica_veres_ukrainska_micna_120g_text = self.add_new_item('gorchica_veres_ukrainska_micna_120g.txt')
        tea_monomah_100_ceylon_original_black_krupn_list_90g_text = self.add_new_item(
            'tea_monomah_100%_ceylon_original_black_krupn_list_90g.txt')
        tea_monomah_ceylon_black_text = self.add_new_item('tea_monomah_ceylon_black.txt')
        apple_gala_text = self.add_new_item('apple_gala.txt')
        desodorant_garnier_spring_spirit_text = self.add_new_item('desodorant_garnier_spring_spirit.txt')
        smetana_galichanska_15_370gr_text = self.add_new_item('smetana_galichanska_15_370gr.txt')
        chips_lays_with_salt_big_pack_text = self.add_new_item('chips_lays_with_salt_big_pack.txt')
        sprite_2l_text = self.add_new_item('sprite_2l.txt')
        fanta_2l_text = self.add_new_item('fanta_2l.txt')
        bond_street_blue_selection_text=self.add_new_item('bond_street_blue_selection.txt')
        camel_blue_text=self.add_new_item('camel_blue.txt')
        LD_red_text=self.add_new_item('LD_red.txt')
        marlboro_gold_text=self.add_new_item('marlboro_gold.txt')
        rotmans_demi_blue_exclusive_text=self.add_new_item('rotmans_demi_blue_exclusive.txt')
        rotmans_demi_click_purple_text=self.add_new_item('rotmans_demi_click_purple.txt')
        winston_caster_text=self.add_new_item('winston_caster.txt')
        parlament_aqua_blue_text=self.add_new_item('parlament_aqua_blue.txt')
        winston_blue_text=self.add_new_item('winston_blue.txt')
        bond_street_red_selection_text=self.add_new_item('bond_street_red_selection.txt')
        LD_blue_text=self.add_new_item('LD_blue.txt')
        kent_silver_text=self.add_new_item('kent_silver.txt')
        kent_navy_blue_new_text=self.add_new_item('kent_navy_blue_new.txt')

        # объединям обучающие выборки:
        texts = obolon_premium_extra_11_text + hetman_sagaydachniy_07_text \
                + coffee_aroma_gold_classic_100gr_text + apple_golden_text \
                + coca_cola_2l_text + KOMO_paprikash_text + garlik_text \
                + kent_8_text + tea_minutka_40_p_black_text + oil_shedriy_dar_850_text \
                + onion_text + fairy_text + apple_black_prince_text + gorchica_kolos_text \
                + smetana_stolica_smaky_20_400_text + limon_text + oil_oleyna_neraf_850_text \
                + pivo_lvivske_svitle_24l_text + pena_arko_cool_200_100_text \
                + pena_arko_sensitive_200_100_text + carrot_text + drojji_text + eggs_text \
                + desodorant_garnier_magniy_text + cabbage_text \
                + marlboro_red_text + mayonez_detsk_shedro_190_text \
                + rexona_aloe_vera_w_text + smetana_stolica_smaky_15jir_400gr_text \
                + tea_monomah_kenya_90_text + toilet_papir_text + coffee_aroma_gold_freeze_dried_70g_text \
                + gorchica_veres_ukrainska_micna_120g_text \
                + tea_monomah_100_ceylon_original_black_krupn_list_90g_text \
                + tea_monomah_ceylon_black_text + apple_gala_text \
                + desodorant_garnier_spring_spirit_text + smetana_galichanska_15_370gr_text \
                + chips_lays_with_salt_big_pack_text + sprite_2l_text + fanta_2l_text\
                + bond_street_blue_selection_text + camel_blue_text + LD_red_text\
                + marlboro_gold_text + rotmans_demi_blue_exclusive_text+rotmans_demi_click_purple_text\
                + winston_caster_text + parlament_aqua_blue_text + winston_blue_text\
                + bond_street_red_selection_text + LD_blue_text + kent_silver_text\
                + kent_navy_blue_new_text

        # подсчитываем кол-во выборок
        count_obolon_premium_extra_11_text = len(obolon_premium_extra_11_text)
        count_hetman_sagaydachniy_07_text = len(hetman_sagaydachniy_07_text)
        count_coffee_aroma_gold_classic_100gr_text = len(coffee_aroma_gold_classic_100gr_text)
        count_apple_golden_text = len(apple_golden_text)
        count_coca_cola_2l_text = len(coca_cola_2l_text)
        count_KOMO_paprikash_text = len(KOMO_paprikash_text)
        count_garlik_text = len(garlik_text)
        count_kent_8_text = len(kent_8_text)
        count_tea_minutka_40_p_black_text = len(tea_minutka_40_p_black_text)
        count_oil_shedriy_dar_850_text = len(oil_shedriy_dar_850_text)
        count_onion_text = len(onion_text)
        count_fairy_text = len(fairy_text)
        count_apple_black_prince_text = len(apple_black_prince_text)
        count_gorchica_kolos_text = len(gorchica_kolos_text)
        count_smetana_stolica_smaky_20_400_text = len(smetana_stolica_smaky_20_400_text)
        count_limon_text = len(limon_text)
        count_oil_oleyna_neraf_850_text = len(oil_oleyna_neraf_850_text)
        count_pivo_lvivske_svitle_24l_text = len(pivo_lvivske_svitle_24l_text)
        count_pena_arko_cool_200_100_text = len(pena_arko_cool_200_100_text)
        count_pena_arko_sensitive_200_100_text = len(pena_arko_sensitive_200_100_text)
        count_carrot_text = len(carrot_text)
        count_drojji_text = len(drojji_text)
        count_eggs_text = len(eggs_text)
        count_desodorant_garnier_magniy_text = len(desodorant_garnier_magniy_text)
        count_cabbage_text = len(cabbage_text)
        count_marlboro_red_text = len(marlboro_red_text)
        count_mayonez_detsk_shedro_190_text = len(mayonez_detsk_shedro_190_text)
        count_rexona_aloe_vera_w_text = len(rexona_aloe_vera_w_text)
        count_smetana_stolica_smaky_15jir_400gr_text = len(smetana_stolica_smaky_15jir_400gr_text)
        count_tea_monomah_kenya_90_text = len(tea_monomah_kenya_90_text)
        count_toilet_papir_text = len(toilet_papir_text)
        count_coffee_aroma_gold_freeze_dried_70g_text = len(coffee_aroma_gold_freeze_dried_70g_text)
        count_gorchica_veres_ukrainska_micna_120g_text = len(gorchica_veres_ukrainska_micna_120g_text)
        count_tea_monomah_100_ceylon_original_black_krupn_list_90g_text = len(
            tea_monomah_100_ceylon_original_black_krupn_list_90g_text)
        count_tea_monomah_ceylon_black_text = len(tea_monomah_ceylon_black_text)
        count_apple_gala_text = len(apple_gala_text)
        count_desodorant_garnier_spring_spirit_text = len(desodorant_garnier_spring_spirit_text)
        count_smetana_galichanska_15_370gr_text = len(smetana_galichanska_15_370gr_text)
        count_chips_lays_with_salt_big_pack_text = len(chips_lays_with_salt_big_pack_text)
        count_sprite_2l_text = len(sprite_2l_text)
        count_fanta_2l_text = len(fanta_2l_text)
        count_bond_street_blue_selection_text=len(bond_street_blue_selection_text)
        count_camel_blue_text=len(camel_blue_text)
        count_LD_red_text=len(LD_red_text)
        count_marlboro_gold_text=len(marlboro_gold_text)
        count_rotmans_demi_blue_exclusive_text=len(rotmans_demi_blue_exclusive_text)
        count_rotmans_demi_click_purple_text=len(rotmans_demi_click_purple_text)
        count_winston_caster_text=len(winston_caster_text)
        count_parlament_aqua_blue_text=len(parlament_aqua_blue_text)
        count_winston_blue_text=len(winston_blue_text)
        count_bond_street_red_selection_text=len(bond_street_red_selection_text)
        count_LD_blue_text=len(LD_blue_text)
        count_kent_silver_text=len(kent_silver_text)
        count_kent_navy_blue_new_text=len(kent_navy_blue_new_text)

        return texts, count_obolon_premium_extra_11_text, count_hetman_sagaydachniy_07_text, \
               count_coffee_aroma_gold_classic_100gr_text, count_apple_golden_text, count_coca_cola_2l_text, \
               count_KOMO_paprikash_text, count_garlik_text, count_kent_8_text, count_tea_minutka_40_p_black_text, \
               count_oil_shedriy_dar_850_text, count_onion_text, count_fairy_text, count_apple_black_prince_text, \
               count_gorchica_kolos_text, count_smetana_stolica_smaky_20_400_text, count_limon_text, count_oil_oleyna_neraf_850_text, \
               count_pivo_lvivske_svitle_24l_text, count_pena_arko_cool_200_100_text, count_pena_arko_sensitive_200_100_text, \
               count_carrot_text, count_drojji_text, count_eggs_text, count_desodorant_garnier_magniy_text, \
               count_cabbage_text, count_marlboro_red_text, count_mayonez_detsk_shedro_190_text, \
               count_rexona_aloe_vera_w_text, count_smetana_stolica_smaky_15jir_400gr_text, \
               count_tea_monomah_kenya_90_text, count_toilet_papir_text, count_coffee_aroma_gold_freeze_dried_70g_text, \
               count_gorchica_veres_ukrainska_micna_120g_text, count_tea_monomah_100_ceylon_original_black_krupn_list_90g_text, \
               count_tea_monomah_ceylon_black_text, count_apple_gala_text, count_desodorant_garnier_spring_spirit_text, \
               count_smetana_galichanska_15_370gr_text, count_chips_lays_with_salt_big_pack_text, count_sprite_2l_text, \
               count_fanta_2l_text,count_bond_street_blue_selection_text,count_camel_blue_text,count_LD_red_text,\
               count_marlboro_gold_text,count_rotmans_demi_blue_exclusive_text,count_rotmans_demi_click_purple_text,\
               count_winston_caster_text,count_parlament_aqua_blue_text,count_winston_blue_text,\
               count_bond_street_red_selection_text,count_LD_blue_text,count_kent_silver_text,count_kent_navy_blue_new_text


    def converted_data(self):
        '''Подготовка обучающих данных'''

        # загружаем общую папку с текстами для обработки:
        texts = self.upload_data()[0]

        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(texts)

        # формируем последовательность из чисел вместо слов
        # (будут индексы каждых слов вместо слов)
        data = tokenizer.texts_to_sequences(texts)

        # короткие тексты дополняем нулями, а длинные урезаем до 10 слов:
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # окончательно формируем обучающую выборку:
        TRAIN_SAMPLE = data_pad
        items = 54
        TARGET_SAMPLE = np.array(
            make_list(items, 0) *
            self.upload_data()[1] + make_list(items, 1) * self.upload_data()[2] + make_list(items, 2) *
            self.upload_data()[3] + make_list(items, 3) * self.upload_data()[4] + make_list(items, 4) *
            self.upload_data()[5] + make_list(items, 5) * self.upload_data()[6] + make_list(items, 6) *
            self.upload_data()[7] + make_list(items, 7) * self.upload_data()[8] + make_list(items, 8) *
            self.upload_data()[9] + make_list(items, 9) * self.upload_data()[10] + make_list(items, 10) *
            self.upload_data()[11] + make_list(items, 11) * self.upload_data()[12] + make_list(items, 12) *
            self.upload_data()[13] + make_list(items, 13) * self.upload_data()[14] + make_list(items, 14) *
            self.upload_data()[15] + make_list(items, 15) * self.upload_data()[16] + make_list(items, 16) *
            self.upload_data()[17] + make_list(items, 17) * self.upload_data()[18] + make_list(items, 18) *
            self.upload_data()[19] + make_list(items, 19) * self.upload_data()[20] + make_list(items, 20) *
            self.upload_data()[21] + make_list(items, 21) * self.upload_data()[22] + make_list(items, 22) *
            self.upload_data()[23] + make_list(items, 23) * self.upload_data()[24] + make_list(items, 24) *
            self.upload_data()[25] + make_list(items, 25) * self.upload_data()[26] + make_list(items, 26) *
            self.upload_data()[27] + make_list(items, 27) * self.upload_data()[28] + make_list(items, 28) *
            self.upload_data()[29] + make_list(items, 29) * self.upload_data()[30] + make_list(items, 30) *
            self.upload_data()[31] + make_list(items, 31) * self.upload_data()[32] + make_list(items, 32) *
            self.upload_data()[33] + make_list(items, 33) * self.upload_data()[34] + make_list(items, 34) *
            self.upload_data()[35] + make_list(items, 35) * self.upload_data()[36] + make_list(items, 36) *
            self.upload_data()[37] + make_list(items, 37) * self.upload_data()[38] + make_list(items, 38) *
            self.upload_data()[39] + make_list(items, 39) *self.upload_data()[40] + make_list(items, 40) *
            self.upload_data()[41] + make_list(items, 41) *self.upload_data()[42] + make_list(items, 42) *
            self.upload_data()[43]+ make_list(items, 43) *self.upload_data()[44]+ make_list(items, 44) *
            self.upload_data()[45]+ make_list(items, 45) *self.upload_data()[46]+ make_list(items, 46) *
            self.upload_data()[47] + make_list(items, 47) *self.upload_data()[48]+ make_list(items, 48) *
            self.upload_data()[49]+ make_list(items, 49) *
            self.upload_data()[50]+ make_list(items, 50) *
            self.upload_data()[51]+ make_list(items, 51) *
            self.upload_data()[52]+ make_list(items, 52) *
            self.upload_data()[53]+ make_list(items, 53) *
            self.upload_data()[54])

        # перемешиваем обучающую выборку для лучшей тренированности НС:
        # создаем рандомные индексы:
        indeces = np.random.choice(TRAIN_SAMPLE.shape[0], size=TRAIN_SAMPLE.shape[0],
                                   replace=False)

        # перемешиаем обучающую и целевую выборки:
        TRAIN_SAMPLE = TRAIN_SAMPLE[indeces]
        TARGET_SAMPLE = TARGET_SAMPLE[indeces]

        return TRAIN_SAMPLE, TARGET_SAMPLE, tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = self.training_NN()[1]
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def defining_item(self, user_text):
        '''Метод определения товара по тексту, который запрашивает пользователь '''

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.converted_data()[2]
        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # смотрим какую на самом деле фразу мы анализируем(т.к. некоторых слов у нас может не быть в словаре)
        print(self.index_convert_to_text(data[0]))

        # получаем прогноз. если перменная argmax принимает значение 0 ( 0 - это первый нейрон,
        # отвечающий за пиво "Оболонь Премиум Экстра 1,1 л"),то пользователь ищет пиво "Оболонь Премиум Экстра 1,1 л",
        # если 1 , то пользователь ищет водку "Гетьман Сагайдачный 0,7 л"

        result = self.model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')
        # if np.argmax(result) == 0:
        #     print('Пиво "Оболонь Премиум Экстра 1,1 л"')
        # else:
        #     print('Водка "Гетьман Сагайдачный 0,7 л"')


user = GroceryAppText()
user.training_NN()
