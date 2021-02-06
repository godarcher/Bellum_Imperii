from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60)]),
  ("iberian_bandits","Iberian Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_iberian_bandit,4,60)]),
  ("sea_raiders","Saxon Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("quest_eagle_captors","Eagle Thiefs",icon_axeman|carries_goods(2),0,fac_eagle_captors,bandit_personality,[(trp_gallic_leader,1,1), (trp_forest_bandit,4,12)] ),
  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_guard,12,40)]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[(trp_caravan_guard,12,40)]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[(trp_caravan_guard,12,40)]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_guard,12,40)]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

	("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_roman_n_recruit,1,3),(trp_roman_n_legionary,1,3),(trp_roman_n_aux_spearman,1,2),(trp_roman_n_auxiliary,1,3)] ),
	("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_roman_n_legionary,2,4),(trp_roman_n_aux_spearman,1,2),(trp_roman_n_aux_light_cavalry,1,2),(trp_roman_n_aux_archer,1,3)] ),
	("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_roman_n_aux_vet_archer,1,3),(trp_roman_n_aux_cavalry,1,3),(trp_roman_n_armoured_legionary,1,3),(trp_roman_n_praetorian,1,2)] ),

	#Vaegir
	("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_burgundiones_e_recruit,2,4),(trp_burgundiones_e_tribesman,2,4),(trp_burgundiones_e_tracker,1,2)] ),
	("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_burgundiones_e_skirmisher,1,2),(trp_burgundiones_e_light_raider,2,4),(trp_burgundiones_e_spearman,2,4),(trp_burgundiones_e_mounted_axeman,2,4)] ),
	("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_burgundiones_e_noble_lancer,1,2),(trp_burgundiones_e_mounted_veteran,2,4),(trp_burgundiones_e_footman,2,4)] ),
#Khergit
	("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dacian_armed_tribesman,2,6),(trp_dacian_light_warrior,2,4),(trp_dacian_light_falxman,2,4),(trp_dacian_hunter,2,4)] ),
	("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dacian_warrior,2, 4),(trp_dacian_falxman,2,4),(trp_dacian_archer,2,4)] ),
	("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dacian_noble_falxman,1,4),(trp_dacian_noble_warrior,1,4),] ),
#Nord
	("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_parthian_n_spear_levy,2,4),(trp_parthian_n_skirmisher,2,4),(trp_parthian_n_light_horseman,1,3)] ),
	("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_parthian_n_footman,2,4),(trp_parthian_n_archer,1,4),(trp_parthian_n_horseman,1,3),(trp_parthian_n_horse_archer,1,3)] ),
	("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_parthian_n_heavy_archer,1,3),(trp_parthian_n_veteran_footman,1,3),(trp_parthian_n_royal_cataphract,1,3),(trp_parthian_n_cataphract,1,2)] ),
#Rhodok
	("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_maurian_levy,2,4),(trp_maurian_light_warrior,2,4),(trp_maurian_scout,2,4)] ),
	("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_maurian_warrior,2,4),(trp_maurian_camel_skirmisher,2,4),(trp_maurian_light_horseman,2,4)] ),
	("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_maurian_chieftain_guard,1,3),(trp_maurian_horseman,2,4),(trp_maurian_chosen_warrior,1,3)] ),
#Sarranid
	("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_celtic_light_raider,1,3),(trp_celtic_clansman,2,4),(trp_celtic_painted_axeman,2,4)] ),
	("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_celtic_warrior,1,3),(trp_celtic_raider,2,6),(trp_celtic_painted_axeman,2,4)] ),
	("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_celtic_noble_warrior,1,3),(trp_celtic_horse_raider,1,2),(trp_celtic_warrior,1,3)] ),
#Roman Gallia
	("kingdom_7_reinforcements_a", "{!}kingdom_7_a_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_roman_n_recruit_gallia,1,3),(trp_roman_n_legionary_gallia,1,3),(trp_roman_n_aux_spearman_gallia,1,2),(trp_roman_n_auxiliary_gallia,1,3)] ),
	("kingdom_7_reinforcements_b", "{!}kingdom_7_a_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_roman_n_legionary_gallia,2,4),(trp_roman_n_aux_spearman_gallia,1,2),(trp_roman_n_aux_light_cavalry_gallia,1,2),(trp_roman_n_aux_archer_gallia,1,3)] ),
	("kingdom_7_reinforcements_c", "{!}kingdom_7_a_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_roman_n_aux_vet_archer_gallia,1,3),(trp_roman_n_aux_cavalry_gallia,1,3),(trp_roman_n_armoured_legionary_gallia,1,3),(trp_roman_n_praetorian_gallia,1,2)] ),
	
	("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_roman_n_recruit_illyricum,1,3),(trp_roman_n_legionary_illyricum,1,3),(trp_roman_n_aux_spearman_illyricum,1,2),(trp_roman_n_auxiliary_illyricum,1,3)] ),
	("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_roman_n_legionary_illyricum,2,4),(trp_roman_n_aux_spearman_illyricum,1,2),(trp_roman_n_aux_light_cavalry_illyricum,1,2),(trp_roman_n_aux_archer_illyricum,1,3)] ),
	("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_roman_n_aux_vet_archer_illyricum,1,3),(trp_roman_n_aux_cavalry_illyricum,1,3),(trp_roman_n_armoured_legionary_illyricum,1,3),(trp_roman_n_praetorian_illyricum,1,2)] ),
	
	("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_roman_n_recruit_asia,1,3),(trp_roman_n_legionary_asia,1,3),(trp_roman_n_aux_spearman_asia,1,2),(trp_roman_n_auxiliary_asia,1,3)] ),
	("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_roman_n_legionary_asia,2,4),(trp_roman_n_aux_archer_asia,1,2),(trp_roman_n_aux_light_cavalry_asia,1,3)] ),
	("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_roman_n_aux_vet_archer_asia,1,3),(trp_roman_n_aux_cavalry_asia,1,3),(trp_roman_n_armoured_legionary_asia,1,3),(trp_roman_n_praetorian_asia,1,2)] ),

	("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_roman_n_recruit_hispania,1,3),(trp_roman_n_legionary_hispania,1,3),(trp_roman_n_aux_spearman_hispania,1,2),(trp_roman_n_auxiliary_hispania,1,3)] ),
	("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_roman_n_legionary_hispania,2,4),(trp_roman_n_aux_spearman_hispania,1,2),(trp_roman_n_aux_light_cavalry_hispania,1,2),(trp_roman_n_aux_archer_hispania,1,3)] ),
	("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_roman_n_aux_vet_archer_hispania,1,3),(trp_roman_n_aux_cavalry_hispania,1,3),(trp_roman_n_armoured_legionary_hispania,1,3),(trp_roman_n_praetorian_hispania,1,2)] ),
	
	("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_celtic_light_raider,1,3),(trp_celtic_clansman,2,4),(trp_celtic_painted_axeman,2,4)] ),
	("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_celtic_warrior,1,3),(trp_celtic_raider,2,6),(trp_celtic_painted_axeman,2,4)] ),
	("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_celtic_noble_warrior,1,3),(trp_celtic_horse_raider,1,2),(trp_celtic_warrior,1,3)] ),

	("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_marcomanni_tribesman,2,4),(trp_marcomanni_hunter,2,4),(trp_marcomanni_spear_tribesman,2,4)] ), 
	("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_marcomanni_skirmisher,1,4),(trp_marcomanni_light_axeman,2,4),(trp_marcomanni_spear_warrior,2,4)] ),
	("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_marcomanni_spear_champion,1,3),(trp_marcomanni_spear_warrior,1,3),(trp_marcomanni_light_scout,1,4)] ),

	("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_frisii_tribesman,2,4),(trp_frisii_light_spearman,2,4),(trp_frisii_scout_rider,1,2)] ), 
	("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_frisii_horseman,1,2),(trp_frisii_seax_warrior,2,4),(trp_frisii_javelinman,2,4)] ),
	("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_frisii_horse_master,1,2),(trp_frisii_elote_warrior,2,4),(trp_frisii_experienced_warrior,2,4)] ),

	("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarmatian_raider,2,6),(trp_sarmatian_herdsman,1,3),(trp_sarmatian_scout_archer,1,3)] ),
	("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarmatian_horse_archer,1,4),(trp_sarmatian_charger,1,3),(trp_sarmatian_female_horse_archer,1,3),(trp_sarmatian_veteran_raider,1,3)] ),
	("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarmatian_noble_raider,1,2),(trp_sarmatian_heavy_charger,1,2),(trp_sarmatian_noble_horse_archer,1,2),(trp_sarmatian_noblewoman,1,3)] ),

	("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_chatti_huntsman,2,4),(trp_chatti_woodsman,2,4),(trp_chatti_spear_warrior,2,4)] ), 
	("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_chatti_axe_warrior,2,4),(trp_chatti_spearman,2,4),(trp_chatti_archer,1,2),(trp_chatti_skirmisher,1,2)] ),
	("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_chatti_nobleman,1,3),(trp_chatti_veteran_warrior,2,4),(trp_chatti_light_horseman,1,4)] ),

	("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_langobardi_tribesman,2,4),(trp_langobardi_slinger,2,4),(trp_langobardi_light_warrior,2,4)] ), 
	("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_langobardi_warrior,1,4),(trp_langobardi_light_spearman,2,4),(trp_langobardi_skirmisher,2,4),(trp_langobardi_horseman,1,2)] ),
	("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_langobardi_armoured_warrior,2,4),(trp_langobardi_trained_singer,2,3),(trp_langobardi_horseman,1,2)] ),

	("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nabatean_recruit,2,6),(trp_nabatean_spearman,2,4),(trp_nabatean_skirmisher,2,4)] ), 
	("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nabatean_slinger,1,3),(trp_nabatean_horse_skirmisher,1,3),(trp_nabatean_armoured_spearman,2,4)]),
	("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nabatean_horseman,1,3),(trp_nabatean_ramqu_guard,1,3),(trp_nabatean_elite_horseman,1,3)] ),

	("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_alanian_tribesman,2,6),(trp_alanian_raider,1,3),(trp_alanian_tribal_horseman,1,3)] ),
	("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_alanian_horse_archer,1, 4),(trp_alanian_horseman,1,3),(trp_alanian_steppe_lancer,1,3),(trp_alanian_heavy_horseman,1,3)] ),
	("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_alanian_steppe_cataphract,1,2),(trp_alanian_noble_cataphract,1,2),(trp_alanian_veteran_horse_archer,1,2),(trp_alanian_heavy_horseman,1,3)] ),

	("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bosporan_bow_militia,2,4),(trp_bosporan_cavalry_militia,2,4),(trp_bosporan_spear_militia,2,4),] ),
	("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bosporan_spearman,2,4),(trp_bosporan_trained_bowman,2,5),(trp_bosporan_swordman,2,5)] ),
	("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_bosporan_royal_swordman,1,4),(trp_bosporan_cataphract_archer,1,4),(trp_bosporan_armoured_swordman,2,4)] ),

	("kingdom_22_reinforcements_a", "{!}kingdom_22_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_aesti_tribesman,2,4),(trp_aesti_huntsman,2,4),(trp_aesti_clan_warrior,2,4)] ), 
	("kingdom_22_reinforcements_b", "{!}kingdom_22_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_aesti_trained_warrior,2,4),(trp_aesti_spear_hunter,2,4),(trp_aesti_bow_hunter,2,4)] ),
	("kingdom_22_reinforcements_c", "{!}kingdom_22_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_aesti_noble_warrior,2,3),(trp_aesti_beserker,1,3)] ),

	("kingdom_23_reinforcements_a", "{!}kingdom_23_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_garamantian_desert_hunter,2,4),(trp_garamantian_desert_bowman,2,4),(trp_garamantian_spear_hunter,2,4)] ),
	("kingdom_23_reinforcements_b", "{!}kingdom_23_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_garamantian_desert_bowman,2,3),(trp_garamantian_veteran_hunter,2,4),(trp_garamantian_desert_lancer,1,3),(trp_garamantian_mounted_skirmisher,2,4)] ),
	("kingdom_23_reinforcements_c", "{!}kingdom_23_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_garamantian_lion_hunter,1,3),(trp_garamantian_mounted_javelinman,1,3),(trp_garamantian_oasis_lancer,1,3)] ),

	("kingdom_26_reinforcements_a", "{!}kingdom_26_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_suebi_hunter,2,4),(trp_suebi_light_spearman,2,4),(trp_suebi_tribesman,2,4)] ), 
	("kingdom_26_reinforcements_b", "{!}kingdom_26_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_suebi_axeman,1,4),(trp_suebi_spearman,2,4),(trp_suebi_light_horseman,2,4),(trp_suebi_javelinman,2,4)] ),
	("kingdom_26_reinforcements_c", "{!}kingdom_26_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_suebi_noble_spearman,1,3),(trp_suebi_spearman,2,4)] ),

	("kingdom_27_reinforcements_a", "{!}kingdom_27_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_jazygian_outrider,2,6),(trp_jazygian_mounted_bowman,2,6),(trp_jazygian_shepherd,1,3)] ), 
	("kingdom_27_reinforcements_b", "{!}kingdom_27_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_jazygian_lancer,1,4),(trp_jazygian_mounted_archer,2,6),(trp_jazygian_mounted_warrior,2,4)]),
	("kingdom_27_reinforcements_c", "{!}kingdom_27_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_jazygian_noble,1,3),(trp_jazygian_cataphract_lancer,1,3),(trp_jazygian_mounted_marskman,1,3)] ),	
	
	("kingdom_28_reinforcements_a", "{!}kingdom_28_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bastarnian_tribesman,2,3),(trp_bastarnian_hurler,2,6),(trp_bastarnian_spearman,2,6)] ), 
	("kingdom_28_reinforcements_b", "{!}kingdom_28_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bastarnian_warrior,1,3),(trp_bastarnian_slinger,2,4),(trp_bastarnian_falxman,2,4),(trp_bastarnian_rider,2,6)]),
	("kingdom_28_reinforcements_c", "{!}kingdom_28_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_bastarnian_champion,1,3),(trp_bastarnian_trained_spearman,2,4)] ),

	("kingdom_29_reinforcements_a", "{!}kingdom_29_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_armenian_slinger,2,4),(trp_armenian_militia,2,4),(trp_armenian_armenian_rider,2,4)] ),
	("kingdom_29_reinforcements_b", "{!}kingdom_29_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_armenian_maceman,2,4),(trp_armenian_spearman,2,5),(trp_armenian_trained_slinger,2,4),(trp_armenian_noble_rider,2,4)] ),
	("kingdom_29_reinforcements_c", "{!}kingdom_29_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_armenian_heavy_spearman,1,4),(trp_armenian_azat_knight,1,2),(trp_armenian_heavy_slinger,1,3)] ),

	("kingdom_30_reinforcements_a", "{!}kingdom_30_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rugii_tribesman,2,4),(trp_rugii_javelin_hunter,2,4),(trp_rugii_light_horseman,1,2)] ), 
	("kingdom_30_reinforcements_b", "{!}kingdom_30_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rugii_swordman,1,4),(trp_rugii_javelin_hunter,2,3),(trp_rugii_light_spearman,2,4),(trp_rugii_horseman,1,3)] ),
	("kingdom_30_reinforcements_c", "{!}kingdom_30_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rugii_spearman,2,5),(trp_rugii_noble_horseman,2,3)] ),

	("kingdom_31_reinforcements_a", "{!}kingdom_31_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_cimbri_tribesman,2,4),(trp_cimbri_hunter,2,4),(trp_cimbri_light_skirmisher,2,4)] ), 
	("kingdom_31_reinforcements_b", "{!}kingdom_31_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_cimbri_skirmisher,1,3),(trp_cimbri_light_horseman,1,2),(trp_cimbri_light_footman,2,4),(trp_cimbri_axeman,2,4)] ),
	("kingdom_31_reinforcements_c", "{!}kingdom_31_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_cimbri_sentinel,1,3),(trp_cimbri_footman,2,4),(trp_cimbri_trained_axeman,2,4)] ),

##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),

  # Merc Camp Begin
    ("merc_camp_legion_1_troops", "{!}XIII Gemina Legion", 0, 0, fac_commoners, 0, [(trp_i_gemina_levy,5,12),(trp_i_gemina_centurion,1,6)]),
    ("merc_camp_legion_2_troops", "{!}II Adiutrix Legion", 0, 0, fac_commoners, 0, [(trp_ii_adiutrix_levy,5,12),(trp_ii_adiutrix_centurion,1,6)]),
    ("merc_camp_legion_3_troops", "{!}VI Victrix Legion", 0, 0, fac_commoners, 0, [(trp_vi_victrix_levy,5,12),(trp_vi_victrix_centurion,1,6)]),
    ("merc_camp_legion_4_troops", "{!}I Parthia Legion", 0, 0, fac_commoners, 0, [(trp_i_parthia_levy,5,12),(trp_i_parthia_centurion,1,6)]),
    ("merc_camp_legion_5_troops", "{!}IX Hispana Legion", 0, 0, fac_commoners, 0, [(trp_ix_hispana_levy,5,12),(trp_ix_hispana_centurion,1,6)]),
    ("merc_camp_legion_6_troops", "{!}XXII Primigenia Legion", 0, 0, fac_commoners, 0, [(trp_xxii_primigenia_levy,5,12),(trp_xxii_primigenia_centurion,1,6)]),
    ("merc_camp_egyptian_troops", "{!}Egyptian Mercs", 0, 0, fac_commoners, 0, [(trp_egyptian_recruit,5,12)]),
    ("merc_camp_iberian_troops", "{!}Iberian Mercs", 0, 0, fac_commoners, 0, [(trp_iberian_scout,5,12)]),
    ("merc_camp_kushan_troops", "{!}Kushan Mercs", 0, 0, fac_commoners, 0, [(trp_kushan_rider,5,12)]),
    ("merc_camp_llyrian_troops", "{!}Illyrian Mercs", 0, 0, fac_commoners, 0, [(trp_illyrian_recruit,5,12)]),
    ("merc_camp_greek_troops", "{!}Greek Mercs", 0, 0, fac_commoners, 0, [(trp_greek_recruit,5,12)]),
    ("merc_camp_nubian_troops", "{!}Nubian Mercs", 0, 0, fac_commoners, 0, [(trp_nubian_spearman,5,12)]),
# Merc Camp End

   ##diplomacy begin
	("dplmc_spouse"					,"Your spouse"							,icon_woman|pf_civilian|pf_show_faction														,0		,fac_neutral		,merchant_personality			,[]),
	#Native
	("dplmc_gift_caravan"			,"Your Caravan"							,icon_gray_knight|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_steppe_bandit,1,1),(trp_steppe_bandit,4,32),(trp_steppe_bandit,1,10),(trp_steppe_bandit,0,4),(trp_steppe_bandit,0,4)]),
	#Reworked
	("dplmc_gift_caravan_r"			,"Your Caravan"							,icon_gray_knight|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_steppe_bandit,1,1),(trp_steppe_bandit,4,32),(trp_steppe_bandit,1,10),(trp_steppe_bandit,0,4),(trp_steppe_bandit,0,4)]),
	#Expanded
	("dplmc_gift_caravan_e"			,"Your Caravan"							,icon_gray_knight|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_steppe_bandit,1,1),(trp_steppe_bandit,4,32),(trp_steppe_bandit,1,10),(trp_steppe_bandit,0,4),(trp_steppe_bandit,0,4)]),
#recruiter kit begin
	("dplmc_recruiter"				,"Recruiter"							,icon_gray_knight|pf_show_faction															,0		,fac_neutral		,merchant_personality			,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
  ("steppe_bandit_lair" ,"Roxolanian Lair",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Caucasian Lair",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Saracen Bandit Lair",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Vandal Lair",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Musulamanian Hideout",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Saxon Landing",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("iberian_bandit_lair" ,"Iberian Hideout",icon_icon_camp_big|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
