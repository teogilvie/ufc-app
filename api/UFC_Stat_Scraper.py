# Tyson O'Gilvie
# UFC site scraper

#possibly start scraping from ufcstats.com instead


from optparse import Option
from ssl import Options
from turtle import title
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

#first_name_athlete = "Firstname"
#last_name_athlete = "Lastname"

def fighter_stat_func (Firstname, Lastname):

    driverloc = "/Users/teogi/Documents/UFC_Application/geckodriver"

    first_name_athlete = f"{Firstname}"
    last_name_athlete = f"{Lastname}"
    whole_name_athlete = f"{first_name_athlete} {last_name_athlete}"

    athlete_name = f"{first_name_athlete}-{last_name_athlete}"

    URL = f"https://www.ufc.com/athlete/{athlete_name}"

    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path="{driverloc}", options=options)
    driver.get(URL)
    #print("Fighter:")
    #print(driver.title)
    #driver.close()
    fight_stats_1 = driver.find_elements(By.CLASS_NAME,'c-stat-3bar__value')
    fight_stats_2 = driver.find_elements(By.CLASS_NAME, 'e-chart-circle__percent')
    fight_stats_3 = driver.find_elements(By.CLASS_NAME, 'c-bio__text')

    #print(len(fight_stats_3))
    #for i in range(0, len(fight_stats_3)):
        #print(fight_stats_3[i].text)

#some fighters dont have a team listed : correct for string length

    if (len(fight_stats_3) == 10):
        var_index = 0
        team_delete = 0
    else:
        var_index = 1
        team_delete = 2

    stat_standing = fight_stats_1[0].text
    stat_clinch = fight_stats_1[1].text
    stat_ground = fight_stats_1[2].text
    stat_ko_tko = fight_stats_1[3].text
    stat_dec = fight_stats_1[4].text
    stat_sub = fight_stats_1[5].text
    striking_accuracy = fight_stats_2[0].text
    takedown_accuracy = fight_stats_2[1].text
    active_status = fight_stats_3[0].text
    home_town = fight_stats_3[1].text
    team_ = fight_stats_3[2 - team_delete].text
    fight_style = fight_stats_3[3 - var_index].text
    fighter_age = fight_stats_3[4 - var_index].text
    fighter_height = fight_stats_3[5 - var_index].text
    fighter_weight = fight_stats_3[6 - var_index].text
    fighter_arm_reach = fight_stats_3[8 - var_index].text
    fighter_leg_reach = fight_stats_3[9 - var_index].text

    return (stat_standing, stat_clinch, stat_ground, stat_ko_tko,
    stat_dec, stat_sub, striking_accuracy, takedown_accuracy, active_status,
    fight_style, fighter_age, fighter_height, fighter_weight, fighter_arm_reach,
    fighter_leg_reach, whole_name_athlete)