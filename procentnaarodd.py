def percentage_to_odd(percentage):
    try:
        return 100 / percentage
    except ZeroDivisionError:
        return None

def odd_to_percentage(odd):
    try:
        return 100 / odd
    except ZeroDivisionError:
        return None

def main():
    while True:
        keuze = input("Heb je een percentage of een odd? (P voor percentage, O voor odd, Q om te stoppen): ").strip().upper()

        if keuze == 'Q':
            print("Programma gestopt.")
            break

        if keuze not in ['P', 'O']:
            print("Ongeldige keuze. Typ 'P' voor percentage, 'O' voor odd, of 'Q' om te stoppen.")
            continue

        waarde_input = input("Voer de waarde in: ").strip().replace(",", ".")

        try:
            waarde = float(waarde_input)
        except ValueError:
            print("Ongeldige invoer. Voer een numerieke waarde in.")
            continue

        if keuze == 'P':
            odd = percentage_to_odd(waarde)
            if odd is not None:
                print(f"De odd is: {odd:.4f}")
            else:
                print("Kan niet delen door nul.")
        else:
            percentage = odd_to_percentage(waarde)
            if percentage is not None:
                print(f"Het percentage is: {percentage:.2f}%")
            else:
                print("Kan niet delen door nul.")

        print("-" * 40)

if __name__ == "__main__":
    main()
