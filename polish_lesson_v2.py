import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Polish for Spanish Speakers",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
# (Includes DM Sans, Google Icons, background, noise, button styles, card styles, progress bar)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');

    html, body, [class*="st-"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* Main background color and noise texture */
    body {
        background-color: #f0f2f6; /* Light grey-blue background */
    }

    /* Noise Texture using pseudo-element */
    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 800 800' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
        opacity: 0.12; /* Equivalent to AE noise level 12ish */
        z-index: -1; /* Place behind content */
        pointer-events: none; /* Allow clicks through */
    }

    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 900px; /* Limit content width for readability */
        margin: auto;
    }

    /* Button Styling */
    .stButton > button {
        border: none;
        border-radius: 12px; /* Rounded corners */
        padding: 12px 24px;
        font-weight: 700;
        color: white;
        background: linear-gradient(90deg, #FF6B6B, #FF8E53); /* Warm gradient */
        transition: transform 0.1s ease-in-out, box-shadow 0.1s ease-in-out;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        display: inline-flex; /* Align icon and text */
        align-items: center;
        justify-content: center;
        gap: 8px; /* Space between icon and text */
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    .stButton > button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Special button for 'Previous' */
    .stButton[data-testid="stButtonPrevious"] > button {
         background: linear-gradient(90deg, #787A91, #A8AABC); /* Grey gradient */
    }

    /* Card Styling */
    .quiz-card, .info-card {
        background-color: white;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        border: 1px solid #e0e0e0;
    }

    .quiz-card h3, .info-card h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #333;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
    }
     .quiz-card h3 .material-icons, .info-card h3 .material-icons {
        color: #FF6B6B; /* Icon color */
     }


    /* Radio button styling */
    .stRadio > label {
        font-weight: 500;
        margin-bottom: 10px;
    }
    .stRadio div[role="radiogroup"] > label { /* Individual radio options */
        background-color: #f8f9fa;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid #e0e0e0;
        transition: background-color 0.2s ease;
    }
     .stRadio div[role="radiogroup"] > label:hover {
        background-color: #e9ecef;
     }


    /* Text Input Styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 10px 15px;
    }
     .stTextInput > div > div > input:focus {
        border-color: #FF6B6B;
        box-shadow: 0 0 0 2px rgba(255, 107, 107, 0.25);
     }

    /* Progress Bar Styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4); /* Gradient for progress */
    }
    .progress-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #e9ecef;
        padding: 10px 0;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        z-index: 100;
    }
     .progress-container .block-container{
         padding: 0 3rem !important;
         max-width: 900px;
         margin: auto;
     }

    /* Icon styling */
    .material-icons {
        font-size: 1.3em; /* Adjust icon size */
        vertical-align: middle;
    }

    /* Headers */
    h1 {
        color: #2c3e50;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }
     h2 {
        color: #FF6B6B; /* Accent color for section titles */
        font-weight: 700;
        border-bottom: 2px solid #FF8E53;
        padding-bottom: 5px;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
     }
      h2 .material-icons {
        font-size: 1.5em;
      }

    /* Feedback messages */
    .stAlert {
        border-radius: 8px;
    }

</style>
""", unsafe_allow_html=True)

# --- Constants ---
TOTAL_SECTIONS = 6 # 0-5

# --- Session State Initialization ---
if 'current_section' not in st.session_state:
    st.session_state.current_section = 0
    st.session_state.progress = 0.0
    # Initialize states for answers if needed, e.g.:
    st.session_state.quiz1_answers = {}
    st.session_state.quiz2_answers = {}
    st.session_state.ex1_gender_answers = {}
    st.session_state.ex2_verb_answers = [""] * 5 # Example for 5 blanks
    st.session_state.ex3_pronoun_answers = {}
    st.session_state.intro_q1_answer = None
    st.session_state.intro_fill_answers = [""] * 3 # Example for 3 blanks
    st.session_state.dialogue_q1_answer = None
    st.session_state.dialogue_input_answer = ""

# --- Helper Functions ---
def update_progress():
    st.session_state.progress = st.session_state.current_section / (TOTAL_SECTIONS - 1)

def next_section():
    if st.session_state.current_section < TOTAL_SECTIONS - 1:
        st.session_state.current_section += 1
        update_progress()
    # Optionally clear answers for the next section if needed

def prev_section():
    if st.session_state.current_section > 0:
        st.session_state.current_section -= 1
        update_progress()
    # Optionally clear answers

# --- Icon Helper ---
def icon(icon_name):
    return f'<span class="material-icons">{icon_name}</span>'

# --- Main Content Area ---
st.title(f"{icon('language')} Nauka polskiego dla Hiszpanów")
st.markdown("---")

# --- Section Content ---

# Section 0: Introduction
if st.session_state.current_section == 0:
    st.header(f"{icon('info')} Sekcja 0: Wprowadzenie / Introducción")
    st.markdown("""
    <div class="info-card">
        <h3>Witaj! / ¡Hola y bienvenido/a!</h3>
        <p>Ten kurs pomoże Ci zacząć naukę języka polskiego, porównując go z hiszpańskim.</p>
        <p><i>Este curso te ayudará a empezar a aprender polaco, comparándolo con el español.</i></p>

        <h4>Kluczowe różnice / Diferencias clave:</h4>
        <ul>
            <li><b>Alfabet:</b> Używa liter łacińskich, ale z dodatkami: ą, ę, ć, ł, ń, ó, ś, ź, ż. Dźwięki jak 'sz', 'cz', 'rz' są częste. <br><i>(Usa letras latinas, pero con añadidos. Sonidos como 'sh', 'ch' son comunes).</i></li>
            <li><b>Wymowa / Pronunciación:</b> Samogłoski nosowe (ą, ę), twarde i miękkie spółgłoski (np. sz vs ś), stały akcent (zwykle na przedostatniej sylabie). <br><i>(Vocales nasales, consonantes duras y blandas, acento fijo - usualmente en la penúltima sílaba).</i></li>
            <li><b>Gramatyka / Gramática:</b> 7 przypadków rzeczownika (deklinacja) zamiast wielu przyimków; 3 rodzaje gramatyczne (męski, żeński, nijaki). <br><i>(7 casos para sustantivos en lugar de muchas preposiciones; 3 géneros gramaticales).</i></li>
        </ul>
        <p><b>Nie martw się! Język polski jest logiczny. / ¡No te preocupes! El polaco es lógico.</b></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"{icon('play_arrow')} Zaczynajmy! / ¡Empecemos!"):
        next_section()
        st.rerun()

