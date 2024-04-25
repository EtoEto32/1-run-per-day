from itertools import zip_longest

def main():
    prefs = ['富山県', '石川県', '福井県','岐阜県']
    capitals = ['富山市', '金沢市', '福井市']


    # for pref, capital in zip(prefs, capitals):   
    #     print(f'{pref}の県庁所在地は{capital}です')
    
    # for pref, capital in zip_longest(prefs, capitals):   
    #     print(f'{pref}の県庁所在地は{capital}です')

    for pref, capital in zip_longest(prefs, capitals, fillvalue='不明'):
        print(f'{pref}の県庁所在地は{capital}です')

if __name__ == "__main__":
    main()