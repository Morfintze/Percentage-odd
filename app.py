import streamlit as st

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

st.title("Percentage ↔ Odd converter")

# Kies conversie
keuze = st.radio("Welke waarde wil je invoeren?", ("Percentage", "Odd"))

# Voer waarde in
waarde_input = st.text_input(f"Voer een {keuze} in:")

if waarde_input:
    # Vervang komma door punt
    waarde_input = waarde_input.replace(",", ".")
    try:
        waarde = float(waarde_input)
        if keuze == "Percentage":
            result = percentage_to_odd(waarde)
            if result is None:
                st.error("Kan niet delen door nul.")
            else:
                st.success(f"Odd is: {result:.4f}")
        else:
            result = odd_to_percentage(waarde)
            if result is None:
                st.error("Kan niet delen door nul.")
            else:
                st.success(f"Percentage is: {result:.2f}%")
    except ValueError:
        st.error("Ongeldige invoer. Voer een numerieke waarde in.")
