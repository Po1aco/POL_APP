import streamlit as st
import time
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="Polski dla Hiszpanów",
    page_icon="🇵🇱",
    layout="wide"
)

# --- Custom CSS (Embedded) ---
st.markdown("""
<style>
/* Import Gabarito font */
@import url('https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700&display=swap');

/* --- Base Font --- */
html, body, [class*="st-"], .stMarkdown {
    font-family: 'Gabarito', sans-serif !important;
    font-weight: 400;
}

/* --- Background --- */
@keyframes gradientAnimation { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
body::before {
    content: ""; position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: -1;
    background: linear-gradient(135deg, #F0F4F8, #FEF9E7, #F0F4F8); /* Lighter Pastel */
    background-size: 400% 400%; animation: gradientAnimation 30s ease infinite;
}
.stApp { background-color: transparent; }

/* --- Main Content Box Styling --- */
.content-box {
    background-color: rgba(255, 255, 255, 0.9); /* Slightly more opaque */
    border: 1px solid #DDE2E6; /* Softened border */
    border-radius: 18px; padding: 25px 30px; margin-bottom: 30px;
    box-shadow: 0 5px 12px rgba(0, 0, 0, 0.05); /* Slightly deeper shadow */
}

/* --- Individual Question Container --- */
.question-box {
    background-color: rgba(255, 255, 255, 0.75); /* More opaque */
    border: 1px solid #E1E4E8; border-radius: 15px;
    padding: 18px 22px; margin-bottom: 18px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
}
.question-box + .question-box { margin-top: 18px; }

/* --- Headings and Text --- */
h1, h2, h3, h4, h5, h6 {
    color: #262626 !important; /* Title color */
    font-family: 'Gabarito', sans-serif !important; font-weight: 600;
}
.stMarkdown, p, li {
   color: #212121; /* Darker Gray for readability */
   line-height: 1.7; font-family: 'Gabarito', sans-serif !important;
}
strong { font-weight: 600; color: #262626 !important; }
code {
    background-color: rgba(235, 237, 240, 0.8); /* Lighter grey */
    padding: 0.2em 0.4em; margin: 0; font-size: 85%;
    border-radius: 6px; border: 1px solid #D1D5DB;
    font-family: monospace; color: #1F2937; /* Darker code text */
}

/* --- Button Styling --- */
.stButton>button {
    border: 1px solid #B0BEC5; border-radius: 12px; /* Slightly darker border */
    padding: 8px 18px; background-color: #FFFFFF; color: #37474F; /* Darker text */
    transition: all 0.2s ease; font-family: 'Gabarito', sans-serif !important;
    font-weight: 500; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.stButton>button:hover {
    background-color: #ECEFF1; color: #1A237E; border-color: #90A4AE; /* Indigo text on hover */
    box-shadow: 0 3px 6px rgba(0,0,0,0.08); transform: translateY(-1px);
}
.stButton>button:active { transform: translateY(0px); box-shadow: 0 1px 2px rgba(0,0,0,0.05); }

/* --- Input/Widget Styling --- */
.stRadio > label, .stTextInput > label, .stSelectbox > label {
    font-weight: 500; color: #262626; font-family: 'Gabarito', sans-serif !important; padding-bottom: 8px;
}
div[data-baseweb="input"] input, div[data-baseweb="select"] div {
   border-radius: 8px !important; border-color: #B0BEC5 !important; /* Match button border */
   background-color: rgba(255, 255, 255, 0.95); font-family: 'Gabarito', sans-serif !important;
}

/* --- Radio Button Styling --- */
div[data-baseweb="radio"] > label {
    background-color: rgba(255, 255, 255, 0.8); border: 1px solid #CFD8DC; /* Slightly lighter border */
    border-radius: 25px; padding: 10px 15px 10px 10px !important; margin: 5px 3px !important;
    transition: all 0.2s ease-in-out; display: flex !important; align-items: center;
    width: auto; min-width: 80px; justify-content: flex-start; color: #37474F; /* Match button text */
}
div[data-baseweb="radio"] input[type="radio"]:checked + div + label {
    background-color: #0D3C70 !important; border-color: #0D3C70 !important;
    color: white !important; box-shadow: 0 3px 6px rgba(13, 60, 112, 0.2);
}
div[data-baseweb="radio"] > label:hover { border-color: #78909C; background-color: #F5F5F5; }
div[data-baseweb="radio"] input[type="radio"]:checked + div + label:hover { background-color: #1C4B82 !important; border-color: #1C4B82 !important; }
.stRadio[role="radiogroup"] > div { display: inline-block; margin-right: 5px; }

/* --- Sidebar Styling --- */
.stSidebar {
    background-color: rgba(253, 236, 236, 0.92); /* #FDECEC More opaque */
    backdrop-filter: blur(6px); border-right: 1px solid rgba(220, 200, 200, 0.6);
}
/* INCREASED CONTRAST FOR SIDEBAR TEXT */
.stSidebar .stMarkdown, .stSidebar .stRadio > label { color: #3E2723 !important; /* Dark Brown */ font-family: 'Gabarito', sans-serif !important; }
.stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar strong { color: #1B0000 !important; /* Very Dark Brown/Black */ font-family: 'Gabarito', sans-serif !important; font-weight: 600; }
.stSidebar .stButton>button {
    font-family: 'Gabarito', sans-serif !important; font-weight: 500;
    border: 1px solid #8D6E63; /* Brown border */ background-color: rgba(255, 255, 255, 0.85);
    color: #3E2723; /* Dark Brown text */ border-radius: 10px;
}
.stSidebar .stButton>button:hover { background-color: #A1887F; color: #FFFFFF; border-color: #FFFFFF; } /* White text on brown hover */

/* --- Alert box styling --- */
.stAlert {
    background-color: rgba(235, 235, 235, 0.85); border: 1px solid #C5C5C5; border-radius: 15px; padding: 15px 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); font-family: 'Gabarito', sans-serif !important; color: #212121; /* Darker text */
}
.stAlert.stSuccess { background-color: rgba(220, 245, 220, 0.9); border-color: #9CCC65; } /* Brighter Green Border */
.stAlert.stWarning { background-color: rgba(255, 240, 220, 0.9); border-color: #FFB74D; } /* Brighter Orange Border */
.stAlert.stError   { background-color: rgba(255, 225, 225, 0.9); border-color: #E57373; } /* Brighter Red Border */

</style>
""", unsafe_allow_html=True)


