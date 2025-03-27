import streamlit as st

# --- Constants (Simplified for Streamlit - Styling is often less direct) ---
# Fonts and detailed colors are managed via themes or custom CSS if needed.
TOTAL_SCREENS = 17 # Based on the plan

# --- Initialize Session State ---
# This runs only once per session or when the script reruns due to interaction.
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 0
    st.session_state.user_answers = {} # Store answers {screen_idx: {item_idx: answer}}
    st.session_state.quiz_feedback = {} # Store feedback {screen_idx: {item_idx: (message, is_correct)}}
    st.session_state.entry_feedback = {} # Store feedback {screen_idx: {item_idx: (message, is_correct)}}


# --- Helper Functions for Navigation ---
def go_next():
    if st.session_state.current_screen < TOTAL_SCREENS - 1:
        st.session_state.current_screen += 1
        # Clear feedback for the new screen if interaction isn't immediate
        st.session_state.quiz_feedback.pop(st.session_state.current_screen, None)
        st.session_state.entry_feedback.pop(st.session_state.current_screen, None)

def go_back():
    if st.session_state.current_screen > 0:
        st.session_state.current_screen -= 1
        # Clear feedback for the new screen
        st.session_state.quiz_feedback.pop(st.session_state.current_screen, None)
        st.session_state.entry_feedback.pop(st.session_state.current_screen, None)


# --- Function to display Screen Content ---
# Instead of classes/methods, we use functions for each screen

def display_screen_0():
    st.title("¡Bienvenido a Aprender Polaco!")
    intro_text = """
Polish (Polski) is a West Slavic language spoken mainly in Poland.
It uses the Latin alphabet like Spanish, but with unique letters and sounds.
We'll explore the basics together!

**Comparison:** Like Spanish, Polish has grammatical gender, but it has three + cases!
Word order is typically SVO like Spanish, but can be more flexible.
"""
    st.markdown(intro_text) # Use markdown for bold etc.
    st.button("Start ->", on_click=go_next, key="start_btn")

def display_screen_1():
    st.title("The Polish Alphabet vs. Spanish")
    alphabet_text = """
Polish uses most Latin letters, plus: **Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż**.

**Key Differences:**
*   **Nasal Vowels:** `Ą`, `Ę` (mąka, ręka) - No Spanish equivalent.
*   **Soft Consonants:** `Ć`, `Ś`, `Ź`, `Dź` (ćma, środa, źle, dziękuję) - Different from Spanish C/S/Z.
*   **Hard Consonants:** `CZ` (like 'ch'), `SZ` ('sh'), `Ż/RZ` ('s' in pleasure) (czekolada, szok, rzeka)
*   **Ł:** Pronounced like 'w' (ładny) - Different from Spanish 'l'.
*   **Ó:** Sounds like 'U' (ósma).
*   **H / Ch:** Both sound like Spanish 'J' (hotel, choroba).
"""
    st.markdown(alphabet_text)
    st.button("Dalej: Pozdrowienia (Next: Greetings) ->", on_click=go_next, key="alphabet_next")

