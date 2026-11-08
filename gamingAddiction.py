def importData(fileName):
    """
    outputs data in the form:
    [[age,daily play time]]
       1               11
    
    Input format:
    user_id,age,gender,country,occupation,income_level,years_gaming,preferred_genre,platform,device_type,rank_tier,daily_playtime_hours,weekly_play_sessions,late_night_sessions_hours,weekend_playtime_hours,consecutive_hours_max,multiplayer_ratio,toxic_chat_reports,rage_quit_frequency,in_game_purchases,monthly_spending_usd,lootbox_openings,subscription_status,stress_score,loneliness_score,dopamine_dependency_index,self_control_score,impulsiveness_score,anxiety_level,depression_indicator,emotional_stability,sleep_hours,exercise_frequency_per_week,caffeine_intake_cups_day,social_interaction_hours,relationship_status,gpa_or_performance_score,missed_deadlines,productivity_drop_percent,absenteeism_days,internet_speed_mbps,screen_time_total_hours,behavioral_cluster,addiction_score,addiction_binary,addiction_severity,burnout_probability,mental_health_risk_score,churn_probability
        0    1     2      3         4           5           6               7           8          9        10             11                   12                  13                          14                      15                  16              17                  18                  19                 20               21                  22                 23           24                      25                   26                 27              28                  29                  30              31               32                         33                      34                          35              36                      37                      38                  39                  40                  41                      42              43               44                 45              46                       47                 48                                     
    """

    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    
    cleanData,xyCoordinates = [],[]

    for j in lines:
        text = j.split(",")
        cleanData.append(text)

    """
    cleanData contains all the data, but split into individual items as 
    dictated by the ";"
    """
    for i in cleanData:
        xyCoordinates.append([float(i[6])/100, float(i[11])/24])
        

    return xyCoordinates


