records = []

while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        city = input("City: ")
        date = input("Date: ")
        temp = input("Temperature (C): ")
        records.append({"city": city, "date": date, "temp": temp})
        print("Record added.")

    elif choice == "2":
        if not records:
            print("No records.")
        for i, r in enumerate(records, 1):
            print(i, r["city"], r["date"], r["temp"], "C")

    elif choice == "3":
        name = input("City to search: ").lower()
        for r in records:
            if r["city"].lower() == name:
                print(r["city"], r["date"], r["temp"], "C")

    elif choice == "4":
        num = int(input("Record number to delete: "))
        if 1 <= num <= len(records):
            records.pop(num - 1)
            print("Deleted.")
        else:
            print("Invalid number.")

    elif choice == "5":
        break
