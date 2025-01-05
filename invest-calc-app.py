import streamlit as st

# Streamlit Web-App Setup
st.title("Investment Vergleichsrechner")

# Eingabefelder
anlagebetrag = st.number_input("Anlagebetrag (€)", min_value=0.0, step=100.0)
jahresrendite = st.number_input("Jahresrendite (%)", min_value=0.0, step=0.1)
laufzeit = st.number_input("Laufzeit (Jahre)", min_value=1, step=1)
steuersatz = st.number_input("Steuersatz (%)", min_value=0.0, step=0.1)

# Funktion zur Berechnung der Nachsteuer-Rendite
def berechnen(anlagebetrag, jahresrendite, laufzeit, steuersatz):
    endwert_vor_steuer = anlagebetrag * ((1 + (jahresrendite / 100)) ** laufzeit)
    gezahlte_steuer = (endwert_vor_steuer - anlagebetrag) * (steuersatz / 100)
    endwert_nach_steuer = endwert_vor_steuer - gezahlte_steuer
    return endwert_vor_steuer, gezahlte_steuer, endwert_nach_steuer

# Berechnung starten, wenn der Button geklickt wird
if st.button("Berechnen"):
    endwert_vor_steuer, gezahlte_steuer, endwert_nach_steuer = berechnen(anlagebetrag, jahresrendite, laufzeit, steuersatz)
    st.write(f"### Ergebnisse:")
    st.write(f"Endwert vor Steuern: €{endwert_vor_steuer:.2f}")
    st.write(f"Gezahlte Steuern: €{gezahlte_steuer:.2f}")
    st.write(f"Endwert nach Steuern: €{endwert_nach_steuer:.2f}")

# Info-Popup mit Steuerinformationen
if st.button("Info zu Steuerregelungen 2025"):
    info_text = (
        "Aktuelle Steuergesetze in Deutschland für 2025:\n\n"
        "1. **Grundfreibetrag**: 12.096 € (2025), 12.348 € (2026).\n"
        "2. **Kinderfreibetrag**: 9.600 € (2025), 9.756 € (2026).\n"
        "3. **Kindergeld**: 255 € pro Monat (2025), 259 € pro Monat (2026).\n"
        "4. **Einkommensteuertarif**: Anpassung zur Vermeidung der kalten Progression.\n"
        "5. **Solidaritätszuschlag**: Anpassung der Freigrenzen.\n"
        "6. **Kleinunternehmerregelung**: Umsatzgrenze steigt auf 25.000 € (2025).\n"
        "7. **Elektronische Rechnungen**: Einführung der E-Rechnungspflicht.\n"
        "\n\nBitte konsultiere einen Steuerberater für detaillierte Informationen und individuelle Beratung."
    )
    st.info(info_text)
