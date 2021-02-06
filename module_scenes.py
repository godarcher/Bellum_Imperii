from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1_1   Sargoth     #plain
#  town_2_1   Tihr        #steppe
#  town_3_1   Veluca      #steppe
#  town_4_1   Suno        #plain
#  town_5_1   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

scenes = [
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[]),
  ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),
  ("random_scene_steppe",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000020a448890007b1f7000060ea00006de0000003a6",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000032a105868005d976000035670000542d00002d0f",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000042a105868005d97600006cf500004822000028ff",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005465058f8005d9760000433a000003f2000028ff",
    [],[], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_desert"),
  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
  ("quick_battle_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30401ee300059966000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x4c6024e3000691a400001b7c0000591500007b52", 
    [],[], "outer_terrain_snow"),
  ("quick_battle_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00001d63c005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a078bb2000589630000667200002fb90000179c", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("salt_mine",sf_generate,"none", "none", (-200,-200),(200,200),-100,"0x2a07b23200025896000023ee00007f9c000022a8",  
    [],[], "outer_terrain_steppe"),
  ("novice_ground",sf_indoors,"training_house_a", "bo_training_house_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("zendar_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[], "outer_terrain_plain"),
  ("dhorak_keep",sf_generate,"none", "none", (0,0),(120,120),-100,"0x33a7946000028ca300007f4a0000479400161992",
    ["exit"],[]),
  ("reserved4",sf_generate,"none", "none", (0,0),(120,120),-100,"28791",
    [],[]),
  ("reserved5",sf_generate,"none", "none", (0,0),(120,120),-100,"117828",
    [],[]),
  ("reserved6",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved7",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved8",sf_generate,"none", "none", (0,0),(100,100),-100,"13278",
    [],[]),
  ("reserved9",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved10",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved11",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved12",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain_1"),
  ("tutorial_1",sf_indoors,"tutorial_1_scene", "bo_tutorial_1_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
##  ("tutorial_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003a04ce140005e17a000030030000780e00006979",
##    [],[], "outer_terrain_plain"),
  ("tutorial_2",sf_indoors,"tutorial_2_scene", "bo_tutorial_2_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_3",sf_indoors,"tutorial_3_scene", "bo_tutorial_3_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
  ("tutorial_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),


  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_snow"),
  #Steppe
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001350455c20005194a000041cb00005ae800000ff5",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000532c8dccb0005194a000041cb00005ae800001bdd",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_ranged_melee_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000054327dcba0005194a00001b1d00005ae800004d63",
    [],[], "outer_terrain_snow"),
  #Steppe
  ("training_ground_ranged_melee_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000012247dcba0005194a000041ef00005ae8000050af",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_ranged_melee_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("zendar_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    ["the_happy_boar","","zendar_merchant"],[], "outer_terrain_plain_1"),
#  ("zendar_center",0,"sargoth_square", "bo_sargoth_square", (-24,-22),(21,13),-100,"0",
#    ["the_happy_boar","","zendar_merchant"],[]),
  ("the_happy_boar",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["zendar_center"],["zendar_chest"]),
  ("zendar_merchant",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# Tvern names:
  #the shy monkey
  #the singing pumpkin
  #three swords
  #red stag
  #the bard's corner


#interior_tavern_a
#  town_1_1   Sargoth     #plain
#  town_2_1   Tihr        #plain
#  town_3_1   Veluca      #steppe
#  town_4_1   Suno        #plain  
#  town_5_1   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe

  ("senate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002308c000063c100001bee00006f14  ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("alexandria_port",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000044d130000104100005e940000147b   ",    [],["bonus_chest_3"],"sea_outer_terrain_2 "),

  ("roman_camp_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006d9b700003b530000280e0000575b",    [],["bonus_chest_3"],"outer_terrain_plain"),

  
  ("roman_temple",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00005000002589600004a2900003efe00007972   ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("roman_temple_interior",sf_indoors,"interior_castle_j", "bo_interior_castle_j ", (0,0),(100,100),-100,"0",    [],["bonus_chest_3"],"outer_terrain_plain"),

  ("rome_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013301c85000059224800072a70000240a00001e090 ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("rome_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013301c85000059224800072a70000240a00001e090",    [],[],"outer_terrain_plain"),
  ("rome_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af ",    [],[],"outer_terrain_plain"),
  ("rome_castle",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a ", (-100,-100),(100,100),-100,"0",    ["exit"],[]),

  ("pergamum_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09  ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("pergamum_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_1_seneschal"]),
  ("pergamum_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("pergamum_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("pergamum_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("pergamum_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",    [],[],"outer_terrain_plain"),
  ("pergamum_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af ",    [],[],"outer_terrain_plain"),

  ("londinium_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0  ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("londinium_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_2_seneschal"]),
  ("londinium_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("londinium_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("londinium_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("londinium_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",    [],[],"outer_terrain_plain"),
  ("londinium_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af ",    [],[],"outer_terrain_plain"),
  
  
  ("byzantium_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0   ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("byzantium_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_3_seneschal"]),
  ("byzantium_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("byzantium_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("byzantium_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("byzantium_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",    [],[],"outer_terrain_plain"),
  ("byzantium_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af ",    [],[],"outer_terrain_plain"),
  
  ("carthago_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013a01c85000057ddf700072a70000240a00001e090   ",    [],["bonus_chest_3"],"sea_outer_terrain_2   "),
  ("carthago_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013a01c85000057ddf700072a70000240a00001e090 ",    [],[],"sea_outer_terrain_2   "),
  ("carthago_castle",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a ", (-100,-100),(100,100),-100,"0",    ["exit"],[]),

  ("neapolis_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000350d4000011a4000017ee000054af0  ",    [],["bonus_chest_3"],"outer_terrain_steppe"),
  ("neapolis_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000350d4000011a4000017ee000054af0   ",    [],[],"outer_terrain_steppe "),
  ("neapolis_castle",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a ", (-100,-100),(100,100),-100,"0",    ["exit"],[]),

  ("ravenna_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000374dd000041ef00005ae800003c55   ",    [],["bonus_chest_3"],"outer_terrain_plain "),
  ("ravenna_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000000374dd000041ef00005ae800003c55   ",    [],[],"outer_terrain_plain "),
  ("ravenna_castle",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a ", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  
  ("jerusalem_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0    ",    [],["bonus_chest_3"],"outer_terrain_desert "),
  ("jerusalem_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_4_seneschal"]),
  ("jerusalem_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("jerusalem_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("jerusalem_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("jerusalem_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0 ",    [],[],"outer_terrain_desert "),
  ("jerusalem_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af  ",    [],[],"outer_terrain_desert "),
 
  ("carhagonova_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000004591c000041ef00005ae800003c55   ",    [],["bonus_chest_3"],"outer_terrain_plain "),
  ("carhagonova_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000004591c000041ef00005ae800003c55   ",    [],[],"outer_terrain_plain "), 
 
 
  ("ctesiphon_center_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220000500000d2348000063f500001bbd00005d54",    ["exit"],[]),
  ("ctesiphon_castle_1",sf_indoors,"viking_interior_keep_a   ", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_5_seneschal"]),
  ("ctesiphon_tavern_1",sf_generate,"none", "none", (-100,-100),(100,100),-100,"0x00000000200005000002c8ae00000114000078710000692c",    ["exit"],[]),
  ("ctesiphon_prison_1",sf_indoors,"interior_prison_cell_a ", "bo_interior_prison_cell_a ", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("ctesiphon_walls_1",sf_generate,"none", "none", (-100,-100),(100,100),-100," 0x0000000220000500000d2348000063f500001bbd00005d54",    ["exit"],[]),

  
  ("panticapaeum_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09    ",    [],["bonus_chest_3"],"outer_terrain_plain "),
  ("panticapaeum_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_6_seneschal"]),
  ("panticapaeum_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("panticapaeum_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("panticapaeum_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("panticapaeum_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09 ",    [],[],"outer_terrain_plain "),
  ("panticapaeum_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af  ",    [],[],"outer_terrain_plain "),
  
  ("alexandria_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005054100002d0b00003a0200002ca5   ",    [],["bonus_chest_3"],"outer_terrain_beach  "),
  ("alexandria_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09  ",    [],[],"outer_terrain_beach  "),
  ("alexandria_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af   ",    [],[],"sea_outer_terrain_2  "),
  ("alexandria_castle",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a ", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
 
  ("roman_town_center_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09 ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("roman_town_castle_1",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_7_seneschal"]),
  ("roman_town_tavern_1",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("roman_town_store_1",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("roman_town_prison_1",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("roman_town_walls_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",    [],[],"outer_terrain_plain"),
  ("roman_town_alley_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",    [],[],"outer_terrain_plain"),
  ("roman_town_arena_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",    [],[],"outer_terrain_plain"),

  ("roman_town_center_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300004000005e17d000041ef00005ae800003c55 ",    [],["bonus_chest_3"],"outer_terrain_beach"),
  ("roman_town_walls_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300004000005e17d000041ef00005ae800003c55",    [],[],"outer_terrain_beach"),
    
  
  ("parthian_town_center_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200005000007b1e100003fc600005f1a00005678   ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("parthian_town_castle_1",sf_indoors,"viking_interior_keep_a ", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_8_seneschal"]),
  ("parthian_town_tavern_1",sf_generate,"none", "none", (-100,-100),(100,100),-100,"0x00000000200005000002c8ae00000114000078710000692c",    ["exit"],[]),
  ("parthian_town_store_1",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("parthian_town_prison_1",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("parthian_town_walls_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220000500000769db00005d000000620700006914 ",    [],[],"outer_terrain_plain"),
  ("parthian_town_arena_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",    [],[],"outer_terrain_plain"),
 

  ("scythian_town_center_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023060080a000d23480000580c000005a800007530",    [],["bonus_chest_3"],"outer_terrain_steppe"),
  ("scythian_town_castle_1",sf_generate,"none", "none", (-100,-100),(100,100),-100,"0x000000023060080a000d23480000580c000005a800007530",   ["exit"],["town_9_seneschal"]),
  ("scythian_town_tavern_1",sf_generate,"none", "none", (-100,-100),(100,100),-100,"0x000000023060080a000d23480000580c000005a800007530",    ["exit"],[]),
  ("scythian_town_store_1",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("scythian_town_prison_1",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("scythian_town_walls_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023060080a000d23480000580c000005a800007530    ",    [],[],"outer_terrain_steppe"),
  ("scythian_town_arena_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023060080a000d23480000580c000005a800007530    ",    [],[],"outer_terrain_steppe"),
  
 
  ("germanic_town_center_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09  ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("germanic_town_castle_1",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_10_seneschal"]),
  ("germanic_town_tavern_1",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("germanic_town_store_1",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("germanic_town_prison_1",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("germanic_town_walls_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",    [],[],"outer_terrain_plain"),
  ("germanic_town_alley_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",    [],[],"outer_terrain_plain"),
  ("germanic_town_arena_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af ",    [],[],"outer_terrain_plain"),

  ("germanic_town_center_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000510000775de0000094c00006c0a00001359     ",    [],["bonus_chest_3"],"outer_terrain_beach"),
  ("germanic_town_walls_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000510000775de0000094c00006c0a00001359",    [],[],"outer_terrain_beach"),
  
  
  ("dacian_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0141eb9000589620000071c0000726b00005042   ",    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("dacian_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_11_seneschal"]),
  ("dacian_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("dacian_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0141eb9000589620000071c0000726b00005042  ",    [],[],"outer_terrain_plain"),
  ("dacian_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c  ",    [],[],"outer_terrain_plain"),

  ("african_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d  ",    [],["bonus_chest_3"],"outer_terrain_desert"),
  ("african_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",   ["exit"],["town_12_seneschal"]),
  ("african_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",    ["exit"],[]),
  ("african_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",   ["exit"],[]),
  ("african_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",    [],[]),
  ("african_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d",    [],[],"outer_terrain_desert"),
  ("african_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09 ",    [],[],"outer_terrain_desert"),

	
  ("roman_fortress_exterior_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00dd2908005795e0000706d8000044400004309 ",    [],[],"outer_terrain_plain"),
  ("roman_fortress_interior_1",sf_indoors, "interior_castle_j ", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_1_seneschal"]),
  
  ("roman_fortress_exterior_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697  ",    [],[],"outer_terrain_plain"),
  ("roman_fortress_interior_2",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_2_seneschal"]),
  ("roman_fortress_prison",sf_indoors, "interior_prison_i", "bo_interior_prison_i",(-100,-100),(100,100),-100,"0",    [],[]),
 
  ("parthian_fortress_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001a00005000005695c00001ebe0000028e00007e37   ",    [],[],"outer_terrain_desert"),
  ("parthian_fortress_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_3_seneschal"]),
  ("parthian_fortress_prison",sf_indoors, "interior_prison_h ", "bo_interior_prison_h ",(-100,-100),(100,100),-100,"0",    [],[]),

  ("steppe_stronghold_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000050000049d2a00003c37000040ef000037cd    ",    [],[],"outer_terrain_steppe"),
  ("steppe_stronghold_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k ", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_4_seneschal"]),
  ("steppe_stronghold_prison",sf_indoors, "interior_prison_i ", "bo_interior_prison_i ",(-100,-100),(100,100),-100,"0",    [],[]),

  ("nomad_castle_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000050044e900003dd02000077b20000400100005697     ",    [],[],"outer_terrain_desert"),
  ("nomad_castle_interior",sf_indoors, "interior_castle_k ", "bo_interior_castle_k  ", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_5_seneschal"]),
  ("nomad_castle_prison",sf_indoors, "interior_prison_i  ", "bo_interior_prison_i  ",(-100,-100),(100,100),-100,"0",    [],[]),

  ("dumatha_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000050044e900003dd02000077b20000400100005697     ",    [],[],"outer_terrain_desert"),
  ("dumatha_interior",sf_indoors, "arabian_interior_keep_b  ", "bo_arabian_interior_keep_b   ", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_6_seneschal"]),
    
  ("germanic_castle_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00dd2908005795e0000706d8000044400004309",    [],[],"outer_terrain_plain"),
  ("germanic_castle_interior",sf_indoors, "interior_castle_j ", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_7_seneschal"]),

  ("germanic_castle_exterior_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b000050000038ce3000070470000175c0000373c",    [],[],"outer_terrain_plain"),
  ("germanic_castle_interior_2",sf_indoors, "interior_castle_j ", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",    ["exit"],["castle_8_seneschal"]),
  
  ("roman_village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",    [],[],"outer_terrain_plain"),
  ("roman_village_2_coast",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030010a8600042110000015150000025000007932",    [],[],"outer_terrain_beach"),

  ("african_village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005020005a16800003f9900007d5600002a9c",    [],[],"outer_terrain_desert"),
  ("eastern_village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005020005a16800003f9900007d5600002a9c",    [],[],"outer_terrain_desert"),
  ("germanic_village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005020005a16800003f9900007d5600002a9c",    [],[],"outer_terrain_plain"),
  ("steppe_village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002002cb030004a1370000620f000075a1000050db",    [],[],"outer_terrain_steppe"),

  ("memphis",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002019098000046917000041010000386000003a38 ",    [],[],"outer_terrain_desert "),
	

  
  ("town_1_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_2_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_3_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_4_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_5_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_6_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_7_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),
  ("town_8_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_9_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
  ("town_10_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_11_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
  ("town_12_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_13_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_14_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_15_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),
  ("town_16_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),
  ("town_17_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_18_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_19_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220002f000003fd0400006e120000359900004e13",
    [],[],"outer_terrain_desert"),
  ("town_20_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000a0650001e9a00a505418000581f000028c800000143",
    [],[],"outer_terrain_desert"),
  ("town_21_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"outer_terrain_desert"),
  ("town_22_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000025a00723200046d1b00003e0200001476000052ae",
    [],[],"outer_terrain_desert"),

#0x30054d228004050000005a768000688400002e3b
#0x30054da28004050000005a76800022aa00002e3b
#Castles:



	
	
  ("field_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a059a5a0009525600002005000060e300001175",
    [],[],"outer_terrain_plain"),
  ("field_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a079a3f000a3a8000006dfd000030a100006522",
    [],[],"outer_terrain_steppe"),
  ("field_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),

  ("test2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0078cb20003fd0000005e480000288c0000286f",
    [],[],"outer_terrain_steppe"),

    ("test3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00511d98004b12e0000039f00004e6300005c7d",
    [],[],"outer_terrain_plain"),

# multiplayer
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
    [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",   
    [],[],"outer_terrain_snow"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_desert"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"outer_terrain_desert"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  ("multi_scene_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002ab630004651800000d7a00007f3100002701",
    [],[],"outer_terrain_plain"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("wedding",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0", [],[]),
  ("lair_steppe_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200c69ac80043d0d0000556b0000768400003ea9",
    [],[],"outer_terrain_steppe"), #a box canyon with a spring? -tents...
  ("lair_taiga_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c079c3e000499280000420f0000495d000048d6",
    [],[],"outer_terrain_snow"),
  ("lair_desert_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005024cd120005595400003882000037a90000673e",
    [],[],"outer_terrain_desert"), #an encampment in the woods
  ("lair_forest_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00326d90003ecfb0000657e0000213500002461",
    [],[],"outer_terrain_plain"), #a cliffside ledge or cave overlooking a valley
  ("lair_mountain_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200434070004450c000022bf00006ad6000060ed",
    [],[],"outer_terrain_steppe"),
  ("lair_sea_raiders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00562e200040900000063f40000679f00006cda",
    [],[],"sea_outer_terrain_1"), #the longships beached on a hidden cove


  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000250001d630005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002b76300046d2400000190000076300000692a", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000025a00f23700057d5f00006d6a000050ba000036df", 
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_plain"),
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("tutorial_training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
    
  ("town_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_room",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_room",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow_forest",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),

  ("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
]
# modmerger_start version=201 type=2
try:
    component_name = "scenes"
    var_set = { "scenes" : scenes }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
