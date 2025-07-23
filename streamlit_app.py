import streamlit as st

st.title("🎈 Badanie zaufania do AI")
st.write(
    ""
)

import streamlit as st
import csv
import os
from datetime import datetime

RESPONSES_FILE = "responses.csv"

# Zadanie: Wybór lodówki
question = {
    "title": "Wybierz najlepszą lodówkę",
    "options": {
        "A": "Lodówka A – Tania, mała, energooszczędna",
        "B": "Lodówka B – Średnia półka, duża pojemność, wysoka jakość",
        "C": "Lodówka C – Premium, inteligentna, wysoka cena"
    },
    "ai_recommendation": "B",
    "ai_reason": "AI rekomenduje lodówkę B, ponieważ ma najlepszy stosunek jakości do ceny i wysoką ocenę użytkowników."
}

# Funkcja zapisu
def save_response(data):
    file_exists = os.path.isfile(RESPONSES_FILE)
    with open(RESPONSES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Sesja
if "step" not in st.session_state:
    st.session_state.step = 0

# Krok 0: pytanie główne
if st.session_state.step == 0:
    st.title("Badanie zaufania do AI")
    st.subheader(question["title"])

    for key, desc in question["options"].items():
        st.radio("", [desc], index=0, disabled=True)

    st.markdown(f"**{question['ai_reason']}**")

    choice = st.radio("Którą lodówkę wybierasz?", list(question["options"].keys()))

    if st.button("Dalej"):
        st.session_state.user_choice = choice
        st.session_state.step = 1

# Krok 1: pytania końcowe
elif st.session_state.step == 1:
    st.subheader("Pytania końcowe")

    trust = st.slider("Na ile ufasz rekomendacjom AI?", 1, 5, 3)
    influence = st.slider("Na ile AI wpłynęło na Twój wybór?", 1, 5, 3)
    comfort = st.slider("Na ile czułeś(aś) się komfortowo z decyzją AI?", 1, 5, 3)

    if st.button("Zakończ"):
        response = {
            "timestamp": datetime.now().isoformat(),
            "choice": st.session_state.user_choice,
            "ai_recommendation": question["ai_recommendation"],
            "matches_ai": st.session_state.user_choice == question["ai_recommendation"],
            "trust": trust,
            "influence": influence,
            "comfort": comfort,
        }
        save_response(response)
        st.session_state.step = 2

# Krok 2: podziękowanie
elif st.session_state.step == 2:
    st.success("Dziękujemy za udział w badaniu!")
    st.markdown("Twoje odpowiedzi zostały zapisane.")

