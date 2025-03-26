import streamlit as st
import time
import random # Import random for shuffling

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="Polski dla Hiszpanów",
    page_icon="🇵🇱",
    layout="wide"
)

# --- Custom CSS (Embedded) ---
st.markdown("""
<style>
/* Import Old Standard TT font (Regular 400, Bold 700, Italic 400) */
@import url('https://fonts.googleapis.com/css2?family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&display=swap');

/* --- Font --- */
html, body, [class*="st-"], .stMarkdown {
    font-family: 'Old Standard TT', serif !important; /* Use Old Standard TT */
    font-weight: 400; /* Default weight */
}

/* --- Gradient Background with Noise and Animation --- */
@keyframes gradientAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Using a pseudo-element for better control over the background */
body::before {
    content: "";
    position: fixed; /* Fixes the background */
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: -1; /* Places it behind other content */

    /* Gradient */
    background: linear-gradient(135deg, #1C5451, #F1EFE9, #1C5451);
    background-size: 400% 400%; /* Larger size for smoother animation */

    /* Improved CSS Noise simulation */
    background-image: linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px),
                       linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px),
                       linear-gradient(135deg, #1C5451, #F1EFE9, #1C5451);
     background-size: 2px 2px, 2px 2px, 400% 400%; /* Small squares for noise + gradient */


    /* Wiggle Animation */
    animation: gradientAnimation 25s ease infinite; /* Slow movement */
}


/* --- Button Styling --- */
.stButton>button {
    border: 2px solid #1C5451; /* Border color */
    border-radius: 20px;
    padding: 10px 20px;
    background-color: #FFFFFF; /* White background */
    color: #1C5451; /* Text color */
    transition: all 0.3s ease;
    font-family: 'Old Standard TT', serif !important; /* Ensure button uses the font */
    font-weight: 700; /* Use bold weight for buttons */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

.stButton>button:hover {
    background-color: #1C5451;
    color: #FFFFFF;
    border-color: #FFFFFF;
    box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
    transform: translateY(-2px); /* Subtle lift */
}

.stButton>button:active {
    transform: translateY(1px);
    box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
}

/* --- General UI --- */
.stApp {
 /* Ensure the app content allows the fixed background to show */
    background-color: transparent;
}

h1, h2, h3, h4, h5, h6 {
    color: #1C5451; /* Heading color */
    font-family: 'Old Standard TT', serif !important; /* Ensure headings use the font */
    font-weight: 700; /* Bold headings */
}

.stMarkdown {
   color: #333333; /* Default text color */
   line-height: 1.6;
   font-family: 'Old Standard TT', serif !important; /* Ensure markdown uses the font */
}

/* Style specific containers if needed */
.stRadio > label, .stTextInput > label, .stSelectbox > label {
    font-weight: 700; /* Bold labels */
    color: #1C5451;
    font-family: 'Old Standard TT', serif !important;
}

/* Feedback boxes */
.stAlert {
    border-radius: 10px;
    font-family: 'Old Standard TT', serif !important;
}

/* --- Sidebar Styling --- */
.stSidebar {
    /* Convert #D0F117 to RGBA: (208, 241, 23) */
    background-color: rgba(208, 241, 23, 0.85); /* #D0F117 with 85% opacity */
    backdrop-filter: blur(5px);
}
/* Ensure text/elements inside sidebar are readable */
.stSidebar .stMarkdown, .stSidebar .stRadio > label {
     color: #222 !important; /* Darker text color for light green background */
     font-family: 'Old Standard TT', serif !important;
}
.stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar strong {
    color: #000 !important; /* Black for titles/bold in sidebar */
     font-family: 'Old Standard TT', serif !important;
}
.stSidebar .stButton>button {
     font-family: 'Old Standard TT', serif !important;
     font-weight: 700;
     border: 2px solid #333; /* Dark border */
     background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent white */
     color: #333; /* Dark text */
}
.stSidebar .stButton>button:hover {
     background-color: #333; /* Dark background on hover */
     color: #D0F117; /* Bright text on hover */
     border-color: #D0F117;
}


</style>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
if 'page' not in st.session_state:
    st.session_state.page = "Introduction"
if 'feedback' not in st.session_state:
    st.session_state.feedback = {} # To store feedback for exercises

# --- Navigation ---
st.sidebar.title("🇵🇱 Nawigacja Lekcji 🇪🇸")
pages = ["Introduction", "Alphabet", "Vocabulary & Phrases", "Grammar Focus", "Pronunciation Practice", "Dialogues & Context"]
page_emojis = ["👋", "🔤", "🗣️", "✍️", "👂", "💬"]

for page, emoji in zip(pages, page_emojis):
    if st.sidebar.button(f"{emoji} {page}"):
        st.session_state.page = page
        st.session_state.feedback = {} # Clear feedback when changing pages
        st.rerun() # Use st.rerun()

# --- Page Content ---

# == INTRODUCTION ==
if st.session_state.page == "Introduction":
    st.title("👋 Witaj! ¡Bienvenido/a al Polaco!")
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
    if st.button("➡️ Dalej / Siguiente: Alfabet"):
        st.session_state.page = "Alphabet"
        st.rerun()

# == ALPHABET ==
elif st.session_state.page == "Alphabet":
    st.title("🔤 Polski Alfabet / El Alfabeto Polaco")
    st.markdown("Oto polski alfabet z przykładami i wymową fonetyczną (uproszczoną).")
    st.markdown("Aquí tienes el alfabeto polaco con ejemplos y pronunciación fonética (simplificada).")

    # Simplified Alphabet Table (Focus on differences)
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

    st.subheader("👂 Ćwiczenie Wymowy / Ejercicio de Pronunciación")
    st.markdown("Wybierz słowo, które słyszysz (symulacja). Elige la palabra que oyes (simulado).")

    pairs = {
        "s / sz / ś": (["stop", "szok", "środa"], 2), # Correct index
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
        q_key = f"{exercise_key}_{q_num}"
        st.markdown(f"**{q_num}.** Dźwięk / Sonido: **{key}**")
        st.info(f"🎧 *Wyobraź sobie, że słyszysz jedno z tych słów... / Imagina que oyes una de estas palabras...*")

        # Retrieve previous answer choice for this question if it exists
        current_choice_index = None
        if q_key in st.session_state.feedback and st.session_state.feedback[q_key] is not None and 'user_choice' in st.session_state.feedback[q_key]:
             try:
                 current_choice_index = options.index(st.session_state.feedback[q_key]['user_choice'])
             except ValueError:
                 current_choice_index = None # Reset if previous choice isn't valid anymore

        user_choice = st.radio(f"Które słowo słyszysz? / ¿Qué palabra oyes?", options, key=q_key, index=current_choice_index, label_visibility="collapsed")

        # Store feedback including the user's choice
        if q_key not in st.session_state.feedback:
            st.session_state.feedback[q_key] = {}

        if user_choice is not None:
            is_correct = options.index(user_choice) == correct_index
            st.session_state.feedback[q_key]['user_choice'] = user_choice
            st.session_state.feedback[q_key]['is_correct'] = is_correct

            if is_correct:
                st.success("✅ Dobrze! ¡Correcto!")
            else:
                st.error(f"❌ Spróbuj ponownie. La respuesta correcta era '{options[correct_index]}'. Intenta de nuevo.")
        # If user_choice is None (initial state), don't display feedback yet

        q_num += 1


    if st.button("➡️ Dalej / Siguiente: Słownictwo"):
        st.session_state.page = "Vocabulary & Phrases"
        st.rerun()

# == VOCABULARY & PHRASES ==
elif st.session_state.page == "Vocabulary & Phrases":
    st.title("🗣️ Podstawowe Słownictwo i Zwroty / Vocabulario y Frases Básicas")

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
    *   **Jak pan się nazywa?** - ¿Cómo se llama usted? (Formal - masculino - *Pan*)
    *   **Jak pani się nazywa?** - ¿Cómo se llama usted? (Formal - femenino - *Pani*)
    *   **Nazywam się...** - Me llamo... (np. *Nazywam się Adam.*)
    *   **Jak masz na imię?** - ¿Cuál es tu nombre (de pila)? (Informal - *ty*)
    *   **Jak pan ma na imię?** - ¿Cuál es su nombre (de pila)? (Formal - *Pan*)
    *   **Jak pani ma na imię?** - ¿Cuál es su nombre (de pila)? (Formal - *Pani*)
    *   **Mam na imię...** - Mi nombre (de pila) es... (np. *Mam na imię Ewa.*)
    *   **Miło mi.** - Encantado/a. / Mucho gusto.
    """)
    st.info("💡 **Pan/Pani vs Ty:** Similar a *Usted vs Tú*. *Pan* (Sr.), *Pani* (Sra./Srta.). Se usan con la 3ª persona del singular del verbo. *Ty* (tú) se usa con la 2ª persona del singular.")

    st.subheader("Zaimki Osobowe / Pronombres Personales")
    st.markdown("""
    *   **ja** - yo
    *   **ty** - tú
    *   **on** - él
    *   **ona** - ella
    *   **ono** - ello (neutro)
    *   **my** - nosotros/as
    *   **wy** - vosotros/as / ustedes (informal plural)
    *   **oni** - ellos (si hay al menos un hombre en el grupo) - *Viril*
    *   **one** - ellas / ellos (si no hay hombres, o para cosas/animales) - *No viril*
    *   **Pan** - usted (masculino)
    *   **Pani** - usted (femenino)
    *   **Państwo** - ustedes (formal, grupo mixto o Sres. y Sras.)
    """)

    st.subheader("📝 Ćwiczenia / Ejercicios")
    exercise_key = "vocab_phrases"
    if exercise_key not in st.session_state.feedback:
         st.session_state.feedback[exercise_key] = {}

    # --- Exercise 1: Matching ---
    st.markdown("**1. Dopasuj polskie zwroty do hiszpańskich tłumaczeń. / Empareja las frases polacas con sus traducciones españolas.**")
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

    # Shuffle Spanish translations for the quiz only if not already done/stored
    if q1_key not in st.session_state:
        st.session_state[q1_key] = {}
    if 'shuffled_spanish' not in st.session_state[q1_key]:
        st.session_state[q1_key]['shuffled_spanish'] = random.sample(spanish_translations, len(spanish_translations))
    if 'user_matches' not in st.session_state[q1_key]:
         st.session_state[q1_key]['user_matches'] = {phrase: "" for phrase in polish_phrases} # Initialize choices


    shuffled_spanish = st.session_state[q1_key]['shuffled_spanish']
    cols1 = st.columns(2)
    with cols1[0]:
        st.markdown("**Polski:**")
        for i, phrase in enumerate(polish_phrases):
            # Get current index based on stored choice
            current_selection = st.session_state[q1_key]['user_matches'].get(phrase, "")
            try:
                 sel_index = ([""] + shuffled_spanish).index(current_selection)
            except ValueError:
                 sel_index = 0 # Default to empty if previous selection is invalid

            # Update selection in session state when user changes it
            st.session_state[q1_key]['user_matches'][phrase] = st.selectbox(
                f"{i+1}. {phrase}",
                options=[""] + shuffled_spanish,
                key=f"{q1_key}_{i}",
                index=sel_index, # Use stored selection index
                label_visibility="collapsed"
            )

    with cols1[1]:
         st.markdown("**Opcje (Español):**")
         for trans in shuffled_spanish:
             st.write(f"- {trans}")


    if st.button("Sprawdź dopasowanie / Comprobar emparejamiento", key=f"{q1_key}_check"):
        correct_count_match = 0
        all_correct_match = True
        feedback_match_html = "<ul>"
        user_matches = st.session_state[q1_key]['user_matches']
        for polish, user_spanish in user_matches.items():
            correct_spanish = match_options[polish]
            if user_spanish == correct_spanish:
                feedback_match_html += f"<li>'{polish}' = '{user_spanish}' ✅</li>"
                correct_count_match += 1
            elif not user_spanish: # Check if empty string
                 feedback_match_html += f"<li>'{polish}' = ? (Nie wybrano / No seleccionado)</li>"
                 all_correct_match = False
            else:
                feedback_match_html += f"<li>'{polish}' = <span style='color:red;'>'{user_spanish}'</span> ❌ (Poprawnie / Correcto: '{correct_spanish}')</li>"
                all_correct_match = False
        feedback_match_html += "</ul>"
        st.markdown(feedback_match_html, unsafe_allow_html=True)
        st.session_state.feedback[exercise_key][q1_key] = all_correct_match # Store overall result

        if all_correct_match:
            st.success("🎉 Wszystkie pary poprawne! / ¡Todos los pares correctos!")
        else:
            st.warning(f"Masz {correct_count_match} z {len(polish_phrases)} poprawnych par. / Tienes {correct_count_match} de {len(polish_phrases)} pares correctos.")


    # --- Exercise 2: Fill-in-the-blanks (from PDF p.1) ---
    st.markdown("**2. Uzupełnij dialog wyrazami z ramki. / Completa el diálogo con las palabras del recuadro.**")
    q2_key = f"{exercise_key}_q2"
    words_bank = ["Miło", "pan", "Nazywam się", "pani", "dobry"]
    st.info(f"Ramka / Recuadro: `{', '.join(words_bank)}`")

    solution = ["dobry", "pani", "dobry", "Nazywam się", "pan", "Miło"]

    # Use session state to store user inputs for this exercise
    if q2_key not in st.session_state:
        st.session_state[q2_key] = [""] * len(solution)

    # Display inputs - simplified presentation
    st.markdown("**Dialog:**")
    st.session_state[q2_key][0] = st.text_input(f"A: Dzień ______! [0]", value=st.session_state[q2_key][0], key=f"{q2_key}_0")
    st.session_state[q2_key][1] = st.text_input(f"A: ... Jak ______ się nazywa? [1]", value=st.session_state[q2_key][1], key=f"{q2_key}_1")
    st.session_state[q2_key][2] = st.text_input(f"B: Dzień ______! [2]", value=st.session_state[q2_key][2], key=f"{q2_key}_2")
    st.session_state[q2_key][3] = st.text_input(f"B: ... ______ Piotr Nowicki. [3]", value=st.session_state[q2_key][3], key=f"{q2_key}_3")
    st.session_state[q2_key][4] = st.text_input(f"B: ... Jak ______ się nazywa? [4]", value=st.session_state[q2_key][4], key=f"{q2_key}_4")
    st.text("A: Anna Kamińska.")
    st.session_state[q2_key][5] = st.text_input(f"B: ______ mi. [5]", value=st.session_state[q2_key][5], key=f"{q2_key}_5")


    if st.button("Sprawdź odpowiedzi / Comprobar respuestas (Fill-in)", key=f"{q2_key}_check"):
        correct_count = 0
        all_correct = True
        # Reconstruct dialogue with feedback
        filled_dialog = [
             f"A: Dzień {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][0].strip() + '</span>' if st.session_state[q2_key][0].strip().lower() == solution[0].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][0].strip() + '</span>' + f' ({solution[0]})'}! Jak {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][1].strip() + '</span>' if st.session_state[q2_key][1].strip().lower() == solution[1].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][1].strip() + '</span>' + f' ({solution[1]})'} się nazywa?",
             f"B: Dzień {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][2].strip() + '</span>' if st.session_state[q2_key][2].strip().lower() == solution[2].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][2].strip() + '</span>' + f' ({solution[2]})'}! {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][3].strip() + '</span>' if st.session_state[q2_key][3].strip().lower() == solution[3].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][3].strip() + '</span>' + f' ({solution[3]})'} Piotr Nowicki. Jak {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][4].strip() + '</span>' if st.session_state[q2_key][4].strip().lower() == solution[4].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][4].strip() + '</span>' + f' ({solution[4]})'} się nazywa?",
             "A: Anna Kamińska.",
             f"B: {'<span style=\'color:green; font-weight:700;\'>' + st.session_state[q2_key][5].strip() + '</span>' if st.session_state[q2_key][5].strip().lower() == solution[5].lower() else '<span style=\'color:red;\'>' + st.session_state[q2_key][5].strip() + '</span>' + f' ({solution[5]})'} mi."
         ]

        # Check correctness
        for i in range(len(solution)):
            if st.session_state[q2_key][i].strip().lower() == solution[i].lower():
                correct_count +=1
            else:
                all_correct = False

        st.markdown("### Wyniki / Resultados:")
        st.markdown("\n".join(filled_dialog), unsafe_allow_html=True)
        st.session_state.feedback[exercise_key][q2_key] = all_correct # Store overall result

        if all_correct:
            st.success("🎉 Gratulacje! Wszystko poprawnie! / ¡Felicidades! ¡Todo correcto!")
        else:
            st.warning(f"Masz {correct_count} z {len(solution)} poprawnych odpowiedzi. Spróbuj jeszcze raz! / Tienes {correct_count} de {len(solution)} respuestas correctas. ¡Inténtalo de nuevo!")


    # --- Exercise 3: Formal/Informal ---
    st.markdown("**3. Formalnie czy nieformalnie? / ¿Formal o informal?**")
    q3_key = f"{exercise_key}_q3"
    scenarios = {
        "Spotykasz profesora na uniwersytecie. / Encuentras a tu profesor en la universidad.": "Dzień dobry!",
        "Witasz się z kolegą. / Saludas a un amigo.": "Cześć!",
        "Żegnasz się z dyrektorem firmy. / Te despides del director de la empresa.": "Do widzenia!",
        "Mówisz 'do zobaczenia' przyjaciółce. / Dices 'hasta luego' a una amiga.": "Na razie!",
    }
    scenario_keys = list(scenarios.keys())

    # Store selected scenario and choice in session state
    if q3_key not in st.session_state:
        st.session_state[q3_key] = {'selected_scenario': None, 'user_choice': None}

    selected_scenario = st.selectbox(
        "Wybierz sytuację / Elige la situación:",
        options=[""] + scenario_keys, # Add empty option for placeholder
        key=f"{q3_key}_select",
        index=0 if st.session_state[q3_key]['selected_scenario'] is None else ([""] + scenario_keys).index(st.session_state[q3_key]['selected_scenario']),
        on_change=lambda: st.session_state[q3_key].update({'user_choice': None}) # Reset choice on scenario change
    )
    st.session_state[q3_key]['selected_scenario'] = selected_scenario if selected_scenario else None # Update state


    if selected_scenario:
         correct_greeting = scenarios[selected_scenario]
         greeting_options = ["Dzień dobry!", "Cześć!", "Do widzenia!", "Na razie!"]
         # Ensure correct answer is always an option
         options_for_radio = list(set(random.sample(greeting_options, 3) + [correct_greeting])) # Ensure 3 unique + correct
         random.shuffle(options_for_radio)

         # Restore previous choice index if available
         current_choice_q3 = st.session_state[q3_key].get('user_choice')
         try:
             radio_index_q3 = options_for_radio.index(current_choice_q3) if current_choice_q3 in options_for_radio else None
         except ValueError:
             radio_index_q3 = None


         user_choice = st.radio(
             "Co powiesz? / ¿Qué dices?",
             options_for_radio,
             key=f"{q3_key}_radio",
             index=radio_index_q3
         )
         st.session_state[q3_key]['user_choice'] = user_choice # Store choice

         # Display feedback based on stored choice
         if user_choice is not None:
             is_correct_q3 = (user_choice == correct_greeting)
             st.session_state.feedback[exercise_key][q3_key] = is_correct_q3 # Store correctness

             if is_correct_q3:
                 st.success("✅ Zgadza się! ¡Correcto!")
             else:
                 st.error(f"❌ W tej sytuacji lepiej powiedzieć '{correct_greeting}'. / En esta situación es mejor decir '{correct_greeting}'.")

    elif f"{q3_key}_select" in st.session_state and not selected_scenario:
         # Clear feedback if placeholder selected
         st.session_state.feedback[exercise_key].pop(q3_key, None)


    if st.button("➡️ Dalej / Siguiente: Gramatyka"):
        st.session_state.page = "Grammar Focus"
        st.rerun()

