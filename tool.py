ideas = []

while True:
    print("\n1. Idee hinzufügen")
    print("2. Ideen anzeigen")
    print("3. Beenden")

    choice = input("Auswahl: ")

    if choice == "1":
        idea = input("Neue Idee: ")
        ideas.append(idea)
    elif choice == "2":
        print("\nIdeen:")
        for i in ideas:
            print("-", i)
    elif choice == "3":
        break
    else:
        print("Ungültig")
