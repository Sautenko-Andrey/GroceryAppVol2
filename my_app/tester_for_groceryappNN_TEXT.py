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
        tea_monomah_100_ceylon_original_black_krupn_list_90g_text = self.add_new_item('tea_monomah_100%_ceylon_original_black_krupn_list_90g.txt')
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
        beer_chernigivske_svitle_05_l_glass_text = self.add_new_item('beer_chernigivske_svitle_05_l_glass.txt')
        beer_stella_artois_05_l_glass_text = self.add_new_item('beer_stella_artois_05_l_glass.txt')
        beer_obolon_svitle_05_l_glass_text=self.add_new_item('beer_obolon_svitle_05_l_glass.txt')
        beer_jigulivske_svitle_05_l_glass_text = self.add_new_item('beer_jigulivske_svitle_05_l_glass.txt')
        beer_rogan_tradiciyne_svitle_05_l_glass_text = self.add_new_item('beer_rogan_tradiciyne_svitle_05_l_glass.txt')
        beer_corona_extra_svitle_033_l_glass_text = self.add_new_item('beer_corona_extra_svitle_033_l_glass.txt')
        beer_chernigivske_bile_nefilter_05_l_glass_text = self.add_new_item('beer_chernigivske_bile_nefilter_05_l_glass.txt')
        beer_yantar_svitle_05_l_glass_text = self.add_new_item('beer_yantar_svitle_05_l_glass.txt')
        beer_zibert_svitle_05_l_glass_text = self.add_new_item('beer_zibert_svitle_05_l_glass.txt')
        beer_arsenal_micne_05_l_glass_text = self.add_new_item('beer_arsenal_micne_05_l_glass.txt')
        beer_persha_brovarnya_zakarpatske_05_l_glass_text = self.add_new_item('beer_persha_brovarnya_zakarpatske_05_l_glass.txt')
        beer_lvivske_svitle_05_l_glass_text = self.add_new_item('beer_lvivske_svitle_05_l_glass.txt')
        beer_lvivske_1715_05_l_glass_text = self.add_new_item('beer_lvivske_1715_05_l_glass.txt')
        beer_zlata_praha_svitle_05_l_glass_text = self.add_new_item('beer_zlata_praha_svitle_05_l_glass.txt')
        beer_tuborg_green_05_l_glass_text = self.add_new_item('beer_tuborg_green_05_l_glass.txt')
        beer_slavutich_ice_mix_lime_svitle_05_l_glass_text = self.add_new_item('beer_slavutich_ice_mix_lime_svitle_05_l_glass.txt')
        beer_teteriv_svitle_05_l_glass_text = self.add_new_item('beer_teteriv_svitle_05_l_glass.txt')
        beer_krusovice_svitle_05_l_glass_text = self.add_new_item('beer_krusovice_svitle_05_l_glass.txt')
        beer_heineken_svitle_05_l_glass_text = self.add_new_item('beer_heineken_svitle_05_l_glass.txt')
        beer_amstel_svitle_05_l_glass_text = self.add_new_item('beer_amstel_svitle_05_l_glass.txt')
        beer_hike_premium_svitle_05_l_glass_text = self.add_new_item('beer_hike_premium_svitle_05_l_glass.txt')
        beer_bochkove_svitle_05_l_glass_text = self.add_new_item('beer_bochkove_svitle_05_l_glass.txt')
        beer_kronenbourg_1664_blanc_046_l_glass_text = self.add_new_item('beer_kronenbourg_1664_blanc_046_l_glass.txt')
        beer_opilla_nepasterizovane_05_l_glass_text = self.add_new_item('beer_opilla_nepasterizovane_05_l_glass.txt')
        beer_yachminniy_kolos_svitle_05_l_glass_text = self.add_new_item('beer_yachminniy_kolos_svitle_05_l_glass.txt')
        beer_opilla_korifey_05_l_glass_text = self.add_new_item('beer_opilla_korifey_05_l_glass.txt')
        beer_chayka_dniprovska_svitle_05_l_glass_text = self.add_new_item('beer_chayka_dniprovska_svitle_05_l_glass.txt')
        beer_chayka_chernomorska_svitle_05_l_glass_text = self.add_new_item('beer_chayka_chernomorska_svitle_05_l_glass.txt')
        beer_uman_pivo_waissburg_svitle_1l_plastic_text = self.add_new_item('beer_uman_pivo_waissburg_svitle_1l_plastic.txt')
        beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text = self.add_new_item('beer_uman_pivo_pshenichnoe_svitle_1l_plastic.txt')
        beer_berdichevske_hmilne_svitle_1l_plastic_text = self.add_new_item('beer_berdichevske_hmilne_svitle_1l_plastic.txt')
        beer_berdichevske_lager_svitle_1l_plastic_text = self.add_new_item('beer_berdichevske_lager_svitle_1l_plastic.txt')
        beer_opilla_korifey_svitle_11l_plastic_text = self.add_new_item('beer_opilla_korifey_svitle_11l_plastic.txt')
        beer_obolon_jigulivske_exportne_svitle_1l_plastic_text = self.add_new_item('beer_obolon_jigulivske_exportne_svitle_1l_plastic.txt')
        beer_yantar_svitle_12l_plastic_text = self.add_new_item('beer_yantar_svitle_12l_plastic.txt')
        beer_jashkivske_pshenichne_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_pshenichne_nefilter_1l_plastic.txt')
        beer_jashkivske_svitle_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_svitle_nefilter_1l_plastic.txt')
        beer_jashkivske_jigulivske_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_jigulivske_nefilter_1l_plastic.txt')
        beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text = self.add_new_item('beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic.txt')
        beer_chayka_dniprovska_svitle_1l_plastic_text = self.add_new_item('beer_chayka_dniprovska_svitle_1l_plastic.txt')
        ketchup_torchin_chasnik_270gr_text = self.add_new_item('ketchup_torchin_chasnik_270gr.txt')
        muka_zolote_zernyatko_pshen_2kg_text = self.add_new_item('muka_zolote_zernyatko_pshen_2kg.txt')
        mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text = self.add_new_item('mayonez_korolivskiy_smak_kororlivskiy_67_300gr.txt')
        beer_chernigivske_bile_nefilter_1l_plastic_text = self.add_new_item('beer_chernigivske_bile_nefilter_1l_plastic.txt')
        beer_obolon_svitle_1l_plastic_text = self.add_new_item('beer_obolon_svitle_1l_plastic.txt')
        beer_rogan_svitle_tradiciyne_1l_plastic_text = self.add_new_item('beer_rogan_svitle_tradiciyne_1l_plastic.txt')
        sous_chumak_chesnochniy_200gr_text = self.add_new_item('sous_chumak_chesnochniy_200gr.txt')
        jvachka_orbit_clubnika_banan_text = self.add_new_item('jvachka_orbit_clubnika_banan.txt')
        LM_red_text = self.add_new_item('LM_red.txt')
        beer_jigulivske_svitle_2_l_plastic_text = self.add_new_item('beer_jigulivske_svitle_2_l_plastic.txt')
        beer_chayka_dniprovska_svitle_2l_plastic_text = self.add_new_item('beer_chayka_dniprovska_svitle_2l_plastic.txt')
        beer_piwny_kubek_svitle_2l_plastic_text = self.add_new_item('beer_piwny_kubek_svitle_2l_plastic.txt')
        ketchup_torchin_do_shasliky_270gr_test = self.add_new_item('ketchup_torchin_do_shasliky_270gr.txt')
        mayonez_chumak_appetitniy_50_300gr_text = self.add_new_item('mayonez_chumak_appetitniy_50_300gr.txt')
        kolbasa_persha_stolica_salyami_firmennaya_vs_text = self.add_new_item('kolbasa_persha_stolica_salyami_firmennaya_vs.txt')
        coffee_chorna_karta_gold_50gr_text = self.add_new_item('coffee_chorna_karta_gold_50gr.txt')
        beer_arsenal_micne_svitle_2l_plastic_text = self.add_new_item('beer_arsenal_micne_svitle_2l_plastic.txt')
        beer_ppb_bochkove_svitle_2l_plastic_text = self.add_new_item('beer_ppb_bochkove_svitle_2l_plastic.txt')
        beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text = self.add_new_item('beer_ppb_zakarpatske_originalne_svitle_2l_plastic.txt')
        beer_zibert_svitle_05_l_banochnoe_text = self.add_new_item('beer_zibert_svitle_05_l_banochnoe.txt')
        yogurt_fanni_1_5_240gr_v_banke_text = self.add_new_item('yogurt_fanni_1_5_240gr_v_banke.txt')
        kefir_slviya_2_5_850gr_v_pakete_text = self.add_new_item('kefir_slviya_2_5_850gr_v_pakete.txt')
        beer_obolon_kievske_rozlivne_svitle_195l_plastic_text = self.add_new_item('beer_obolon_kievske_rozlivne_svitle_195l_plastic.txt')
        beer_chernigivske_light_svitle_2l_plastic_text = self.add_new_item('beer_chernigivske_light_svitle_2l_plastic.txt')
        beer_opilla_korifey_svitle_2l_plastic_text = self.add_new_item('beer_opilla_korifey_svitle_2l_plastic.txt')
        beer_yantar_svitle_2l_plastic_text = self.add_new_item('beer_yantar_svitle_2l_plastic.txt')
        beer_tuborg_green_05_4_banki_2litra_text = self.add_new_item('beer_tuborg_green_05_4_banki_2litra.txt')
        beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text = self.add_new_item('beer_ppb_zakarpatske_svitle_05_4_banki_2litra.txt')
        beer_ppb_bochkove_svitle_05_4_banki_2litra_text = self.add_new_item('beer_ppb_bochkove_svitle_05_4_banki_2litra.txt')
        beer_budweiser_budvar_05_l_glass_text = self.add_new_item('beer_budweiser_budvar_05_l_glass.txt')
        beer_pilsner_urquell_05_l_glass_text = self.add_new_item('beer_pilsner_urquell_05_l_glass.txt')
        beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text = self.add_new_item('beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass.txt')
        beer_chernigivske_svitle_05_l_jb_text = self.add_new_item('beer_chernigivske_svitle_05_l_jb.txt')
        beer_chernigivske_bile_nefilter_05_l_jb_text = self.add_new_item('beer_chernigivske_bile_nefilter_05_l_jb.txt')
        beer_velkopopovicky_kozel_temne_05_l_jb_text = self.add_new_item('beer_velkopopovicky_kozel_temne_05_l_jb.txt')
        beer_edelmeister_pilsner_svitle_05_l_jb_text = self.add_new_item('beer_edelmeister_pilsner_svitle_05_l_jb.txt')
        beer_faxe_svitle_05_l_jb_text = self.add_new_item('beer_faxe_svitle_05_l_jb.txt')
        beer_livu_pilzenes_svitle_05_l_jb_text = self.add_new_item('beer_livu_pilzenes_svitle_05_l_jb.txt')
        beer_velkopopovicky_kozel_svitle_05_l_jb_text = self.add_new_item('beer_velkopopovicky_kozel_svitle_05_l_jb.txt')
        beer_obolon_beermix_limon_05_l_jb_text = self.add_new_item('beer_obolon_beermix_limon_05_l_jb.txt')
        beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb.txt')
        beer_edelmeister_schwarzbier_temnoe_05_l_jb_text = self.add_new_item('beer_edelmeister_schwarzbier_temnoe_05_l_jb.txt')
        beer_hike_blanche_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_hike_blanche_svitle_nefilter_05_l_jb.txt')
        beer_zlata_praha_svitle_05_l_jb_text = self.add_new_item('beer_zlata_praha_svitle_05_l_jb.txt')
        beer_thuringer_premium_beer_svitle_05_l_jb_text = self.add_new_item('beer_thuringer_premium_beer_svitle_05_l_jb.txt')
        beer_livu_sencu_svitle_05_l_jb_text = self.add_new_item('beer_livu_sencu_svitle_05_l_jb.txt')
        beer_germanarich_svitle_05_l_jb_text = self.add_new_item('beer_germanarich_svitle_05_l_jb.txt')
        beer_hike_premium_svitle_05_l_jb_text = self.add_new_item('beer_hike_premium_svitle_05_l_jb.txt')
        beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_obolon_nonalcohol_svitle_nefilter_05_l_jb.txt')
        beer_zibert_bavarske_svitle_05_l_jb_text = self.add_new_item('beer_zibert_bavarske_svitle_05_l_jb.txt')
        beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb.txt')
        beer_heineken_svitle_05_l_jb_text = self.add_new_item('beer_heineken_svitle_05_l_jb.txt')
        beer_rychtar_grunt_11_svitle_05_l_jb_text = self.add_new_item('beer_rychtar_grunt_11_svitle_05_l_jb.txt')
        beer_amstel_svitle_05_l_jb_text = self.add_new_item('beer_amstel_svitle_05_l_jb.txt')
        beer_bavaria_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_svitle_05_l_jb.txt')
        beer_bavaria_svitle_nonalcohol_05_l_jb_text = self.add_new_item('beer_bavaria_svitle_nonalcohol_05_l_jb.txt')
        beer_edelburg_lager_svitle_05_l_jb_text = self.add_new_item('beer_edelburg_lager_svitle_05_l_jb.txt')
        beer_donner_pills_svitle_05_l_jb_text = self.add_new_item('beer_donner_pills_svitle_05_l_jb.txt')
        beer_dutch_windmill_svitle_05_l_jb_text = self.add_new_item('beer_dutch_windmill_svitle_05_l_jb.txt')
        beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb.txt')
        beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb.txt')
        beer_estrella_damm_barcelona_svitle_05_l_jb_text = self.add_new_item('beer_estrella_damm_barcelona_svitle_05_l_jb.txt')
        beer_halne_jasne_pelne_05_l_jb_text = self.add_new_item('beer_halne_jasne_pelne_05_l_jb.txt')
        beer_eurotour_hefeweissbier_svitle_05_l_jb_text = self.add_new_item('beer_eurotour_hefeweissbier_svitle_05_l_jb.txt')
        beer_hollandia_strong_svitle_05_l_jb_text = self.add_new_item('beer_hollandia_strong_svitle_05_l_jb.txt')
        beer_lander_brau_premium_svitle_05_l_jb_text = self.add_new_item('beer_lander_brau_premium_svitle_05_l_jb.txt')
        beer_saku_kuld_05_l_jb_text = self.add_new_item('beer_saku_kuld_05_l_jb.txt')
        beer_saku_original_05_l_jb_text = self.add_new_item('beer_saku_original_05_l_jb.txt')
        beer_stangen_lager_svitle_05_l_jb_text = self.add_new_item('beer_stangen_lager_svitle_05_l_jb.txt')
        beer_van_pur_premium_svitle_05_l_jb_text = self.add_new_item('beer_van_pur_premium_svitle_05_l_jb.txt')
        beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb.txt')
        beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_granat_bezalkogol_svitle_05_l_jb.txt')
        beer_obolon_beermix_malina_05_l_jb_text = self.add_new_item('beer_obolon_beermix_malina_05_l_jb.txt')
        beer_obolon_beermix_vishnya_05_l_jb_text = self.add_new_item('beer_obolon_beermix_vishnya_05_l_jb.txt')
        beer_lomza_svitle_05_l_jb_text = self.add_new_item('beer_lomza_svitle_05_l_jb.txt')
        beer_paderborner_pilsener_svitle_05_l_jb_text = self.add_new_item('beer_paderborner_pilsener_svitle_05_l_jb.txt')
        beer_paderborner_export_05_l_jb_text = self.add_new_item('beer_paderborner_export_05_l_jb.txt')
        beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_greipfruit_nonalcohol_05_l_jb.txt')
        beer_clausthaler_original_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_original_nonalcohol_05_l_jb.txt')
        beer_clausthaler_lemon_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_lemon_nonalcohol_05_l_jb.txt')
        beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_rock_n_roll_svitle_nefilter_05_l_jb.txt')
        beer_forever_black_queen_temne_nefilter_05_l_jb_text = self.add_new_item('beer_forever_black_queen_temne_nefilter_05_l_jb.txt')
        beer_forever_kite_safari_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_kite_safari_svitle_nefilter_05_l_jb.txt')
        beer_forever_crazy_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_crazy_svitle_nefilter_05_l_jb.txt')
        beer_hike_light_svitle_05_l_jb_text = self.add_new_item('beer_hike_light_svitle_05_l_jb.txt')
        beer_hike_zero_nonalcohol_05_l_jb_text = self.add_new_item('beer_hike_zero_nonalcohol_05_l_jb.txt')
        beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text = self.add_new_item('beer_horn_disel_ice_pilsner_svitle_0568_l_jb.txt')
        beer_horn_original_svitle_0568_l_jb_text = self.add_new_item('beer_horn_original_svitle_0568_l_jb.txt')
        beer_horn_traditional_svitle_0568_l_jb_text = self.add_new_item('beer_horn_traditional_svitle_0568_l_jb.txt')
        beer_horn_premium_svitle_05_l_jb_text = self.add_new_item('beer_horn_premium_svitle_05_l_jb.txt')
        beer_krusovice_cerne_temne_05_l_jb_text = self.add_new_item('beer_krusovice_cerne_temne_05_l_jb.txt')
        beer_lander_brau_micne_05_l_jb_text = self.add_new_item('beer_lander_brau_micne_05_l_jb.txt')
        beer_lander_brau_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_lander_brau_svitle_nefilter_05_l_jb.txt')
        beer_padeborner_pilger_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_padeborner_pilger_nefilter_svitle_05_l_jb.txt')
        beer_platan_jedenactka_05_l_jb_text = self.add_new_item('beer_platan_jedenactka_05_l_jb.txt')
        beer_praga_svitle_05_l_jb_text = self.add_new_item('beer_praga_svitle_05_l_jb.txt')
        beer_saku_rock_svitle_0568_l_jb_text = self.add_new_item('beer_saku_rock_svitle_0568_l_jb.txt')
        beer_sitnan_svitle_05_l_jb_text = self.add_new_item('beer_sitnan_svitle_05_l_jb.txt')
        beer_vienas_premium_golden_svitle_05_l_jb_text = self.add_new_item('beer_vienas_premium_golden_svitle_05_l_jb.txt')
        beer_vienas_premium_traditional_svitle_05_l_jb_text = self.add_new_item('beer_vienas_premium_traditional_svitle_05_l_jb.txt')
        beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb.txt')
        beer_zahringer_premium_svitle_05_l_jb_text = self.add_new_item('beer_zahringer_premium_svitle_05_l_jb.txt')
        beer_zahringer_hefeweizen_svitle_05_l_jb_text = self.add_new_item('beer_zahringer_hefeweizen_svitle_05_l_jb.txt')
        beer_jajkivske_svitle__nefilter_05_l_jb_text = self.add_new_item('beer_jajkivske_svitle__nefilter_05_l_jb.txt')
        beer_obolon_svitle_05_l_jb_text = self.add_new_item('beer_obolon_svitle_05_l_jb.txt')
        beer_pubster_svitle_05_l_jb_text = self.add_new_item('beer_pubster_svitle_05_l_jb.txt')
        beer_chaika_chernomorskaya_05_l_jb_text = self.add_new_item('beer_chaika_chernomorskaya_05_l_jb.txt')
        beer_ppb_zakarpatske_orig_svitle_05_l_jb_text = self.add_new_item('beer_ppb_zakarpatske_orig_svitle_05_l_jb.txt')
        beer_ppb_bochkove_nefilter_05_l_jb_text = self.add_new_item('beer_ppb_bochkove_nefilter_05_l_jb.txt')
        beer_ppb_nefilter_svitle_nonalco_05_l_jb_text = self.add_new_item('beer_ppb_nefilter_svitle_nonalco_05_l_jb.txt')
        beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text = self.add_new_item('beer_ppb_limon_lime_nonalco_nefilter_05_l_jb.txt')
        beer_chaika_dniprovskaya_05_l_jb_text = self.add_new_item('beer_chaika_dniprovskaya_05_l_jb.txt')
        beer_brok_export_svitle_05_l_jb_text = self.add_new_item('beer_brok_export_svitle_05_l_jb.txt')
        beer_carling_svitle_05_l_jb_text = self.add_new_item('beer_carling_svitle_05_l_jb.txt')
        beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text = self.add_new_item('beer_keten_brug_blanche_elegant_nefilter_05_l_jb.txt')
        beer_budweiser_nonalco_svitle_05_l_jb_text = self.add_new_item('beer_budweiser_nonalco_svitle_05_l_jb.txt')
        beer_feldschlosschen_wheat_beer_svitle05_l_jb_text = self.add_new_item('beer_feldschlosschen_wheat_beer_svitle05_l_jb.txt')
        beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text = self.add_new_item('beer_teteriv_hmilna_vishnya_polutemne_05_l_jb.txt')
        beer_grotwerg_svitle_nonalco_05_l_jb_text = self.add_new_item('beer_grotwerg_svitle_nonalco_05_l_jb.txt')
        beer_holland_import_svitle_05_l_jb_text = self.add_new_item('beer_holland_import_svitle_05_l_jb.txt')
        beer_golden_castle_export_svitle_05_l_jb_text = self.add_new_item('beer_golden_castle_export_svitle_05_l_jb.txt')
        beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb.txt')
        beer_guinness_draught_temne_044_l_jb_text = self.add_new_item('beer_guinness_draught_temne_044_l_jb.txt')

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
                + bond_street_red_selection_text + LD_blue_text + kent_silver_text\
                + kent_navy_blue_new_text + beer_chernigivske_svitle_05_l_glass_text\
                + beer_stella_artois_05_l_glass_text + beer_obolon_svitle_05_l_glass_text\
                + beer_jigulivske_svitle_05_l_glass_text + beer_rogan_tradiciyne_svitle_05_l_glass_text\
                + beer_corona_extra_svitle_033_l_glass_text + beer_chernigivske_bile_nefilter_05_l_glass_text\
                + beer_yantar_svitle_05_l_glass_text + beer_zibert_svitle_05_l_glass_text\
                + beer_arsenal_micne_05_l_glass_text + beer_persha_brovarnya_zakarpatske_05_l_glass_text\
                + beer_lvivske_svitle_05_l_glass_text + beer_lvivske_1715_05_l_glass_text\
                + beer_zlata_praha_svitle_05_l_glass_text + beer_tuborg_green_05_l_glass_text\
                + beer_slavutich_ice_mix_lime_svitle_05_l_glass_text + beer_teteriv_svitle_05_l_glass_text\
                + beer_krusovice_svitle_05_l_glass_text + beer_heineken_svitle_05_l_glass_text\
                + beer_amstel_svitle_05_l_glass_text + beer_hike_premium_svitle_05_l_glass_text\
                + beer_bochkove_svitle_05_l_glass_text + beer_kronenbourg_1664_blanc_046_l_glass_text\
                + beer_opilla_nepasterizovane_05_l_glass_text + beer_yachminniy_kolos_svitle_05_l_glass_text\
                + beer_opilla_korifey_05_l_glass_text + beer_chayka_dniprovska_svitle_05_l_glass_text\
                + beer_chayka_chernomorska_svitle_05_l_glass_text + beer_uman_pivo_waissburg_svitle_1l_plastic_text\
                + beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text + beer_berdichevske_hmilne_svitle_1l_plastic_text\
                + beer_berdichevske_lager_svitle_1l_plastic_text + beer_opilla_korifey_svitle_11l_plastic_text\
                + beer_obolon_jigulivske_exportne_svitle_1l_plastic_text + beer_yantar_svitle_12l_plastic_text\
                + beer_jashkivske_pshenichne_nefilter_1l_plastic_text + beer_jashkivske_svitle_nefilter_1l_plastic_text\
                + beer_jashkivske_jigulivske_nefilter_1l_plastic_text + beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text\
                + beer_chayka_dniprovska_svitle_1l_plastic_text + ketchup_torchin_chasnik_270gr_text\
                + muka_zolote_zernyatko_pshen_2kg_text + mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text\
                + beer_chernigivske_bile_nefilter_1l_plastic_text + beer_obolon_svitle_1l_plastic_text\
                + beer_rogan_svitle_tradiciyne_1l_plastic_text + sous_chumak_chesnochniy_200gr_text + jvachka_orbit_clubnika_banan_text\
                + LM_red_text + beer_jigulivske_svitle_2_l_plastic_text + beer_chayka_dniprovska_svitle_2l_plastic_text\
                + beer_piwny_kubek_svitle_2l_plastic_text + ketchup_torchin_do_shasliky_270gr_test\
                + mayonez_chumak_appetitniy_50_300gr_text + kolbasa_persha_stolica_salyami_firmennaya_vs_text\
                + coffee_chorna_karta_gold_50gr_text + beer_arsenal_micne_svitle_2l_plastic_text\
                + beer_ppb_bochkove_svitle_2l_plastic_text + beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text\
                + beer_zibert_svitle_05_l_banochnoe_text + yogurt_fanni_1_5_240gr_v_banke_text\
                + kefir_slviya_2_5_850gr_v_pakete_text + beer_obolon_kievske_rozlivne_svitle_195l_plastic_text\
                + beer_chernigivske_light_svitle_2l_plastic_text + beer_opilla_korifey_svitle_2l_plastic_text\
                + beer_yantar_svitle_2l_plastic_text + beer_tuborg_green_05_4_banki_2litra_text\
                + beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text + beer_ppb_bochkove_svitle_05_4_banki_2litra_text\
                + beer_budweiser_budvar_05_l_glass_text + beer_pilsner_urquell_05_l_glass_text\
                + beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text + beer_chernigivske_svitle_05_l_jb_text\
                + beer_chernigivske_bile_nefilter_05_l_jb_text + beer_velkopopovicky_kozel_temne_05_l_jb_text\
                + beer_edelmeister_pilsner_svitle_05_l_jb_text + beer_faxe_svitle_05_l_jb_text\
                + beer_livu_pilzenes_svitle_05_l_jb_text + beer_velkopopovicky_kozel_svitle_05_l_jb_text\
                + beer_obolon_beermix_limon_05_l_jb_text + beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text\
                + beer_edelmeister_schwarzbier_temnoe_05_l_jb_text + beer_hike_blanche_svitle_nefilter_05_l_jb_text\
                + beer_zlata_praha_svitle_05_l_jb_text + beer_thuringer_premium_beer_svitle_05_l_jb_text\
                + beer_livu_sencu_svitle_05_l_jb_text + beer_germanarich_svitle_05_l_jb_text\
                + beer_hike_premium_svitle_05_l_jb_text + beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text\
                + beer_zibert_bavarske_svitle_05_l_jb_text + beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text\
                + beer_heineken_svitle_05_l_jb_text + beer_rychtar_grunt_11_svitle_05_l_jb_text + beer_amstel_svitle_05_l_jb_text\
                + beer_bavaria_svitle_05_l_jb_text + beer_bavaria_svitle_nonalcohol_05_l_jb_text + beer_edelburg_lager_svitle_05_l_jb_text\
                + beer_donner_pills_svitle_05_l_jb_text + beer_dutch_windmill_svitle_05_l_jb_text + beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text\
                + beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text + beer_estrella_damm_barcelona_svitle_05_l_jb_text\
                + beer_halne_jasne_pelne_05_l_jb_text + beer_eurotour_hefeweissbier_svitle_05_l_jb_text + beer_hollandia_strong_svitle_05_l_jb_text\
                + beer_lander_brau_premium_svitle_05_l_jb_text + beer_saku_kuld_05_l_jb_text + beer_saku_original_05_l_jb_text\
                + beer_stangen_lager_svitle_05_l_jb_text + beer_van_pur_premium_svitle_05_l_jb_text + beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text\
                + beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text + beer_obolon_beermix_malina_05_l_jb_text + beer_obolon_beermix_vishnya_05_l_jb_text\
                + beer_lomza_svitle_05_l_jb_text + beer_paderborner_pilsener_svitle_05_l_jb_text + beer_paderborner_export_05_l_jb_text\
                + beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text + beer_clausthaler_original_nonalcohol_05_l_jb_text\
                + beer_clausthaler_lemon_nonalcohol_05_l_jb_text + beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text\
                + beer_forever_black_queen_temne_nefilter_05_l_jb_text + beer_forever_kite_safari_svitle_nefilter_05_l_jb_text\
                + beer_forever_crazy_svitle_nefilter_05_l_jb_text + beer_hike_light_svitle_05_l_jb_text + beer_hike_zero_nonalcohol_05_l_jb_text\
                + beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text + beer_horn_original_svitle_0568_l_jb_text + beer_horn_traditional_svitle_0568_l_jb_text\
                + beer_horn_premium_svitle_05_l_jb_text + beer_krusovice_cerne_temne_05_l_jb_text + beer_lander_brau_micne_05_l_jb_text\
                + beer_lander_brau_svitle_nefilter_05_l_jb_text + beer_padeborner_pilger_nefilter_svitle_05_l_jb_text + beer_platan_jedenactka_05_l_jb_text\
                + beer_praga_svitle_05_l_jb_text + beer_saku_rock_svitle_0568_l_jb_text + beer_sitnan_svitle_05_l_jb_text\
                + beer_vienas_premium_golden_svitle_05_l_jb_text + beer_vienas_premium_traditional_svitle_05_l_jb_text\
                + beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text + beer_zahringer_premium_svitle_05_l_jb_text\
                + beer_zahringer_hefeweizen_svitle_05_l_jb_text + beer_jajkivske_svitle__nefilter_05_l_jb_text + beer_obolon_svitle_05_l_jb_text\
                + beer_pubster_svitle_05_l_jb_text + beer_chaika_chernomorskaya_05_l_jb_text + beer_ppb_zakarpatske_orig_svitle_05_l_jb_text\
                + beer_ppb_bochkove_nefilter_05_l_jb_text + beer_ppb_nefilter_svitle_nonalco_05_l_jb_text + beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text\
                + beer_chaika_dniprovskaya_05_l_jb_text + beer_brok_export_svitle_05_l_jb_text + beer_carling_svitle_05_l_jb_text\
                + beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text + beer_budweiser_nonalco_svitle_05_l_jb_text\
                + beer_feldschlosschen_wheat_beer_svitle05_l_jb_text + beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text\
                + beer_grotwerg_svitle_nonalco_05_l_jb_text + beer_holland_import_svitle_05_l_jb_text + beer_golden_castle_export_svitle_05_l_jb_text\
                + beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text + beer_guinness_draught_temne_044_l_jb_text

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
        model = load_model('/home/andrey/GroceryAppVol2/FBApp/my_app/my_model_text')

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
        elif np.argmax(result) == 54:
            return 'Пиво "Черниговское Светлое" 0,5 л в стекле'
        elif np.argmax(result) == 55:
            return 'Пиво "Stella Artois" 0,5 л в стекле'
        elif np.argmax(result) == 56:
            return 'Пиво "Оболонь Светлое" 0,5 л в стекле'
        elif np.argmax(result) == 57:
            return 'Пиво Жигулевское светлое 0,5 л в стекле'
        elif np.argmax(result) == 58:
            return 'Пиво Рогань традиционное светлое 0,5 л в стекле'
        elif np.argmax(result) == 59:
            return 'Пиво Корона Экстра светлое 0,33 л в стекле'
        elif np.argmax(result) == 60:
            return 'Пиво Черниговоское Белое нефильтрованное 0,5 л в стекле'
        elif np.argmax(result) == 61:
            return 'Пиво Янтарь светлое 0,5 л в стекле'
        elif np.argmax(result) == 62:
            return 'Пиво Zibert светлое 0,5 л в стекле'
        elif np.argmax(result) == 63:
            return 'Пиво Арсенал мицне 0,5 л в стекле'
        elif np.argmax(result) == 64:
            return 'Пиво Перша Броварня Закарпатське 0,5 л в стекле'
        elif np.argmax(result) == 65:
            return 'Пиво Львовское светлое 0,5 л в стекле'
        elif np.argmax(result) == 66:
            return 'Пиво Львовское 1715 0,5 л в стекле'
        elif np.argmax(result) == 67:
            return 'Пиво Zlata Praha светлое 0,5 л в стекле'
        elif np.argmax(result) == 68:
            return 'Пиво Tuborg Green 0,5 л в стекле'
        elif np.argmax(result) == 69:
            return 'Пиво Славутич ICE MIX Lime 0,5 л в стекле'
        elif np.argmax(result) == 70:
            return 'Пиво Тетерев 0,5 л в стекле'
        elif np.argmax(result) == 71:
            return 'Пиво Krusovice светлое 0,5 л в стекле'
        elif np.argmax(result) == 72:
            return 'Пиво Heineken светлое 0,5 л в стекле'
        elif np.argmax(result) == 73:
            return 'Пиво Amstel светлое 0,5 л в стекле'
        elif np.argmax(result) == 74:
            return 'Пиво Hike premium светлое 0,5 л в стекле'
        elif np.argmax(result) == 75:
            return 'Пиво Бочкове светлое 0,5 л в стекле'
        elif np.argmax(result) == 76:
            return 'Пиво Kronenbourg 1664 Blanc светлое 0,5 л в стекле'
        elif np.argmax(result) == 77:
            return 'Пиво Опилля Фирменное непастеризоване светлое 0,5 л в стекле'
        elif np.argmax(result) == 78:
            return 'Пиво Ячменный Колос светлое 0,5 л в стекле'
        elif np.argmax(result) == 79:
            return 'Пиво "Опилля Корифей" светлое 0,5 в стекле'
        elif np.argmax(result) == 80:
            return 'Пиво "Чайка Днепровская" 0,5 л в стекле'
        elif np.argmax(result) == 81:
            return 'Пиво "Чайка Черноморская" светлое 0,5 л в стекле'
        elif np.argmax(result) == 82:
            return 'Пиво Умань Waissburg светлое 1 литр'
        elif np.argmax(result) == 83:
            return 'Пиво Умань Пшеничное светлое 1 литр'
        elif np.argmax(result) == 84:
            return 'Пиво Бердичевское Хмельное светлое 1 литр'
        elif np.argmax(result) == 85:
            return 'Пиво Бердичевское Лагер светлое 1 литр'
        elif np.argmax(result) == 86:
            return 'Пиво Опилля Корифей 1.1 литра'
        elif np.argmax(result) == 87:
            return 'Пиво Оболонь жигулевское экспортное 1.5 литра'
        elif np.argmax(result) == 88:
            return 'Пиво Янтарь светлое 1,2 литра'
        elif np.argmax(result) == 89:
            return 'Пиво Жашковское пшеничное нефильтрованное 1 литр'
        elif np.argmax(result) == 90:
            return 'Пиво Жашковское светлое нефильтрованное 1 литр'
        elif np.argmax(result) == 91:
            return 'Пиво Жашковское жигулевское нефильтрованное 1 литр'
        elif np.argmax(result) == 92:
            return 'Пиво Перша приватна броварня бочкове 1 литр'
        elif np.argmax(result) == 93:
            return 'Пиво Чайка днипровська 1 литр'
        elif np.argmax(result) == 94:
            return 'Кетчуп Торчин с чесноком 270 гр'
        elif np.argmax(result) == 95:
            return 'Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг'
        elif np.argmax(result) == 96:
            return 'Майонез Королевский Смак королевский 67 % 300 гр'
        elif np.argmax(result) == 97:
            return 'Пиво Черниговское Белое нефильтрованное 1 л'
        elif np.argmax(result) == 98:
            return 'Пиво Оболонь светлое 1 л'
        elif np.argmax(result) == 99:
            return 'Пиво Рогань традиционное светлое 1 л'
        elif np.argmax(result) == 100:
            return 'Соус Чумак чесночный 200 грамм'
        elif np.argmax(result) == 101:
            return 'Жвачка Orbit полуниця-банан'
        elif np.argmax(result) == 102:
            return 'Сигареты LM красные'
        elif np.argmax(result) == 103:
            return 'Жигулевское светлое 2 литра'
        elif np.argmax(result) == 104:
            return 'Пиво Чайка Днепровская 2 литра'
        elif np.argmax(result) == 105:
            return 'Пиво Piwny Kebek 2 литра'
        elif np.argmax(result) == 106:
            return 'Кетчуп Торчин до шашлику 270 грамм'
        elif np.argmax(result) == 107:
            return 'Майонез Чумак аппетитный 50% 300 грамм'
        elif np.argmax(result) == 108:
            return 'Колбаса Перша Столиця Салями Фирменная высший сорт'
        elif np.argmax(result) == 109:
            return 'Кофе Чорна Карта GOLD 50 грамм'
        elif np.argmax(result) == 110:
            return 'Пиво Арсенал "Міцне" світле, 2л'
        elif np.argmax(result) == 111:
            return 'Пиво "ППБ Бочкове" світле, 2л'
        elif np.argmax(result) == 112:
            return 'Пиво "ППБ Закарпатське оригінальне" світле, 2л'
        elif np.argmax(result) == 113:
            return 'Пиво Zibert светлое 0,5 л в банке'
        elif np.argmax(result) == 114:
            return 'Йогурт Фанни 240 грамм 1.5% лесовые ягоды'
        elif np.argmax(result) == 115:
            return 'Кефир Славия 2,5% 850 грамм'
        elif np.argmax(result) == 116:
            return 'Пиво Оболонь Киевское розливное светлое 1,95 литра в пластике'
        elif np.argmax(result) == 117:
            return 'Пиво Черниговское light светлое 2,0 л в пластике'
        elif np.argmax(result) == 118:
            return 'Пиво Опилля Корифей светлое 2,0 л в пластике'
        elif np.argmax(result) == 119:
            return 'Пиво Янтарь светлое 2,0 л в пластике'
        elif np.argmax(result) == 120:
            return 'Пиво Tuborg Green 4 банки х 0,5 л'
        elif np.argmax(result) == 121:
            return 'Пиво ППБ Закарпатське 4 банки х 0,5 л'
        elif np.argmax(result) == 122:
            return 'Пиво ППБ Бочкове 4 банки х 0,5 л'
        elif np.argmax(result) == 123:
            return 'Пиво Budweiser Budvar светлое 0,5 л в стекле'
        elif np.argmax(result) == 124:
            return 'Пиво Pilsner Urquell светлое 0,5 л в стекле'
        elif np.argmax(result) == 125:
            return 'Пиво Robert Doms бельгийский светлое нефильтрованное 0,5 л в стекле'
        elif np.argmax(result) == 126:
            return 'Пиво 0,5 л Чернігівське світле жб'
        elif np.argmax(result) == 127:
            return 'Пивo 0,5 л Чepнігівськe Білe жб'
        elif np.argmax(result) == 128:
            return 'Пиво 0,5л Velkopopovicky Kozel темне жб'
        elif np.argmax(result) == 129:
            return 'Пиво 0,5 л Edelmeister Pilsner світле фільтроване жб'
        elif np.argmax(result) == 130:
            return 'Пиво 0,5 л Faxe світле фільтроване жб'
        elif np.argmax(result) == 131:
            return 'Пиво 0,5л Livu Pilzenes світле фільтроване жб'
        elif np.argmax(result) == 132:
            return 'Пиво 0,5л Velkopopovicky Kozel світле жб'
        elif np.argmax(result) == 133:
            return 'Пиво 0,5л Оболонь BeerMix Лимон жб'
        elif np.argmax(result) == 134:
            return 'Пиво 0,5 л Edelmeister Weizenbier світле нефільтроване жб'
        elif np.argmax(result) == 135:
            return 'Пиво 0,5 л Edelmeister Schwarzbier темне фільтроване жб'
        elif np.argmax(result) == 136:
            return 'Пивo 0,5л Hike Blanche світлe нeфільтpoвaнe жб'
        elif np.argmax(result) == 137:
            return 'Пиво 0,5л Zlata Praha світле жб'
        elif np.argmax(result) == 138:
            return 'Пиво 0,5л Thuringer Premium Beer світле фільтроване жб'
        elif np.argmax(result) == 139:
            return 'Пиво 0,5л Livu Sencu світле фільтроване жб'
        elif np.argmax(result) == 140:
            return 'Пиво 0,5 л Germanarich светлое жб'
        elif np.argmax(result) == 141:
            return 'Пиво 0,5л Hike Преміум світле жб'
        elif np.argmax(result) == 142:
            return 'Пивo бeзaлкoгoльнe 0,5л Обoлoнь 0 світлe нефільтроване пaстepизoвaнe жб'
        elif np.argmax(result) == 143:
            return 'Пивo Zibert Баварское светлое 0,5 л жб'
        elif np.argmax(result) == 144:
            return 'Пивo Bavaria Liquid Apple безалкогольное светлое 0,5 л жб'
        elif np.argmax(result) == 145:
            return 'Пивo Heineken светлое 0,5 л жб'
        elif np.argmax(result) == 146:
            return 'Пивo Rychtar Grant 11 светлое 0,5 л жб'
        elif np.argmax(result) == 147:
            return 'Пивo Amstel светлое 0,5 л жб'
        elif np.argmax(result) == 148:
            return 'Пивo Bavaria светлое 0,5 л жб'
        elif np.argmax(result) == 149:
            return 'Пивo Bavaria светлое безалкогольное 0,5 л жб'
        elif np.argmax(result) == 150:
            return 'Пиво Edelburg Lager світле 5,2% 0,5л жб'
        elif np.argmax(result) == 151:
            return 'Пиво Donner Pils світле 3,5% 0,5л жб'
        elif np.argmax(result) == 152:
            return 'Пиво Dutch Windmill світле 4,6% 0,5л жб'
        elif np.argmax(result) == 153:
            return 'Пиво Edelburg Hefeweizen світле нефільтроване 5,1% 0,5л жб'
        elif np.argmax(result) == 154:
            return 'Пиво Edelmeister Unfiltered світле нефільтроване 5,7% 0,5л жб'
        elif np.argmax(result) == 155:
            return 'Пиво Estrella Damm Barcelona світле 4,6% 0,5л жб'
        elif np.argmax(result) == 156:
            return 'Пиво Halne Jasne Pelne з/б 6% 0,5л жб'
        elif np.argmax(result) == 157:
            return 'Пиво Eurotour Hefeweissbier світле 5% 0,5л жб'
        elif np.argmax(result) == 158:
            return 'Пиво Hollandia Strong світле 7,5% 0,5л жб'
        elif np.argmax(result) == 159:
            return 'Пиво Lander Brau Premium світле 4,9% 0,5л жб'
        elif np.argmax(result) == 160:
            return 'Пиво Saku Kuld 5,2% 0,5л жб'
        elif np.argmax(result) == 161:
            return 'Пиво Saku Originaal 4,7% 0,5л л жб'
        elif np.argmax(result) == 162:
            return 'Пиво Stangen Lager світле 5,4% 0,5л л жб'
        elif np.argmax(result) == 163:
            return 'Пиво Van Pur Premium світле 5% 0,5л жб'
        elif np.argmax(result) == 164:
            return 'Пиво Bavaria манго-маракуйя світле безалкогольне 0,5л жб'
        elif np.argmax(result) == 165:
            return 'Пиво Bavaria Гранат безалкогольне 0,5л жб'
        elif np.argmax(result) == 166:
            return 'Пиво Оболонь Beermix Малина світле 2,5% 0,5л жб'
        elif np.argmax(result) == 167:
            return 'Пиво Оболонь Beermix Вишня спеціальне світле 2,5% 0,5л жб'
        elif np.argmax(result) == 168:
            return 'Пиво Lomza світле 5,7% 0,5л жб'
        elif np.argmax(result) == 169:
            return 'Пиво Paderborner Pilsener світле 4,8% 0,5л жб'
        elif np.argmax(result) == 170:
            return 'Пиво Paderborner Export світле 5,5% 0,5л жб'
        elif np.argmax(result) == 171:
            return 'Пиво Clausthaler Grapefruit безалкогольне 0,5л жб'
        elif np.argmax(result) == 172:
            return 'Пиво Clausthaler Original безалкогольне 0,5л жб'
        elif np.argmax(result) == 173:
            return 'Пиво Clausthaler Lemon безалкогольне 0,5л жб'
        elif np.argmax(result) == 174:
            return 'Пиво Forever Rock & Roll світле нефільтроване 7,5% 0,5л жб'
        elif np.argmax(result) == 175:
            return 'Пиво Forever Black Queen темне нефільтроване 5,5% 0,5л жб'
        elif np.argmax(result) == 176:
            return 'Пиво Forever Kite Safari світле нефільтроване 7% 0,5л жб'
        elif np.argmax(result) == 177:
            return 'Пиво Forever Crazy світле нефільтроване 6,5% 0,5л жб'
        elif np.argmax(result) == 178:
            return 'Пиво Hike Light світле 3,5% 0,5л жб'
        elif np.argmax(result) == 179:
            return 'Пиво Hike Zero безалкогольне 0,5л жб'
        elif np.argmax(result) == 180:
            return 'Пиво Horn Disel Ice Pilsner світле 4,7% 0,568л жб'
        elif np.argmax(result) == 181:
            return 'Пиво Horn Disel Original 5,3% 0,568л жб'
        elif np.argmax(result) == 182:
            return 'Пиво Horn Disel Traditional світле 6% 0,568л жб'
        elif np.argmax(result) == 183:
            return 'Пиво Horn Diesel Premium світле 5% 0,5л жб'
        elif np.argmax(result) == 184:
            return 'Пиво Krusovice Cerne темне 3,8% 0,5л жб'
        elif np.argmax(result) == 185:
            return 'Пиво Lander Brau міцне 4,9% 0,5л жб'
        elif np.argmax(result) == 186:
            return 'Пиво Lander Brau світле нефільтроване 4,7% 0,5л жб'
        elif np.argmax(result) == 187:
            return 'Пиво Paderborner Pilger світле нефільтроване пастеризоване 5% 0,5л жб'
        elif np.argmax(result) == 188:
            return 'Пиво Platan Jedenactka 11 світле 4,6% 0,5л жб'
        elif np.argmax(result) == 189:
            return 'Пиво Praga світле фільтроване 4,7% 0,5л жб'
        elif np.argmax(result) == 190:
            return 'Пиво Saku Rock світле 5,3% 0,568л жб'
        elif np.argmax(result) == 191:
            return 'Пиво Sitnan світле 5% 0,5л жб'
        elif np.argmax(result) == 192:
            return 'Пиво Vienas Premium Golden світле 5% 0,568л жб'
        elif np.argmax(result) == 193:
            return 'Пиво Vienas Premium Traditional світле 5,8% 0,568л жб'
        elif np.argmax(result) == 194:
            return 'Пиво Volynski Browar Forever Sweet Wit пшеничне світле нефільтроване 4,5% 0,5л жб'
        elif np.argmax(result) == 195:
            return 'Пиво Zahringer Преміум світле 0,5л жб'
        elif np.argmax(result) == 196:
            return 'Пиво Zahringer Hefeweizen світле 0,5л жб'
        elif np.argmax(result) == 197:
            return 'Пиво Жашківське світле нефільтроване 4,5% 0,5л жб'
        elif np.argmax(result) == 198:
            return 'Пиво Оболонь світле 4,5% 0,5л жб'
        elif np.argmax(result) == 199:
            return 'Пиво Pubster світле 5% 0,5л жб'
        elif np.argmax(result) == 200:
            return 'Пиво ППБ Чайка Чорноморська 4,5% 0,5л жб'
        elif np.argmax(result) == 201:
            return 'Пиво ППБ Закарпатське Оригінальне світле 4,4% 0,5л'
        elif np.argmax(result) == 202:
            return 'Пиво ППБ Бочкове Нефільтроване з/б 4,8% 0,5л'
        elif np.argmax(result) == 203:
            return 'Пиво ППБ Нефільтроване світле безалкогольне 0,5л'
        elif np.argmax(result) == 204:
            return 'Пиво ППБ Лимон-Лайм безалкогольне нефільтроване 0,5л'
        elif np.argmax(result) == 205:
            return 'Пиво Чайка Дніпровська світле фільтроване 4,8% 0,5л'
        elif np.argmax(result) == 206:
            return 'Пиво Brok Export світле 5,2% 0,5л'
        elif np.argmax(result) == 207:
            return 'Пиво Carling світле фільроване з/б 4% 0.5 л'
        elif np.argmax(result) == 208:
            return 'Пиво Keten Brug Blanche Elegant 4.8% 0.5 л'
        elif np.argmax(result) == 209:
            return 'Пиво Budweiser безалкогольне 0.5 л'
        elif np.argmax(result) == 210:
            return 'Пиво Feldschlosschen Wheat Beer світле нефільтроване 5% 0.5 л'
        elif np.argmax(result) == 211:
            return 'Пиво Тетерів Хмільна Вишня напівтемне фільтроване з/б 8% 0.5 л'
        elif np.argmax(result) == 212:
            return 'Пиво Grotwerg світле пастеризоване фільтроване безалкогольне 0.5 л'
        elif np.argmax(result) == 213:
            return 'Пиво Holland Import світле фільтроване 4.8% 0.5 л'
        elif np.argmax(result) == 214:
            return 'Пиво Golden Castle Export світле 4.8% 0.5 л'
        elif np.argmax(result) == 215:
            return 'Пиво 5.0 Original Craft Beer сітле нефільтроване 4.1% 0.5 л'
        elif np.argmax(result) == 216:
            return 'Пиво Guinness Draught темне фільтроване 4.1% 0.44 л'


