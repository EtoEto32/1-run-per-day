def main():
    c_temps = [0, 8, 17, 36, 102, 6, 8, 31, 17]

    temp_set = {(t * 9/5) + 32 for t in c_temps if t < 100}
    print(temp_set)


if __name__ == "__main__":
    main()