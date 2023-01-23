

# Tyson O'Gilvie
# Stat comparison
# Get a list of stats from two different fighters using scraper script 
# Wrap stat comparison in a function to be used with the api

import UFC_Stat_Scraper
import SQLPullFcn

def fight_prediction(fighter_1_firstName, fighter_1_lastName, fighter_2_firstName, fighter_2_lastName):

    Fighter_1_Stats = SQLPullFcn.SQL_Pull(fighter_1_firstName, fighter_1_lastName)

    if Fighter_1_Stats == 'NULL':

        Fighter_1_Stats = UFC_Stat_Scraper.fighter_stat_func(fighter_1_firstName, fighter_1_lastName)

        stat_standing_F1 = Fighter_1_Stats[0]
        stat_clinch_F1 = Fighter_1_Stats[1]    
        stat_ground_F1 = Fighter_1_Stats[2]
        stat_ko_tko_F1 = Fighter_1_Stats[3]
        stat_dec_F1 = Fighter_1_Stats[4]
        stat_sub_F1 = Fighter_1_Stats[5]
        striking_accuracy_F1 = Fighter_1_Stats[6]
        takedown_accuracy_F1 = Fighter_1_Stats[7]
        active_status_F1 = Fighter_1_Stats[8]
        fight_style_F1 = Fighter_1_Stats[9]
        fighter_age_F1 = Fighter_1_Stats[10]
        fighter_height_F1 = Fighter_1_Stats[11]
        fighter_weight_F1 = Fighter_1_Stats[12]
        fighter_arm_reach_F1 = Fighter_1_Stats[13]
        fighter_leg_reach_F1 = Fighter_1_Stats[14] 
        athlete_name_F1 = Fighter_1_Stats[15]
    else: 
        stat_standing_F1 = Fighter_1_Stats[7]
        stat_clinch_F1 = Fighter_1_Stats[8]    
        stat_ground_F1 = Fighter_1_Stats[9]
        stat_ko_tko_F1 = Fighter_1_Stats[10]
        stat_dec_F1 = Fighter_1_Stats[11]
        stat_sub_F1 = Fighter_1_Stats[12]
        striking_accuracy_F1 = Fighter_1_Stats[3]
        takedown_accuracy_F1 = Fighter_1_Stats[4]
        fighter_age_F1 = Fighter_1_Stats[2]
        fighter_height_F1 = Fighter_1_Stats[1]
        fighter_weight_F1 = Fighter_1_Stats[0]
        fighter_arm_reach_F1 = Fighter_1_Stats[5]
        fighter_leg_reach_F1 = Fighter_1_Stats[6] 
        athlete_name_F1 = f"{fighter_1_firstName} {fighter_1_lastName}"


    Fighter_2_Stats = SQLPullFcn.SQL_Pull(fighter_2_firstName, fighter_2_lastName)

    if Fighter_2_Stats == 'NULL':

        Fighter_2_Stats = UFC_Stat_Scraper.fighter_stat_func(fighter_2_firstName, fighter_2_lastName)

        stat_standing_F2 = Fighter_2_Stats[0]
        stat_clinch_F2 = Fighter_2_Stats[1]    
        stat_ground_F2 = Fighter_2_Stats[2]
        stat_ko_tko_F2 = Fighter_2_Stats[3]
        stat_dec_F2 = Fighter_2_Stats[4]
        stat_sub_F2 = Fighter_2_Stats[5]
        striking_accuracy_F2 = Fighter_2_Stats[6]
        takedown_accuracy_F2 = Fighter_2_Stats[7]
        active_status_F2 = Fighter_2_Stats[8]
        fight_style_F2 = Fighter_2_Stats[9]
        fighter_age_F2 = Fighter_2_Stats[10]
        fighter_height_F2 = Fighter_2_Stats[11]
        fighter_weight_F2 = Fighter_2_Stats[12]
        fighter_arm_reach_F2 = Fighter_2_Stats[13]
        fighter_leg_reach_F2 = Fighter_2_Stats[14] 
        athlete_name_F2 = Fighter_2_Stats[15]
    else: 
        stat_standing_F2 = Fighter_2_Stats[7]
        stat_clinch_F2 = Fighter_2_Stats[8]    
        stat_ground_F2 = Fighter_2_Stats[9]
        stat_ko_tko_F2 = Fighter_2_Stats[10]
        stat_dec_F2 = Fighter_2_Stats[11]
        stat_sub_F2 = Fighter_2_Stats[12]
        striking_accuracy_F2 = Fighter_2_Stats[3]
        takedown_accuracy_F2 = Fighter_2_Stats[4]
        fighter_age_F2 = Fighter_2_Stats[2]
        fighter_height_F2 = Fighter_2_Stats[1]
        fighter_weight_F2 = Fighter_2_Stats[0]
        fighter_arm_reach_F2 = Fighter_2_Stats[5]
        fighter_leg_reach_F2 = Fighter_2_Stats[6] 
        athlete_name_F2 = f"{fighter_2_firstName} {fighter_2_lastName}"


    #start defining logical parameters

    f1_score = 0
    f2_score = 0
    pred_win = "unknown"

    if int(fighter_age_F1) - int(fighter_age_F2) > 4:
        f2_score = f2_score + 1

    if int(fighter_age_F2) - int(fighter_age_F1) > 4:
        f1_score = f1_score + 1

    if float(fighter_weight_F1) - float(fighter_weight_F2) > 29:
        f1_score = f1_score + 10000

    if float(fighter_weight_F2) - float(fighter_weight_F1) > 29:
        f2_score = f2_score + 10000

    if int(striking_accuracy_F1[0:2]) > int(striking_accuracy_F2[0:2]):
        if float(fighter_arm_reach_F1) > float(fighter_arm_reach_F2):
            f1_score = f1_score + 1
        if float(fighter_leg_reach_F1) > float(fighter_leg_reach_F2):
            f1_score = f1_score + 1

    if int(striking_accuracy_F2[0:2]) > int(striking_accuracy_F1[0:2]):
        if float(fighter_arm_reach_F2) > float(fighter_arm_reach_F1):
            f2_score = f2_score + 1
        if float(fighter_leg_reach_F2) > float(fighter_leg_reach_F1):
            f2_score = f2_score + 1

    if f1_score > f2_score:
        pred_win = athlete_name_F1

    if f2_score > f1_score:
        pred_win = athlete_name_F2

    if f1_score == f2_score:
        pred_win = "anybody's guess"

    return pred_win 
