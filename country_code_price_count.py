def get_country_codes(prices):
    return ", ".join([item.split("$")[0] for item in prices.split(", ")])


def main():
    prices = ("NZ$300, KR$1200, DK$5")
    print(get_country_codes(prices))
    

if __name__ == '__main__':
    main()