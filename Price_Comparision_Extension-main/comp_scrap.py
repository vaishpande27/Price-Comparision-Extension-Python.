import urllib.request
import webbrowser
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import datetime
import comp_database as cd

#-------------------------------------------------------------
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client['Tarun']
    current_time = datetime.datetime.now()
    name = str(current_time.date())
    print(name)
    collection = db[name]

#-------------------------------------------------------------

obj = dict()
name_list = list()
price_list = list()


def flipkart(link):
    global name_list
    global price_list
    if link != "na" and link != "NA":
        try:
            first = urllib.request.urlopen(link)
        except:
            print("URL not found, please check again!")
            name_list = name_list + ["Flipkart"]
            price_list = price_list + [0]
        else:
            global flipkart_price
            obj = BeautifulSoup(first, "html.parser")
            name = obj.findAll("span", {"class": "B_NuCI"})
            for name_f in name:
                print(name_f.get_text())
            price = obj.findAll("div", {"class": "_30jeq3 _16Jk6d"})
            for num in price:
                num_price = num.get_text()
                print("price - ", num_price)
                num_price = num_price[1:]
                hi = num_price.split(',')
                num_price = "".join(hi)
                try:
                    flipkart_price = float(num_price)
                except:
                    print("", end="")
                    flipkart_price = 0
                finally:
                    name_list = ["Flipkart"]
                    price_list = [flipkart_price]
                    break


def amazon(link):
    global name_list
    global price_list
    if link != "na" and link != "NA":
        try:
            first = urllib.request.urlopen(link)
        except:
            print("URL not found, please check again!")
            name_list = name_list + ["Amazon"]
            price_list = price_list + [0]
        else:
            global amazon_price
            obj = BeautifulSoup(first, "html.parser")
            name = obj.find("span", {"class": "a-size-large product-title-word-break"})
            for name_f in name:
                name_f = name_f.get_text()
                a = len(name_f) - 7
                print(name_f[8:a])
            #price = obj.findAll("span", {"id": "priceblock_ourprice"})
            price = obj.findAll("span", {"class": "a-offscreen"})
            for num in price:
                num_price = num.get_text()
                print("price - ", num_price)
                num_price = num_price[1:]
                hi = num_price.split(',')
                num_price = "".join(hi)
                try:
                    amazon_price = float(num_price)
                except:
                    print("", end="")
                    amazon_price = 0
                finally:
                    name_list = name_list + ["Amazon"]
                    price_list = price_list + [amazon_price]
                    break


def indiamart(link):
    global name_list
    global price_list
    if link != "na" and link != "NA":
        try:
            first = urllib.request.urlopen(link)
        except:
            print("URL not found, please check again!")
            name_list = name_list + ["Indiamart"]
            price_list = price_list + [0]
        else:
            global indiamart_price
            obj = BeautifulSoup(first, "html.parser")
            name = obj.findAll("h1", {"class": "bo"})
            for name_f in name:
                print(name_f.get_text())
            price = obj.findAll("span", {"class": "prc-tip bo price-unit"})
            for num in price:
                num_price = num.get_text()
                print("price - ", num_price)
                num_price = num_price[2:len(num_price)-2]
                hi = num_price.split(',')
                num_price = "".join(hi)
                try:
                    indiamart_price = float(num_price)
                except:
                    print("", end="")
                    indiamart_price = 0
                else:
                    name_list = name_list + ["Indiamart"]
                    price_list = price_list + [indiamart_price]
                    break


def snapdeal(link):
    global name_list
    global price_list
    if link != "na" and link != "NA":
        try:
            first = urllib.request.urlopen(link)
        except:
            print("URL not found, please check again!")
            name_list = name_list + ["Snapdeal"]
            price_list = price_list + [0]
        else:
            global snapdeal_price
            obj = BeautifulSoup(first, "html.parser")
            name = obj.findAll("h1", {"class": "pdp-e-i-head"})
            for name_f in name:
                print(name_f.get_text()[7:])
            price = obj.findAll("span", {"class": "payBlkBig"})
            for num in price:
                num_price = num.get_text()
                print("price - Rs.", num_price)
                hi = num_price.split(',')
                num_price = "".join(hi)
                try:
                    snapdeal_price = float(num_price)
                except:
                    print("", end="")
                    snapdeal_price = 0
                finally:
                    name_list = name_list + ["Snapdeal"]
                    price_list = price_list + [snapdeal_price]
                    break