# == GRAMMAR FOCUS ==
elif st.session_state.page == "Grammar Focus":
    st.title("✍️ Gramatyka / Gramática")
    st.info("💡 Pamiętaj: *Pan/Pani* używają formy czasownika jak *on/ona/ono* (3 os. l.poj.). / Recuerda: *Pan/Pani* usan la forma verbal de *on/ona/ono* (3ª pers. sing.).")

    # --- Mówić ---
    st.subheader("Czasownik *mówić* (hablar)")
    st.markdown("""
    | Osoba (Persona) | Czasownik (Verbo) | Tłumaczenie (Traducción) |
    |---|---|---|
    | ja (yo) | mów**ię** | hablo |
    | ty (tú) | mów**isz** | hablas |
    | on/ona/ono (él/ella/ello) | mów**i** | habla |
    | **Pan/Pani** (usted) | mów**i** | habla |
    | my (nosotros/as) | mów**imy** | hablamos |
    | wy (vosotros/as / ustedes inf.) | mów**icie** | habláis / hablan |
    | oni/one (ellos/as) | mów**ią** | hablan |
    | **Państwo** (ustedes form.) | mów**ią** | hablan |
    """)
    st.markdown("**Przykład (Ejemplo):** *Ona mówi po francusku.* (Ella habla francés.) *Ja nie mówię.* (Yo no hablo.)")

    # --- Exercise: Mówić (PDF p.1) ---
    st.markdown("**Ćwiczenie: Uzupełnij zdania poprawną formą czasownika MÓWIĆ.**")
    st.markdown("**Ejercicio: Completa las frases con la forma correcta del verbo MÓWIĆ.**")
    exercise_key = "grammar_mowic"
    # Use session state for inputs - Ensure the main key exists
    if exercise_key not in st.session_state:
        st.session_state[exercise_key] = {}
    if 'inputs' not in st.session_state[exercise_key]:
        st.session_state[exercise_key]['inputs'] = {}


    mowic_sentences = [
        ("Czy ______ po polsku? (ty)", ["mówisz"]),
        ("______ po angielsku. (my)", ["mówimy"]),
        ("Oni nie ______ po francusku, ale ______ po polsku. (oni / oni)", ["mówią", "mówią"]),
        ("On ______ trochę po rosyjsku, ale ja nie ______. (on / ja)", ["mówi", "mówię"]),
        ("Czy ______ po niemiecku? (wy)", ["mówicie"]),
        ("One nie ______ po hiszpańsku. (one)", ["mówią"]),
        ("Czy ona ______ po polsku?", ["mówi"]), # Pronoun inferred
        ("Nie ______ po włosku. (ja)", ["mówię"])
    ]

    # Initialize inputs in session state if not present
    for i in range(len(mowic_sentences)):
        q_key = f"{exercise_key}_{i}"
        num_blanks = mowic_sentences[i][0].count("______")
        if q_key not in st.session_state[exercise_key]['inputs']:
             st.session_state[exercise_key]['inputs'][q_key] = [""] * num_blanks


    # Display inputs using session state values
    for i, (sentence, correct_forms) in enumerate(mowic_sentences):
        q_key = f"{exercise_key}_{i}"
        num_blanks = sentence.count("______")
        prompt = sentence.replace("______", "_______") # Visual placeholder

        if num_blanks == 1:
            st.session_state[exercise_key]['inputs'][q_key][0] = st.text_input(f"{i+1}. {prompt}", value=st.session_state[exercise_key]['inputs'][q_key][0], key=q_key, placeholder="Wpisz formę")
        elif num_blanks == 2:
             cols = st.columns(2)
             with cols[0]:
                 st.session_state[exercise_key]['inputs'][q_key][0] = st.text_input(f"{i+1}a. {prompt} (luka 1)", value=st.session_state[exercise_key]['inputs'][q_key][0], key=f"{q_key}_a", placeholder="Forma 1")
             with cols[1]:
                 st.session_state[exercise_key]['inputs'][q_key][1] = st.text_input(f"{i+1}b. {prompt} (luka 2)", value=st.session_state[exercise_key]['inputs'][q_key][1], key=f"{q_key}_b", placeholder="Forma 2")


    if st.button("Sprawdź MÓWIĆ / Comprobar MÓWIĆ", key=f"{exercise_key}_check"):
         all_correct_mowic = True
         feedback_html_mowic = "<ul>"
         for i, (sentence, correct_forms_list) in enumerate(mowic_sentences):
              q_key = f"{exercise_key}_{i}"
              user_answers = [ans.strip().lower() for ans in st.session_state[exercise_key]['inputs'][q_key]]
              correct_forms_list_lower = [f.lower() for f in correct_forms_list]

              sentence_display = sentence
              correct_in_sentence = True
              # Replace blanks with feedback spans
              for j in range(len(correct_forms_list_lower)):
                   user_ans = user_answers[j]
                   correct_ans = correct_forms_list_lower[j]
                   if user_ans == correct_ans:
                       replacement = f"<span style='color:green; font-weight:700;'>{user_ans}</span>"
                   else:
                       replacement = f"<span style='color:red;'>{user_ans}</span> (Poprawnie: {correct_ans})"
                       correct_in_sentence = False
                       all_correct_mowic = False
                   # Use a placeholder that won't be replaced again in the same loop
                   sentence_display = sentence_display.replace("______", f"__PLACEHOLDER_{j}__", 1)

              # Now replace placeholders with actual feedback
              for j in range(len(correct_forms_list_lower)):
                   user_ans = user_answers[j]
                   correct_ans = correct_forms_list_lower[j]
                   if user_ans == correct_ans:
                        replacement = f"<span style='color:green; font-weight:700;'>{user_ans}</span>"
                   else:
                        replacement = f"<span style='color:red;'>{user_ans}</span> (Poprawnie: {correct_ans})"
                   sentence_display = sentence_display.replace(f"__PLACEHOLDER_{j}__", replacement)


              feedback_html_mowic += f"<li>{sentence_display} {'✅' if correct_in_sentence else '❌'}</li>"

         feedback_html_mowic += "</ul>"
         st.markdown(feedback_html_mowic, unsafe_allow_html=True)
         st.session_state.feedback[exercise_key] = {'all_correct': all_correct_mowic} # Store overall result

         if all_correct_mowic:
             st.success("🎉 Świetnie! Czasownik 'mówić' opanowany! / ¡Genial! ¡Verbo 'mówić' dominado!")
         else:
             st.warning("Popraw błędy i spróbuj ponownie. / Corrige los errores e inténtalo de nuevo.")


    # --- Nazywać się & Mieć ---
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


    # --- Gender & Pronouns ---
    st.subheader("Rodzaj i Zaimki (Género y Pronombres)")
    st.markdown("""
        *   **Rodzaj (Género):** Męski (*on* - masculino), Żeński (*ona* - femenino), Nijaki (*ono* - neutro).
        *   **Liczba mnoga (Plural):**
            *   **Oni** (Viril): Używany dla grup ludzi, jeśli jest w nich **choć jeden mężczyzna**. (Se usa para grupos de personas si hay **al menos un hombre**.) - *Oni mówią.* (Ellos hablan.)
            *   **One** (Nie-viril / Non-virile): Używany dla grup składających się **tylko z kobiet**, lub dla **dzieci, zwierząt, rzeczy**. (Se usa para grupos de **solo mujeres**, o para **niños, animales, cosas**.) - *One mówią.* (Ellas/Esos hablan.)
    """)
    st.info("💡 Zwróć uwagę na różnicę *oni* vs *one* - nie ma jej w hiszpańskim 'ellos/ellas' w ten sam sposób. / Presta atención a la diferencia *oni* vs *one* - no existe de la misma manera en español.")

    # --- Introduction to Cases ---
    st.subheader("Wprowadzenie do Przypadków (Introducción a los Casos)")
    st.warning("""
    **🚨 Ważne! / ¡Importante!** Język polski ma **7 przypadków**. Oznacza to, że **końcówki rzeczowników, przymiotników i zaimków zmieniają się** w zależności od ich roli w zdaniu (podmiot, dopełnienie, miejsce itp.).
    El polaco tiene **7 casos**. Esto significa que **las terminaciones de sustantivos, adjetivos y pronombres cambian** según su función en la frase (sujeto, objeto, lugar, etc.).

    Na razie skupiamy się na **Mianowniku (Nominativo)** - przypadek podmiotu.
    Por ahora, nos centramos en el **Nominativo** - el caso del sujeto.
    *   *To jest **Piotr**.* (Este es Piotr.) - *Piotr* jest podmiotem (sujeto).
    *   *Ona jest **miła**.* (Ella es amable.) - *Ona* (podmiot), *miła* (adjetivo en Nominativo).

    Czasami używamy też **Narzędnika (Instrumental)**, np.
    A veces también usamos el **Instrumental**, p.ej.:
    *   *Nazywam się **Adamem**.* (Me llamo Adam.) - Bardziej gramatycznie / Más gramatical.
    *   *Jestem **studentem**.* (Soy estudiante.)

    Nie martw się! Będziemy się tego uczyć stopniowo.
    ¡No te preocupes! Lo aprenderemos gradualmente.
    """)

    if st.button("➡️ Dalej / Siguiente: Wymowa"):
        st.session_state.page = "Pronunciation Practice"
        st.rerun()

