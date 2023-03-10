import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model


class TesterForGroceryAppText:
    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    def add_new_item(self,path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'
        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def prepearing_data(self):

        #загрузка обучающего текста
        obolon_premium_extra_11_text=self.add_new_item('pivo_obolon_extra(1.1).txt')
        hetman_sagaydachniy_07_text=self.add_new_item('vodka_hetman(0.7).txt')
        coffee_aroma_gold_classic_100gr_text=self.add_new_item('coffee_aroma_gold_classic_100gr.txt')
        apple_golden_text=self.add_new_item('apple_golden.txt')
        coca_cola_2l_text=self.add_new_item('coca_cola.txt')
        KOMO_paprikash_text=self.add_new_item('furnaced_cheese_KOMO_paprikash.txt')
        garlik_text=self.add_new_item('garlik.txt')
        kent_8_text=self.add_new_item('kent_8.txt')
        tea_minutka_40_p_black_text=self.add_new_item('tea_minutka_40_packs_black.txt')
        oil_shedriy_dar_850_text=self.add_new_item('oil_shedriy_dar_850.txt')
        onion_text=self.add_new_item('onion.txt')
        fairy_text=self.add_new_item('fairy.txt')
        apple_black_prince_text=self.add_new_item('apple_black_prince.txt')
        gorchica_kolos_text=self.add_new_item('gorchica_kolos.txt')
        smetana_stolica_smaky_20_400_text=self.add_new_item('smetana_stolica_smaky_20jir_400g.txt')
        limon_text=self.add_new_item('limon.txt')
        oil_oleyna_neraf_850_text=self.add_new_item('oil_oleyna_neraf_850.txt')
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
        fanta_2l_text=self.add_new_item('fanta_2l.txt')
        bond_street_blue_selection_text = self.add_new_item('bond_street_blue_selection.txt')
        camel_blue_text = self.add_new_item('camel_blue.txt')
        LD_red_text = self.add_new_item('LD_red.txt')
        marlboro_gold_text = self.add_new_item('marlboro_gold.txt')
        rotmans_demi_blue_exclusive_text = self.add_new_item('rotmans_demi_blue_exclusive.txt')
        rotmans_demi_click_purple_text = self.add_new_item('rotmans_demi_click_purple.txt')
        winston_caster_text = self.add_new_item('winston_caster.txt')
        parlament_aqua_blue_text = self.add_new_item('parlament_aqua_blue.txt')
        winston_blue_text = self.add_new_item('winston_blue.txt')
        bond_street_red_selection_text = self.add_new_item('bond_street_red_selection.txt')
        LD_blue_text = self.add_new_item('LD_blue.txt')
        kent_silver_text = self.add_new_item('kent_silver.txt')
        kent_navy_blue_new_text = self.add_new_item('kent_navy_blue_new.txt')

        # объединям обучающие выборки:
        texts = obolon_premium_extra_11_text+ hetman_sagaydachniy_07_text\
                + coffee_aroma_gold_classic_100gr_text+ apple_golden_text\
                + coca_cola_2l_text + KOMO_paprikash_text+ garlik_text\
                + kent_8_text+ tea_minutka_40_p_black_text\
                + oil_shedriy_dar_850_text+ onion_text+ fairy_text\
                + apple_black_prince_text+ gorchica_kolos_text\
                + smetana_stolica_smaky_20_400_text+ limon_text\
                + oil_oleyna_neraf_850_text+ pivo_lvivske_svitle_24l_text\
                + pena_arko_cool_200_100_text+ pena_arko_sensitive_200_100_text\
                + carrot_text + drojji_text + eggs_text\
                + desodorant_garnier_magniy_text + cabbage_text\
                + marlboro_red_text + mayonez_detsk_shedro_190_text\
                + rexona_aloe_vera_w_text + smetana_stolica_smaky_15jir_400gr_text\
                + tea_monomah_kenya_90_text + toilet_papir_text\
                + coffee_aroma_gold_freeze_dried_70g_text + gorchica_veres_ukrainska_micna_120g_text\
                + tea_monomah_100_ceylon_original_black_krupn_list_90g_text\
                + tea_monomah_ceylon_black_text + apple_gala_text\
                + desodorant_garnier_spring_spirit_text + smetana_galichanska_15_370gr_text\
                + chips_lays_with_salt_big_pack_text + sprite_2l_text\
                + fanta_2l_text + bond_street_blue_selection_text + camel_blue_text + LD_red_text\
                + marlboro_gold_text + rotmans_demi_blue_exclusive_text + rotmans_demi_click_purple_text\
                + winston_caster_text + parlament_aqua_blue_text + winston_blue_text\
                + bond_street_red_selection_text + LD_blue_text + kent_silver_text + kent_navy_blue_new_text

        return texts

    def create_tokenizer(self):
        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(self.prepearing_data())

        return tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = dict(map(reversed, self.create_tokenizer().word_index.items()))
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def identify_item(self, user_text):

        # загружаем обученную модель НС для распознования товара по тексту:
        model = load_model('/home/andrey/GroceryApp/FBApp/my_app/my_model_text_v56')

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.create_tokenizer()

        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # получаем прогноз. если переменная argmax принимает значение 0 ( 0 - это первый нейрон,
        # отвечающий за пиво "Оболонь Премиум Экстра 1,1 л"),то пользователь ищет пиво "Оболонь Премиум Экстра 1,1 л",
        # если 1 , то пользователь ищет водку "Гетьман Сагайдачный 0,7 л"

        result = model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')
        if np.argmax(result) == 0:
            return 'Пиво "Оболонь Премиум Экстра 1,1 л"'
        elif np.argmax(result)==1:
            return 'Водка "Гетьман ICE 0,7 л"'
        elif np.argmax(result)==2:
            return 'Кофе "Арома Голд Классик 100 гр"'
        elif np.argmax(result)==3:
            return 'Яблоко Голден, 1 кг'
        elif np.argmax(result)==4:
            return 'Напиток Coca Cola 2 л'
        elif np.argmax(result)==5:
            return 'Сырок плавленный КОМО Паприкаш'
        elif np.argmax(result)==6:
            return 'Чеснок'
        elif np.argmax(result)==7:
            return 'Сигареты Кент 8'
        elif np.argmax(result)==8:
            return 'Чай "Минутка" черный 40 пакетиков'
        elif np.argmax(result) == 9:
            return 'Масло подсолнечное "Щедрый Дар" 850 г рафинированное'
        elif np.argmax(result) == 10:
            return 'Лук, 1 кг'
        elif np.argmax(result) == 11:
            return 'Средство для мытья посуды Fairy, лимон, 500 г'
        elif np.argmax(result) == 12:
            return 'Яблоко "Черный принц"'
        elif np.argmax(result) == 13:
            return 'Горчица "Колос"'
        elif np.argmax(result) == 14:
            return 'Сметана "Столица Смаку" 20% 400 гр'
        elif np.argmax(result) == 15:
            return 'Лимон, 1 кг'
        elif np.argmax(result) ==16:
            return 'Масло подсолнечное нерафинированное Олейна, 850 гр'
        elif np.argmax(result) == 17:
            return 'Пиво Львовское светлое 2.4 литра'
        elif np.argmax(result) == 18:
            return 'Пена для бритья "Arko Cool 200 млг + бонус 100 млг"'
        elif np.argmax(result) == 19:
            return 'Пена для бритья "Arko Sensitive 200 млг + бонус 100 млг"'
        elif np.argmax(result)==20:
            return 'Морковь, 1 кг'
        elif np.argmax(result) ==21:
            return 'Дрожжи харьковские 100 гр хлебо-пекарские пресованные'
        elif np.argmax(result) == 22:
            return 'Яйца куринные, 10 штук'
        elif np.argmax(result) == 23:
            return 'Дезодорант Garnier Магний для мужчин'
        elif np.argmax(result) == 24:
            return 'Капуста белокачанная , 1 кг'
        elif np.argmax(result)==25:
            return 'Сигареты Marlboro Red'
        elif np.argmax(result) == 26:
            return 'Майонез детский Щедро домашний 67% жирности'
        elif np.argmax(result) == 27:
            return 'Дезодорант Rexona Aloe Vera женский'
        elif np.argmax(result) == 28:
            return 'Сметана Столица Смаку 15% жирности 400 гр'
        elif np.argmax(result) == 29:
            return 'Чай Мономах Кения черный 90 гр'
        elif np.argmax(result) == 30:
            return 'Туалетная бумага Киев 63 м'
        elif np.argmax(result) == 31:
            return 'Кофе Арома Голд Freeze Dried 70 грамм'
        elif np.argmax(result) == 32:
            return 'Горчица Верес украинска мицна 120 грамм'
        elif np.argmax(result) == 33:
            return 'Чай Мономах 100% Цейлон Original черный крупнолистовой'
        elif np.argmax(result) == 34:
            return 'Чай Мономах Цейлон черный'
        elif np.argmax(result) == 35:
            return 'Яблоко Гала, кг'
        elif np.argmax(result) == 36:
            return 'Дезодорант Garnier весенняя свежесть'
        elif np.argmax(result) == 37:
            return 'Сметана Галичанская 15% 370 грамм'
        elif np.argmax(result) == 38:
            return 'Чипсы Lays с солью большая пачка 30 грамм'
        elif np.argmax(result) == 39:
            return 'Напиток Sprite 2 литра'
        elif np.argmax(result) == 40:
            return 'Напиток Fanta 2 литра'
        elif np.argmax(result) == 41:
            return 'Сигареты Bond Street Blue Selection'
        elif np.argmax(result) == 42:
            return 'Сигареты Camel Blue'
        elif np.argmax(result) == 43:
            return 'Сигареты LD Red'
        elif np.argmax(result) == 44:
            return 'Сигареты Marlboro Gold'
        elif np.argmax(result) == 45:
            return 'Сигареты Rothmans Demi BLue Exclusive'
        elif np.argmax(result) == 46:
            return 'Сигареты Rothmans Demi Click Purple'
        elif np.argmax(result) == 47:
            return 'Сигареты Winston Caster'
        elif np.argmax(result) == 48:
            return 'Сигареты Parlament Aqua Blue'
        elif np.argmax(result) == 49:
            return 'Сигареты Winston Blue'
        elif np.argmax(result) == 50:
            return 'Сигареты Bond Street Red Selection'
        elif np.argmax(result) == 51:
            return 'Сигареты LD Blue'
        elif np.argmax(result) == 52:
            return 'Сигареты Kent Silver'
        elif np.argmax(result) == 53:
            return 'Kent Navy Blue New'

# user_Andrey=TesterForGroceryAppText()
# user_Andrey.identify_item('Пиво Оболонь Премиум 1 л')
