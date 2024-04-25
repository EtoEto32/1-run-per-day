def main():
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    odd_squared = []

    for odd in odds:
        odd_squared.append(odd ** 2)
    
    print(odd_squared)

if __name__ == "__main__":
    main()