import json
from parsers import ProductParserVol2


parser=ProductParserVol2()

all_products_names=[
    {'obolon_premium_1.1_l':{
    "atb":parser.obolon_premium_parser()[0],
    "eko":parser.obolon_premium_parser()[1]
}},
    {'vodka_hetman_ice_07':{
        "atb":parser.vodka_getman_ICE_parcer()[0]
}},
    {'coca_cola_2l':{
        "atb":parser.coca_cola_2l_parcer()[0],
        "eko":parser.coca_cola_2l_parcer()[1],
        "varus":parser.coca_cola_2l_parcer()[2],
        "silpo":parser.coca_cola_2l_parcer()[3],
        "ashan":parser.coca_cola_2l_parcer()[4],
        "novus":parser.coca_cola_2l_parcer()[5],
        "metro":parser.coca_cola_2l_parcer()[6],
        "nash_kray":parser.coca_cola_2l_parcer()[7],
        "fozzy":parser.coca_cola_2l_parcer()[8]
}},
    {'garlik':{
        "atb":parser.garlik_parcer()[0],
        "eko":parser.garlik_parcer()[1],
        "varus":parser.garlik_parcer()[2],
        "silpo":parser.garlik_parcer()[3],
        "novus":parser.garlik_parcer()[5],
        "nash_kray":parser.garlik_parcer()[7],
        "fozzy":parser.garlik_parcer()[8]
}},
    {'tea_minutka':{
        "atb":parser.tea_minutka_black_40_b_parcer()[0],
        "eko":parser.tea_minutka_black_40_b_parcer()[1],
        "metro":parser.tea_minutka_black_40_b_parcer()[6]
}},
    {'apple_golden':{
        "atb":parser.apple_golden_parcer()[0],
        "eko":parser.apple_golden_parcer()[1],
        "varus":parser.apple_golden_parcer()[2],
        "silpo":parser.apple_golden_parcer()[3],
        "metro":parser.apple_golden_parcer()[6],
        "nash_kray":parser.apple_golden_parcer()[7],
        "fozzy":parser.apple_golden_parcer()[8]
}},
    {'sigarets_kent_8':{
        "atb":parser.kent_8_parcer()[0],
        "eko":parser.kent_8_parcer()[1],
        "varus":parser.kent_8_parcer()[2],
        "silpo":parser.kent_8_parcer()[3],
        "ashan":parser.kent_8_parcer()[4],
        "novus":parser.kent_8_parcer()[5],
        "fozzy":parser.kent_8_parcer()[8]
}},
    {'coffee_aroma_gold':{
        "eko":parser.coffee_aroma_gold_parcer()[1],
        "fozzy":parser.coffee_aroma_gold_parcer()[8]
}},
    {'oil_shedriy_dar_raf_850':{
        "atb":parser.oil_shedriy_dar_850_parcer()[0],
        "eko":parser.oil_shedriy_dar_850_parcer()[1],
        "varus":parser.oil_shedriy_dar_850_parcer()[2],
        "silpo":parser.oil_shedriy_dar_850_parcer()[3],
        "ashan":parser.oil_shedriy_dar_850_parcer()[4],
        "novus":parser.oil_shedriy_dar_850_parcer()[5],
        "metro":parser.oil_shedriy_dar_850_parcer()[6],
        "fozzy":parser.oil_shedriy_dar_850_parcer()[8]
}},
    {'fairy_limon_500':{
        "atb":parser.fairy_limon_500_parcer()[0],
        "eko":parser.fairy_limon_500_parcer()[1],
        "varus":parser.fairy_limon_500_parcer()[2],
        "silpo":parser.fairy_limon_500_parcer()[3],
        "novus":parser.fairy_limon_500_parcer()[5],
        "metro":parser.fairy_limon_500_parcer()[6],
        "fozzy":parser.fairy_limon_500_parcer()[8]
}},
    {'onion':{
        "atb":parser.onion_parcer()[0],
        "eko":parser.onion_parcer()[1],
        "varus":parser.onion_parcer()[2],
        "silpo":parser.onion_parcer()[3],
        "novus":parser.onion_parcer()[5],
        "metro":parser.onion_parcer()[6],
        "nash_kray":parser.onion_parcer()[7],
        "fozzy":parser.onion_parcer()[8]
}},
    {'apple_black_prince':{
        "atb":parser.apple_black_prince_parcer()[0],
        "eko":parser.apple_black_prince_parcer()[1],
        "varus":parser.apple_black_prince_parcer()[2],
        "silpo":parser.apple_black_prince_parcer()[3],
        "metro":parser.apple_black_prince_parcer()[6],
        "fozzy":parser.apple_black_prince_parcer()[8]
}},
    {'smetana_stol_smaky_20%':{
        "varus":parser.smetana_stolica_smaky_400_20()[2]
}},
    {'limon':{
        "atb":parser.limon_parcer()[0],
        "eko":parser.limon_parcer()[1],
        "varus":parser.limon_parcer()[2],
        "silpo":parser.limon_parcer()[3],
        "novus":parser.limon_parcer()[5],
        "metro":parser.limon_parcer()[6],
        "nash_kray":parser.limon_parcer()[7],
        "fozzy":parser.limon_parcer()[8]
}},
    {'oil_oleyna_neraf_850':{
        "eko":parser.oil_oleyna_neraf_850_parcer()[1],
        "ashan":parser.oil_oleyna_neraf_850_parcer()[4]
}},
    {'tea_monomah_kenya_90':{
        "eko":parser.tea_monomah_black_kenya_90_parcer()[1]
}},
    {'arko_cool_200':{
        "atb":parser.arko_cool_200_bonus100_parcer()[0],
        "eko":parser.arko_cool_200_bonus100_parcer()[1],
        "varus":parser.arko_cool_200_bonus100_parcer()[2],
        "silpo":parser.arko_cool_200_bonus100_parcer()[3],
        "ashan":parser.arko_cool_200_bonus100_parcer()[4],
        "novus":parser.arko_cool_200_bonus100_parcer()[5],
        "metro":parser.arko_cool_200_bonus100_parcer()[6],
        "fozzy":parser.arko_cool_200_bonus100_parcer()[8]
}},
    {'arko_sensitive_200':{
        "atb":parser.arko_sensitive_200_bonus100_parcer()[0],
        "eko":parser.arko_sensitive_200_bonus100_parcer()[1],
        "varus":parser.arko_sensitive_200_bonus100_parcer()[2],
        "silpo":parser.arko_sensitive_200_bonus100_parcer()[3],
        "ashan":parser.arko_sensitive_200_bonus100_parcer()[4],
        "novus":parser.arko_sensitive_200_bonus100_parcer()[5],
        "metro":parser.arko_sensitive_200_bonus100_parcer()[6],
        "nash_kray":parser.arko_sensitive_200_bonus100_parcer()[7],
        "fozzy":parser.arko_sensitive_200_bonus100_parcer()[8]
}},
    {'carrot':{
        "atb":parser.carrot_parcer()[0],
        "eko":parser.carrot_parcer()[1],
        "varus":parser.carrot_parcer()[2],
        "silpo":parser.carrot_parcer()[3],
        "novus":parser.carrot_parcer()[5],
        "metro":parser.carrot_parcer()[6],
        "nash_kray":parser.carrot_parcer()[7],
        "fozzy":parser.carrot_parcer()[8]
}},
    {'cabbage':{
        "atb":parser.cabbage_parcer()[0],
        "eko":parser.cabbage_parcer()[1],
        "varus":parser.cabbage_parcer()[2],
        "silpo":parser.cabbage_parcer()[3],
        "novus":parser.cabbage_parcer()[5],
        "metro":parser.cabbage_parcer()[6],
        "nash_kray":parser.cabbage_parcer()[7],
        "fozzy":parser.cabbage_parcer()[8]
}},
    {'eggs':{
        "atb":parser.egg_parcer()[0],
        "eko":parser.egg_parcer()[1],
        "varus":parser.egg_parcer()[2],
        "silpo":parser.egg_parcer()[3],
        "ashan":parser.egg_parcer()[4],
        "novus":parser.egg_parcer()[5],
        "metro":parser.egg_parcer()[6],
        "nash_kray":parser.egg_parcer()[7],
        "fozzy":parser.egg_parcer()[8]
}},
    {'mayonez_detsk_shedro_67%':{
        "atb":parser.mayonez_detsk_shedro_67_parcer()[0],
        "eko":parser.mayonez_detsk_shedro_67_parcer()[1],
        "varus":parser.mayonez_detsk_shedro_67_parcer()[2],
        "silpo":parser.mayonez_detsk_shedro_67_parcer()[3],
        "metro":parser.mayonez_detsk_shedro_67_parcer()[6],
        "fozzy":parser.mayonez_detsk_shedro_67_parcer()[8]
}},
    {'rexona_aloe_vera':{
        "eko":parser.rexona_aloe_vera_w_parcer()[1],
        "ashan":parser.rexona_aloe_vera_w_parcer()[4]
}},
    {'marlboro_red':{
        "atb":parser.marloboro_red_parcer()[0],
        "eko":parser.marloboro_red_parcer()[1],
        "varus":parser.marloboro_red_parcer()[2],
        "silpo":parser.marloboro_red_parcer()[3],
        "ashan":parser.marloboro_red_parcer()[4],
        "novus":parser.marloboro_red_parcer()[5],
        "fozzy":parser.marloboro_red_parcer()[8]
}},
    {'beer_lvivske_svetl_2.4 l':{
        "varus":parser.beer_lvivske_svitle_24l()[2],
        "silpo":parser.beer_lvivske_svitle_24l()[3],
        "ashan":parser.beer_lvivske_svitle_24l()[4],
        "fozzy":parser.beer_lvivske_svitle_24l()[8]
}},
    {'smetana_stol_smaky_15%':{
        "varus":parser.smetana_stolica_smaky_400_15_parcer()[2]
}},
    {'water_in_bottle_6l':{
        "atb":parser.water_in_6l_bottle_parser()[0],
        "eko":parser.water_in_6l_bottle_parser()[1],
        "varus":parser.water_in_6l_bottle_parser()[2],
        "novus":parser.water_in_6l_bottle_parser()[5],
        "nash_kray":parser.water_in_6l_bottle_parser()[7],
        "fozzy":parser.water_in_6l_bottle_parser()[8]
}},
    {'pork_lopatka':{
        "atb":parser.pork_lopatka_parser()[0],
        "eko":parser.pork_lopatka_parser()[1],
        "varus":parser.pork_lopatka_parser()[2],
        "novus":parser.pork_lopatka_parser()[5],
        "metro":parser.pork_lopatka_parser()[6],
        "fozzy":parser.pork_lopatka_parser()[8]
}},
    {'potato':{
        "atb":parser.potato_parser()[0],
        "eko":parser.potato_parser()[1],
        "varus":parser.potato_parser()[2],
        "novus":parser.potato_parser()[5],
        "metro":parser.potato_parser()[6],
        "fozzy":parser.potato_parser()[8]
}},
    {'beet':{
        "atb":parser.beet_parser()[0],
        "eko":parser.beet_parser()[1],
        "varus":parser.beet_parser()[2],
        "silpo":parser.beet_parser()[3],
        "novus":parser.beet_parser()[5],
        "metro":parser.beet_parser()[6],
        "fozzy":parser.beet_parser()[8]
}},
    {'four':{
        "atb":parser.four_parser()[0],
        "eko":parser.four_parser()[1],
        "varus":parser.four_parser()[2],
        "novus":parser.four_parser()[5],
        "metro":parser.four_parser()[6],
        "nash_kray":parser.four_parser()[7],
        "fozzy":parser.four_parser()[8]
}},
    {'oil_for_dish':{
        "atb":parser.oil_for_dishes_parser()[0],
        "eko":parser.oil_for_dishes_parser()[1],
        "varus":parser.oil_for_dishes_parser()[2],
        "novus":parser.oil_for_dishes_parser()[5],
        "metro":parser.oil_for_dishes_parser()[6],
        "nash_kray":parser.oil_for_dishes_parser()[7],
        "fozzy":parser.oil_for_dishes_parser()[8]
}},
    {'smetana_for_dish':{
        "atb":parser.sour_cream_for_dishes_parser()[0],
        "eko":parser.sour_cream_for_dishes_parser()[1],
        "varus":parser.sour_cream_for_dishes_parser()[2],
        "novus":parser.sour_cream_for_dishes_parser()[5],
        "metro":parser.sour_cream_for_dishes_parser()[6],
        "fozzy":parser.sour_cream_for_dishes_parser()[8]
}},
    {'desodorant_garnier_man':{
        "silpo":parser.desodorant_garnier_magniy_man_parser()[3],
        "fozzy":parser.sour_cream_for_dishes_parser()[8]
}},
    {'cofee_aroma_gold_freeze_dried_70g':{
        "eko":parser.coffee_aroma_gold_freeze_dried_70g_parser()[1],
        "silpo":parser.coffee_aroma_gold_freeze_dried_70g_parser()[3],
        "nash_kray":parser.coffee_aroma_gold_freeze_dried_70g_parser()[7],
}},
    {'gorchica_veres_ukrainska_micna_120g':{
        "silpo":parser.gorchica_veres_ukrainska_micna_120g_parser()[3],
        "novus":parser.gorchica_veres_ukrainska_micna_120g_parser()[5],
        "metro":parser.gorchica_veres_ukrainska_micna_120g_parser()[6],
}},
    {'sir_plavlenniy_komo_paprikash':{
        "novus":parser.sir_plavlenniy_komo_paprikash_parser()[5],
        "metro":parser.sir_plavlenniy_komo_paprikash_parser()[6],
        "nash_kray":parser.sir_plavlenniy_komo_paprikash_parser()[7],
        "fozzy":parser.sir_plavlenniy_komo_paprikash_parser()[8]
}},
    {'apple_gala':{
        "atb":parser.apple_gala_parser()[0],
        "eko":parser.apple_gala_parser()[1],
        "varus":parser.apple_gala_parser()[2],
        "silpo":parser.apple_gala_parser()[3],
        "novus":parser.apple_gala_parser()[5],
        "metro":parser.apple_gala_parser()[6],
        "fozzy":parser.apple_gala_parser()[8]
}},
    {'smetana_galichanska_15_370gr':{
        "atb":parser.smetana_galichanska_15_370g_parser()[0],
        "eko":parser.smetana_galichanska_15_370g_parser()[1],
        "novus":parser.smetana_galichanska_15_370g_parser()[5],
        "metro":parser.smetana_galichanska_15_370g_parser()[6],
        "fozzy":parser.smetana_galichanska_15_370g_parser()[8]
}},
    {'desodorant_garnier_spring_spirit':{
        "silpo":parser.desodorant_garnier_spring_spirit_parser()[3],
        "novus":parser.desodorant_garnier_spring_spirit_parser()[5],
        "metro":parser.desodorant_garnier_spring_spirit_parser()[6],
        "fozzy":parser.desodorant_garnier_spring_spirit_parser()[8]
}},
    {'chips_lays_with_salt_big_pack':{
        "eko":parser.chips_lays_with_salt_parser()[1],
        "fozzy":parser.chips_lays_with_salt_parser()[8]
}},
    {'sprite_2l':{
        "eko":parser.sprite_2l_parser()[1],
        "varus":parser.sprite_2l_parser()[2],
        "silpo":parser.sprite_2l_parser()[3],
        "ashan":parser.sprite_2l_parser()[4],
        "novus":parser.sprite_2l_parser()[5],
        "metro":parser.sprite_2l_parser()[6],
        "nash_kray":parser.sprite_2l_parser()[7],
        "fozzy":parser.sprite_2l_parser()[8]
}},
    {'fanta_2l':{
        "eko":parser.fanta_2l_parser()[1],
        "varus":parser.fanta_2l_parser()[2],
        "silpo":parser.fanta_2l_parser()[3],
        "ashan":parser.fanta_2l_parser()[4],
        "novus":parser.fanta_2l_parser()[5],
        "metro":parser.fanta_2l_parser()[6],
        "nash_kray":parser.fanta_2l_parser()[7],
        "fozzy":parser.fanta_2l_parser()[8]
}},
    {'bond_street_blue_selection':{
        "atb":parser.bond_street_blue_selection_parser()[0],
        "eko":parser.bond_street_blue_selection_parser()[1],
        "varus":parser.bond_street_blue_selection_parser()[2],
        "silpo":parser.bond_street_blue_selection_parser()[3],
        "ashan":parser.bond_street_blue_selection_parser()[4],
        "novus":parser.bond_street_blue_selection_parser()[5],
        "fozzy":parser.bond_street_blue_selection_parser()[8]
}},
    {'camel_blue':{
        "atb":parser.camel_blue_parser()[0],
        "eko":parser.camel_blue_parser()[1],
        "varus":parser.camel_blue_parser()[2],
        "silpo":parser.camel_blue_parser()[3],
        "ashan":parser.camel_blue_parser()[4],
        "novus":parser.camel_blue_parser()[5],
        "fozzy":parser.camel_blue_parser()[8]
}},
    {'ld_red':{
        "atb":parser.camel_blue_parser()[0],
        "eko":parser.camel_blue_parser()[1],
        "silpo":parser.camel_blue_parser()[3],
        "fozzy":parser.camel_blue_parser()[8]
}},
    {'marlboro_gold':{
        "atb":parser.marlboro_gold_parser()[0],
        "eko":parser.marlboro_gold_parser()[1],
        "varus":parser.marlboro_gold_parser()[2],
        "silpo":parser.marlboro_gold_parser()[3],
        "ashan":parser.marlboro_gold_parser()[4],
        "novus":parser.marlboro_gold_parser()[5],
        "fozzy":parser.marlboro_gold_parser()[8]
}},
    {'rothmans_demi_blue_exclusive':{
        "atb":parser.rothmans_demi_blue_exclusive_parser()[0],
        "eko":parser.rothmans_demi_blue_exclusive_parser()[1],
        "varus":parser.rothmans_demi_blue_exclusive_parser()[2],
        "silpo":parser.rothmans_demi_blue_exclusive_parser()[3],
        "ashan":parser.rothmans_demi_blue_exclusive_parser()[4],
        "novus":parser.rothmans_demi_blue_exclusive_parser()[5]
}},
    {'rothmans_demi_click_purple':{
        "atb":parser.rothmans_demi_click_purple_parser()[0],
        "eko":parser.rothmans_demi_click_purple_parser()[1],
        "ashan":parser.rothmans_demi_click_purple_parser()[4]
}},
    {'rothmans_demi_click_purple':{
        "atb":parser.rothmans_demi_click_purple_parser()[0],
        "eko":parser.rothmans_demi_click_purple_parser()[1],
        "ashan":parser.rothmans_demi_click_purple_parser()[4]
}},
    {'winston_caster':{
        "atb":parser.winston_caster_parser()[0]
}},

]

def get_all_prices():
    to_json=dict()
    for item in all_products_names:
        for product,values in item.items():
            to_json[product]=values
    with open('/home/andrey/GroceryApp/FBApp/my_app/prices_store.json','w') as f:
        json.dump(to_json, f, sort_keys=False, indent=len(all_products_names))
        print('?????? ???????????????? ?? ???? ???????? ?????????????????? ?? ???????? ????????????!')

get_all_prices()