# == PRONUNCIATION PRACTICE ==
elif st.session_state.page == "Pronunciation Practice":
    st.title("👂 Ćwiczenia Wymowy / Práctica de Pronunciación")
    st.markdown("Skupmy się na dźwiękach trudnych dla Hiszpanów. / Centrémonos en los sonidos difíciles para hispanohablantes.")

    sound_pairs = {
        "S vs SZ vs Ś": ([("sok", "[s] como en 'sol'"), ("szok", "[ʂ] como 'sh' inglesa"), ("siwy", "[ɕ] 'sh' suave/palatal")], 1), # 'ś' often via 'si'
        "C vs CZ vs Ć": ([("co", "[ts] como 'tsé-tsé'"), ("czekam", "[tʂ] como 'ch' inglesa"), ("ciocia", "[tɕ] 'ch' suave/palatal")], 0), # 'ć' often via 'ci'
        "Z vs Ż/RZ vs Ź": ([("zero", "[z] como 's' sonora ('mismo')"), ("rzeka", "[ʐ] como 'j' francesa"), ("źle", "[ʑ] 'j' francesa suave/palatal")], 2),
        "L vs Ł": ([("lato", "[l] como 'l' española"), ("łatwo", "[w] como 'w' inglesa")], 1),
        "I vs Y": ([("biły", "[bʲi] 'i' española, suaviza 'b'"), ("były", "[bɨ] sonido 'y' difícil")], 1) # Example showing softening effect of 'i'
    }
    exercise_key = "pronunciation_pairs"
    if exercise_key not in st.session_state.feedback:
         st.session_state.feedback[exercise_key] = {}

    st.subheader("Rozróżnianie dźwięków / Distinguir sonidos")
    st.markdown("Wybierz słowo, które słyszysz (symulacja). / Elige la palabra que oyes (simulado).")

    q_num_pron = 1
    for key, (options_with_hints, correct_index) in sound_pairs.items():
        q_key = f"{exercise_key}_{q_num_pron}"
        st.markdown(f"**{q_num_pron}.** Dźwięki / Sonidos: **{key.replace('_', ' ')}**") # Display key nicely
        st.info(f"🎧 *Wyobraź sobie, że słyszysz jedno z tych słów... / Imagina que oyes una de estas palabras...*")

        options = [opt[0] for opt in options_with_hints]
        hints_str = " / ".join([f"'{opt[0]}' ({opt[1]})" for opt in options_with_hints])
        st.caption(f"Opcje / Opciones: {hints_str}")

        # Store/retrieve choice for persistence
        if q_key not in st.session_state.feedback[exercise_key]:
             st.session_state.feedback[exercise_key][q_key] = {'user_choice': None}

        current_choice_pron = st.session_state.feedback[exercise_key][q_key]['user_choice']
        try:
            index_pron = options.index(current_choice_pron) if current_choice_pron in options else None
        except ValueError:
            index_pron = None

        user_choice = st.radio(
            f"Które słowo słyszysz? / ¿Qué palabra oyes?",
            options,
            key=q_key,
            index=index_pron,
            label_visibility="collapsed"
        )
        st.session_state.feedback[exercise_key][q_key]['user_choice'] = user_choice # Update stored choice


        # Display feedback based on stored choice
        if user_choice is not None:
            is_correct_pron = (options.index(user_choice) == correct_index)
            st.session_state.feedback[exercise_key][q_key]['is_correct'] = is_correct_pron

            if is_correct_pron:
                st.success("✅ Dobrze! ¡Correcto!")
            else:
                st.error(f"❌ Spróbuj ponownie. La respuesta correcta era '{options[correct_index]}'. Intenta de nuevo.")

        q_num_pron += 1

    st.subheader("Czytanie na głos / Leer en voz alta")
    st.markdown("Spróbuj przeczytać te słowa. Zwróć uwagę na trudne dźwięki.")
    st.markdown("Intenta leer estas palabras. Presta atención a los sonidos difíciles.")
    words_to_read = [
        "Szczecin", "chrząszcz", "źdźbło", "pięćdziesiąt", "dziękuję",
        "Warszawa", "Wrocław", "Kraków", "Łódź", "Gdańsk" # Cities from PDF
    ]
    st.table([[word] for word in words_to_read]) # Display as a table for better spacing
    st.info("💡 Nagraj siebie i porównaj z wymową native speakera online! / ¡Grábate y compara con la pronunciación de un hablante nativo online!")


    if st.button("➡️ Dalej / Siguiente: Dialogi"):
        st.session_state.page = "Dialogues & Context"
        st.rerun()