def plot_graph():
    print("\nminimum price is - ", min(t for t in price_list if t>0))
    plt.bar(name_list, price_list, color=['r', 'b', 'g', 'black', 'yellow'])
    plt.xlabel("Company names")
    plt.ylabel("Product price")
    plt.show()


# main()
countt = 0
print("\tPRICE COMPARISON EXTENSION")
print("Websites available for comparison - \n1. Flipkart\n2. Amazon\n3. Ebay\n4. Indiamart\n5. Snapdeal")

flipkart_url = input("enter the url of product(flipkart)\n(if not available, enter 'na'/'NA') - ")
if flipkart_url == 'na' or flipkart_url == 'NA':
    countt += 1

amazon_url = input("\nenter the url of product(amazon)\n(if not available, enter 'na'/'NA') - ")
if amazon_url == 'na' or amazon_url == 'NA':
    countt += 1

indiamart_url = input("\nenter the url of product(indiamart)\n(if not available, enter 'na'/'NA') - ")
if indiamart_url == 'na' or indiamart_url == 'NA':
    countt += 1

snapdeal_url = input("\nenter the url of product(snapdeal)\n(if not available, enter 'na'/'NA') - ")
if snapdeal_url == 'na' or snapdeal_url == 'NA':
    countt += 1

if countt == 0:
    print("\nFLIPKART :")
    flipkart(flipkart_url)

    print("\nAMAZON :")
    amazon(amazon_url)

    print("\nINDIAMART :")
    indiamart(indiamart_url)

    print("\nSNAPDEAL :")
    snapdeal(snapdeal_url)

#---------------------------------------------------------------------------------------------------------------------
    obj['time'] = str(current_time.time())
    obj['flipkart'] = [flipkart_url, price_list[0]]
    obj['amazon'] = [amazon_url, price_list[1]]
    obj['indiamart'] = [indiamart_url, price_list[2]]
    obj['snapdeal'] = [snapdeal_url, price_list[3]]
    
    obj['min'] = [name_list[price_list.index(min(t for t in price_list if t>0))], min(t for t in price_list if t>0)]
    cd.i(collection, obj)
#---------------------------------------------------------------------------------------------------------------------

    plot_graph()

    print("\nDo you wish to open any url?")
    print("1. Flipkart   2. Amazon   3. Indiamart   4. Snapdeal")
    i = input("press 1/2/3/4 to open any url or anything else to continue- ")
    if i == "1":
        webbrowser.open_new_tab(flipkart_url)
        print("Thank you for using this price comparison extension!")
    elif i == "2":
        webbrowser.open_new_tab(amazon_url)
        print("Thank you for using this price comparison extension!")
    elif i == "3":
        webbrowser.open_new_tab(indiamart_url)
        print("Thank you for using this price comparison extension!")
    elif i == "4":
        webbrowser.open_new_tab(snapdeal_url)
        print("Thank you for using this price comparison extension!")
    else:
        print("Thank you for using this price comparison extension!")

else:
    print("\nNo url provided!")
    cd.d(db, current_time)

    ans = input('\nDo you wish to see previous searches and results?(y/n) - ')
    while ans == 'y' or ans == 'Y':
        print('\nData available for last 7 days\n')
        day = int(input('enter day(dd) - '))
        mon = int(input('enter month(mm) - '))
        year = int(input('enter year(yyyy) - '))
        final = datetime.date(year, mon, day)
        cd.search(db, final)
        ans = input('Want to search more?(y/n) - ')
    
    print('\nThank you for using this price comparison extension!')