# --- Screen 4: Greetings Quiz --- (Example with Streamlit Interaction)
def display_screen_4():
    screen_index = 4
    st.title("Szybki Test: Powitania (Quick Quiz: Greetings)")

    # Initialize state for this screen if not already done
    if screen_index not in st.session_state.user_answers:
        st.session_state.user_answers[screen_index] = {}
    if screen_index not in st.session_state.quiz_feedback:
        st.session_state.quiz_feedback[screen_index] = {}

    st.markdown("---")
    st.subheader("P1: Spotykasz profesora rano. Co mówisz?")

    q1_options = ["A) Cześć", "B) Dzień dobry", "C) Dobranoc"]
    q1_correct = "B"
    q1_key_prefix = f"s{screen_index}_q1"

    # Use columns for buttons, or display vertically
    cols1 = st.columns(len(q1_options))
    q1_answered = 0 in st.session_state.user_answers[screen_index]

    for i, option in enumerate(q1_options):
        opt_letter = option.split(")")[0].strip()
        unique_key = f"{q1_key_prefix}_opt{i}"

        # Disable buttons after answering
        is_disabled = q1_answered

        if cols1[i].button(option, key=unique_key, disabled=is_disabled, use_container_width=True):
            # Store answer
            st.session_state.user_answers[screen_index][0] = opt_letter
            is_correct = (opt_letter == q1_correct)
            if is_correct:
                 st.session_state.quiz_feedback[screen_index][0] = (f"Poprawnie! ({opt_letter})", True)
            else:
                 st.session_state.quiz_feedback[screen_index][0] = (f"Niepoprawnie. Poprawna: {q1_correct}.", False)
            st.rerun() # Rerun script to update UI and disable buttons

    # Display feedback for Q1 if answered
    if 0 in st.session_state.quiz_feedback[screen_index]:
         msg, is_correct = st.session_state.quiz_feedback[screen_index][0]
         if is_correct:
             st.success(msg)
         else:
             st.error(msg)


    st.markdown("---")
    st.subheader("P2: Wychodzisz od przyjaciela. Co możesz powiedzieć?")

    q2_options = ["A) Do widzenia", "B) Dzień dobry", "C) Cześć / Na razie"]
    q2_correct = "C"
    q2_key_prefix = f"s{screen_index}_q2"
    q2_answered = 1 in st.session_state.user_answers[screen_index]

    cols2 = st.columns(len(q2_options))

    for i, option in enumerate(q2_options):
        opt_letter = option.split(")")[0].strip()
        unique_key = f"{q2_key_prefix}_opt{i}"
        is_disabled = q2_answered

        if cols2[i].button(option, key=unique_key, disabled=is_disabled, use_container_width=True):
            st.session_state.user_answers[screen_index][1] = opt_letter
            is_correct = (opt_letter == q2_correct)
            if is_correct:
                 st.session_state.quiz_feedback[screen_index][1] = (f"Poprawnie! ({opt_letter})", True)
            else:
                 st.session_state.quiz_feedback[screen_index][1] = (f"Niepoprawnie. Poprawna: {q2_correct}.", False)
            st.rerun()

    # Display feedback for Q2
    if 1 in st.session_state.quiz_feedback[screen_index]:
         msg, is_correct = st.session_state.quiz_feedback[screen_index][1]
         if is_correct:
             st.success(msg)
         else:
             st.error(msg)

    st.markdown("---")

    # Navigation button only if both answered
    if q1_answered and q2_answered:
        st.button("Dalej: Przedstawianie się ->", on_click=go_next, key="quiz4_next")


