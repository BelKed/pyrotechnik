while True:
    cables_count = input("Zadaj počet káblikov (5 – 8): ")

    if cables_count.isdigit() and 5 <= int(cables_count) <= 8:
        break

print(cables_count)
