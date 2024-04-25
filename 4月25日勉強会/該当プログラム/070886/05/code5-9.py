def main():
    c_temps = [0, 8, 17, 36, 102]

    temp_dict = {t: (t * 9/5) + 32 for t in c_temps if t < 100}
    print(temp_dict)
    print(temp_dict[8])


if __name__ == "__main__":
    main()