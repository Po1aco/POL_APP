import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk  # For themed widgets like Progressbar

# --- Constants ---
# Try DM Sans, fall back to Calibri/Arial/system default
try:
    # Increase default font size slightly
    DEFAULT_FONT_FAMILY = "DM Sans"
    DEFAULT_FONT_SIZE = 11
    TITLE_FONT_SIZE = 22
    # Check if font exists (basic check)
    fonts = list(tkFont.families())
    if DEFAULT_FONT_FAMILY not in fonts:
        raise Exception("DM Sans not found")
    DEFAULT_FONT = tkFont.Font(family=DEFAULT_FONT_FAMILY, size=DEFAULT_FONT_SIZE)
    TITLE_FONT = tkFont.Font(family=DEFAULT_FONT_FAMILY, size=TITLE_FONT_SIZE, weight="bold")
except Exception:
    DEFAULT_FONT_FAMILY = "Calibri" # Common fallback
    DEFAULT_FONT_SIZE = 10
    TITLE_FONT_SIZE = 18
    print("DM Sans font not found, using Calibri/Default.")
    DEFAULT_FONT = tkFont.Font(family=DEFAULT_FONT_FAMILY, size=DEFAULT_FONT_SIZE)
    TITLE_FONT = tkFont.Font(family=DEFAULT_FONT_FAMILY, size=TITLE_FONT_SIZE, weight="bold")

# Colors (approximating the p5js palette)
BG_COLOR = '#F0E8F8' # Soft Lavender
TEXT_COLOR = '#333333' # Dark Gray
PRIMARY_COLOR = '#E53935' # Red (Slightly less harsh than F44336)
SECONDARY_COLOR = '#1E88E5' # Blue (Slightly less harsh than 2196F3)
ACCENT_COLOR = '#F06292' # Pink (Adjusted from FF8FAB)
CORRECT_COLOR = '#4CAF50' # Green
INCORRECT_COLOR = PRIMARY_COLOR # Red for incorrect
BUTTON_TEXT_COLOR = '#FFFFFF' # White

PAD_X = 15
PAD_Y = 10
WRAP_LENGTH = 650 # Default text wrap length

