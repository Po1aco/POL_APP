import streamlit as st
import time
import random # Import random for shuffling

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="Polski dla Hiszpanów",
    page_icon="🇵🇱",
    layout="wide" # Use wide layout and control width with columns
)

# --- Custom CSS (Embedded) ---
st.markdown("""
<style>
/* Import Gabarito font (Weights 400-700 recommended) */
@import url('https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700&display=swap');

/* --- Base Font --- */
html, body, [class*="st-"], .stMarkdown {
    font-family: 'Gabarito', sans-serif !important; /* Use Gabarito */
    font-weight: 400; /* Default weight */
}

/* --- Background --- */
/* Using a very light pastel gradient */
@keyframes gradientAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
body::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: -1;
    /* Pastel Gradient: Light Blue to Soft Pink/Beige */
    background: linear-gradient(135deg, #E0F7FA, #FFF0F5, #E0F7FA); /* Example: Light Cyan to Lavender Blush */
    background-size: 400% 400%;
    /* Optional: Subtle Noise */
    /* background-image: linear-gradient(rgba(0,0,0,0.01) 1px, transparent 1px),
                       linear-gradient(90deg, rgba(0,0,0,0.01) 1px, transparent 1px),
                       linear-gradient(135deg, #E0F7FA, #FFF0F5, #E0F7FA);
    background-size: 3px 3px, 3px 3px, 400% 400%; */
    animation: gradientAnimation 30s ease infinite;
}
.stApp {
    background-color: transparent; /* Let body::before show through */
}

/* --- Content Box Styling (like reference image) --- */
.content-box {
    background-color: rgba(255, 255, 255, 0.8); /* Slightly transparent white */
    border: 1px solid #E0E0E0; /* Light grey border */
    border-radius: 15px; /* Rounded corners */
    padding: 20px 25px; /* Internal padding */
    margin-bottom: 25px; /* Space between boxes */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* Soft shadow */
}
/* Apply similar style to standard Streamlit alerts */
.stAlert {
    background-color: rgba(232, 245, 253, 0.85); /* Light blue base for alerts */
    border: 1px solid #B3E5FC;
    border-radius: 15px;
    padding: 15px 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    font-family: 'Gabarito', sans-serif !important;
}
.stAlert code { /* Style code blocks inside alerts */
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 5px;
}
.stAlert.stSuccess {
    background-color: rgba(232, 255, 236, 0.85); /* Pastel green */
    border-color: #C8E6C9;
}
.stAlert.stWarning {
    background-color: rgba(255, 243, 232, 0.85); /* Pastel orange */
    border-color: #FFCCBC;
}
.stAlert.stError {
    background-color: rgba(255, 235, 238, 0.85); /* Pastel red/pink */
    border-color: #FFCDD2;
}

/* --- Headings and Text --- */
h1, h2, h3, h4, h5, h6 {
    color: #335C67; /* Darker Teal/Blue for contrast */
    font-family: 'Gabarito', sans-serif !important;
    font-weight: 600; /* Slightly bolder headings */
}
.stMarkdown, p, li {
   color: #4F4F4F; /* Dark Gray for readability */
   line-height: 1.7;
   font-family: 'Gabarito', sans-serif !important;
}
strong {
   font-weight: 600; /* Make bold text stand out more */
   color: #335C67;
}
code { /* Style inline code */
    background-color: rgba(224, 247, 250, 0.7); /* Very light cyan */
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    border-radius: 6px;
    border: 1px solid rgba(178, 235, 242, 0.8);
    font-family: monospace; /* Keep monospace for code */
    color: #006064; /* Dark cyan text */
}

/* --- Button Styling --- */
.stButton>button {
    border: 1px solid #99AAB5; /* Soft grey border */
    border-radius: 12px;
    padding: 8px 18px;
    background-color: #FFFFFF;
    color: #546E7A; /* Muted Blue-Gray */
    transition: all 0.2s ease;
    font-family: 'Gabarito', sans-serif !important;
    font-weight: 500; /* Medium weight */
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.stButton>button:hover {
    background-color: #E3F2FD; /* Light blue hover */
    color: #1E88E5; /* Brighter blue text */
    border-color: #90CAF9;
    box-shadow: 0 3px 6px rgba(0,0,0,0.08);
    transform: translateY(-1px);
}
.stButton>button:active {
    transform: translateY(0px);
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

/* --- Input/Widget Styling --- */
.stRadio > label, .stTextInput > label, .stSelectbox > label {
    font-weight: 500;
    color: #335C67; /* Match heading color */
    font-family: 'Gabarito', sans-serif !important;
    padding-bottom: 5px; /* Add some space below label */
}
div[data-baseweb="input"] > div, /* Text Input background */
div[data-baseweb="select"] > div, /* Selectbox background */
div[data-baseweb="radio"] { /* Radio button styling */
    font-family: 'Gabarito', sans-serif !important;
}
div[data-baseweb="input"] input,
div[data-baseweb="select"] div { /* Target inner parts */
   border-radius: 8px !important;
   border-color: #CFD8DC !important; /* Lighter border */
   background-color: rgba(255, 255, 255, 0.8);
   font-family: 'Gabarito', sans-serif !important;
}


/* --- Sidebar Styling --- */
.stSidebar {
    /* Pastel Pink */
    background-color: rgba(250, 218, 221, 0.9); /* #FADADD with 90% opacity */
    backdrop-filter: blur(6px);
    border-right: 1px solid rgba(230, 190, 194, 0.5); /* Soft border */
}
.stSidebar .stMarkdown, .stSidebar .stRadio > label {
     color: #5D4037 !important; /* Brownish text for contrast on pink */
     font-family: 'Gabarito', sans-serif !important;
}
.stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar strong {
    color: #4E342E !important; /* Darker Brown */
     font-family: 'Gabarito', sans-serif !important;
     font-weight: 600;
}
.stSidebar .stButton>button {
     font-family: 'Gabarito', sans-serif !important;
     font-weight: 500;
     border: 1px solid #A1887F; /* Muted brown border */
     background-color: rgba(255, 255, 255, 0.75); /* Transparent white */
     color: #5D4037; /* Brownish text */
     border-radius: 10px;
}
.stSidebar .stButton>button:hover {
     background-color: #A1887F; /* Muted brown background */
     color: #FFF0F5; /* Lavender blush text */
     border-color: #FFF0F5;
}

</style>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
if 'page' not in st.session_state:
    st.session_state.page = "Introduction"
if 'feedback' not in st.session_state:
    st.session_state.feedback = {} # To store feedback for exercises

# --- Navigation ---
with st.sidebar: # Keep navigation in sidebar
    st.title("🇵🇱 Nawigacja 🇪🇸")
    pages = ["Introduction", "Alphabet", "Vocabulary & Phrases", "Grammar Focus", "Pronunciation Practice", "Dialogues & Context"]
    page_emojis = ["👋", "🔤", "🗣️", "✍️", "👂", "💬"]

    for page, emoji in zip(pages, page_emojis):
        if st.button(f"{emoji} {page}"):
            st.session_state.page = page
            st.session_state.feedback = {} # Clear feedback when changing pages
            st.rerun() # Use st.rerun()

    st.markdown("---")
    st.info("Lekcja oparta na materiałach PDF.")

# --- Main Content Area with Padding ---
# Define columns for padding: Adjust the middle number (6) to change content width
body_col_left, body_col_main, body_col_right = st.columns([1, 6, 1])

with body_col_main: # All main page content goes in this middle column

    # == INTRODUCTION ==
    if st.session_state.page == "Introduction":
        st.title("👋 Witaj! ¡Bienvenido/a al Polaco!")

        with st.container(): # Use container for grouping, box styling applied via CSS class
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.header("Lekcja 0/1: Pierwsze kroki / Primeros pasos")
             st.markdown("""
                Witaj w interaktywnej lekcji języka polskiego dla osób mówiących po hiszpańsku!
                ¡Bienvenido/a a esta lección interactiva de polaco para hispanohablantes!

                **Język polski (El idioma polaco):**
                *   Jest językiem zachodniosłowiańskim. (Es una lengua eslava occidental.)
                *   Używa alfabetu łacińskiego z dodatkowymi znakami. (Usa el alfabeto latino con caracteres adicionales.)
                *   Ma **7 przypadków gramatycznych** (esto es importante: los sustantivos, adjetivos y pronombres cambian su terminación según su función en la frase - ¡muy diferente al español!).
                *   Posiada **3 rodzaje** (masculino, femenino, neutro) oraz specjalne formy liczby mnogiej (viril/no viril). (Tiene 3 géneros y formas plurales especiales.)
                *   **Nie ma rodzajników** (a/an, the). (No tiene artículos.)
                *   Akcent pada zazwyczaj na **przedostatnią sylabę**. (El acento cae generalmente en la penúltima sílaba, como en las palabras llanas en español.)

                **Cele tej lekcji (Objetivos de esta lección):**
                1.  Poznać polski alfabet i wymowę. (Conocer el alfabeto polaco y su pronunciación.)
                2.  Nauczyć się podstawowych powitań i przedstawiania się. (Aprender saludos básicos y cómo presentarse.)
                3.  Zrozumieć podstawowe czasowniki: *mówić* (hablar), *nazywać się* (llamarse), *mieć* (tener). (Entender verbos básicos.)
                4.  Zobaczyć pierwsze różnice i podobieństwa do hiszpańskiego. (Ver las primeras diferencias y similitudes con el español.)

                Zaczynajmy! ¡Empecemos!
            """)
             st.markdown('</div>', unsafe_allow_html=True)

        if st.button("➡️ Dalej / Siguiente: Alfabet"):
            st.session_state.page = "Alphabet"
            st.rerun()

    # == ALPHABET ==
    elif st.session_state.page == "Alphabet":
        st.title("🔤 Polski Alfabet / El Alfabeto Polaco")

        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("Oto polski alfabet z przykładami i wymową fonetyczną (uproszczoną).")
            st.markdown("Aquí tienes el alfabeto polaco con ejemplos y pronunciación fonética (simplificada).")
            # Alphabet Table (ensure markdown table format is correct)
            st.markdown("""
            | Litera | Nazwa (aproximado) | Wymowa (IPA approx.) | Przykład (Ejemplo) | Nota para hispanohablantes |
            |---|---|---|---|---|
            | **A a** | a | [a] | **a**dres | Como la 'a' española. |
            | **Ą ą** | o~ / on | [ɔ̃] (nasal) | m**ą**ka (harina) | **¡Nasal!** Como 'on' francés o 'ão' portugués. No existe en español. |
            | **B b** | be | [b] | **b**alkon | Como la 'b' española (al inicio o tras 'm'). |
            | **C c** | ce | [ts] | **c**ena (precio) | Como 'ts' en 'tsé-tsé'. **¡No como 's' ni 'k'!** |
            | **Ć ć** | cie | [tɕ] | **ć**ma (polilla) | Sonido suave, como 'ch' muy suave, palatalizado. No existe en español. |
            | **Ch ch**| ce ha | [x] | **ch**oroba (enfermedad) | **Como la 'j' española** (ja, jo, ju) o 'g' (ge, gi). |
            | **Cz cz**| cze | [tʂ] | **cz**ekolada | **Como 'ch' en 'chocolate' en inglés.** Más fuerte que 'ch' español. |
            | **D d** | de | [d] | **d**ata | Como la 'd' española (al inicio o tras 'n'/'l'). |
            | **Dz dz**| dze | [dz] | **dz**won (campana) | Sonido sonoro de 'ts'. Como 'ds' en inglés 'kids'. |
            | **Dź dź**| dzie | [dʑ] | **dź**więk (sonido) | Sonido suave de 'dż'. Similar a 'j' en inglés 'judge', pero más suave/palatal. |
            | **Dż dż**| dże | [dʐ] | **dż**em (mermelada) | Como 'j' en inglés 'judge' o 'g' en 'George'. |
            | **E e** | e | [ɛ] | **e**fekt | Como la 'e' española (abierta). |
            | **Ę ę** | e~ / en | [ɛ̃] (nasal) | r**ę**ka (mano) | **¡Nasal!** Similar a 'in' francés o 'em' portugués. No existe en español. |
            | **F f** | ef | [f] | **f**irma | Como la 'f' española. |
            | **G g** | gie | [ɡ] | **g**olf | Como 'g' en 'gato', 'lago'. **Siempre sonido fuerte.** |
            | **H h** | ha | [x] | **h**otel | **Como la 'j' española**. Igual que 'ch'. |
            | **I i** | i | [i] | **i**gnorant | Como la 'i' española. **Importante:** Suaviza la consonante anterior (np. *ni* = 'ñi', *si* = 'shi' suave). |
            | **J j** | jot | [j] | **j**oga | Como 'y' en 'yo' o 'i' en 'bien'. |
            | **K k** | ka | [k] | **k**alkulator | Como la 'k' o 'c' (ca, co, cu) española. |
            | **L l** | el | [l] | **l**ekcja | Como la 'l' española. |
            | **Ł ł** | eł | [w] | **ł**adny (bonito) | **¡Importante!** **Como la 'w' inglesa** en 'water'. No como 'l' española. |
            | **M m** | em | [m] | **m**ama | Como la 'm' española. |
            | **N n** | en | [n] | **n**ormalny | Como la 'n' española. |
            | **Ń ń** | eń | [ɲ] | ko**ń** (caballo) | **Como la 'ñ' española.** |
            | **O o** | o | [ɔ] | **o**ferta | Como la 'o' española (abierta). |
            | **Ó ó** | o kreskowane | [u] | **ó**sma (octava) | **¡Importante! Suena exactamente como 'u'.** Mismo sonido que 'U u'. |
            | **P p** | pe | [p] | **p**rogram | Como la 'p' española. |
            | **R r** | er | [r] | **r**uiny | Vibrante simple, como 'r' en 'pero'. Puede ser múltiple a veces. |
            | **Rz rz**| er zet | [ʐ] / [ʂ] | **rz**eka (río) | **Como 'ż'.** Sonido como 'll' argentina/uruguaya fuerte, o 'j' francesa. Después de p, k, t, ch suena como 'sz' [ʂ]. |
            | **S s** | es | [s] | **s**top | Como la 's' española (siempre sorda). |
            | **Ś ś** | eś | [ɕ] | **ś**roda (miércoles) | Sonido suave, como 'sh' muy suave, palatalizado. No existe en español. |
            | **Sz sz**| esz | [ʂ] | **sz**ok | **Como 'sh' inglesa** en 'show'. |
            | **T t** | te | [t] | **t**enis | Como la 't' española. |
            | **U u** | u | [u] | **u**waga (atención) | Como la 'u' española. Mismo sonido que 'Ó ó'. |
            | **W w** | wu | [v] | **w**ulkan | **Como la 'v' inglesa/francesa.** Labiodental. **¡No como 'b'!** |
            | **Y y** | igrek | [ɨ] | s**y**stem | **¡Sonido difícil!** No existe en español. Similar a 'i' pero más atrás y central en la boca. Como 'i' en ruso 'мы'. Escucha atentamente. |
            | **Z z** | zet | [z] | **z**oo | Como 's' sonora, como zumbido de abeja 'zzz'. Como 's' en español 'mismo'. |
            | **Ź ź** | ziet | [ʑ] | **ź**le (mal) | Sonido suave de 'ż'. Como 'j' francesa suave o 's' en inglés 'pleasure' palatalizada. |
            | **Ż ż** | żet | [ʐ] | **ż**aba (rana) | **Como 'rz'.** Sonido como 'll' argentina/uruguaya fuerte, o 'j' francesa. |
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("👂 Ćwiczenie Wymowy / Ejercicio de Pronunciación")

        pairs = {
            "s / sz / ś": (["stop", "szok", "środa"], 2),
            "c / cz / ć": (["cena", "czekolada", "ćma"], 1),
            "z / rz / ź": (["zoo", "rzeka", "źle"], 0),
            "l / ł": (["lekcja", "ładny"], 1),
            "i / y": (["miły", "myły"], 0)
        }
        exercise_key = "alphabet_pronunciation"
        if exercise_key not in st.session_state.feedback:
             st.session_state.feedback[exercise_key] = {}

        q_num = 1
        for key, (options, correct_index) in pairs.items():
             with st.container():
                 st.markdown('<div class="content-box">', unsafe_allow_html=True)
                 q_key = f"{exercise_key}_{q_num}"
                 st.markdown(f"**{q_num}.** Dźwięk / Sonido: **{key}**")
                 st.info(f"🎧 *Wyobraź sobie, że słyszysz jedno z tych słów...*")

                 current_choice_index = None
                 if q_key in st.session_state.feedback and st.session_state.feedback[q_key] is not None and 'user_choice' in st.session_state.feedback[q_key]:
                      try:
                          current_choice_index = options.index(st.session_state.feedback[q_key]['user_choice'])
                      except ValueError:
                          current_choice_index = None

                 user_choice = st.radio(f"Które słowo słyszysz? / ¿Qué palabra oyes?", options, key=q_key, index=current_choice_index, label_visibility="collapsed", horizontal=True) # Try horizontal layout

                 if q_key not in st.session_state.feedback:
                     st.session_state.feedback[q_key] = {}

                 if user_choice is not None:
                     is_correct = options.index(user_choice) == correct_index
                     st.session_state.feedback[q_key]['user_choice'] = user_choice
                     st.session_state.feedback[q_key]['is_correct'] = is_correct

                     # Display feedback immediately below radio buttons
                     if is_correct:
                         st.success("✅ Dobrze! ¡Correcto!")
                     else:
                         st.error(f"❌ Spróbuj ponownie. Poprawnie: '{options[correct_index]}'.")
                 st.markdown('</div>', unsafe_allow_html=True)
             q_num += 1


        if st.button("➡️ Dalej / Siguiente: Słownictwo"):
            st.session_state.page = "Vocabulary & Phrases"
            st.rerun()

    # == VOCABULARY & PHRASES ==
    elif st.session_state.page == "Vocabulary & Phrases":
        st.title("🗣️ Podstawowe Słownictwo i Zwroty")

        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("Pozdrowienia / Saludos")
            st.markdown("""
            *   **Dzień dobry!** - ¡Buenos días! / ¡Buenas tardes! (Formal)
            *   **Cześć!** - ¡Hola! / ¡Adiós! (Informal)
            *   **Dobry wieczór!** - ¡Buenas noches! (Al llegar - Formal)
            *   **Dobranoc!** - ¡Buenas noches! (Al despedirse/irse a dormir)
            *   **Do widzenia!** - ¡Adiós! (Formal)
            *   **Na razie!** - ¡Hasta luego! (Informal)
            """)
            st.subheader("Przedstawianie się / Presentaciones")
            st.markdown("""
            *   **Jak się nazywasz?** - ¿Cómo te llamas? (Informal - *ty*)
            *   **Jak pan/pani się nazywa?** - ¿Cómo se llama usted? (Formal - *Pan/Pani*)
            *   **Nazywam się...** - Me llamo... (np. *Nazywam się Adam.*)
            *   **Jak masz/ma na imię?** - ¿Cuál es tu/su nombre (de pila)? (Informal/Formal)
            *   **Mam na imię...** - Mi nombre (de pila) es... (np. *Mam na imię Ewa.*)
            *   **Miło mi.** - Encantado/a. / Mucho gusto.
            """)
            st.info("💡 **Pan/Pani vs Ty:** Similar a *Usted vs Tú*. *Pan* (Sr.), *Pani* (Sra./Srta.).")
            st.subheader("Zaimki Osobowe / Pronombres Personales")
            st.markdown("""
            *   **ja** - yo | **my** - nosotros/as
            *   **ty** - tú | **wy** - vosotros/as / ustedes (inf.)
            *   **on** - él | **oni** - ellos (grupo con hombres)
            *   **ona** - ella | **one** - ellas / ellos (sin hombres/cosas)
            *   **ono** - ello (neutro)
            *   **Pan/Pani** - usted (m/f) | **Państwo** - ustedes (form.)
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("📝 Ćwiczenia / Ejercicios")
        exercise_key = "vocab_phrases"
        if exercise_key not in st.session_state.feedback:
             st.session_state.feedback[exercise_key] = {}

        # --- Exercise 1: Matching ---
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("**1. Dopasuj polskie zwroty do hiszpańskich tłumaczeń.**")
            q1_key = f"{exercise_key}_q1"
            match_options = {
                "Dzień dobry!": "¡Buenos días/tardes! (Formal)",
                "Jak się nazywasz?": "¿Cómo te llamas? (Informal)",
                "Do widzenia!": "¡Adiós! (Formal)",
                "Miło mi.": "Encantado/a.",
                "Cześć!": "¡Hola! / ¡Adiós! (Informal)"
            }
            polish_phrases = list(match_options.keys())
            spanish_translations = list(match_options.values())

            if q1_key not in st.session_state:
                st.session_state[q1_key] = {}
            if 'shuffled_spanish' not in st.session_state[q1_key]:
                st.session_state[q1_key]['shuffled_spanish'] = random.sample(spanish_translations, len(spanish_translations))
            if 'user_matches' not in st.session_state[q1_key]:
                 st.session_state[q1_key]['user_matches'] = {phrase: "" for phrase in polish_phrases}

            shuffled_spanish = st.session_state[q1_key]['shuffled_spanish']
            cols1 = st.columns(2)
            with cols1[0]:
                # st.markdown("**Polski:**") # Label implicit
                for i, phrase in enumerate(polish_phrases):
                    current_selection = st.session_state[q1_key]['user_matches'].get(phrase, "")
                    try: sel_index = ([""] + shuffled_spanish).index(current_selection)
                    except ValueError: sel_index = 0
                    st.session_state[q1_key]['user_matches'][phrase] = st.selectbox(
                        f"{i+1}. {phrase}", options=[""] + shuffled_spanish, key=f"{q1_key}_{i}", index=sel_index, label_visibility="visible" # Show label this time
                    )
            with cols1[1]:
                 st.markdown("**Opcje (Español):**")
                 st.table([[trans] for trans in shuffled_spanish]) # Use table for cleaner look

            if st.button("Sprawdź dopasowanie", key=f"{q1_key}_check"):
                # Feedback logic (remains the same)
                correct_count_match = 0
                all_correct_match = True
                feedback_match_html = "<ul>"
                user_matches = st.session_state[q1_key]['user_matches']
                for polish, user_spanish in user_matches.items():
                    correct_spanish = match_options[polish]
                    if user_spanish == correct_spanish:
                        feedback_match_html += f"<li>'{polish}' = '{user_spanish}' ✅</li>"
                        correct_count_match += 1
                    elif not user_spanish:
                         feedback_match_html += f"<li>'{polish}' = ? (Nie wybrano)</li>"
                         all_correct_match = False
                    else:
                        feedback_match_html += f"<li>'{polish}' = <span style='color:red;'>'{user_spanish}'</span> ❌ (Poprawnie: '{correct_spanish}')</li>"
                        all_correct_match = False
                feedback_match_html += "</ul>"
                st.markdown(feedback_match_html, unsafe_allow_html=True)
                st.session_state.feedback[exercise_key][q1_key] = all_correct_match
                if all_correct_match: st.success("🎉 Wszystkie pary poprawne!")
                else: st.warning(f"Masz {correct_count_match} z {len(polish_phrases)} poprawnych par.")
            st.markdown('</div>', unsafe_allow_html=True)


        # --- Exercise 2: Fill-in-the-blanks ---
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("**2. Uzupełnij dialog wyrazami z ramki.**")
            q2_key = f"{exercise_key}_q2"
            words_bank = ["Miło", "pan", "Nazywam się", "pani", "dobry"]
            st.info(f"Ramka / Recuadro: `{', '.join(words_bank)}`")
            solution = ["dobry", "pani", "dobry", "Nazywam się", "pan", "Miło"]
            if q2_key not in st.session_state: st.session_state[q2_key] = [""] * len(solution)

            # Display inputs within the box
            st.markdown("**Dialog:**")
            st.session_state[q2_key][0] = st.text_input(f"A: Dzień ______! [0]", value=st.session_state[q2_key][0], key=f"{q2_key}_0")
            st.session_state[q2_key][1] = st.text_input(f"A: ... Jak ______ się nazywa? [1]", value=st.session_state[q2_key][1], key=f"{q2_key}_1")
            st.session_state[q2_key][2] = st.text_input(f"B: Dzień ______! [2]", value=st.session_state[q2_key][2], key=f"{q2_key}_2")
            st.session_state[q2_key][3] = st.text_input(f"B: ... ______ Piotr Nowicki. [3]", value=st.session_state[q2_key][3], key=f"{q2_key}_3")
            st.session_state[q2_key][4] = st.text_input(f"B: ... Jak ______ się nazywa? [4]", value=st.session_state[q2_key][4], key=f"{q2_key}_4")
            st.markdown("<p style='margin-left: 10px;'>A: Anna Kamińska.</p>", unsafe_allow_html=True) # Indent slightly
            st.session_state[q2_key][5] = st.text_input(f"B: ______ mi. [5]", value=st.session_state[q2_key][5], key=f"{q2_key}_5")

            if st.button("Sprawdź odpowiedzi (Fill-in)", key=f"{q2_key}_check"):
                # Feedback logic (remains the same)
                correct_count = 0; all_correct = True
                filled_dialog = [ # Using f-strings directly
                     f"A: Dzień {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][0].strip() + '</span>' if st.session_state[q2_key][0].strip().lower() == solution[0].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][0].strip() + '</span>' + f' ({solution[0]})'}! Jak {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][1].strip() + '</span>' if st.session_state[q2_key][1].strip().lower() == solution[1].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][1].strip() + '</span>' + f' ({solution[1]})'} się nazywa?",
                     f"B: Dzień {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][2].strip() + '</span>' if st.session_state[q2_key][2].strip().lower() == solution[2].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][2].strip() + '</span>' + f' ({solution[2]})'}! {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][3].strip() + '</span>' if st.session_state[q2_key][3].strip().lower() == solution[3].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][3].strip() + '</span>' + f' ({solution[3]})'} Piotr Nowicki. Jak {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][4].strip() + '</span>' if st.session_state[q2_key][4].strip().lower() == solution[4].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][4].strip() + '</span>' + f' ({solution[4]})'} się nazywa?",
                     "<span style='margin-left: 10px;'>A: Anna Kamińska.</span>",
                     f"B: {'<span style=\'color:green; font-weight:600;\'>' + st.session_state[q2_key][5].strip() + '</span>' if st.session_state[q2_key][5].strip().lower() == solution[5].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][5].strip() + '</span>' + f' ({solution[5]})'} mi."
                 ]
                for i in range(len(solution)):
                    if st.session_state[q2_key][i].strip().lower() == solution[i].lower(): correct_count +=1
                    else: all_correct = False
                st.markdown("<h5>Wyniki:</h5>" + "<br>".join(filled_dialog), unsafe_allow_html=True)
                st.session_state.feedback[exercise_key][q2_key] = all_correct
                if all_correct: st.success("🎉 Gratulacje! Wszystko poprawnie!")
                else: st.warning(f"Masz {correct_count} z {len(solution)} poprawnych odpowiedzi.")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Exercise 3: Formal/Informal ---
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("**3. Formalnie czy nieformalnie? / ¿Formal o informal?**")
            q3_key = f"{exercise_key}_q3"
            scenarios = {
                "Spotykasz profesora na uniwersytecie.": "Dzień dobry!",
                "Witasz się z kolegą.": "Cześć!",
                "Żegnasz się z dyrektorem firmy.": "Do widzenia!",
                "Mówisz 'do zobaczenia' przyjaciółce.": "Na razie!",
            }
            scenario_keys = list(scenarios.keys())
            if q3_key not in st.session_state: st.session_state[q3_key] = {'selected_scenario': None, 'user_choice': None}

            # Selectbox for scenario
            selected_scenario = st.selectbox(
                "Wybierz sytuację / Elige la situación:", options=[""] + scenario_keys, key=f"{q3_key}_select",
                index=0 if st.session_state[q3_key]['selected_scenario'] is None else ([""] + scenario_keys).index(st.session_state[q3_key]['selected_scenario']),
                on_change=lambda: st.session_state[q3_key].update({'user_choice': None})
            )
            st.session_state[q3_key]['selected_scenario'] = selected_scenario if selected_scenario else None

            if selected_scenario:
                 correct_greeting = scenarios[selected_scenario]
                 greeting_options = ["Dzień dobry!", "Cześć!", "Do widzenia!", "Na razie!"]
                 options_for_radio = list(set(random.sample(greeting_options, 3) + [correct_greeting]))
                 random.shuffle(options_for_radio)

                 current_choice_q3 = st.session_state[q3_key].get('user_choice')
                 try: radio_index_q3 = options_for_radio.index(current_choice_q3) if current_choice_q3 in options_for_radio else None
                 except ValueError: radio_index_q3 = None

                 # Radio buttons for choice
                 user_choice = st.radio("Co powiesz? / ¿Qué dices?", options=options_for_radio, key=f"{q3_key}_radio", index=radio_index_q3, horizontal=True)
                 st.session_state[q3_key]['user_choice'] = user_choice

                 # Display feedback
                 if user_choice is not None:
                     is_correct_q3 = (user_choice == correct_greeting)
                     st.session_state.feedback[exercise_key][q3_key] = is_correct_q3
                     if is_correct_q3: st.success("✅ Zgadza się!")
                     else: st.error(f"❌ Lepiej powiedzieć '{correct_greeting}'.")
            elif f"{q3_key}_select" in st.session_state and not selected_scenario:
                 st.session_state.feedback[exercise_key].pop(q3_key, None)
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("➡️ Dalej / Siguiente: Gramatyka"):
            st.session_state.page = "Grammar Focus"
            st.rerun()

    # == GRAMMAR FOCUS ==
    elif st.session_state.page == "Grammar Focus":
        st.title("✍️ Gramatyka / Gramática")
        st.info("💡 Pamiętaj: *Pan/Pani* używają formy czasownika jak *on/ona/ono* (3 os. l.poj.).")

        # --- Mówić ---
        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("Czasownik *mówić* (hablar)")
            # Table and example remain the same
            st.markdown("""
            | Osoba | Czasownik | Tłumaczenie |
            |---|---|---|
            | ja | mów**ię** | hablo |
            | ty | mów**isz** | hablas |
            | on/ona/ono | mów**i** | habla |
            | **Pan/Pani** | mów**i** | habla |
            | my | mów**imy** | hablamos |
            | wy | mów**icie** | habláis / hablan |
            | oni/one | mów**ią** | hablan |
            | **Państwo** | mów**ią** | hablan |
            """)
            st.markdown("**Przykład:** *Ona mówi po francusku. Ja nie mówię.*")

            # --- Exercise: Mówić ---
            st.markdown("**Ćwiczenie: Uzupełnij zdania poprawną formą MÓWIĆ.**")
            exercise_key = "grammar_mowic"
            if exercise_key not in st.session_state: st.session_state[exercise_key] = {}
            if 'inputs' not in st.session_state[exercise_key]: st.session_state[exercise_key]['inputs'] = {}

            mowic_sentences = [ # Structure: (Sentence template, [correct forms])
                ("Czy ______ po polsku? (ty)", ["mówisz"]),
                ("______ po angielsku. (my)", ["mówimy"]),
                ("Oni nie ______ po francusku, ale ______ po polsku. (oni / oni)", ["mówią", "mówią"]),
                ("On ______ trochę po rosyjsku, ale ja nie ______. (on / ja)", ["mówi", "mówię"]),
                ("Czy ______ po niemiecku? (wy)", ["mówicie"]),
                ("One nie ______ po hiszpańsku. (one)", ["mówią"]),
                ("Czy ona ______ po polsku?", ["mówi"]),
                ("Nie ______ po włosku. (ja)", ["mówię"])
            ]

            # Initialize inputs
            for i in range(len(mowic_sentences)):
                q_key = f"{exercise_key}_{i}"
                num_blanks = mowic_sentences[i][0].count("______")
                if q_key not in st.session_state[exercise_key]['inputs']: st.session_state[exercise_key]['inputs'][q_key] = [""] * num_blanks

            # Display inputs
            for i, (sentence, correct_forms) in enumerate(mowic_sentences):
                q_key = f"{exercise_key}_{i}"
                num_blanks = sentence.count("______")
                prompt = sentence.replace("______", "_______")
                if num_blanks == 1:
                    st.session_state[exercise_key]['inputs'][q_key][0] = st.text_input(f"{i+1}. {prompt}", value=st.session_state[exercise_key]['inputs'][q_key][0], key=q_key, placeholder="Wpisz formę")
                elif num_blanks == 2:
                     cols_mowic = st.columns(2)
                     with cols_mowic[0]: st.session_state[exercise_key]['inputs'][q_key][0] = st.text_input(f"{i+1}a. {prompt} (luka 1)", value=st.session_state[exercise_key]['inputs'][q_key][0], key=f"{q_key}_a", placeholder="Forma 1")
                     with cols_mowic[1]: st.session_state[exercise_key]['inputs'][q_key][1] = st.text_input(f"{i+1}b. {prompt} (luka 2)", value=st.session_state[exercise_key]['inputs'][q_key][1], key=f"{q_key}_b", placeholder="Forma 2")

            if st.button("Sprawdź MÓWIĆ", key=f"{exercise_key}_check"):
                 # Feedback logic (remains the same, uses updated session state structure)
                all_correct_mowic = True; feedback_html_mowic = "<ul>"
                for i, (sentence, correct_forms_list) in enumerate(mowic_sentences):
                    q_key = f"{exercise_key}_{i}"
                    user_answers = [ans.strip().lower() for ans in st.session_state[exercise_key]['inputs'][q_key]]
                    correct_forms_list_lower = [f.lower() for f in correct_forms_list]
                    sentence_display = sentence; correct_in_sentence = True
                    for j in range(len(correct_forms_list_lower)):
                        user_ans = user_answers[j]; correct_ans = correct_forms_list_lower[j]
                        if user_ans == correct_ans: replacement = f"<span style='color:green; font-weight:600;'>{user_ans}</span>"
                        else: replacement = f"<span style='color:red;'>{user_ans}</span> (Poprawnie: {correct_ans})"; correct_in_sentence = False; all_correct_mowic = False
                        sentence_display = sentence_display.replace("______", f"__PLACEHOLDER_{j}__", 1)
                    for j in range(len(correct_forms_list_lower)):
                        user_ans = user_answers[j]; correct_ans = correct_forms_list_lower[j]
                        if user_ans == correct_ans: replacement = f"<span style='color:green; font-weight:600;'>{user_ans}</span>"
                        else: replacement = f"<span style='color:red;'>{user_ans}</span> (Poprawnie: {correct_ans})"
                        sentence_display = sentence_display.replace(f"__PLACEHOLDER_{j}__", replacement)
                    feedback_html_mowic += f"<li>{sentence_display} {'✅' if correct_in_sentence else '❌'}</li>"
                feedback_html_mowic += "</ul>"; st.markdown(feedback_html_mowic, unsafe_allow_html=True)
                st.session_state.feedback[exercise_key] = {'all_correct': all_correct_mowic}
                if all_correct_mowic: st.success("🎉 Świetnie! 'mówić' opanowany!")
                else: st.warning("Popraw błędy.")
            st.markdown('</div>', unsafe_allow_html=True) # Close content-box for Mówić

        # --- Nazywać się & Mieć ---
        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.subheader("Czasowniki *nazywać się* (llamarse) i *mieć* (tener)")
             cols_verbs = st.columns(2)
             with cols_verbs[0]:
                 st.markdown("**Nazywać się (llamarse)**")
                 st.markdown("""
                 | Osoba | Czasownik | Tłumaczenie |
                 |---|---|---|
                 | ja | nazywam **się** | me llamo |
                 | ty | nazywasz **się** | te llamas |
                 | on/ona/ono | nazywa **się** | se llama |
                 | **Pan/Pani** | nazywa **się** | se llama |
                 | my | nazywamy **się** | nos llamamos |
                 | wy | nazywacie **się** | os llamáis / se llaman |
                 | oni/one | nazywają **się** | se llaman |
                 | **Państwo** | nazywają **się** | se llaman |
                 """)
                 st.markdown("*Przykład: Jak pan się nazywa? Nazywam się Kowalski.*")
             with cols_verbs[1]:
                 st.markdown("**Mieć (tener)**")
                 st.markdown("""
                 | Osoba | Czasownik | Tłumaczenie |
                 |---|---|---|
                 | ja | m**am** | tengo |
                 | ty | m**asz** | tienes |
                 | on/ona/ono | m**a** | tiene |
                 | **Pan/Pani** | m**a** | tiene |
                 | my | m**amy** | tenemos |
                 | wy | m**acie** | tenéis / tienen |
                 | oni/one | m**ają** | tienen |
                 | **Państwo** | m**ają** | tienen |
                 """)
                 st.markdown("*Przykład: Jak masz na imię? Mam na imię Anna.*")
             st.markdown('</div>', unsafe_allow_html=True) # Close content-box for these verbs

        # --- Gender & Pronouns / Cases ---
        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.subheader("Rodzaj i Zaimki (Género y Pronombres)")
             st.markdown("""
                 *   **Rodzaj:** Męski (*on*), Żeński (*ona*), Nijaki (*ono*).
                 *   **Liczba mnoga:**
                     *   **Oni** (Viril): Grupa z min. 1 mężczyzną.
                     *   **One** (Nie-viril): Grupa bez mężczyzn / dzieci / zwierzęta / rzeczy.
             """)
             st.info("💡 Różnica *oni* vs *one* jest ważna w polskim!")
             st.subheader("Wprowadzenie do Przypadków (Intro a los Casos)")
             st.warning("""
             **🚨 Ważne!** Polski ma **7 przypadków** - końcówki słów się zmieniają!
             Na razie poznajemy **Mianownik (Nominativo)** - kto? co? (podmiot).
             *   *To jest **Piotr**.* (Piotr = Mianownik)
             *   *Ona jest **miła**.* (miła = Mianownik)
             """)
             st.markdown('</div>', unsafe_allow_html=True) # Close content-box for grammar notes

        if st.button("➡️ Dalej / Siguiente: Wymowa"):
            st.session_state.page = "Pronunciation Practice"
            st.rerun()

    # == PRONUNCIATION PRACTICE ==
    elif st.session_state.page == "Pronunciation Practice":
        st.title("👂 Ćwiczenia Wymowy / Práctica de Pronunciación")

        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown("Skupmy się na dźwiękach trudnych dla Hiszpanów.")
            sound_pairs = {
                "S vs SZ vs Ś": ([("sok", "[s]"), ("szok", "[ʂ] like 'sh'"), ("siwy", "[ɕ] soft 'sh'")], 1),
                "C vs CZ vs Ć": ([("co", "[ts]"), ("czekam", "[tʂ] like 'ch'"), ("ciocia", "[tɕ] soft 'ch'")], 0),
                "Z vs Ż/RZ vs Ź": ([("zero", "[z]"), ("rzeka", "[ʐ] like French 'j'"), ("źle", "[ʑ] soft French 'j'")], 2),
                "L vs Ł": ([("lato", "[l]"), ("łatwo", "[w] like 'w'")], 1),
                "I vs Y": ([("biły", "[bʲi]"), ("były", "[bɨ] difficult sound")], 1)
            }
            exercise_key = "pronunciation_pairs"
            if exercise_key not in st.session_state.feedback: st.session_state.feedback[exercise_key] = {}

            st.subheader("Rozróżnianie dźwięków / Distinguir sonidos")
            st.markdown("Wybierz słowo, które słyszysz (symulacja).")

            q_num_pron = 1
            for key, (options_with_hints, correct_index) in sound_pairs.items():
                q_key = f"{exercise_key}_{q_num_pron}"
                st.markdown(f"**{q_num_pron}.** Dźwięki: **{key}**")
                st.info(f"🎧 *Wyobraź sobie, że słyszysz jedno z tych słów...*")
                options = [opt[0] for opt in options_with_hints]
                hints_str = " / ".join([f"'{opt[0]}' ({opt[1]})" for opt in options_with_hints])
                st.caption(f"Opcje: {hints_str}")

                if q_key not in st.session_state.feedback[exercise_key]: st.session_state.feedback[exercise_key][q_key] = {'user_choice': None}
                current_choice_pron = st.session_state.feedback[exercise_key][q_key]['user_choice']
                try: index_pron = options.index(current_choice_pron) if current_choice_pron in options else None
                except ValueError: index_pron = None

                user_choice = st.radio("Które słowo?", options, key=q_key, index=index_pron, label_visibility="collapsed", horizontal=True)
                st.session_state.feedback[exercise_key][q_key]['user_choice'] = user_choice

                if user_choice is not None:
                    is_correct_pron = (options.index(user_choice) == correct_index)
                    st.session_state.feedback[exercise_key][q_key]['is_correct'] = is_correct_pron
                    if is_correct_pron: st.success("✅ Dobrze!")
                    else: st.error(f"❌ Poprawnie: '{options[correct_index]}'.")
                st.divider() # Add visual separation between questions
                q_num_pron += 1
            st.markdown('</div>', unsafe_allow_html=True) # Close pronunciation box

        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.subheader("Czytanie na głos / Leer en voz alta")
             st.markdown("Spróbuj przeczytać te słowa.")
             words_to_read = ["Szczecin", "chrząszcz", "źdźbło", "pięćdziesiąt", "dziękuję", "Warszawa", "Wrocław", "Kraków", "Łódź", "Gdańsk"]
             st.table([[word] for word in words_to_read])
             st.info("💡 Nagraj siebie i porównaj z wymową online!")
             st.markdown('</div>', unsafe_allow_html=True) # Close reading box

        if st.button("➡️ Dalej / Siguiente: Dialogi"):
            st.session_state.page = "Dialogues & Context"
            st.rerun()

    # == DIALOGUES & CONTEXT ==
    elif st.session_state.page == "Dialogues & Context":
        st.title("💬 Dialogi i Kontekst / Diálogos y Contexto")

        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("Dialog 1: Formalne przedstawienie")
            st.markdown("""
            **Adam:** Dzień dobry! Nazywam się Adam Kowalski. A pani?
            **Ewa:** Dzień dobry! Nazywam się Ewa Nowak.
            **Adam:** Miło mi.
            **Ewa:** Miło mi.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("Dialog 2: Nieformalne przedstawienie (Ćwiczenie)")
            exercise_key = "dialogue_informal"
            q_key = f"{exercise_key}_fill"
            if q_key not in st.session_state: st.session_state[q_key] = ["", "", ""]

            st.markdown("Uzupełnij dialog:")
            words_bank_d2 = ["Nazywam się", "Jak", "Miło mi"]
            st.info(f"Użyj / Usa: `{', '.join(words_bank_d2)}`")
            solution_d2 = ["Nazywam się", "jak", "Miło mi"]

            st.session_state[q_key][0] = st.text_input("Marek: Cześć! ______ Marek Mazur. [0]", value=st.session_state[q_key][0], key=f"{q_key}_0")
            st.session_state[q_key][1] = st.text_input("Marek: ... A ty, ______ się nazywasz? [1]", value=st.session_state[q_key][1], key=f"{q_key}_1")
            st.markdown("<p style='margin-left: 10px;'>Julia: Cześć! Nazywam się Julia Lewandowska.</p>", unsafe_allow_html=True)
            st.session_state[q_key][2] = st.text_input("Marek: ______. [2]", value=st.session_state[q_key][2], key=f"{q_key}_2")

            if st.button("Sprawdź Dialog 2", key=f"{q_key}_check"):
                 correct_d2 = True; feedback_d2_html = "Wyniki:<ul>"
                 for i in range(len(solution_d2)):
                     user_ans = st.session_state[q_key][i].strip(); correct_ans = solution_d2[i]
                     if user_ans.lower() == correct_ans.lower(): feedback_d2_html += f"<li>Luka {i}: <span style='color:green;'>{user_ans}</span> ✅</li>"
                     else: feedback_d2_html += f"<li>Luka {i}: <span style='color:red;'>{user_ans}</span> ❌ (Poprawnie: {correct_ans})</li>"; correct_d2 = False
                 feedback_d2_html += "</ul>"; st.markdown(feedback_d2_html, unsafe_allow_html=True)
                 st.session_state.feedback[exercise_key] = {'overall_correct': correct_d2}
                 if correct_d2: st.success("🎉 Super!")
                 else: st.warning("Popraw błędy.")
            st.markdown('</div>', unsafe_allow_html=True)


        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.subheader("Ćwiczenie: Pytanie o innych")
             exercise_key = "dialogue_others"; q_key_pronoun = f"{exercise_key}_pronoun"
             if q_key_pronoun not in st.session_state: st.session_state[q_key_pronoun] = {'selected_person': None, 'user_choice': None}

             st.markdown("Wybierz poprawny zaimek:")
             people = {
                 "Andrzej Wajda (mężczyzna)": "on",
                 "Agnieszka & Urszula Radwańska (kobiety)": "one",
                 "Andrzej & Maria Seweryn (mężczyzna i kobieta)": "oni",
                 "Wisława Szymborska (kobieta)": "ona"
             }
             people_keys = list(people.keys())
             selected_person = st.selectbox( "O kim mówimy?", options=[""] + people_keys, key=f"{q_key_pronoun}_select",
                 index=0 if st.session_state[q_key_pronoun]['selected_person'] is None else ([""] + people_keys).index(st.session_state[q_key_pronoun]['selected_person']),
                 on_change=lambda: st.session_state[q_key_pronoun].update({'user_choice': None})
             )
             st.session_state[q_key_pronoun]['selected_person'] = selected_person if selected_person else None

             if selected_person:
                 pronoun_options = ["on", "ona", "ono", "oni", "one"]; correct_pronoun = people[selected_person]
                 verb_form = "nazywa się" if correct_pronoun in ["on", "ona", "ono"] else "nazywają się"
                 current_choice_pronoun = st.session_state[q_key_pronoun].get('user_choice')
                 try: radio_index_pronoun = pronoun_options.index(current_choice_pronoun) if current_choice_pronoun in pronoun_options else None
                 except ValueError: radio_index_pronoun = None
                 user_choice = st.radio(f"Jak ______ {verb_form}?", pronoun_options, key=f"{q_key_pronoun}_radio", index=radio_index_pronoun, horizontal=True)
                 st.session_state[q_key_pronoun]['user_choice'] = user_choice
                 if user_choice is not None:
                      is_correct_pronoun = (user_choice == correct_pronoun)
                      st.session_state.feedback[exercise_key] = {'correctness': is_correct_pronoun}
                      if is_correct_pronoun: st.success(f"✅ Tak! Poprawny zaimek to '{correct_pronoun}'.")
                      else: st.error(f"❌ Niezupełnie. Poprawny zaimek to '{correct_pronoun}'.")
             elif f"{q_key_pronoun}_select" in st.session_state and not selected_person: st.session_state.feedback.pop(exercise_key, None)
             st.markdown('</div>', unsafe_allow_html=True) # Close content-box

        with st.container():
             st.markdown('<div class="content-box">', unsafe_allow_html=True)
             st.subheader("Ćwiczenie: Ułóż zdania / Ordena las frases")
             exercise_key = "dialogue_reorder"; q_key_reorder = f"{exercise_key}_reorder"
             if q_key_reorder not in st.session_state: st.session_state[q_key_reorder] = ""

             words_to_order = ["się", "Adam", "Nazywam"]; correct_order = "Nazywam się Adam"
             st.markdown(f"Ułóż słowa w poprawnej kolejności:")
             if 'shuffled_words_reorder' not in st.session_state: st.session_state['shuffled_words_reorder'] = random.sample(words_to_order, len(words_to_order))
             st.code(f"{' / '.join(st.session_state['shuffled_words_reorder'])}")

             user_order = st.text_input("Wpisz poprawne zdanie:", value=st.session_state[q_key_reorder], key=q_key_reorder + "_input")
             st.session_state[q_key_reorder] = user_order

             if st.button("Sprawdź kolejność", key=f"{q_key_reorder}_check"):
                 normalized_user = user_order.strip().rstrip('.?!').lower(); normalized_correct = correct_order.lower()
                 is_correct_reorder = (normalized_user == normalized_correct)
                 st.session_state.feedback[exercise_key] = {'correctness': is_correct_reorder}
                 if is_correct_reorder: st.success(f"✅ Doskonale! '{correct_order}'.")
                 else: st.error(f"❌ Prawie! Poprawna kolejność: '{correct_order}'.")
             st.markdown('</div>', unsafe_allow_html=True) # Close content-box

        st.success("🎉 **Gratulacje! Ukończyłeś/aś pierwszą lekcję!** 🎉")
        st.markdown("Ćwicz dalej i wracaj do materiałów!")
