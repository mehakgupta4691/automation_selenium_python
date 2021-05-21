from expedia.expedia import Expedia

with Expedia() as bot:
    bot.land_first_page()
    #bot.select_place_to_go('New York')
    bot.select_dates(check_in_date = "8", check_out_date = "10")