# --- Main Application Class ---
class PolishLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nauka Polskiego dla Hiszpanów")
        self.geometry("800x650") # Set a default size
        self.configure(bg=BG_COLOR)

        # --- State Variables ---
        self.current_screen_index = 0
        self.user_answers = {} # Store answers for quizzes/entries per screen {screen_idx: {item_idx: answer}}
        self.frames = []       # List to hold all screen frames
        self.feedback_var = tk.StringVar() # For displaying feedback

        # --- Create Main Container ---
        container = tk.Frame(self, bg=BG_COLOR)
        container.pack(side="top", fill="both", expand=True, padx=PAD_X, pady=PAD_Y)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.container = container

        # --- Create Screens (Frames) ---
        self._create_screens()

        # --- Create Footer (Navigation & Progress) ---
        self._create_footer()

        # --- Show First Screen ---
        self.show_screen(0)

    def _create_screens(self):
        # Create a frame for each screen defined in the lesson plan
        # Store them in self.frames
        num_screens = 17 # Based on the plan
        for i in range(num_screens):
            frame = tk.Frame(self.container, bg=BG_COLOR)
            frame.grid(row=0, column=0, sticky="nsew")
            populate_func = getattr(self, f"_populate_screen_{i}", self._populate_placeholder)
            populate_func(frame, i) # Pass index for answer storage
            self.frames.append(frame)

    def _create_footer(self):
        footer_frame = tk.Frame(self, bg=BG_COLOR, pady=5)
        footer_frame.pack(side="bottom", fill="x")

        # Back Button
        self.back_button = ttk.Button(footer_frame, text="<- Cofnij (Back)",
                                     command=lambda: self.navigate_to(self.current_screen_index - 1),
                                     style="App.TButton")
        self.back_button.pack(side="left", padx=PAD_X)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(footer_frame, variable=self.progress_var, maximum=len(self.frames),
                                             style="App.Horizontal.TProgressbar")
        self.progress_bar.pack(side="left", expand=True, fill="x", padx=PAD_X)

        # Next Button (often managed per screen, but keep placeholder)
        self.next_button = ttk.Button(footer_frame, text="Dalej (Next) ->",
                                     command=lambda: self.navigate_to(self.current_screen_index + 1),
                                     style="App.TButton")
        # Initially hidden, shown/updated by screens
        # self.next_button.pack(side="right", padx=PAD_X) # We'll pack it in show_screen logic if needed

         # Feedback Label
        feedback_label = tk.Label(footer_frame, textvariable=self.feedback_var, font=DEFAULT_FONT,
                                  bg=BG_COLOR, fg=TEXT_COLOR, wraplength=400)
        feedback_label.pack(side="bottom", fill="x", pady=5) # Below progress/buttons

        # --- Configure Styles (Basic Theming) ---
        style = ttk.Style()
        style.theme_use('clam') # Use a theme that allows easier color configuration

        style.configure("App.TButton",
                        font=DEFAULT_FONT,
                        background=SECONDARY_COLOR,
                        foreground=BUTTON_TEXT_COLOR,
                        padding=(10, 5),
                        borderwidth=0)
        style.map("App.TButton",
                  background=[('active', ACCENT_COLOR)]) # Basic hover effect

        style.configure("Correct.TButton", background=CORRECT_COLOR)
        style.configure("Incorrect.TButton", background=INCORRECT_COLOR)


        style.configure("App.Horizontal.TProgressbar",
                        thickness=15,
                        background=PRIMARY_COLOR, # Color of the moving bar
                        troughcolor= '#d3d3d3') # Background of the trough

    def show_screen(self, index):
        if 0 <= index < len(self.frames):
            # Clear previous screen's answers and feedback (important!)
            self.user_answers[self.current_screen_index] = {} # Reset answers for old screen
            self.feedback_var.set("") # Clear feedback text

            # Reset any temporary button styles from quiz feedback
            self._reset_widget_styles(self.frames[self.current_screen_index])

            frame_to_show = self.frames[index]
            self.current_screen_index = index

            # Reset and clear dynamic widgets (like Entries created per screen)
            # This might need more specific handling based on screen type
            for widget in frame_to_show.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END) # Clear entry fields
                    widget.configure(validate="none") # Reset validation state if used

            frame_to_show.tkraise() # Bring the selected frame to the front

            # Update Navigation Buttons
            self.back_button.config(state="normal" if index > 0 else "disabled")
            # Decide if Next button should be shown globally or per screen
            # Global 'Next' - Might be confusing for quiz/input screens
            # self.next_button.config(state="normal" if index < len(self.frames) - 1 else "disabled")
            # Let's handle "Next" within each screen's logic for clarity

            # Update Progress Bar
            self.progress_var.set(index + 1)

    def navigate_to(self, index):
        if 0 <= index < len(self.frames):
            self.show_screen(index)
        else:
            print(f"Navigation index {index} out of bounds.")

    def _clear_feedback_after_delay(self, delay=3000):
         # Schedules the feedback to be cleared
         self.after(delay, lambda: self.feedback_var.set(""))

    def _reset_widget_styles(self, frame):
        """Resets styles for widgets like buttons after feedback."""
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Button) and widget.cget("style") in ["Correct.TButton", "Incorrect.TButton"]:
                widget.configure(style="App.TButton")
            if isinstance(widget, tk.Entry):
                 widget.config(validate="none", borderwidth=1, relief="sunken") # Reset entry border

    # --- Screen Content Population Functions ---

    def _create_utility_widget(self, parent, widget_type, text="", **kwargs):
        """Helper to create styled widgets."""
        options = {
            'bg': BG_COLOR,
            'fg': TEXT_COLOR,
            'font': DEFAULT_FONT
        }
        # Button needs different fg/bg setup handled via style mostly
        if widget_type == tk.Label:
             if 'font' not in kwargs:
                 options['font'] = kwargs.pop('font', DEFAULT_FONT)
             options['text'] = text
             options['wraplength'] = kwargs.pop('wraplength', WRAP_LENGTH)
             options.update(kwargs)
             widget = tk.Label(parent, **options)
        elif widget_type == ttk.Button:
             # ttk buttons use styles
            options = {'style': "App.TButton"} # Apply default style
            options['text'] = text
            options.update(kwargs)
            widget = ttk.Button(parent, **options)

        elif widget_type == tk.Entry:
             options['fg'] = TEXT_COLOR # Text color inside entry
             options['relief'] = "sunken"
             options['borderwidth'] = 1
             options['width'] = kwargs.pop('width', 40) # Default width
             options.update(kwargs)
             widget = tk.Entry(parent, **options)
        # Add other types (Radiobutton, etc.) if needed
        else:
             widget = widget_type(parent, text=text, **kwargs) # Fallback

        return widget

    def _populate_placeholder(self, parent_frame, screen_index):
        self._create_utility_widget(parent_frame, tk.Label, text=f"Screen {screen_index}: Placeholder", font=TITLE_FONT).pack(pady=20)
        self._create_utility_widget(parent_frame, tk.Label, text="Content for this screen will be added here.").pack(pady=10)
        self._create_utility_widget(parent_frame, ttk.Button, text="Dalej (Next) ->",
                                   command=lambda: self.navigate_to(screen_index + 1)).pack(pady=20, side="bottom")


    # --- Screen 0: Introduction ---
    def _populate_screen_0(self, frame, screen_index):
        self._create_utility_widget(frame, tk.Label, "¡Bienvenido a Aprender Polaco!", font=TITLE_FONT).pack(pady=20)
        intro_text = """Polish (Polski) is a West Slavic language spoken mainly in Poland.
It uses the Latin alphabet like Spanish, but with unique letters and sounds.
We'll explore the basics together!

Comparison: Like Spanish, Polish has grammatical gender, but it has three + cases!
Word order is typically SVO like Spanish, but can be more flexible."""
        self._create_utility_widget(frame, tk.Label, intro_text, justify=tk.LEFT).pack(pady=15)
        self._create_utility_widget(frame, ttk.Button, text="Start ->",
                                   command=lambda: self.navigate_to(screen_index + 1)).pack(pady=30, side="bottom")

    # --- Screen 1: Alphabet ---
    def _populate_screen_1(self, frame, screen_index):
        self._create_utility_widget(frame, tk.Label, "The Polish Alphabet vs. Spanish", font=TITLE_FONT).pack(pady=20)
        alphabet_text = """Polish uses most Latin letters, plus: Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż.
   Key Differences:
   - Nasal Vowels: Ą, Ę (mąka, ręka) - No Spanish equivalent.
   - Soft Consonants: Ć, Ś, Ź, Dź (ćma, środa, źle, dziękuję) - Different from Spanish C/S/Z.
   - Hard Consonants: CZ (like 'ch'), SZ ('sh'), Ż/RZ ('s' in pleasure) (czekolada, szok, rzeka)
   - Ł: Pronounced like 'w' (ładny) - Different from Spanish 'l'.
   - Ó: Sounds like 'U' (ósma).
   - H / Ch: Both sound like Spanish 'J' (hotel, choroba).
   """
        self._create_utility_widget(frame, tk.Label, alphabet_text, justify=tk.LEFT).pack(pady=15)
        self._create_utility_widget(frame, ttk.Button, text="Dalej: Pozdrowienia (Next: Greetings) ->",
                                   command=lambda: self.navigate_to(screen_index + 1)).pack(pady=30, side="bottom")

    # --- Screen 4: Greetings Quiz --- (Example with Interaction)
    def _populate_screen_4(self, frame, screen_index):
        self._create_utility_widget(frame, tk.Label, "Szybki Test: Powitania (Quick Quiz: Greetings)", font=TITLE_FONT).pack(pady=20)

        q1_frame = tk.Frame(frame, bg=BG_COLOR)
        q1_frame.pack(pady=10, fill='x', padx=50)
        self._create_utility_widget(q1_frame, tk.Label, "P1: Spotykasz profesora rano. Co mówisz?").pack()

        q1_options = ["A) Cześć", "B) Dzień dobry", "C) Dobranoc"]
        q1_correct = "B"
        for i, option in enumerate(q1_options):
            opt_letter = option.split(")")[0].strip()
            btn = self._create_utility_widget(q1_frame, ttk.Button, option, width=20,
                command=lambda s_idx=screen_index, q_idx=0, opt=opt_letter, correct=q1_correct, button_widget=None: self.handle_quiz_selection(s_idx, q_idx, opt, correct, button_widget)
            )
             # Need to pass the button itself to the lambda for styling - slight hack
            btn.configure(command=lambda s_idx=screen_index, q_idx=0, opt=opt_letter, correct=q1_correct, button_widget=btn: self.handle_quiz_selection(s_idx, q_idx, opt, correct, button_widget))
            btn.pack(pady=3)


        q2_frame = tk.Frame(frame, bg=BG_COLOR)
        q2_frame.pack(pady=10, fill='x', padx=50)
        self._create_utility_widget(q2_frame, tk.Label, "P2: Wychodzisz od przyjaciela. Co możesz powiedzieć?").pack()
        q2_options = ["A) Do widzenia", "B) Dzień dobry", "C) Cześć / Na razie"]
        q2_correct = "C"
        for i, option in enumerate(q2_options):
            opt_letter = option.split(")")[0].strip()
            btn = self._create_utility_widget(q2_frame, ttk.Button, option, width=20,
                 command=lambda s_idx=screen_index, q_idx=1, opt=opt_letter, correct=q2_correct, button_widget=None: self.handle_quiz_selection(s_idx, q_idx, opt, correct, button_widget)
            )
            btn.configure(command=lambda s_idx=screen_index, q_idx=1, opt=opt_letter, correct=q2_correct, button_widget=btn: self.handle_quiz_selection(s_idx, q_idx, opt, correct, button_widget))
            btn.pack(pady=3)

        # Conditional Next Button for Quiz Screen
        self._create_utility_widget(frame, ttk.Button, text="Dalej: Przedstawianie się ->",
             command=lambda s_idx=screen_index: self.check_quiz_completion_and_navigate(s_idx, 2, s_idx + 1) # Check 2 questions complete
        ).pack(pady=30, side="bottom")


    # --- Screen 6: Intro Fill-in --- (Example with Entry)
    def _populate_screen_6(self, frame, screen_index):
        self._create_utility_widget(frame, tk.Label, "Ćwiczenie: Przedstawianie się", font=TITLE_FONT).pack(pady=20)
        prompts = [
            ("A: Dzień dobry! Jak ______ się nazywa? (Do kobiety)", "pani", 0),
            ("B: Dzień dobry! Nazywam ______ Ewa Nowak.", "się", 1),
            ("A: Miło ______.", "mi", 2),
            ("A: Cześć! Jak się ______?", "nazywasz", 3),
            ("B: Cześć! ______ się Piotr.", "Nazywam", 4),
        ]
        entries = {}

        for text, answer, index in prompts:
             prompt_frame = tk.Frame(frame, bg=BG_COLOR)
             prompt_frame.pack(pady=7, fill='x', padx=50)
             self._create_utility_widget(prompt_frame, tk.Label, text, justify=tk.LEFT).pack(side=tk.LEFT, anchor='w')
             entry = self._create_utility_widget(prompt_frame, tk.Entry, width=15) # Adjust width as needed
             entry.pack(side=tk.RIGHT, anchor='e', padx=10)
             entries[index] = (entry, answer)

        # Check Button & Conditional Next
        # Let's make Check update feedback and enable Next if all are correct
        next_btn = self._create_utility_widget(frame, ttk.Button, text="Dalej: Gramatyka ->", state="disabled",
             command=lambda: self.navigate_to(screen_index + 1)
        )
        check_btn = self._create_utility_widget(frame, ttk.Button, text="Sprawdź (Check)",
             command=lambda s_idx=screen_index, ents=entries, next_button=next_btn: self.check_fill_in_answers(s_idx, ents, next_button)
        )
        check_btn.pack(pady=20, side="bottom")
        next_btn.pack(pady=20, side="bottom")


    # Add other _populate_screen_N methods here following the same pattern...
    # e.g., _populate_screen_2, _populate_screen_3, _populate_screen_5, _populate_screen_7 etc.
    # Use Labels for text, Buttons for quiz options/navigation, Entry for fill-ins.
    # Remember to pass screen_index and adjust command lambdas.


    # --- Interaction Handlers ---

    def handle_quiz_selection(self, screen_index, question_index, selected_option, correct_option, button_widget):
        # Prevent re-answering if already answered
        if self.user_answers.get(screen_index, {}).get(question_index):
             self.feedback_var.set(f"Pytanie {question_index + 1} już odpowiedziane.")
             return

        # Store the answer
        if screen_index not in self.user_answers:
            self.user_answers[screen_index] = {}
        self.user_answers[screen_index][question_index] = selected_option

        # Provide feedback and style the button
        is_correct = (selected_option.strip() == correct_option.strip())
        if is_correct:
            self.feedback_var.set(f"Pytanie {question_index + 1}: Poprawnie! ({selected_option})")
            if button_widget: button_widget.configure(style="Correct.TButton")
            # Disable buttons for this question to prevent re-answering
            parent_frame = button_widget.master
            for child in parent_frame.winfo_children():
                 if isinstance(child, ttk.Button):
                    child.configure(state="disabled")

        else:
            self.feedback_var.set(f"Pytanie {question_index + 1}: Niepoprawnie. Wybrano {selected_option}, poprawna: {correct_option}.")
            if button_widget: button_widget.configure(style="Incorrect.TButton")
            # Disable buttons and mark the correct one
            parent_frame = button_widget.master
            for child in parent_frame.winfo_children():
                 if isinstance(child, ttk.Button):
                     child.configure(state="disabled")
                     # Highlight the correct button
                     btn_opt_letter = child.cget('text').split(")")[0].strip()
                     if btn_opt_letter == correct_option.strip():
                          child.configure(style="Correct.TButton") # Mark correct one green

        #self._clear_feedback_after_delay()

    def check_quiz_completion_and_navigate(self, screen_index, num_questions_expected, next_screen_index):
        """Checks if all quiz questions on a screen are answered before navigating."""
        answers_on_screen = self.user_answers.get(screen_index, {})
        if len(answers_on_screen) == num_questions_expected:
            self.navigate_to(next_screen_index)
        else:
            self.feedback_var.set(f"Proszę odpowiedzieć na wszystkie {num_questions_expected} pytania.")
            self._clear_feedback_after_delay()

    def check_fill_in_answers(self, screen_index, entries_dict, next_button):
        """Checks fill-in answers, gives feedback, enables Next if all correct."""
        all_correct = True
        correct_count = 0
        total_entries = len(entries_dict)

        if screen_index not in self.user_answers:
            self.user_answers[screen_index] = {}

        for index, (entry_widget, correct_answer) in entries_dict.items():
            user_answer = entry_widget.get().strip()
            self.user_answers[screen_index][index] = user_answer # Store user attempt

            if user_answer.lower() == correct_answer.lower():
                entry_widget.config(foreground="black", relief="solid", borderwidth=2, highlightthickness=2, highlightbackground=CORRECT_COLOR, highlightcolor=CORRECT_COLOR)
                correct_count += 1
            elif user_answer == "":
                all_correct = False # Cannot be all correct if any are empty
                entry_widget.config(foreground="black", relief="sunken", borderwidth=1, highlightthickness=0) # Reset if empty
            else:
                all_correct = False
                entry_widget.config(foreground="black", relief="solid", borderwidth=2, highlightthickness=2, highlightbackground=INCORRECT_COLOR, highlightcolor=INCORRECT_COLOR)

        if all_correct:
            self.feedback_var.set("Wszystko poprawnie!")
            next_button.config(state="normal") # Enable Next button
        else:
            self.feedback_var.set(f"Poprawnie: {correct_count}/{total_entries}. Spróbuj ponownie.")
            next_button.config(state="disabled") # Keep Next disabled
            self._clear_feedback_after_delay(4000)


# --- Run the Application ---
if __name__ == "__main__":
    app = PolishLearningApp()
    app.mainloop()
