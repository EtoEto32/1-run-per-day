def main():
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # odd_squared = [e ** 2 for e in odds]
    # map関数版
    # odd_squared = list(map(lambda e: e**2, odds)) 
    odd_squared = [e ** 2 for e in odds if e > 3 and e < 17]
    # map関数、filter関数
    # odd_squared = list(map(lambda e: e**2, filter(lambda e: e > 3 and e < 17,odds)))  
    print(odd_squared)
    
if __name__ == "__main__":
    main()