# == DIALOGUES & CONTEXT ==
elif st.session_state.page == "Dialogues & Context":
    st.title("💬 Dialogi i Kontekst / Diálogos y Contexto")

    st.subheader("Dialog 1: Formalne przedstawienie (z PDF str. 5)")
    st.markdown("Diálogo 1: Presentación formal (de la pág. 5 del PDF)")
    st.markdown("""
    **Adam:** Dzień dobry! Nazywam się Adam Kowalski. A pani?
    **Ewa:** Dzień dobry! Nazywam się Ewa Nowak.
    **Adam:** Miło mi.
    **Ewa:** Miło mi.
    """)

    st.subheader("Dialog 2: Nieformalne przedstawienie (z PDF str. 5)")
    st.markdown("Diálogo 2: Presentación informal (de la pág. 5 del PDF)")
    exercise_key = "dialogue_informal"
    q_key = f"{exercise_key}_fill"
    # Session state for inputs
    if q_key not in st.session_state:
        st.session_state[q_key] = ["", "", ""]


    st.markdown("Uzupełnij dialog / Completa el diálogo:")
    words_bank_d2 = ["Nazywam się", "Jak", "Miło mi"]
    st.info(f"Użyj / Usa: `{', '.join(words_bank_d2)}`")

    st.session_state[q_key][0] = st.text_input("Marek: Cześć! ______ Marek Mazur. [0]", value=st.session_state[q_key][0], key=f"{q_key}_0")
    st.session_state[q_key][1] = st.text_input("Marek: ... A ty, ______ się nazywasz? [1]", value=st.session_state[q_key][1], key=f"{q_key}_1")
    st.markdown("Julia: Cześć! Nazywam się Julia Lewandowska.")
    st.session_state[q_key][2] = st.text_input("Marek: ______. [2]", value=st.session_state[q_key][2], key=f"{q_key}_2")


    solution_d2 = ["Nazywam się", "jak", "Miło mi"] # Lowercase 'jak' typical

    if st.button("Sprawdź Dialog 2 / Comprobar Diálogo 2", key=f"{q_key}_check"):
         correct_d2 = True
         feedback_d2_html = "Wyniki / Resultados:<ul>"
         for i in range(len(solution_d2)):
             user_ans = st.session_state[q_key][i].strip()
             correct_ans = solution_d2[i]
             if user_ans.lower() == correct_ans.lower():
                 feedback_d2_html += f"<li>Luka {i}: <span style='color:green; font-weight:700;'>{user_ans}</span> ✅</li>"
             else:
                 feedback_d2_html += f"<li>Luka {i}: <span style='color:red;'>{user_ans}</span> ❌ (Poprawnie: {correct_ans})</li>"
                 correct_d2 = False
         feedback_d2_html += "</ul>"

         st.markdown(feedback_d2_html, unsafe_allow_html=True)
         st.session_state.feedback[exercise_key] = {'overall_correct': correct_d2} # Store overall result

         if correct_d2:
             st.success("🎉 Super!")
         else:
             st.warning("Popraw błędy. / Corrige los errores.")


    st.subheader("Ćwiczenie: Pytanie o innych (z PDF str. 6, 7)")
    st.markdown("Ejercicio: Preguntar por otros (de las pág. 6, 7 del PDF)")
    exercise_key = "dialogue_others"
    q_key_pronoun = f"{exercise_key}_pronoun"
     # Session state for this exercise
    if q_key_pronoun not in st.session_state:
        st.session_state[q_key_pronoun] = {'selected_person': None, 'user_choice': None}


    st.markdown("Wybierz poprawny zaimek / Elige el pronombre correcto:")
    people = {
        "Andrzej Wajda (mężczyzna / hombre)": "on",
        "Agnieszka Radwańska i Urszula Radwańska (kobiety / mujeres)": "one",
        "Andrzej Seweryn i Maria Seweryn (mężczyzna i kobieta / hombre y mujer)": "oni",
        "Wisława Szymborska (kobieta / mujer)": "ona"
    }
    people_keys = list(people.keys())

    selected_person = st.selectbox(
        "O kim mówimy? / ¿De quién hablamos?",
        options=[""] + people_keys,
        index=0 if st.session_state[q_key_pronoun]['selected_person'] is None else ([""] + people_keys).index(st.session_state[q_key_pronoun]['selected_person']),
        key=f"{q_key_pronoun}_select",
        on_change=lambda: st.session_state[q_key_pronoun].update({'user_choice': None}) # Reset choice on change
    )
    st.session_state[q_key_pronoun]['selected_person'] = selected_person if selected_person else None


    if selected_person:
        pronoun_options = ["on", "ona", "ono", "oni", "one"]
        correct_pronoun = people[selected_person]
        verb_form = "nazywa się" if correct_pronoun in ["on", "ona", "ono"] else "nazywają się"

        # Restore previous choice index
        current_choice_pronoun = st.session_state[q_key_pronoun].get('user_choice')
        try:
            radio_index_pronoun = pronoun_options.index(current_choice_pronoun) if current_choice_pronoun in pronoun_options else None
        except ValueError:
            radio_index_pronoun = None

        user_choice = st.radio(
            f"Jak ______ {verb_form}?",
             pronoun_options,
             key=f"{q_key_pronoun}_radio",
             index=radio_index_pronoun
        )
        st.session_state[q_key_pronoun]['user_choice'] = user_choice # Store choice


        # Display feedback based on stored choice
        if user_choice is not None:
             is_correct_pronoun = (user_choice == correct_pronoun)
             st.session_state.feedback[exercise_key] = {'correctness': is_correct_pronoun} # Store result

             if is_correct_pronoun:
                 st.success(f"✅ Tak! Poprawny zaimek to '{correct_pronoun}'. / ¡Sí! El pronombre correcto es '{correct_pronoun}'.")
             else:
                 st.error(f"❌ Niezupełnie. Dla '{selected_person}' poprawny zaimek to '{correct_pronoun}'. / No exactamente. Para '{selected_person}' el pronombre correcto es '{correct_pronoun}'.")
    elif f"{q_key_pronoun}_select" in st.session_state and not selected_person:
         st.session_state.feedback.pop(exercise_key, None) # Clear feedback


    st.subheader("Ćwiczenie: Ułóż zdania / Ordena las frases")
    exercise_key = "dialogue_reorder"
    q_key_reorder = f"{exercise_key}_reorder"
    # Session state for input
    if q_key_reorder not in st.session_state:
        st.session_state[q_key_reorder] = ""

    words_to_order = ["się", "Adam", "Nazywam"]
    correct_order = "Nazywam się Adam"
    st.markdown(f"Ułóż słowa w poprawnej kolejności: / Ordena las palabras en el orden correcto:")
    # Shuffle words for display, store shuffled version if not already stored
    if 'shuffled_words' not in st.session_state:
         st.session_state['shuffled_words'] = random.sample(words_to_order, len(words_to_order))
    st.code(f"{' / '.join(st.session_state['shuffled_words'])}")


    user_order = st.text_input(
        "Wpisz poprawne zdanie: / Escribe la frase correcta:",
        value=st.session_state[q_key_reorder], # Use stored value
        key=q_key_reorder + "_input" # Use unique key for widget
    )
    st.session_state[q_key_reorder] = user_order # Update stored value


    if st.button("Sprawdź kolejność / Comprobar orden", key=f"{q_key_reorder}_check"):
        normalized_user = user_order.strip().rstrip('.?!').lower()
        normalized_correct = correct_order.lower()

        is_correct_reorder = (normalized_user == normalized_correct)
        st.session_state.feedback[exercise_key] = {'correctness': is_correct_reorder} # Store result

        if is_correct_reorder:
            st.success(f"✅ Doskonale! '{correct_order}'.")
        else:
            st.error(f"❌ Prawie! Poprawna kolejność to: '{correct_order}'. / ¡Casi! El orden correcto es: '{correct_order}'.")


    st.success("🎉 **Gratulacje! Ukończyłeś/aś pierwszą lekcję!** 🎉")
    st.success("🎉 **¡Felicidades! ¡Has completado la primera lección!** 🎉")
    st.markdown("Ćwicz dalej i wracaj do materiałów! / ¡Sigue practicando y revisando los materiales!")

# --- Footer or End Note ---
st.sidebar.markdown("---")
st.sidebar.info("Lekcja oparta na materiałach PDF. / Lección basada en materiales PDF.")
