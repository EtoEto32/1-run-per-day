def main():
    tpl_01 = ("Pigeon","Sparrow","Parrot","Owl")
    lst_01 = ["鳩","雀","オウム","フクロウ"]

    #タプルとリストからタプルを
    for bird in zip(tpl_01,lst_01):
        print(bird)
    #dict関数でディクショナリーに
    dict_01 = dict(zip(tpl_01, lst_01))
    print(dict_01)

if __name__ == "__main__":
    main()