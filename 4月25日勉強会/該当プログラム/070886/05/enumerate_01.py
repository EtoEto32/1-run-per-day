def main():
    prefs = ('富山県', '石川県', '福井県')
    '''
    このように出力したい
    1.富山県
    2.石川県
    3.福井県
    '''
    for idx in range(len(prefs)):
        print(f'{idx+1}.{prefs[idx]}')

    for idx, pref in enumerate(prefs, start=1):
        print(f'{idx}.{pref}')

if __name__ == "__main__":
    main()