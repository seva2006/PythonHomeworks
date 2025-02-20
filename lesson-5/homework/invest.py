def invest(amount,rate,years):
    for i in range(1,years+1):
        amount+=rate*amount
        print(f"year {i}: ${amount:.2f}")

amount=float(input("Enter the initial amount: "))
rate=float(input("Enter the annual rate of return: "))
years=int(input("Enter the number of years: "))
invest(amount,rate, years)


