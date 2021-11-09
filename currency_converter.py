import requests, json
import tkinter as tk
from tkinter import *

def createWidgets():

    country_list = ["India (INR)", "United states of America (USD)", "Canada (CAD)", "China (CNY)", "Denmark (DKK)", "Europian union (EUR)", "Afganistan (AFN)", "Algeria (DZD)", "Albania (AOA)", "Anguilla (XCD)", "Argentina (ARS)", "Armenia (AMD)", "Aruba (AWG)", "Australia (AUD)", "Bahamas (BSD)", "Bahrain (BHD)", "Bangladesh (BDT)", "Barbados (BBD)", "Belarus (BYN)", "Benin (XDF)", "Bhutan (BTN)", "Bolivia (BOB)", "Colombia (COP)", "Comoros (KMF)" ]

    text_label = Label(root, text="currency converter", bg="white")
    text_label.grid(row=1, column=1, pady=10)

    amount_label = Label(root, text="Enter amount  ", bg="white")
    amount_label.grid(row=2, column=0, padx=20, pady=10)

    amount_entry1 = Entry(root, width=40, textvariable=amount1)
    amount_entry1.grid(row=2, column=1, padx=20, pady=10)

    from_country = Label(root, text="From country", bg="white")
    from_country.grid(row=3, column=0, padx=20, pady=10)

    from_menu = OptionMenu(root, variable1, *country_list )
    from_menu.grid(row=3, column=1, padx=20, pady=10)

    to_country = Label(root, text="To country", bg="white")
    to_country.grid(row=4, column=0, padx=20, pady=10)

    to_menu = OptionMenu(root, variable2, *country_list )
    to_menu.grid(row=3, column=1, padx=20, pady=10)

    convert_but = Button(root, width=15, text="Convert", command="", bg="light blue" )
    convert_but.grid(row=4, column=2, padx=20, pady=10)

    converted_text = Label(root, text="Convert", command="", bg="light blue")
    converted_text.grid(row=5, column=0, padx=20, pady=10)

    amount_entry2 = Entry(root, width=40)
    amount_entry2.grid(row=5, column=1, pady=10)

    clear_but = Button(root, text="Clear", width=10, command="", bg="light blue")
    clear_but.grid(row=5, column=2, pady=10)

def data(str):
    for i in str:
        if i == "(":
             start = str.index(i)+1
        if i == ")":
            end = str.index(i)
    return str[start:end]

def Calculate():

    api_key = " CNGEM3N7KYSP8O4H"
    base_url = r"https://www.alphavantage.co/?function=CURRENCY_EXCHANGE_RATE"
    var1 = data(Variable1.get())
    var2 = data(Variable2.get())

    main_url = base_url+"&from country="+var1+"&to_country="+var2+"&apikey="+api_key



root = tk.Tk()
root.geometry("650x250")
root.title("Currency Converter")
root.config(background="grey")

amount1 = StringVar()
Variable1 = StringVar()
Variable2 = StringVar()
Variable1.set("From country")
Variable2.set("To country")

createWidgets()




root.mainloop()
