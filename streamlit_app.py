import streamlit as st
import math

# Definere brukergrensesnittet med Streamlit
st.title("GAS Transport Kalkulator")

total_gas = st.number_input("Total mengde GAS", min_value=1, value=1000000, step=1)
ship_capacity = st.number_input("Kapasitet per tur", min_value=1, value=120000, step=1)
trip_duration = st.number_input("Varighet av en rundtur (dager)", min_value=1, value=20, step=1)
days_in_year = st.number_input("Antall dager i et år", min_value=1, value=365, step=1)

# Beregner antall nødvendige turer
total_trips = math.ceil(total_gas / ship_capacity)

# Beregner antall mulige turer innenfor et år
max_trips_in_year = days_in_year // trip_duration

if total_trips <= max_trips_in_year:
    st.write("Prosjektet er gjennomførbar innenfor et år. Antall nødvendige turer: ", total_trips)
    st.write("Dette vil ta ", total_trips * trip_duration, " dager.")
else:
    st.write("Prosjektet kan ikke gjennomføres innenfor et år med det gitte skipet. Minst antall turer nødvendig: ", total_trips)
    st.write("Det vil ta ", total_trips * trip_duration, " dager.")
