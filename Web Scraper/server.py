from bottle import route, run, template
import mystocks
import main

@route("/")
def get_home():
    # pulling stock information from main.py
    stock1_name = main.stock1.name_
    stock1_price = main.stock1.price_
    stock1_percent_change = main.stock1.percent_change_
    stock1_price_change = main.stock1.price_change_

    stock2_name = main.stock2.name_
    stock2_price = main.stock2.price_
    stock2_percent_change = main.stock2.percent_change_
    stock2_price_change = main.stock2.price_change_

    stock3_name = main.stock3.name_
    stock3_price = main.stock3.price_
    stock3_percent_change = main.stock3.percent_change_
    stock3_price_change = main.stock3.price_change_

    stock4_name = main.stock4.name_
    stock4_price = main.stock4.price_
    stock4_percent_change = main.stock4.percent_change_
    stock4_price_change = main.stock4.price_change_
    
    stock5_name = main.stock5.name_
    stock5_price = main.stock5.price_
    stock5_percent_change = main.stock5.percent_change_
    stock5_price_change = main.stock5.price_change_

    stock6_name = main.stock6.name_
    stock6_price = main.stock6.price_
    stock6_percent_change = main.stock6.percent_change_
    stock6_price_change = main.stock6.price_change_

    stock7_name = main.stock7.name_
    stock7_price = main.stock7.price_
    stock7_percent_change = main.stock7.percent_change_
    stock7_price_change = main.stock7.price_change_

    stock8_name = main.stock8.name_
    stock8_price = main.stock8.price_
    stock8_percent_change = main.stock8.percent_change_
    stock8_price_change = main.stock8.price_change_

    stock9_name = main.stock9.name_
    stock9_price = main.stock9.price_
    stock9_percent_change = main.stock9.percent_change_
    stock9_price_change = main.stock9.price_change_
    
    stock10_name = main.stock10.name_
    stock10_price = main.stock10.price_
    stock10_percent_change = main.stock10.percent_change_
    stock10_price_change = main.stock10.price_change_
    
    return  template("home",
        ## passing that information on to the home template page
        row1_name = stock1_name,
        row1_price = stock1_price,
        row1_percent_change = stock1_percent_change,
        row1_price_change = stock1_price_change,

        row2_name = stock2_name,
        row2_price = stock2_price,
        row2_percent_change = stock2_percent_change,
        row2_price_change = stock2_price_change,

        row3_name = stock3_name,
        row3_price = stock3_price,
        row3_percent_change = stock3_percent_change,
        row3_price_change = stock3_price_change,

        row4_name = stock4_name,
        row4_price = stock4_price,
        row4_percent_change = stock4_percent_change,
        row4_price_change = stock4_price_change,

        row5_name = stock5_name,
        row5_price = stock5_price,
        row5_percent_change = stock5_percent_change,
        row5_price_change = stock5_price_change,

        row6_name = stock6_name,
        row6_price = stock6_price,
        row6_percent_change = stock6_percent_change,
        row6_price_change = stock6_price_change,

        row7_name = stock7_name,
        row7_price = stock7_price,
        row7_percent_change = stock7_percent_change,
        row7_price_change = stock7_price_change,

        row8_name = stock8_name,
        row8_price = stock8_price,
        row8_percent_change = stock8_percent_change,
        row8_price_change = stock8_price_change,

        row9_name = stock9_name,
        row9_price = stock9_price,
        row9_percent_change = stock9_percent_change,
        row9_price_change = stock9_price_change,

        row10_name = stock10_name,
        row10_price = stock10_price,
        row10_percent_change = stock10_percent_change,
        row10_price_change = stock10_price_change

        )

run(host="localhost", port=8068)