# --- Screen 6: Intro Fill-in --- (Example with Streamlit Text Input)
def display_screen_6():
    screen_index = 6
    st.title("Ćwiczenie: Przedstawianie się")

    # Initialize state
    if screen_index not in st.session_state.user_answers:
        st.session_state.user_answers[screen_index] = {}
    if screen_index not in st.session_state.entry_feedback:
         st.session_state.entry_feedback[screen_index] = {}

    prompts = [
        ("A: Dzień dobry! Jak ______ się nazywa? (Do kobiety)", "pani", 0),
        ("B: Dzień dobry! Nazywam ______ Ewa Nowak.", "się", 1),
        ("A: Miło ______.", "mi", 2),
        ("A: Cześć! Jak się ______?", "nazywasz", 3),
        ("B: Cześć! ______ się Piotr.", "Nazywam", 4),
    ]

    # Store text input values directly in user_answers using unique keys
    for text, _, index in prompts:
        input_key = f"s{screen_index}_entry{index}"
        st.markdown(text.replace("______", "`______`")) # Show prompt
        # Value is taken from session_state if already exists
        current_value = st.session_state.user_answers.get(screen_index, {}).get(index, "")
        st.session_state.user_answers[screen_index][index] = st.text_input(
            label="Wpisz słowo / Enter word",
            value=current_value,
            key=input_key,
            label_visibility="collapsed" # Hide the default label
        )

        # Display feedback if check button was pressed
        if index in st.session_state.entry_feedback.get(screen_index, {}):
            msg, is_correct = st.session_state.entry_feedback[screen_index][index]
            if is_correct:
                st.success(msg)
            else:
                st.warning(msg) # Use warning instead of error for incorrect fill-ins

    st.markdown("---")

    # Check Button logic
    if st.button("Sprawdź (Check)", key=f"s{screen_index}_check"):
        all_correct = True
        correct_count = 0
        st.session_state.entry_feedback[screen_index] = {} # Reset feedback before checking

        for _, correct_answer, index in prompts:
            user_answer = st.session_state.user_answers.get(screen_index, {}).get(index, "").strip()
            if user_answer.lower() == correct_answer.lower():
                 st.session_state.entry_feedback[screen_index][index] = (f"'{user_answer}': Poprawnie!", True)
                 correct_count += 1
            elif user_answer == "":
                 st.session_state.entry_feedback[screen_index][index] = ("Proszę wpisać odpowiedź.", False)
                 all_correct = False
            else:
                 st.session_state.entry_feedback[screen_index][index] = (f"'{user_answer}': Spróbuj ponownie (poprawnie: {correct_answer}).", False)
                 all_correct = False

        if all_correct:
            st.success("Wszystko poprawnie!")
            # You might store a flag in session state to enable the Next button conditionally
            st.session_state[f"screen_{screen_index}_complete"] = True
        else:
             st.info(f"Poprawnie: {correct_count}/{len(prompts)}. Spróbuj ponownie.")
             st.session_state[f"screen_{screen_index}_complete"] = False

        st.rerun() # Rerun to display feedback immediately


    # Conditional Next button
    if st.session_state.get(f"screen_{screen_index}_complete", False):
        st.button("Dalej: Gramatyka ->", on_click=go_next, key="fill_in6_next")


# Placeholder for other screens
def display_placeholder(screen_idx):
     st.title(f"Screen {screen_idx}: Placeholder")
     st.write("Content for this screen to be implemented using Streamlit widgets.")
     st.button("Dalej (Next) ->", on_click=go_next, key=f"placeholder_next_{screen_idx}")

# --- Main App Logic: Display current screen ---
current_screen_func = {
    0: display_screen_0,
    1: display_screen_1,
    4: display_screen_4, # Example quiz screen
    6: display_screen_6, # Example fill-in screen
    # Add mappings for all other screens here, potentially using display_placeholder
}.get(st.session_state.current_screen, display_placeholder) # Default to placeholder

# Call the function for the current screen
# Pass screen index if needed by the function (like placeholder does)
import inspect
sig = inspect.signature(current_screen_func)
if 'screen_idx' in sig.parameters:
     current_screen_func(st.session_state.current_screen)
else:
     current_screen_func()


# --- Persistent Footer/Sidebar ---
st.divider() # Visual separator

# Use columns for footer layout
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.session_state.current_screen > 0:
        st.button("<- Cofnij (Back)", on_click=go_back, key="global_back", use_container_width=True)

with col2:
     # Progress Bar
     progress_value = (st.session_state.current_screen + 1) / TOTAL_SCREENS
     st.progress(progress_value, text=f"Lekcja: {st.session_state.current_screen + 1} / {TOTAL_SCREENS}")

# col3 can be used for a global 'Next' if needed, but we handled 'Next' per screen mostly.
# Example: Always show Next except on last screen
# with col3:
#      if st.session_state.current_screen < TOTAL_SCREENS - 1:
#           # This button's on_click might conflict if specific screens have validation before proceeding
#           st.button("Dalej ->", on_click=go_next, key="global_next", use_container_width=True)

# Optionally use the sidebar for progress/navigation:
# st.sidebar.progress(progress_value)
# st.sidebar.button("<- Back", on_click=go_back, key="sidebar_back", disabled=st.session_state.current_screen == 0)
# st.sidebar.button("Next ->", on_click=go_next, key="sidebar_next", disabled=st.session_state.current_screen == TOTAL_SCREENS - 1)