# --- Session State Initialization --- (Keep as is)
if 'page' not in st.session_state: st.session_state.page = "Introduction"
if 'feedback' not in st.session_state: st.session_state.feedback = {}

# --- Navigation --- (Keep as is)
with st.sidebar:
    st.title("🇵🇱 Nawigacja 🇪🇸")
    pages = ["Introduction", "Alphabet", "Vocabulary & Phrases", "Grammar Focus", "Pronunciation Practice", "Dialogues & Context"]
    page_emojis = ["👋", "🔤", "🗣️", "✍️", "👂", "💬"]
    for page, emoji in zip(pages, page_emojis):
        if st.button(f"{emoji} {page}"): st.session_state.page = page; st.session_state.feedback = {}; st.rerun()
    st.markdown("---"); st.info("Lekcja oparta na PDF.")

# --- Main Content Area with Padding --- (Keep as is)
body_col_left, body_col_main, body_col_right = st.columns([1, 5, 1])

with body_col_main:

    # == INTRODUCTION == (Keep as is)
    if st.session_state.page == "Introduction":
        st.title("👋 Witaj! ¡Bienvenido/a al Polaco!")
        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.header("Lekcja 0/1: Pierwsze kroki / Primeros pasos")
             st.markdown("""
                Witaj w interaktywnej lekcji języka polskiego dla osób mówiących po hiszpańsku!
                ¡Bienvenido/a a esta lección interactiva de polaco para hispanohablantes!

                **Język polski (El idioma polaco):**
                *   Jest językiem zachodniosłowiańskim.
                *   Używa alfabetu łacińskiego z dodatkowymi znakami.
                *   Ma **7 przypadków gramatycznych** (końcówki słów się zmieniają!).
                *   Posiada **3 rodzaje** (masculino, femenino, neutro) + specjalne formy liczby mnogiej.
                *   **Nie ma rodzajników** (a/an, the).
                *   Akcent pada zazwyczaj na **przedostatnią sylabę**.

                **Cele tej lekcji (Objetivos):**
                1.  Poznać polski alfabet i wymowę.
                2.  Nauczyć się podstawowych powitań i przedstawiania się.
                3.  Zrozumieć czasowniki: *mówić*, *nazywać się*, *mieć*.
                4.  Zobaczyć różnice i podobieństwa do hiszpańskiego.

                Zaczynajmy! ¡Empecemos!
            """)
             st.markdown('</div>', unsafe_allow_html=True)
        if st.button("➡️ Dalej: Alfabet"): st.session_state.page = "Alphabet"; st.rerun()

    # == ALPHABET == (Keep as is)
    elif st.session_state.page == "Alphabet":
        st.title("🔤 Polski Alfabet / El Alfabeto Polaco")
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("Polski alfabet z przykładami i wymową (uproszczoną).")
            st.markdown("""
            | Litera | Nazwa | Wymowa (IPA approx.) | Przykład | Nota dla Hiszpanów |
            |---|---|---|---|---|
            | **A a** | a | [a] | **a**dres | Como 'a' española. |
            | **Ą ą** | o~ | [ɔ̃] (nasal) | m**ą**ka | **¡Nasal!** No existe en español. |
            | **B b** | be | [b] | **b**alkon | Como 'b'. |
            | **C c** | ce | [ts] | **c**ena | Como 'ts'. **¡No 's' ni 'k'!** |
            | **Ć ć** | cie | [tɕ] | **ć**ma | 'ch' suave/palatal. No existe. |
            | **Ch ch**| ce ha | [x] | **ch**oroba | **Como 'j' española**. |
            | **Cz cz**| cze | [tʂ] | **cz**ekolada | **'ch' inglesa**. Más fuerte. |
            | **D d** | de | [d] | **d**ata | Como 'd'. |
            | **Dz dz**| dze | [dz] | **dz**won | Sonido sonoro 'ts'. |
            | **Dź dź**| dzie | [dʑ] | **dź**więk | 'j' inglesa suave/palatal. |
            | **Dż dż**| dże | [dʐ] | **dż**em | 'j' inglesa ('judge'). |
            | **E e** | e | [ɛ] | **e**fekt | Como 'e' abierta. |
            | **Ę ę** | e~ | [ɛ̃] (nasal) | r**ę**ka | **¡Nasal!** No existe en español. |
            | **F f** | ef | [f] | **f**irma | Como 'f'. |
            | **G g** | gie | [ɡ] | **g**olf | Como 'g' en 'gato'. **Siempre fuerte.** |
            | **H h** | ha | [x] | **h**otel | **Como 'j' española**. Igual que 'ch'. |
            | **I i** | i | [i] | **i**gnorant | Como 'i'. Suaviza cons. anterior. |
            | **J j** | jot | [j] | **j**oga | Como 'y' en 'yo'. |
            | **K k** | ka | [k] | **k**alkulator | Como 'k'. |
            | **L l** | el | [l] | **l**ekcja | Como 'l'. |
            | **Ł ł** | eł | [w] | **ł**adny | **¡Importante! Como 'w' inglesa**. |
            | **M m** | em | [m] | **m**ama | Como 'm'. |
            | **N n** | en | [n] | **n**ormalny | Como 'n'. |
            | **Ń ń** | eń | [ɲ] | ko**ń** | **Como 'ñ' española.** |
            | **O o** | o | [ɔ] | **o**ferta | Como 'o' abierta. |
            | **Ó ó** | u | [u] | **ó**sma | **¡Importante! Suena como 'u'.** |
            | **P p** | pe | [p] | **p**rogram | Como 'p'. |
            | **R r** | er | [r] | **r**uiny | Vibrante simple ('pero'). |
            | **Rz rz**| żet | [ʐ]/[ʂ] | **rz**eka | **Como 'ż'.** ('j' francesa / 'sh'). |
            | **S s** | es | [s] | **s**top | Como 's' (siempre sorda). |
            | **Ś ś** | eś | [ɕ] | **ś**roda | 'sh' suave/palatal. No existe. |
            | **Sz sz**| esz | [ʂ] | **sz**ok | **'sh' inglesa**. |
            | **T t** | te | [t] | **t**enis | Como 't'. |
            | **U u** | u | [u] | **u**waga | Como 'u'. Mismo sonido que 'Ó ó'. |
            | **W w** | wu | [v] | **w**ulkan | **Como 'v' inglesa/francesa.** Labiodental. |
            | **Y y** | igrek | [ɨ] | s**y**stem | **¡Sonido difícil!** No existe. Más atrás que 'i'. |
            | **Z z** | zet | [z] | **z**oo | Como 's' sonora ('mismo', 'zzz'). |
            | **Ź ź** | ziet | [ʑ] | **ź**le | 'j' francesa suave/palatal. |
            | **Ż ż** | żet | [ʐ] | **ż**aba | **Como 'rz'.** ('j' francesa). |
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("👂 Ćwiczenie Wymowy / Ejercicio de Pronunciación")
        st.markdown("Wybierz słowo, które słyszysz (symulacja).")
        pairs = { "s / sz / ś": (["stop", "szok", "środa"], 2), "c / cz / ć": (["cena", "czekolada", "ćma"], 1), "z / rz / ź": (["zoo", "rzeka", "źle"], 0), "l / ł": (["lekcja", "ładny"], 1), "i / y": (["miły", "myły"], 0) }
        exercise_key = "alphabet_pronunciation"; q_num = 1
        if exercise_key not in st.session_state.feedback: st.session_state.feedback[exercise_key] = {}
        for key, (options, correct_index) in pairs.items():
             st.markdown('<div class="question-box">', unsafe_allow_html=True)
             q_key = f"{exercise_key}_{q_num}"; st.markdown(f"**{q_num}. Dźwięk: {key}**"); st.caption(f"🎧 *Wyobraź sobie, że słyszysz...*")
             current_choice_index = None
             if q_key in st.session_state.feedback and st.session_state.feedback[q_key] is not None and 'user_choice' in st.session_state.feedback[q_key]:
                  try: current_choice_index = options.index(st.session_state.feedback[q_key]['user_choice'])
                  except ValueError: current_choice_index = None
             user_choice = st.radio(f"Słowo:", options, key=q_key, index=current_choice_index, label_visibility="visible", horizontal=True)
             if q_key not in st.session_state.feedback: st.session_state.feedback[q_key] = {}
             if user_choice is not None:
                 is_correct = options.index(user_choice) == correct_index
                 st.session_state.feedback[q_key]['user_choice'] = user_choice; st.session_state.feedback[q_key]['is_correct'] = is_correct
                 if is_correct: st.success("✅ Dobrze!")
                 else: st.error(f"❌ Poprawnie: '{options[correct_index]}'.")
             st.markdown('</div>', unsafe_allow_html=True)
             q_num += 1
        if st.button("➡️ Dalej: Słownictwo"): st.session_state.page = "Vocabulary & Phrases"; st.rerun()

    # == VOCABULARY & PHRASES == (Logic including corrected try/except blocks and fill-in fix remains the same)
    elif st.session_state.page == "Vocabulary & Phrases":
        st.title("🗣️ Słownictwo i Zwroty")
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("Pozdrowienia / Saludos"); st.markdown("""*   **Dzień dobry!** - B. días/tardes (F) | *   **Cześć!** - Hola/Adiós (Inf) | *   **Dobry wieczór!** - B. noches (F) | *   **Dobranoc!** - B. noches (parting) | *   **Do widzenia!** - Adiós (F) | *   **Na razie!** - H. luego (Inf)""")
            st.subheader("Przedstawianie się / Presentaciones"); st.markdown("""*   **Jak się nazywasz?** - ¿Cómo te llamas? (Inf) | *   **Jak pan/pani się nazywa?** - ¿Cómo se llama Ud.? (F) | *   **Nazywam się...** - Me llamo... | *   **Jak masz/ma na imię?** - ¿Cuál es tu/su nombre? | *   **Mam na imię...** - Mi nombre es... | *   **Miło mi.** - Encantado/a.""")
            st.subheader("Zaimki Osobowe / Pronombres"); st.markdown("""*   ja - yo | my - nosotros | *   ty - tú | wy - vosotros | *   on - él | oni - ellos (con hombres) | *   ona - ella | one - ellas/ellos (sin hombres/cosas) | *   ono - ello | *   Pan/Pani - Ud. | Państwo - Uds.""")
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("📝 Ćwiczenia / Ejercicios")
        exercise_key = "vocab_phrases";
        if exercise_key not in st.session_state.feedback: st.session_state.feedback[exercise_key] = {}

        # --- Exercise 1: Matching ---
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**1. Dopasuj polskie zwroty do hiszpańskich.**")
        q1_key = f"{exercise_key}_q1"; match_options = { "Dzień dobry!": "¡Buenos días/tardes! (Formal)", "Jak się nazywasz?": "¿Cómo te llamas? (Informal)", "Do widzenia!": "¡Adiós! (Formal)", "Miło mi.": "Encantado/a.", "Cześć!": "¡Hola! / ¡Adiós! (Informal)"}
        polish_phrases = list(match_options.keys()); spanish_translations = list(match_options.values())
        if q1_key not in st.session_state: st.session_state[q1_key] = {}
        if 'shuffled_spanish' not in st.session_state[q1_key]: st.session_state[q1_key]['shuffled_spanish'] = random.sample(spanish_translations, len(spanish_translations))
        if 'user_matches' not in st.session_state[q1_key]: st.session_state[q1_key]['user_matches'] = {phrase: "" for phrase in polish_phrases}
        shuffled_spanish = st.session_state[q1_key]['shuffled_spanish']
        cols1 = st.columns(2)
        with cols1[0]:
            for i, phrase in enumerate(polish_phrases):
                current_selection = st.session_state[q1_key]['user_matches'].get(phrase, "")
                sel_index = 0
                try: sel_index = ([""] + shuffled_spanish).index(current_selection)
                except ValueError: sel_index = 0
                st.session_state[q1_key]['user_matches'][phrase] = st.selectbox(f"{i+1}. {phrase}", options=[""] + shuffled_spanish, key=f"{q1_key}_{i}", index=sel_index, label_visibility="visible")
        with cols1[1]: st.markdown("**Opcje:**"); st.table([[trans] for trans in shuffled_spanish])
        if st.button("Sprawdź dopasowanie", key=f"{q1_key}_check"):
            correct_count_match = 0; all_correct_match = True; feedback_match_html = "<ul>"; user_matches = st.session_state[q1_key]['user_matches']
            for polish, user_spanish in user_matches.items():
                correct_spanish = match_options[polish]
                if user_spanish == correct_spanish: feedback_match_html += f"<li>'{polish}' = '{user_spanish}' ✅"; correct_count_match += 1
                elif not user_spanish: feedback_match_html += f"<li>'{polish}' = ? (Nie wybrano)"; all_correct_match = False
                else: feedback_match_html += f"<li>'{polish}' = <span style='color:red;'>'{user_spanish}'</span> ❌ (Popr: '{correct_spanish}')"; all_correct_match = False
            feedback_match_html += "</ul>"; st.markdown(feedback_match_html, unsafe_allow_html=True)
            st.session_state.feedback[exercise_key][q1_key] = all_correct_match
            if all_correct_match: st.success("🎉 Poprawnie!")
            else: st.warning(f"Masz {correct_count_match} z {len(polish_phrases)} poprawnych par.")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Exercise 2: Fill-in-the-blanks ---
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**2. Uzupełnij dialog wyrazami z ramki.**")
        q2_key = f"{exercise_key}_q2"; words_bank = ["Miło", "pan", "Nazywam się", "pani", "dobry"]; solution = ["dobry", "pani", "dobry", "Nazywam się", "pan", "Miło"]
        st.info(f"Ramka: `{', '.join(words_bank)}`");
        if q2_key not in st.session_state: st.session_state[q2_key] = [""] * len(solution)
        st.markdown("**Dialog:**")
        st.session_state[q2_key][0] = st.text_input(f"A: Dzień ______! [0]", value=st.session_state[q2_key][0], key=f"{q2_key}_0")
        st.session_state[q2_key][1] = st.text_input(f"A: ... Jak ______ się nazywa? [1]", value=st.session_state[q2_key][1], key=f"{q2_key}_1")
        st.session_state[q2_key][2] = st.text_input(f"B: Dzień ______! [2]", value=st.session_state[q2_key][2], key=f"{q2_key}_2")
        st.session_state[q2_key][3] = st.text_input(f"B: ... ______ Piotr Nowicki. [3]", value=st.session_state[q2_key][3], key=f"{q2_key}_3")
        st.session_state[q2_key][4] = st.text_input(f"B: ... Jak ______ się nazywa? [4]", value=st.session_state[q2_key][4], key=f"{q2_key}_4")
        st.markdown("<p style='margin-left: 10px;'>A: Anna Kamińska.</p>", unsafe_allow_html=True)
        st.session_state[q2_key][5] = st.text_input(f"B: ______ mi. [5]", value=st.session_state[q2_key][5], key=f"{q2_key}_5")
        if st.button("Sprawdź Fill-in", key=f"{q2_key}_check"):
            correct_count = 0; all_correct = True
            # --- CORRECTED list construction ---
            user_answers = [st.session_state[q2_key][i].strip() for i in range(len(solution))]
            sol = solution
            filled_dialog = [
                f"A: Dzień {'<span style=\'color:green; font-weight:600;\'>' + user_answers[0] + '</span>' if user_answers[0].lower() == sol[0].lower() else '<span style=\'color:red;\'>' + user_answers[0] + '</span>' + f' ({sol[0]})'}! Jak {'<span style=\'color:green; font-weight:600;\'>' + user_answers[1] + '</span>' if user_answers[1].lower() == sol[1].lower() else '<span style=\'color:red;\'>' + user_answers[1] + '</span>' + f' ({sol[1]})'} się nazywa?",
                f"B: Dzień {'<span style=\'color:green; font-weight:600;\'>' + user_answers[2] + '</span>' if user_answers[2].lower() == sol[2].lower() else '<span style=\'color:red;\'>' + user_answers[2] + '</span>' + f' ({sol[2]})'}! {'<span style=\'color:green; font-weight:600;\'>' + user_answers[3] + '</span>' if user_answers[3].lower() == sol[3].lower() else '<span style=\'color:red;\'>' + user_answers[3] + '</span>' + f' ({sol[3]})'} Piotr Nowicki. Jak {'<span style=\'color:green; font-weight:600;\'>' + user_answers[4] + '</span>' if user_answers[4].lower() == sol[4].lower() else '<span style=\'color:red;\'>' + user_answers[4] + '</span>' + f' ({sol[4]})'} się nazywa?",
                "<span style='margin-left: 10px;'>A: Anna Kamińska.</span>",
                f"B: {'<span style=\'color:green; font-weight:600;\'>' + user_answers[5] + '</span>' if user_answers[5].lower() == sol[5].lower() else '<span style=\'color:red;\'>' + user_answers[5] + '</span>' + f' ({sol[5]})'} mi."
            ]
            # --- END CORRECTION ---
            for i in range(len(solution)):
                if user_answers[i].lower() == solution[i].lower(): correct_count +=1
                else: all_correct = False
            st.markdown("<h5>Wyniki:</h5>" + "<br>".join(filled_dialog), unsafe_allow_html=True)
            st.session_state.feedback[exercise_key][q2_key] = all_correct
            if all_correct: st.success("🎉 Poprawnie!")
            else: st.warning(f"Masz {correct_count} z {len(solution)} poprawnych.")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Exercise 3: Formal/Informal ---
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**3. Formalnie czy nieformalnie?**")
        q3_key = f"{exercise_key}_q3"; scenarios = { "Spotykasz profesora": "Dzień dobry!", "Witasz się z kolegą": "Cześć!", "Żegnasz się z dyrektorem": "Do widzenia!", "Mówisz 'do zobaczenia' przyjaciółce": "Na razie!"}
        scenario_keys = list(scenarios.keys())
        if q3_key not in st.session_state: st.session_state[q3_key] = {'selected_scenario': None, 'user_choice': None}
        selected_scenario = st.selectbox("Wybierz sytuację:", options=[""] + scenario_keys, key=f"{q3_key}_select",
            index=0 if st.session_state[q3_key]['selected_scenario'] is None else ([""] + scenario_keys).index(st.session_state[q3_key]['selected_scenario']),
            on_change=lambda: st.session_state[q3_key].update({'user_choice': None}) )
        st.session_state[q3_key]['selected_scenario'] = selected_scenario if selected_scenario else None
        if selected_scenario:
             correct_greeting = scenarios[selected_scenario]; greeting_options = ["Dzień dobry!", "Cześć!", "Do widzenia!", "Na razie!"]
             options_for_radio = list(set(random.sample(greeting_options, 3) + [correct_greeting])); random.shuffle(options_for_radio)
             current_choice_q3 = st.session_state[q3_key].get('user_choice')
             # --- CORRECTED try/except block ---
             radio_index_q3 = None
             if current_choice_q3 in options_for_radio:
                 try: radio_index_q3 = options_for_radio.index(current_choice_q3)
                 except ValueError: radio_index_q3 = None
             # --- END CORRECTION ---
             user_choice = st.radio("Co powiesz?", options=options_for_radio, key=f"{q3_key}_radio", index=radio_index_q3, horizontal=True)
             st.session_state[q3_key]['user_choice'] = user_choice
             if user_choice is not None:
                 is_correct_q3 = (user_choice == correct_greeting); st.session_state.feedback[exercise_key][q3_key] = is_correct_q3
                 if is_correct_q3: st.success("✅ Zgadza się!")
                 else: st.error(f"❌ Lepiej: '{correct_greeting}'.")
        elif f"{q3_key}_select" in st.session_state and not selected_scenario: st.session_state.feedback[exercise_key].pop(q3_key, None)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("➡️ Dalej: Gramatyka"): st.session_state.page = "Grammar Focus"; st.rerun()

    # == GRAMMAR FOCUS ==
    elif st.session_state.page == "Grammar Focus":
        st.title("✍️ Gramatyka / Gramática")
        st.info("💡 Pamiętaj: *Pan/Pani* używają formy czasownika jak *on/ona/ono*.")
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Czasownik *mówić* (hablar)")
        st.markdown("| Osoba | Czasownik | Tłum. ||---|---|---| | ja | mów**ię** | hablo | | ty | mów**isz** | hablas | | on/ona/ono | mów**i** | habla | | **Pan/Pani** | mów**i** | habla | | my | mów**imy** | hablamos | | wy | mów**icie** | habláis | | oni/one | mów**ią** | hablan | | **Państwo** | mów**ią** | hablan |")
        st.markdown("**Przykład:** *Ona mówi po francusku. Ja nie mówię.*")
        st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("Ćwiczenie: MÓWIĆ")
        exercise_key = "grammar_mowic";
        if exercise_key not in st.session_state: st.session_state[exercise_key] = {}
        # Don't need 'inputs' sub-dict if reading directly from widget state
        # if 'inputs' not in st.session_state[exercise_key]: st.session_state[exercise_key]['inputs'] = {} # REMOVE or comment out
        mowic_sentences = [ ("Czy ______ po polsku? (ty)", ["mówisz"]), ("______ po angielsku. (my)", ["mówimy"]), ("Oni nie ______ po francusku, ale ______ po polsku. (oni / oni)", ["mówią", "mówią"]), ("On ______ trochę po rosyjsku, ale ja nie ______. (on / ja)", ["mówi", "mówię"]), ("Czy ______ po niemiecku? (wy)", ["mówicie"]), ("One nie ______ po hiszpańsku. (one)", ["mówią"]), ("Czy ona ______ po polsku?", ["mówi"]), ("Nie ______ po włosku. (ja)", ["mówię"]) ]

        # Initialize state for widgets if not present
        for i in range(len(mowic_sentences)):
             q_key = f"{exercise_key}_{i}"
             num_blanks = mowic_sentences[i][0].count("______")
             if num_blanks == 1:
                  if q_key not in st.session_state: st.session_state[q_key] = ""
             elif num_blanks == 2:
                  if f"{q_key}_a" not in st.session_state: st.session_state[f"{q_key}_a"] = ""
                  if f"{q_key}_b" not in st.session_state: st.session_state[f"{q_key}_b"] = ""


        # Display inputs, reading value directly from widget state key
        for i, (sentence, correct_forms) in enumerate(mowic_sentences):
            st.markdown('<div class="question-box">', unsafe_allow_html=True)
            q_key = f"{exercise_key}_{i}"; num_blanks = sentence.count("______"); prompt = sentence.replace("______", "_______")
            if num_blanks == 1:
                # --- CORRECTED: Use widget key for value ---
                st.text_input(f"{i+1}. {prompt}",
                              value=st.session_state.get(q_key, ""), # Read from widget key
                              key=q_key, # Assign unique key to widget
                              placeholder="Wpisz")
            elif num_blanks == 2:
                 cols_mowic = st.columns(2);
                 with cols_mowic[0]:
                     # --- CORRECTED: Use widget key for value ---
                     st.text_input(f"{i+1}a. {prompt} (1)",
                                    value=st.session_state.get(f"{q_key}_a", ""), # Read from widget key
                                    key=f"{q_key}_a", # Assign unique key
                                    placeholder="Forma 1")
                 with cols_mowic[1]:
                     # --- CORRECTED: Use widget key for value ---
                     st.text_input(f"{i+1}b. {prompt} (2)",
                                    value=st.session_state.get(f"{q_key}_b", ""), # Read from widget key
                                    key=f"{q_key}_b", # Assign unique key
                                    placeholder="Forma 2")
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Sprawdź MÓWIĆ", key=f"{exercise_key}_check"):
            all_correct_mowic = True; feedback_html_mowic = "<ul>"
            for i, (sentence, correct_forms_list) in enumerate(mowic_sentences):
                q_key = f"{exercise_key}_{i}"
                num_blanks = sentence.count("______")
                user_answers = []
                # --- CORRECTED: Read directly from widget state ---
                if num_blanks == 1:
                    user_answers.append(st.session_state.get(q_key, "").strip().lower())
                elif num_blanks == 2:
                    user_answers.append(st.session_state.get(f"{q_key}_a", "").strip().lower())
                    user_answers.append(st.session_state.get(f"{q_key}_b", "").strip().lower())
                # --- END CORRECTION ---

                correct_forms_list_lower = [f.lower() for f in correct_forms_list]
                sentence_display = sentence; correct_in_sentence = True
                # Feedback generation logic remains the same...
                for j in range(len(correct_forms_list_lower)): user_ans = user_answers[j]; correct_ans = correct_forms_list_lower[j];
                if user_ans == correct_ans: replacement = f"<span style='color:green; font-weight:600;'>{user_ans}</span>"
                else: replacement = f"<span style='color:red;'>{user_ans}</span> (Popr: {correct_ans})"; correct_in_sentence = False; all_correct_mowic = False
                sentence_display = sentence_display.replace("______", f"__PLACEHOLDER_{j}__", 1)
                for j in range(len(correct_forms_list_lower)): user_ans = user_answers[j]; correct_ans = correct_forms_list_lower[j];
                if user_ans == correct_ans: replacement = f"<span style='color:green; font-weight:600;'>{user_ans}</span>"
                else: replacement = f"<span style='color:red;'>{user_ans}</span> (Popr: {correct_ans})";
                sentence_display = sentence_display.replace(f"__PLACEHOLDER_{j}__", replacement)
                feedback_html_mowic += f"<li>{sentence_display} {'✅' if correct_in_sentence else '❌'}</li>"
            feedback_html_mowic += "</ul>"; st.markdown(feedback_html_mowic, unsafe_allow_html=True)
            st.session_state.feedback[exercise_key] = {'all_correct': all_correct_mowic}
            if all_correct_mowic: st.success("🎉 Świetnie!")
            else: st.warning("Popraw błędy.")

        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Inne Czasowniki i Notatki") # Content... (Keep as is)
        cols_verbs = st.columns(2)
        with cols_verbs[0]: st.markdown("**Nazywać się (llamarse)**"); st.markdown("""(ja) nazywam się | (ty) nazywasz się | (on/ona/ono) nazywa się | (my) nazywamy się | (wy) nazywacie się | (oni/one) nazywają się""")
        with cols_verbs[1]: st.markdown("**Mieć (tener)**"); st.markdown("""(ja) mam | (ty) masz | (on/ona/ono) ma | (my) mamy | (wy) macie | (oni/one) mają""")
        st.markdown("**Rodzaj i Zaimki:** *on, ona, ono* (sing.); *oni* (pl. con hombres), *one* (pl. sin hombres/cosas).")
        st.warning("**Przypadki (Casos):** Polski ma 7! Końcówki słów się zmieniają. Uczymy się stopniowo.")
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("➡️ Dalej: Wymowa"): st.session_state.page = "Pronunciation Practice"; st.rerun()

    # == PRONUNCIATION PRACTICE == (Logic including corrected try/except blocks remains the same)
    elif st.session_state.page == "Pronunciation Practice":
        st.title("👂 Ćwiczenia Wymowy")
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("Skupmy się na dźwiękach trudnych dla Hiszpanów.")
        sound_pairs = { "S vs SZ vs Ś": ([("sok","[s]"),("szok","[ʂ] 'sh'"),("siwy","[ɕ] soft 'sh'")],1), "C vs CZ vs Ć": ([("co","[ts]"),("czekam","[tʂ] 'ch'"),("ciocia","[tɕ] soft 'ch'")],0), "Z vs Ż/RZ vs Ź": ([("zero","[z]"),("rzeka","[ʐ] Fr 'j'"),("źle","[ʑ] soft Fr 'j'")],2), "L vs Ł": ([("lato","[l]"),("łatwo","[w]")],1), "I vs Y": ([("biły","[bʲi]"),("były","[bɨ] difficult")],1) }
        exercise_key = "pronunciation_pairs"; q_num_pron = 1
        if exercise_key not in st.session_state.feedback: st.session_state.feedback[exercise_key] = {}
        st.subheader("Rozróżnianie dźwięków (symulacja)")
        for key, (options_with_hints, correct_index) in sound_pairs.items():
            st.markdown('<div class="question-box">', unsafe_allow_html=True)
            q_key = f"{exercise_key}_{q_num_pron}"; st.markdown(f"**{q_num_pron}. Dźwięki: {key}**"); st.caption(f"🎧 *Wyobraź sobie, że słyszysz...*")
            options = [opt[0] for opt in options_with_hints]; hints_str = " / ".join([f"'{opt[0]}' ({opt[1]})" for opt in options_with_hints]); st.caption(f"Opcje: {hints_str}")
            if q_key not in st.session_state.feedback[exercise_key]: st.session_state.feedback[exercise_key][q_key] = {'user_choice': None}
            current_choice_pron = st.session_state.feedback[exercise_key][q_key]['user_choice']
            # --- CORRECTED try/except block ---
            index_pron = None
            if current_choice_pron in options:
                try: index_pron = options.index(current_choice_pron)
                except ValueError: index_pron = None
            # --- END CORRECTION ---
            user_choice = st.radio("Które słowo?", options, key=q_key, index=index_pron, label_visibility="collapsed", horizontal=True)
            st.session_state.feedback[exercise_key][q_key]['user_choice'] = user_choice
            if user_choice is not None:
                is_correct_pron = (options.index(user_choice) == correct_index); st.session_state.feedback[exercise_key][q_key]['is_correct'] = is_correct_pron
                if is_correct_pron: st.success("✅ Dobrze!")
                else: st.error(f"❌ Poprawnie: '{options[correct_index]}'.")
            st.markdown('</div>', unsafe_allow_html=True)
            q_num_pron += 1
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Czytanie na głos / Leer en voz alta"); st.markdown("Spróbuj przeczytać te słowa.")
        words_to_read = ["Szczecin", "chrząszcz", "źdźbło", "pięćdziesiąt", "dziękuję", "Warszawa", "Wrocław", "Kraków", "Łódź", "Gdańsk"]
        st.table([[word] for word in words_to_read]); st.info("💡 Nagraj siebie i porównaj!")
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("➡️ Dalej: Dialogi"): st.session_state.page = "Dialogues & Context"; st.rerun()

    # == DIALOGUES & CONTEXT == (Logic including corrected try/except blocks remains the same)
    elif st.session_state.page == "Dialogues & Context":
        st.title("💬 Dialogi i Kontekst")
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Dialog 1: Formalne przedstawienie")
        st.markdown("""**Adam:** Dzień dobry! Nazywam się Adam Kowalski. A pani? \n**Ewa:** Dzień dobry! Nazywam się Ewa Nowak. \n**Adam:** Miło mi. \n**Ewa:** Miło mi.""")
        st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("Ćwiczenia / Ejercicios")

        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**Dialog 2: Nieformalne (Uzupełnij)**")
        exercise_key = "dialogue_informal"; q_key = f"{exercise_key}_fill"
        if q_key not in st.session_state: st.session_state[q_key] = ["", "", ""]
        words_bank_d2 = ["Nazywam się", "Jak", "Miło mi"]; solution_d2 = ["Nazywam się", "jak", "Miło mi"]
        st.info(f"Użyj: `{', '.join(words_bank_d2)}`")
        st.session_state[q_key][0] = st.text_input("Marek: Cześć! ______ Marek Mazur. [0]", value=st.session_state[q_key][0], key=f"{q_key}_0")
        st.session_state[q_key][1] = st.text_input("Marek: ... A ty, ______ się nazywasz? [1]", value=st.session_state[q_key][1], key=f"{q_key}_1")
        st.markdown("<p style='margin-left: 10px;'>Julia: Cześć! Nazywam się Julia Lewandowska.</p>", unsafe_allow_html=True)
        st.session_state[q_key][2] = st.text_input("Marek: ______. [2]", value=st.session_state[q_key][2], key=f"{q_key}_2")
        if st.button("Sprawdź Dialog 2", key=f"{q_key}_check"):
             correct_d2 = True; feedback_d2_html = "Wyniki:<ul>"
             user_answers = [st.session_state[q_key][i].strip() for i in range(len(solution_d2))] # Get user answers
             for i in range(len(solution_d2)): user_ans = user_answers[i]; correct_ans = solution_d2[i];
             if user_ans.lower() == correct_ans.lower(): feedback_d2_html += f"<li>Luka {i}: <span style='color:green;'>{user_ans}</span> ✅</li>"
             else: feedback_d2_html += f"<li>Luka {i}: <span style='color:red;'>{user_ans}</span> ❌ (Popr: {correct_ans})</li>"; correct_d2 = False
             feedback_d2_html += "</ul>"; st.markdown(feedback_d2_html, unsafe_allow_html=True)
             st.session_state.feedback[exercise_key] = {'overall_correct': correct_d2}
             if correct_d2: st.success("🎉 Super!")
             else: st.warning("Popraw błędy.")
        st.markdown('</div>', unsafe_allow_html=True)


        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**Pytanie o innych (Wybierz zaimek)**")
        exercise_key = "dialogue_others"; q_key_pronoun = f"{exercise_key}_pronoun"
        if q_key_pronoun not in st.session_state: st.session_state[q_key_pronoun] = {'selected_person': None, 'user_choice': None}
        people = { "Andrzej Wajda (m)": "on", "Agnieszka & Urszula R. (ż)": "one", "Andrzej & Maria S. (m+ż)": "oni", "Wisława Szymborska (ż)": "ona" }
        people_keys = list(people.keys())
        selected_person = st.selectbox("O kim mówimy?", options=[""] + people_keys, key=f"{q_key_pronoun}_select",
            index=0 if st.session_state[q_key_pronoun]['selected_person'] is None else ([""] + people_keys).index(st.session_state[q_key_pronoun]['selected_person']),
            on_change=lambda: st.session_state[q_key_pronoun].update({'user_choice': None}) )
        st.session_state[q_key_pronoun]['selected_person'] = selected_person if selected_person else None
        if selected_person:
            pronoun_options = ["on", "ona", "ono", "oni", "one"]; correct_pronoun = people[selected_person]; verb_form = "nazywa się" if correct_pronoun in ["on", "ona", "ono"] else "nazywają się"
            current_choice_pronoun = st.session_state[q_key_pronoun].get('user_choice')
            # --- CORRECTED try/except block ---
            radio_index_pronoun = None
            if current_choice_pronoun in pronoun_options:
                try: radio_index_pronoun = pronoun_options.index(current_choice_pronoun)
                except ValueError: radio_index_pronoun = None
            # --- END CORRECTION ---
            user_choice = st.radio(f"Jak ______ {verb_form}?", pronoun_options, key=f"{q_key_pronoun}_radio", index=radio_index_pronoun, horizontal=True)
            st.session_state[q_key_pronoun]['user_choice'] = user_choice
            if user_choice is not None:
                 is_correct_pronoun = (user_choice == correct_pronoun); st.session_state.feedback[exercise_key] = {'correctness': is_correct_pronoun}
                 if is_correct_pronoun: st.success(f"✅ Tak! '{correct_pronoun}'.")
                 else: st.error(f"❌ Nie. Poprawny: '{correct_pronoun}'.")
        elif f"{q_key_pronoun}_select" in st.session_state and not selected_person: st.session_state.feedback.pop(exercise_key, None)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("**Ułóż zdania / Ordena las frases**")
        exercise_key = "dialogue_reorder"; q_key_reorder = f"{exercise_key}_reorder"
        if q_key_reorder not in st.session_state: st.session_state[q_key_reorder] = ""
        words_to_order = ["się", "Adam", "Nazywam"]; correct_order = "Nazywam się Adam"
        st.markdown(f"Ułóż słowa:");
        if 'shuffled_words_reorder' not in st.session_state: st.session_state['shuffled_words_reorder'] = random.sample(words_to_order, len(words_to_order))
        st.code(f"{' / '.join(st.session_state['shuffled_words_reorder'])}")
        user_order = st.text_input("Wpisz poprawne zdanie:", value=st.session_state[q_key_reorder], key=q_key_reorder + "_input")
        st.session_state[q_key_reorder] = user_order
        if st.button("Sprawdź kolejność", key=f"{q_key_reorder}_check"):
            normalized_user = user_order.strip().rstrip('.?!').lower(); normalized_correct = correct_order.lower()
            is_correct_reorder = (normalized_user == normalized_correct); st.session_state.feedback[exercise_key] = {'correctness': is_correct_reorder}
            if is_correct_reorder: st.success(f"✅ Doskonale! '{correct_order}'.")
            else: st.error(f"❌ Prawie! Poprawnie: '{correct_order}'.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.success("🎉 **Gratulacje! Ukończyłeś/aś pierwszą lekcję!** 🎉")
        st.markdown("Ćwicz dalej! / ¡Sigue practicando!")