# Section 1: Basic Vocabulary & Phrases
elif st.session_state.current_section == 1:
    st.header(f"{icon('chat')} Sekcja 1: Podstawowe słownictwo i zwroty / Vocabulario y frases básicas")

    st.markdown("""
    <div class="info-card">
    <h3>{icon('record_voice_over')} Podstawowe zwroty / Frases esenciales</h3>
    <p><b>Powitania / Saludos:</b></p>
    <ul>
        <li><b>Dzień dobry:</b> Buenos días/tardes (Formal)</li>
        <li><b>Cześć:</b> Hola / Chao (Informal)</li>
        <li><b>Dobry wieczór:</b> Buenas noches (al llegar - Formal)</li>
        <li><b>Dobranoc:</b> Buenas noches (al despedirse/dormir)</li>
    </ul>
    <p><b>Pożegnania / Despedidas:</b></p>
    <ul>
        <li><b>Do widzenia:</b> Adiós / Hasta la vista (Formal)</li>
        <li><b>Na razie:</b> Hasta luego / Chao (Informal)</li>
    </ul>
    <p><b>Uprzejmość / Cortesía:</b></p>
    <ul>
        <li><b>Proszę:</b> Por favor / Aquí tienes / De nada</li>
        <li><b>Dziękuję:</b> Gracias</li>
        <li><b>Przepraszam:</b> Perdón / Disculpe</li>
    </ul>
     <p><b>Proste pytania i odpowiedzi / Preguntas y respuestas simples:</b></p>
    <ul>
        <li><b>Tak / Nie:</b> Sí / No</li>
        <li><b>Jak się masz?:</b> ¿Cómo estás? (Informal)</li>
        <li><b>Jak się pan/pani ma?:</b> ¿Cómo está usted? (Formal M/F)</li>
        <li><b>Dobrze, dziękuję.:</b> Bien, gracias.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="quiz-card">
    <h3>{icon('quiz')} Quiz 1: Dopasuj zwroty / Empareja las frases</h3>
    """, unsafe_allow_html=True)
    q1_options = {
        "Dzień dobry": ["Hola", "Buenos días/tardes", "Buenas noches"],
        "Proszę": ["Gracias", "Perdón", "Por favor / De nada"],
        "Do widzenia": ["Adiós (Formal)", "Hasta luego (Informal)", "Hola"]
    }
    correct_q1 = {"Dzień dobry": "Buenos días/tardes", "Proszę": "Por favor / De nada", "Do widzenia": "Adiós (Formal)"}

    for i, (polish_phrase, spanish_options) in enumerate(q1_options.items()):
        key = f"q1_{i}"
        st.session_state.quiz1_answers[key] = st.radio(f"Co znaczy '{polish_phrase}'?", spanish_options, key=key, index=None)
        if st.session_state.quiz1_answers[key] is not None:
            if st.session_state.quiz1_answers[key] == correct_q1[polish_phrase]:
                st.success(f"{icon('check_circle')} Dobrze! / ¡Correcto!")
            else:
                st.error(f"{icon('cancel')} Źle. Poprawna odpowiedź: {correct_q1[polish_phrase]} / Incorrecto. Respuesta correcta: {correct_q1[polish_phrase]}")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card

    st.markdown("---")
    st.markdown(f"""
    <div class="quiz-card">
    <h3>{icon('quiz')} Quiz 2: Formalny czy nieformalny? / ¿Formal o informal?</h3>
    """, unsafe_allow_html=True)
    q2_phrases = ["Cześć", "Do widzenia", "Jak się pan ma?", "Jak się masz?"]
    correct_q2 = {"Cześć": "Nieformalny", "Do widzenia": "Formalny", "Jak się pan ma?": "Formalny", "Jak się masz?": "Nieformalny"}
    options_q2 = ["Formalny", "Nieformalny"]

    for i, phrase in enumerate(q2_phrases):
         key = f"q2_{i}"
         st.session_state.quiz2_answers[key] = st.radio(f"Czy '{phrase}' jest formalne czy nieformalne?", options_q2, key=key, index=None)
         if st.session_state.quiz2_answers[key] is not None:
            if st.session_state.quiz2_answers[key] == correct_q2[phrase]:
                st.success(f"{icon('check_circle')} Zgadza się! / ¡Así es!")
            else:
                st.error(f"{icon('cancel')} Niezupełnie. '{phrase}' jest {correct_q2[phrase]}. / No exactamente. '{phrase}' es {correct_q2[phrase]}.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card


# Section 2: Pronunciation
elif st.session_state.current_section == 2:
    st.header(f"{icon('volume_up')} Sekcja 2: Wymowa / Pronunciación")
    st.markdown(f"""
    <div class="info-card">
    <h3>{icon('record_voice_over')} Dźwięki polskie vs hiszpańskie / Sonidos polacos vs españoles</h3>
    <p>Niektóre polskie dźwięki są inne niż w hiszpańskim. / <i>Algunos sonidos polacos son diferentes al español.</i></p>
    <ul>
        <li><b>Ą / Ę (samogłoski nosowe / vocales nasales):</b> Jak 'on'/'en' we francuskim. Np. <i>m<b>ą</b>ka</i> (harina), <i>r<b>ę</b>ka</i> (mano). W hiszpańskim nie ma nosówek. / <i>Como 'on'/'en' en francés. No existen en español.</i></li>
        <li><b>SZ [ʃ]:</b> Jak angielskie 'sh'. Np. <i><b>sz</b>ok</i> (shock). Hiszpańskie 'ch' [tʃ] jest inne. / <i>Como 'sh' inglés. La 'ch' española es diferente.</i></li>
        <li><b>CZ [tʃ]:</b> Jak angielskie 'ch' i hiszpańskie 'ch'. Np. <i><b>cz</b>ekolada</i> (chocolate).</li>
        <li><b>Ż / RZ [ʒ]:</b> Jak 's' w angielskim 'plea<b>s</b>ure'. Np. <i><b>ż</b>aba</i> (rana), <i><b>rz</b>eka</i> (río). Nie ma odpowiednika w hiszpańskim standardowym. / <i>Como la 's' en 'plea<b>s</b>ure' inglés. Sin equivalente directo en español estándar.</i></li>
        <li><b>Ś / Ć / Ź / DŹ(DZI) [ɕ, tɕ, ʑ, dʑ]:</b> Miękkie wersje sz/cz/ż/dż. Dźwięki palatalizowane. Np. <i><b>ś</b>roda</i> (miércoles), <i><b>ć</b>ma</i> (polilla), <i><b>ź</b>le</i> (mal), <i><b>dź</b>więk</i> (sonido). Trudne dla Hiszpanów. / <i>Versiones 'suaves' de sz/cz/ż/dż. Sonidos palatalizados. Difíciles para hispanohablantes.</i></li>
        <li><b>Ł [w]:</b> Jak angielskie 'w'. Np. <i><b>ł</b>adny</i> (bonito). Hiszpańskie 'l' [l] jest inne. / <i>Como la 'w' inglesa. La 'l' española es diferente.</i></li>
    </ul>
    <p><b>Posłuchaj uważnie przykładów (tekstowych)! / ¡Escucha con atención los ejemplos (textuales)!</b></p>
    </div>

    <div class="quiz-card">
    <h3>{icon('quiz')} Ćwiczenie 1: Rozpoznaj dźwięk / Reconoce el sonido</h3>
    <p>Które słowo zawiera dźwięk...? / ¿Qué palabra contiene el sonido...?</p>
    """, unsafe_allow_html=True)

    # Example Quiz (add more)
    sound_q1 = st.radio("... 'sz' [ʃ]?", ["sok", "szok", "syn"], index=None, key="sound_q1")
    if sound_q1:
        if sound_q1 == "szok": st.success(f"{icon('check_circle')} Tak!")
        else: st.error(f"{icon('cancel')} Nie, 'szok' ma dźwięk 'sz'.")

    sound_q2 = st.radio("... 'cz' [tʃ]?", ["cena", "czekolada", "cebula"], index=None, key="sound_q2")
    if sound_q2:
        if sound_q2 == "czekolada": st.success(f"{icon('check_circle')} Tak!")
        else: st.error(f"{icon('cancel')} Nie, 'czekolada' ma dźwięk 'cz'.")

    sound_q3 = st.radio("... 'ł' [w]?", ["lampa", "ładny", "las"], index=None, key="sound_q3")
    if sound_q3:
        if sound_q3 == "ładny": st.success(f"{icon('check_circle')} Tak!")
        else: st.error(f"{icon('cancel')} Nie, 'ładny' ma dźwięk 'ł'.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card


# Section 3: Grammar
elif st.session_state.current_section == 3:
    st.header(f"{icon('functions')} Sekcja 3: Gramatyka / Gramática")

    st.markdown(f"""
    <div class="info-card">
    <h3>{icon('label')} Rodzaj gramatyczny / Género gramatical</h3>
    <p>W polskim są 3 rodzaje: / <i>En polaco hay 3 géneros:</i></p>
    <ul>
        <li><b>Męski (m):</b> często kończy się na spółgłoskę (<i>stół</i> - mesa, <i>pan</i> - señor).</li>
        <li><b>Żeński (f):</b> często kończy się na <b>-a</b> (<i>książka</i> - libro, <i>kawa</i> - café).</li>
        <li><b>Nijaki (n):</b> często kończy się na <b>-o, -e, -ę</b> (<i>okno</i> - ventana, <i>imię</i> - nombre).</li>
    </ul>
    <p><i>Porównanie: Hiszpański ma męski/żeński. Polski dodaje nijaki. Końcówki są wskazówkami, nie regułami absolutnymi. / Comparación: El español tiene M/F. El polaco añade Neutro. Las terminaciones son pistas, no reglas absolutas.</i></p>
    </div>

    <div class="info-card">
    <h3>{icon('spellcheck')} Czasowniki: Czas teraźniejszy / Verbos: Presente</h3>
    <p><b>być (ser/estar):</b> jestem, jesteś, jest, jesteśmy, jesteście, są</p>
    <p><b>mówić (hablar):</b> mówię, mówisz, mówi, mówimy, mówicie, mówią</p>
    <p><b>nazywać się (llamarse):</b> nazywam się, nazywasz się, nazywa się, nazywamy się, nazywacie się, nazywają się</p>
    <p><b>mieć (tener):</b> mam, masz, ma, mamy, macie, mają</p>
    <p><i>Zwróć uwagę na końcówki! / ¡Presta atención a las terminaciones!</i></p>
    </div>

    <div class="quiz-card">
    <h3>{icon('quiz')} Ćwiczenie 1: Jaki to rodzaj? / ¿Qué género es?</h3>
    """, unsafe_allow_html=True)
    gender_words = {"dom (casa)": "Męski", "woda (agua)": "Żeński", "dziecko (niño)": "Nijaki", "nauczyciel (profesor)": "Męski"}
    options_gender = ["Męski", "Żeński", "Nijaki"]
    for i, (word, correct_gender) in enumerate(gender_words.items()):
        key = f"gender_{i}"
        st.session_state.ex1_gender_answers[key] = st.radio(f"Jaki rodzaj ma słowo '{word}'?", options_gender, key=key, index=None)
        if st.session_state.ex1_gender_answers[key]:
            if st.session_state.ex1_gender_answers[key] == correct_gender:
                st.success(f"{icon('check_circle')} Dobrze!")
            else:
                st.error(f"{icon('cancel')} Raczej {correct_gender}.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card

    st.markdown(f"""
    <div class="quiz-card">
    <h3>{icon('edit')} Ćwiczenie 2: Uzupełnij czasowniki / Completa los verbos</h3>
    <p>Wpisz poprawną formę czasownika w nawiasie. / <i>Escribe la forma correcta del verbo entre paréntesis.</i></p>
    """, unsafe_allow_html=True)

    sentences_verbs = [
        ("Ona ___ po francusku. (mówić)", "mówi"),
        ("My ___ studentami. (być)", "jesteśmy"),
        ("Jak ty ___ ___? (nazywać się)", "się nazywasz"), # Split for two inputs maybe? Simpler: one input
        ("Ja ___ na imię Piotr. (mieć)", "mam"),
        ("Czy wy ___ po polsku? (mówić)", "mówicie")
    ]

    for i, (sentence, correct_form) in enumerate(sentences_verbs):
        key = f"verb_fill_{i}"
        # Handle potential split answers like "się nazywasz" - keep simple for now
        user_input = st.text_input(sentence, key=key, value=st.session_state.ex2_verb_answers[i])
        st.session_state.ex2_verb_answers[i] = user_input # Store input

        # Simple validation on button click (or could be live if desired)
        # For now, just show input field. Validation could be added with a submit button per section.
        # Example validation (if a button was pressed):
        # if st.button("Sprawdź ćw. 2 / Comprobar ej. 2"):
        #    if user_input.strip().lower() == correct_form:
        #        st.success(...)
        #    else:
        #        st.error(...)

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card


# Section 4: Introductions
elif st.session_state.current_section == 4:
    st.header(f"{icon('account_circle')} Sekcja 4: Przedstawianie się / Presentaciones")

    st.markdown(f"""
    <div class="info-card">
    <h3>{icon('contact_mail')} Jak zapytać o imię? / ¿Cómo preguntar el nombre?</h3>
    <ul>
        <li><b>Jak się nazywasz?</b> (¿Cómo te llamas? - Informal)</li>
        <li><b>Jak pan się nazywa?</b> (¿Cómo se llama usted? - Formal, a un hombre)</li>
        <li><b>Jak pani się nazywa?</b> (¿Cómo se llama usted? - Formal, a una mujer)</li>
    </ul>
    <h3>{icon('badge')} Jak odpowiedzieć? / ¿Cómo responder?</h3>
    <ul>
        <li><b>Nazywam się [Imię Nazwisko]:</b> Me llamo [Nombre Apellido]</li>
        <li><b>Jestem [Imię]:</b> Soy [Nombre]</li>
        <li><b>Mam na imię [Imię]:</b> Mi nombre (de pila) es [Nombre]</li>
    </ul>
     <h3>{icon('group')} Pytanie o innych / Preguntar por otros</h3>
     <ul>
        <li><b>Jak on/ona się nazywa?</b> (¿Cómo se llama él/ella?)</li>
        <li><b>Jak oni/one się nazywają?</b> (¿Cómo se llaman ellos/ellas?)</li>
     </ul>
     <p><b>Miło mi:</b> Encantado/a / Mucho gusto</p>
    </div>

    <div class="quiz-card">
    <h3>{icon('quiz')} Ćwiczenie 1: Wybierz pytanie / Elige la pregunta</h3>
    <p>Spotykasz starszego mężczyznę. Jak zapytasz o jego imię? / <i>Conoces a un hombre mayor. ¿Cómo le preguntas su nombre?</i></p>
    """, unsafe_allow_html=True)

    q1_intro_options = ["Jak się nazywasz?", "Jak pani się nazywa?", "Jak pan się nazywa?"]
    st.session_state.intro_q1_answer = st.radio("Wybierz poprawną formę:", q1_intro_options, index=None, key="intro_q1")
    if st.session_state.intro_q1_answer:
        if st.session_state.intro_q1_answer == "Jak pan się nazywa?":
            st.success(f"{icon('check_circle')} Doskonale! To forma formalna do mężczyzny.")
        else:
            st.error(f"{icon('cancel')} Nie, do starszego mężczyzny użyjemy formy 'Jak pan się nazywa?'.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card

    st.markdown(f"""
    <div class="quiz-card">
    <h3>{icon('edit')} Ćwiczenie 2: Uzupełnij dialog / Completa el diálogo</h3>
    """, unsafe_allow_html=True)
    # Example fill-in dialogue
    st.markdown("A: Dzień dobry! ___ się Adam Kowalski. A pani?")
    st.session_state.intro_fill_answers[0] = st.text_input("Uzupełnij 1:", key="fill_1", value=st.session_state.intro_fill_answers[0])
    st.markdown("B: Dzień dobry. Nazywam ___ Ewa Nowak.")
    st.session_state.intro_fill_answers[1] = st.text_input("Uzupełnij 2:", key="fill_2", value=st.session_state.intro_fill_answers[1])
    st.markdown("A: ___ mi.")
    st.session_state.intro_fill_answers[2] = st.text_input("Uzupełnij 3:", key="fill_3", value=st.session_state.intro_fill_answers[2])

    # Add a check button if desired for validation
    if st.button(f"{icon('check')} Sprawdź dialog / Comprobar diálogo"):
        correct_fills = ["Nazywam", "się", "Miło"]
        correct_count = 0
        for i, correct in enumerate(correct_fills):
            if st.session_state.intro_fill_answers[i].strip().lower() == correct.lower():
                correct_count += 1
            else:
                 st.warning(f"Poprawka w luce {i+1}: powinno być '{correct}' / Corrección en el hueco {i+1}: debería ser '{correct}'")
        if correct_count == len(correct_fills):
            st.success("Wszystko dobrze! / ¡Todo bien!")
        else:
            st.error(f"Masz {correct_count} z {len(correct_fills)} poprawnych odpowiedzi. / Tienes {correct_count} de {len(correct_fills)} respuestas correctas.")


    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card


# Section 5: Dialogue Practice
elif st.session_state.current_section == 5:
    st.header(f"{icon('forum')} Sekcja 5: Ćwiczenia dialogowe / Práctica de diálogo")

    st.markdown(f"""
    <div class="info-card">
    <h3>{icon('question_answer')} Scenariusz 1: Spotkanie formalne / Escenario 1: Encuentro formal</h3>
    <p>A: Dzień dobry. Nazywam się Jan Kowalski. Jak pani się nazywa?</p>
    <p>B: Dzień dobry. Nazywam się Maria Nowak. Miło mi.</p>
    <p>A: Miło mi również. Czy mówi pani po angielsku?</p>
    <p>B: Nie, mówię tylko po polsku i trochę po hiszpańsku.</p>
    </div>

    <div class="quiz-card">
    <h3>{icon('quiz')} Ćwiczenie 1: Uzupełnij rozmowę / Completa la conversación</h3>
    <p>A: Cześć! Jestem Piotr. Jak się nazywasz?</p>
    <p>B: Cześć! Nazywam się Anna. ___</p>
    """, unsafe_allow_html=True)

    dialogue_q1_options = ["Do widzenia.", "Miło mi.", "Przepraszam."]
    st.session_state.dialogue_q1_answer = st.radio("Wybierz odpowiedź B:", dialogue_q1_options, index=None, key="dialogue_q1")
    if st.session_state.dialogue_q1_answer:
        if st.session_state.dialogue_q1_answer == "Miło mi.":
            st.success(f"{icon('check_circle')} Świetnie! / ¡Genial!")
        else:
            st.error(f"{icon('cancel')} Zazwyczaj po przedstawieniu mówimy 'Miło mi'.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card

    st.markdown(f"""
     <div class="quiz-card">
    <h3>{icon('edit_note')} Ćwiczenie 2: Twoja kolej / Tu turno</h3>
    <p>Przywitaj się formalnie z nową koleżanką (panią Nowak) i przedstaw się. / <i>Saluda formalmente a tu nueva colega (Sra. Nowak) y preséntate.</i></p>
    """, unsafe_allow_html=True)
    st.session_state.dialogue_input_answer = st.text_area("Wpisz swoją odpowiedź: / Escribe tu respuesta:", key="dialogue_input", value=st.session_state.dialogue_input_answer)

    if st.button(f"{icon('check')} Sprawdź odpowiedź / Comprobar respuesta"):
        response = st.session_state.dialogue_input_answer.lower().strip()
        if "dzień dobry" in response and ("nazywam się" in response or "jestem" in response):
             st.success(f"{icon('thumb_up')} Dobrze! Użyłeś formalnego powitania i przedstawiłeś się. / ¡Bien! Usaste un saludo formal y te presentaste.")
        elif "dzień dobry" not in response:
             st.warning("Pamiętaj o formalnym powitaniu 'Dzień dobry'. / Recuerda el saludo formal 'Dzień dobry'.")
        elif "nazywam się" not in response and "jestem" not in response:
             st.warning("Nie zapomnij się przedstawić używając 'Nazywam się...' lub 'Jestem...'. / No olvides presentarte usando 'Nazywam się...' o 'Jestem...'.")
        else:
             st.info("Spróbuj jeszcze raz. / Inténtalo de nuevo.")

    st.markdown("</div>", unsafe_allow_html=True) # Close quiz-card


# --- Navigation Buttons ---
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.current_section > 0:
        # Use a unique key or identifier for the previous button if needed for specific styling
        if st.button(f"{icon('arrow_back')} Poprzednia / Anterior", key="stButtonPrevious"):
            prev_section()
            st.rerun()

with col3:
    if st.session_state.current_section < TOTAL_SECTIONS - 1:
        if st.button(f"{icon('arrow_forward')} Następna / Siguiente"):
            next_section()
            st.rerun()
    elif st.session_state.current_section == TOTAL_SECTIONS - 1:
         if st.button(f"{icon('done_all')} Zakończ lekcję / Finalizar lección"):
            st.balloons()
            st.success("Gratulacje! Ukończyłeś lekcję! / ¡Felicidades! ¡Has completado la lección!")
            # Optionally reset state here if needed for a new session
            # st.session_state.current_section = 0
            # update_progress()
            # ... reset other states ...


# --- Progress Bar ---
# Place progress bar in a container at the bottom
st.markdown("""
    <div class="progress-container">
        <div class="block-container">
        </div>
    </div>
""", unsafe_allow_html=True)
# The actual progress bar needs to be outside the container for Streamlit's rendering
# It will appear visually within the styled container due to fixed positioning
st.progress(st.session_state.progress)
# Add text label for progress inside the container logic if needed, e.g.,
# with st.container(): # This container is just for layout logic, not the fixed bar
#    st.markdown(f"<div style='text-align: center; position: fixed; bottom: 15px; width: 100%; left:0;'>Postęp: {int(st.session_state.progress * 100)}%</div>", unsafe_allow_html=True)
