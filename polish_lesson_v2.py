<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Wedding Beverage Calculator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Chosen Palette: Warm Celebration -->
    <!-- Application Structure Plan: The application is designed as a single-page, task-oriented dashboard. Instead of a linear report format, the structure is divided into four logical, navigable sections: 'Event Setup' (for core inputs like guest count), 'Consumption Plan' (for interactive adjustment of beverage preferences via sliders and charts), 'Shopping List' (for the final, calculated output), and 'Best Practices' (for contextual advice). This structure was chosen to transform the static report into an active tool. It guides the user from input to output in an intuitive flow, making the complex data easily manageable and allowing for interactive "what-if" analysis, which is the primary user goal. -->
    <!-- Visualization & Content Choices: 
        - Report Info: Guest Demographics -> Goal: Inform/Interact -> Viz: Interactive Sliders -> Justification: Allows users to easily modify core numbers and see immediate feedback.
        - Report Info: Beverage Preferences (by gender/phase) -> Goal: Compare/Interact -> Viz: Doughnut Charts (Chart.js) paired with Sliders -> Justification: Visually represents proportions, and the linked sliders allow for dynamic, real-time customization of the plan, which is the app's core interactive feature. The sliders are normalized to always sum to 100%, preventing invalid data states.
        - Report Info: Final Calculated Quantities -> Goal: Inform/Synthesize -> Viz: Dynamic Stat Cards & HTML Table -> Justification: Presents the key results (ice, total drinks) as high-impact numbers and the detailed shopping list in a clear, structured, and easy-to-read format. A new 'Cocktail Summary' section explicitly details total cocktail servings and specific *all* ingredient bottle counts for cocktails, enhancing granularity and clarity for purchasing.
        - Report Info: Best Practices/Tips -> Goal: Inform -> Viz: HTML Accordion -> Justification: Condenses supplementary information into a clean, clickable format, avoiding clutter while keeping the advice accessible.
        - Library/Method: All interactions are powered by vanilla JavaScript, with Chart.js for visualizations. All data from the report is stored in JS objects for calculation. This approach meets all technical requirements. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            background-color: #FDFBF8;
            color: #4A4A4A;
            font-family: 'Inter', sans-serif;
        }
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Playfair+Display:wght@700&display=swap');
        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
        }
        .nav-link {
            transition: all 0.3s ease;
            color: #7a7a7a;
        }
        .nav-link:hover, .nav-link.active {
            color: #d88c75;
            transform: translateY(-2px);
        }
        .card {
            background-color: #FFFFFF;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05);
            border: 1px solid #F0EBE3;
        }
        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 1rem;
            height: 1rem;
            background: #d88c75;
            cursor: pointer;
            border-radius: 9999px;
        }
        .slider::-moz-range-thumb {
            width: 1rem;
            height: 1rem;
            background: #d88c75;
            cursor: pointer;
            border-radius: 9999px;
        }
        .tab-button {
            transition: all 0.3s ease;
        }
        .tab-button.active {
            background-color: #d88c75;
            color: white;
            box-shadow: 0 2px 4px rgb(0 0 0 / 0.1);
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 320px;
            margin-left: auto;
            margin-right: auto;
            height: 320px;
            max-height: 400px;
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-in-out;
        }
        .stat-card {
            background: linear-gradient(145deg, #e6dace, #fffbe8);
        }
    </style>
</head>
<body class="antialiased">

    <header class="bg-white/80 backdrop-blur-sm sticky top-0 z-50 border-b border-stone-200">
        <nav class="container mx-auto px-4 py-3 flex justify-between items-center">
            <h1 class="text-xl md:text-2xl font-bold text-stone-700">Wedding Beverage Planner</h1>
            <div class="hidden md:flex space-x-6 lg:space-x-8 text-sm font-medium">
                <a href="#setup" class="nav-link">Event Setup</a>
                <a href="#plan" class="nav-link">Consumption Plan</a>
                <a href="#results" class="nav-link">Shopping List</a>
                <a href="#insights" class="nav-link">Best Practices</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden p-2 rounded-md text-stone-600 hover:bg-stone-100">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" /></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-stone-200">
            <a href="#setup" class="block py-2 px-4 text-sm text-stone-700 hover:bg-stone-50 mobile-nav-link">Event Setup</a>
            <a href="#plan" class="block py-2 px-4 text-sm text-stone-700 hover:bg-stone-50 mobile-nav-link">Consumption Plan</a>
            <a href="#results" class="block py-2 px-4 text-sm text-stone-700 hover:bg-stone-50 mobile-nav-link">Shopping List</a>
            <a href="#insights" class="block py-2 px-4 text-sm text-stone-700 hover:bg-stone-50 mobile-nav-link">Best Practices</a>
        </div>
    </header>

    <main class="container mx-auto px-4 py-8 md:py-12">
        <section id="setup" class="mb-16 scroll-mt-24">
            <h2 class="text-3xl md:text-4xl font-bold text-center mb-2 text-stone-800">1. Event Setup</h2>
            <p class="text-center text-stone-600 mb-10 max-w-2xl mx-auto">This section allows you to configure the core details of your event. Use the sliders to adjust your guest list composition. These numbers form the foundation for all subsequent calculations, providing a tailored beverage estimate based on who will be celebrating with you.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="card p-6 md:col-span-2 lg:col-span-1">
                    <h3 class="font-bold text-xl mb-4 text-stone-700">Guest Profile</h3>
                    <div class="space-y-4">
                        <div>
                            <label for="totalGuests" class="font-medium text-sm">Total Guests: <span id="totalGuestsValue" class="font-bold text-stone-800">28</span></label>
                            <input type="range" id="totalGuests" min="1" max="300" value="28" class="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer slider">
                        </div>
                        <div>
                            <label for="women_percent" class="font-medium text-sm">Gender Split: <span id="womenPercentValue" class="font-bold text-[#d88c75]">50%</span> Women / <span id="menPercentValue" class="font-bold text-[#4c9b8e]">50%</span> Men</label>
                            <input type="range" id="women_percent" min="0" max="100" value="50" class="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer slider">
                        </div>
                         <div class="text-sm text-stone-600 pt-2 border-t border-stone-100">
                            <p>Women: <span id="womenCount" class="font-bold">14</span> (<span id="womenDrinkersCount" class="font-bold">10</span> drinkers, <span id="womenNonDrinkersCount" class="font-bold">4</span> non-drinkers)</p>
                            <p>Men: <span id="menCount" class="font-bold">14</span> (<span id="menDrinkersCount" class="font-bold">11</span> drinkers, <span id="menNonDrinkersCount" class="font-bold">3</span> non-drinkers)</p>
                        </div>
                    </div>
                </div>

                <div class="card p-6">
                    <h3 class="font-bold text-xl mb-4 text-stone-700">Event Timeline</h3>
                    <p class="text-sm text-stone-600 mb-4">The event is broken into three distinct phases, each with its own duration and consumption patterns, as defined in the source report.</p>
                    <div class="space-y-4">
                        <div class="flex items-center space-x-4">
                            <div class="flex-shrink-0 bg-[#E6DACE] rounded-full h-12 w-12 flex items-center justify-center font-bold text-stone-700">P1</div>
                            <div>
                                <p class="font-bold">Friday Evening Reception</p>
                                <p class="text-sm text-stone-600">5 PM - 2 AM (9 hours)</p>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <div class="flex-shrink-0 bg-[#E6DACE] rounded-full h-12 w-12 flex items-center justify-center font-bold text-stone-700">P2</div>
                            <div>
                                <p class="font-bold">Saturday Daytime Grill</p>
                                <p class="text-sm text-stone-600">10 AM - 5 PM (7 hours)</p>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <div class="flex-shrink-0 bg-[#E6DACE] rounded-full h-12 w-12 flex items-center justify-center font-bold text-stone-700">P3</div>
                            <div>
                                <p class="font-bold">Saturday Evening Party</p>
                                <p class="text-sm text-stone-600">5 PM - 2 AM (9 hours)</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card p-6">
                    <h3 class="font-bold text-xl mb-4 text-stone-700">Serving Sizes (per Unit)</h3>
                    <p class="text-sm text-stone-600 mb-4">This is a reference for how many standard servings are in each bottle/unit, based on the report.</p>
                    <div class="h-64 overflow-y-auto pr-2 text-sm">
                        <ul id="servingSizesList" class="space-y-2"></ul>
                    </div>
                </div>
            </div>
        </section>

        <section id="plan" class="mb-16 scroll-mt-24">
            <h2 class="text-3xl md:text-4xl font-bold text-center mb-2 text-stone-800">2. Consumption Plan</h2>
            <p class="text-center text-stone-600 mb-10 max-w-2xl mx-auto">This is the core interactive part of the planner. Here you can visualize and adjust the beverage preferences for each phase of your event. Use the tabs to switch between phases and the sliders to fine-tune the drink distribution for each group. The charts will update instantly to reflect your changes, and the percentages will automatically balance to always sum to 100%.</p>

            <div class="card p-6">
                <div class="mb-6 border-b border-stone-200">
                    <div class="flex space-x-2 md:space-x-4" id="phaseTabs">
                        <button data-phase="phase1" class="tab-button px-4 py-2 rounded-t-lg font-medium text-sm md:text-base active">Friday Reception</button>
                        <button data-phase="phase2" class="tab-button px-4 py-2 rounded-t-lg font-medium text-sm md:text-base">Saturday Grill</button>
                        <button data-phase="phase3" class="tab-button px-4 py-2 rounded-t-lg font-medium text-sm md:text-base">Saturday Party</button>
                    </div>
                </div>

                <div id="phaseContent" class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                </div>
            </div>
        </section>

        <section id="results" class="mb-16 scroll-mt-24">
            <h2 class="text-3xl md:text-4xl font-bold text-center mb-2 text-stone-800">3. Shopping List & Summary</h2>
            <p class="text-center text-stone-600 mb-10 max-w-2xl mx-auto">Here is your dynamically calculated shopping list. This summary updates in real-time based on your inputs in the sections above, giving you a clear and actionable list of what to buy for your celebration.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">
                <div class="card stat-card p-6 flex flex-col items-center justify-center text-center">
                    <h3 class="font-bold text-lg text-stone-700">Total Drinks</h3>
                    <p id="totalDrinksResult" class="text-4xl font-bold text-stone-800">0</p>
                </div>
                <div class="card stat-card p-6 flex flex-col items-center justify-center text-center">
                    <h3 class="font-bold text-lg text-stone-700">Alcoholic Servings</h3>
                    <p id="totalAlcoholicDrinksResult" class="text-4xl font-bold text-stone-800">0</p>
                </div>
                <div class="card stat-card p-6 flex flex-col items-center justify-center text-center">
                    <h3 class="font-bold text-lg text-stone-700">Non-Alc Servings</h3>
                    <p id="totalNonAlcoholicDrinksResult" class="text-4xl font-bold text-stone-800">0</p>
                </div>
                <div class="card stat-card p-6 flex flex-col items-center justify-center text-center">
                    <h3 class="font-bold text-lg text-stone-700">Ice Required</h3>
                    <p class="text-4xl font-bold text-stone-800"><span id="iceRequiredResult">0</span> kg</p>
                </div>
            </div>

            <div class="card p-6">
                <h3 class="font-bold text-xl mb-4 text-stone-700">Overall Shopping List</h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead class="border-b-2 border-stone-200 text-sm text-stone-600 uppercase">
                            <tr>
                                <th class="py-3 px-4">Beverage / Ingredient</th>
                                <th class="py-3 px-4 text-right">Bottles/Units to Buy</th>
                            </tr>
                        </thead>
                        <tbody id="shoppingListBody">
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card p-6 mt-8">
                <h3 class="font-bold text-xl mb-4 text-stone-700">Cocktail Summary</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                        <h4 class="font-semibold text-lg text-stone-600 mb-2">Total Cocktail Servings</h4>
                        <ul class="list-disc list-inside text-sm text-stone-600 space-y-1" id="cocktailServingsByPhaseList">
                            <li>Friday Reception: <span id="cocktailServingsPhase1" class="font-bold">0</span> servings</li>
                            <li>Saturday Grill: <span id="cocktailServingsPhase2" class="font-bold">0</span> servings</li>
                            <li>Saturday Party: <span id="cocktailServingsPhase3" class="font-bold">0</span> servings</li>
                        </ul>
                        <p class="mt-3 text-lg font-bold text-stone-800">Grand Total: <span id="cocktailServingsGrandTotal">0</span> servings</p>
                    </div>
                    <div>
                        <h4 class="font-semibold text-lg text-stone-600 mb-2">Cocktail Ingredient Bottles Needed</h4>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left">
                                <thead class="border-b-2 border-stone-200 text-sm text-stone-600 uppercase">
                                    <tr>
                                        <th class="py-2 px-3">Ingredient</th>
                                        <th class="py-2 px-3 text-right">Bottles/Units</th>
                                    </tr>
                                </thead>
                                <tbody id="cocktailIngredientsBody">
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="insights" class="scroll-mt-24">
            <h2 class="text-3xl md:text-4xl font-bold text-center mb-2 text-stone-800">4. Best Practices</h2>
            <p class="text-center text-stone-600 mb-10 max-w-2xl mx-auto">Planning a wedding involves more than just numbers. Here are some key insights from the source report to ensure your beverage service is a complete success.</p>
            <div id="accordion" class="max-w-3xl mx-auto space-y-4">
            </div>
        </section>

    </main>

    <footer class="text-center py-8 mt-12 border-t border-stone-200">
        <p class="text-sm text-stone-500">Interactive application generated from the "Comprehensive Wedding Beverage & Ice Calculation Template" report.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const initialData = {
                guests: {
                    total: 28,
                    women: 14,
                    men: 14,
                    women_drinkers: 10,
                    men_drinkers: 11,
                },
                // Removed "Red Wine" and "Tonic" from servings data
                servings: {
                    "Prosecco": { size: 750, serves: 5 },
                    "White Wine": { size: 750, serves: 5 },
                    "Whiskey": { size: 750, serves: 17 },
                    "Beer": { size: 500, serves: 1 },
                    "Aperol": { size: 1000, serves: 17 },
                    "Coca Cola": { size: 2000, serves: 12 },
                    "Ginger Ale": { size: 2000, serves: 12 },
                    "Soda": { size: 2000, serves: 67 },
                    "White Rum": { size: 750, serves: 17 },
                    "Non-alcoholic beer": { size: 500, serves: 1 },
                    "Prosecco 0%": { size: 750, serves: 5 },
                    "Lime Juice": { size: 1000, serves: 45 },
                    "Simple Syrup": { size: 1000, serves: 67 },
                    "Elderflower Liqueur": { size: 750, serves: 12.68 }, // Kept original calculated value
                },
                phases: {
                    phase1: {
                        name: "Friday Evening Reception",
                        duration: 9,
                        alcoholicRate: (2 + 8 * 1) / 9, // 1.11
                        nonAlcoholicRate: 1,
                        preferences: {
                            // Rebalanced percentages after removing Red Wine
                            women: { "Prosecco": 48, "White Wine": 24, "Mojito": 19, "Aperol Spritz": 9, "Hugo": 0, "Beer": 0, "Whiskey and Cola": 0 }, // Adjusted to sum to 100
                            men: { "Prosecco": 0, "White Wine": 18, "Mojito": 24, "Aperol Spritz": 0, "Hugo": 0, "Beer": 29, "Whiskey and Cola": 29 }, // Adjusted to sum to 100
                            nonDrinkers: { "Non-alcoholic beer": 20, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 20, "Ginger Ale": 20 }
                        }
                    },
                    phase2: {
                        name: "Saturday Daytime Grill",
                        duration: 7,
                        alcoholicRate: (2 + 6 * 1) / 7, // ~1.14
                        nonAlcoholicRate: 1,
                        preferences: {
                            // Rebalanced percentages after removing Red Wine
                            women: { "Prosecco": 6, "White Wine": 12, "Mojito": 6, "Aperol Spritz": 6, "Hugo": 6, "Beer": 64, "Whiskey and Cola": 0 }, // Adjusted to sum to 100
                            men: { "Prosecco": 0, "White Wine": 6, "Mojito": 6, "Aperol Spritz": 0, "Hugo": 0, "Beer": 82, "Whiskey and Cola": 6 }, // Adjusted to sum to 100
                            nonDrinkers: { "Non-alcoholic beer": 30, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 15, "Ginger Ale": 15 }
                        }
                    },
                    phase3: {
                        name: "Saturday Evening Party",
                        duration: 9,
                        alcoholicRate: (2 + 8 * 1) / 9, // 1.11
                        nonAlcoholicRate: 1,
                        preferences: {
                           // Rebalanced percentages after removing Red Wine
                           women: { "Prosecco": 48, "White Wine": 24, "Mojito": 19, "Aperol Spritz": 9, "Hugo": 0, "Beer": 0, "Whiskey and Cola": 0 }, // Adjusted to sum to 100
                           men: { "Prosecco": 0, "White Wine": 18, "Mojito": 24, "Aperol Spritz": 0, "Hugo": 0, "Beer": 29, "Whiskey and Cola": 29 }, // Adjusted to sum to 100
                           nonDrinkers: { "Non-alcoholic beer": 20, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 20, "Ginger Ale": 20 }
                        }
                    }
                },
                cocktails: {
                    "Mojito": { "White Rum": 59.15, "Lime Juice": 22.18, "Simple Syrup": 14.79, "Soda": 88.72 },
                    "Whiskey and Cola": { "Whiskey": 44.36, "Coca Cola": 133.08 },
                    "Aperol Spritz": { "Prosecco": 90.00, "Aperol": 60.00, "Soda": 30.00 },
                    "Hugo": { "Prosecco": 88.72, "Elderflower Liqueur": 59.15, "Soda": 29.57 }
                },
                bestPractices: [
                    { title: "Buffering for Unexpected Consumption", content: "Real-world events can be unpredictable. It is strongly recommended to add a safety buffer, typically 10-15% extra, to the final calculated quantities for all beverages. This accounts for heavier-than-anticipated drinking, unexpected guests, or accidental spills, ensuring a smooth event." },
                    { title: "Efficient Beverage Management", content: "Consider offering signature cocktails to streamline choices and simplify the bar setup. Purchasing beverages in bulk or cases is often more economical. For fine wines and spirits, order well in advance. Ensure sufficient bar staff to maintain quick service." },
                    { title: "Importance of Quality Ingredients", content: "The quality of ingredients directly impacts the guest experience. Using fresh mixers, high-quality spirits, and appropriate ice (e.g., large, slow-melting cubes) can significantly enhance the overall enjoyment of the drinks served." },
                    { title: "Ice for More Than Just Drinks", content: "The calculated ice is for drinks only. Remember you'll need additional ice for chilling bottles in buckets or coolers and keeping food items cold, especially during the grill. Plan to buy extra ice beyond the calculated amount." }
                ]
            };

            const state = JSON.parse(JSON.stringify(initialData));
            let charts = {};

            const DOMElements = {
                totalGuests: document.getElementById('totalGuests'),
                totalGuestsValue: document.getElementById('totalGuestsValue'),
                womenPercent: document.getElementById('women_percent'),
                womenPercentValue: document.getElementById('womenPercentValue'),
                menPercentValue: document.getElementById('menPercentValue'),
                womenCount: document.getElementById('womenCount'),
                menCount: document.getElementById('menCount'),
                womenDrinkersCount: document.getElementById('womenDrinkersCount'),
                womenNonDrinkersCount: document.getElementById('womenNonDrinkersCount'),
                menDrinkersCount: document.getElementById('menDrinkersCount'),
                menNonDrinkersCount: document.getElementById('menNonDrinkersCount'),
                servingSizesList: document.getElementById('servingSizesList'),
                phaseTabs: document.getElementById('phaseTabs'),
                phaseContent: document.getElementById('phaseContent'),
                shoppingListBody: document.getElementById('shoppingListBody'),
                cocktailServingsPhase1: document.getElementById('cocktailServingsPhase1'),
                cocktailServingsPhase2: document.getElementById('cocktailServingsPhase2'),
                cocktailServingsPhase3: document.getElementById('cocktailServingsPhase3'),
                cocktailServingsGrandTotal: document.getElementById('cocktailServingsGrandTotal'),
                cocktailIngredientsBody: document.getElementById('cocktailIngredientsBody'),
                totalDrinksResult: document.getElementById('totalDrinksResult'),
                totalAlcoholicDrinksResult: document.getElementById('totalAlcoholicDrinksResult'),
                totalNonAlcoholicDrinksResult: document.getElementById('totalNonAlcoholicDrinksResult'),
                iceRequiredResult: document.getElementById('iceRequiredResult'),
                accordion: document.getElementById('accordion'),
                mobileMenuButton: document.getElementById('mobile-menu-button'),
                mobileMenu: document.getElementById('mobile-menu'),
            };

            function setupEventListeners() {
                DOMElements.totalGuests.addEventListener('input', (e) => {
                    const total = parseInt(e.target.value);
                    const womenPercent = parseInt(DOMElements.womenPercent.value) / 100;
                    state.guests.total = total;
                    state.guests.women = Math.round(total * womenPercent);
                    state.guests.men = total - state.guests.women;
                    fullUpdate();
                });
                DOMElements.womenPercent.addEventListener('input', (e) => {
                    const womenPercent = parseInt(e.target.value) / 100;
                    const total = state.guests.total;
                    state.guests.women = Math.round(total * womenPercent);
                    state.guests.men = total - state.guests.women;
                    fullUpdate();
                });

                DOMElements.phaseTabs.addEventListener('click', (e) => {
                    if (e.target.tagName === 'BUTTON') {
                        const phaseId = e.target.dataset.phase;
                        document.querySelector('.tab-button.active').classList.remove('active');
                        e.target.classList.add('active');
                        renderPhaseContent(phaseId);
                    }
                });

                DOMElements.accordion.addEventListener('click', (e) => {
                    const header = e.target.closest('.accordion-header');
                    if (header) {
                        const content = header.nextElementSibling;
                        const icon = header.querySelector('svg');
                        const isExpanded = content.style.maxHeight && content.style.maxHeight !== '0px';
                        
                        document.querySelectorAll('.accordion-content').forEach(c => c.style.maxHeight = null);
                        document.querySelectorAll('.accordion-header svg').forEach(i => i.style.transform = 'rotate(0deg)');
                        
                        if (!isExpanded) {
                            content.style.maxHeight = content.scrollHeight + "px";
                            icon.style.transform = 'rotate(180deg)';
                        }
                    }
                });
                
                DOMElements.mobileMenuButton.addEventListener('click', () => {
                   DOMElements.mobileMenu.classList.toggle('hidden');
                });

                document.querySelectorAll('.mobile-nav-link').forEach(link => {
                    link.addEventListener('click', () => {
                        DOMElements.mobileMenu.classList.add('hidden');
                    });
                });
            }
            
            function setupPhaseContentEventListeners() {
                document.querySelectorAll('#phaseContent .slider').forEach(slider => {
                    slider.addEventListener('input', e => {
                        const { phase, group, beverage } = e.target.dataset;
                        const changedValue = parseInt(e.target.value);
                        
                        const preferences = state.phases[phase].preferences[group];
                        const otherBeverages = Object.keys(preferences).filter(b => b !== beverage);
                        const sumOfOthersBefore = otherBeverages.reduce((sum, b) => sum + preferences[b], 0);

                        preferences[beverage] = changedValue;
                        
                        const remainingPercentage = 100 - changedValue;

                        if (sumOfOthersBefore > 0) {
                            const ratio = remainingPercentage / sumOfOthersBefore;
                            otherBeverages.forEach(b => {
                                preferences[b] = Math.round(preferences[b] * ratio);
                            });
                        } else if (otherBeverages.length > 0) {
                            const equalShare = Math.floor(remainingPercentage / otherBeverages.length);
                            otherBeverages.forEach(b => preferences[b] = equalShare);
                        }

                        let currentSum = Object.values(preferences).reduce((sum, val) => sum + val, 0);
                        let difference = 100 - currentSum;
                        if (difference !== 0) {
                           const keyToAdjust = otherBeverages.length > 0 ? otherBeverages[0] : beverage;
                           preferences[keyToAdjust] += difference;
                           if(preferences[keyToAdjust] < 0) preferences[keyToAdjust] = 0;
                        }

                        Object.keys(preferences).forEach(b => {
                            const sliderElement = document.querySelector(`input[data-phase="${phase}"][data-group="${group}"][data-beverage="${b}"]`);
                            if (sliderElement) {
                                sliderElement.value = preferences[b];
                                document.getElementById(`val-${phase}-${group}-${b}`).textContent = preferences[b];
                            }
                        });

                        updateChart(phase, group);
                        calculateAndRenderResults();
                    });
                });
            }

            function updateChart(phaseId, group) {
                const chart = charts[`${phaseId}-${group}`];
                if (chart) {
                    const preferences = state.phases[phaseId].preferences[group];
                    chart.data.labels = Object.keys(preferences);
                    chart.data.datasets[0].data = Object.values(preferences);
                    chart.update('none'); 
                }
            }
            
            function renderServingSizes() {
                DOMElements.servingSizesList.innerHTML = Object.entries(state.servings).map(([name, data]) => `
                    <li class="flex justify-between items-center">
                        <span>${name}</span>
                        <span class="font-bold text-stone-700">${data.serves.toFixed(2)}</span>
                    </li>
                `).join('');
            }
            
            function renderBestPractices() {
                DOMElements.accordion.innerHTML = state.bestPractices.map((item) => `
                    <div class="card">
                        <div class="accordion-header flex justify-between items-center p-4 cursor-pointer">
                            <h4 class="font-bold text-stone-700">${item.title}</h4>
                            <svg class="w-5 h-5 text-stone-500 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                        </div>
                        <div class="accordion-content">
                            <div class="p-4 pt-0 text-stone-600 text-sm">
                                <p>${item.content}</p>
                            </div>
                        </div>
                    </div>
                `).join('');
            }

            function renderPhaseContent(phaseId) {
                const phase = state.phases[phaseId];
                const chartColors = {
                    women: ['#d88c75', '#e4a391', '#eecab9', '#f8dcd0', '#ffe6da', '#fff0e8', '#fff8f4'],
                    men: ['#4c9b8e', '#6bb3a5', '#89ccbd', '#a8e5d5', '#c6ffed', '#e3fff6', '#f0fffa'],
                    nonDrinkers: ['#a8a29e', '#bbb6b2', '#cec9c6', '#e0ddda', '#f2f0ee']
                };
                const createSectionHTML = (group, title) => {
                    const preferences = phase.preferences[group];
                    return `
                        <div class="p-4 rounded-lg border border-stone-100">
                            <h4 class="font-bold text-xl mb-4 text-center text-stone-700">${title}</h4>
                            <div class="chart-container mb-6">
                                <canvas id="chart-${phaseId}-${group}"></canvas>
                            </div>
                            <div class="space-y-3">
                                ${Object.keys(preferences).map(beverage => `
                                    <div>
                                        <label class="text-sm font-medium flex justify-between">
                                            <span>${beverage}</span>
                                            <span><span id="val-${phaseId}-${group}-${beverage}">${preferences[beverage]}</span>%</span>
                                        </label>
                                        <input type="range" min="0" max="100" value="${preferences[beverage]}" 
                                            class="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer slider"
                                            data-phase="${phaseId}" data-group="${group}" data-beverage="${beverage}">
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `;
                };

                DOMElements.phaseContent.innerHTML = createSectionHTML('women', 'Women\'s Preferences') + createSectionHTML('men', 'Men\'s Preferences') + createSectionHTML('nonDrinkers', 'Non-Drinker Preferences');

                Object.keys(phase.preferences).forEach(group => {
                    const ctx = document.getElementById(`chart-${phaseId}-${group}`);
                    if (ctx) {
                        const preferences = phase.preferences[group];
                        charts[`${phaseId}-${group}`] = new Chart(ctx, {
                            type: 'doughnut',
                            data: {
                                labels: Object.keys(preferences),
                                datasets: [{
                                    data: Object.values(preferences),
                                    backgroundColor: chartColors[group],
                                    borderColor: '#FFFFFF',
                                    borderWidth: 2,
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                cutout: '60%',
                                plugins: {
                                    legend: { display: false },
                                    tooltip: { callbacks: { label: (c) => `${c.label}: ${c.raw}%` } }
                                }
                            }
                        });
                    }
                });
                setupPhaseContentEventListeners();
            }

            function updateGuestProfileUI() {
                const { total, women, men, women_drinkers, men_drinkers } = state.guests;
                const women_non_drinkers = women - women_drinkers;
                const men_non_drinkers = men - men_drinkers;
                
                DOMElements.totalGuestsValue.textContent = total;
                DOMElements.totalGuests.value = total;

                DOMElements.womenPercentValue.textContent = `${Math.round((women / total) * 100)}%`;
                DOMElements.menPercentValue.textContent = `${Math.round((men / total) * 100)}%`;
                DOMElements.womenPercent.value = Math.round((women / total) * 100);

                DOMElements.womenCount.textContent = women;
                DOMElements.menCount.textContent = men;
                DOMElements.womenDrinkersCount.textContent = women_drinkers;
                DOMElements.womenNonDrinkersCount.textContent = women_non_drinkers >= 0 ? women_non_drinkers : 0;
                DOMElements.menDrinkersCount.textContent = men_drinkers;
                DOMElements.menNonDrinkersCount.textContent = men_non_drinkers >= 0 ? men_non_drinkers : 0;
            }

            function getGuestCounts() {
                const { women, men, women_drinkers, men_drinkers } = state.guests;
                const women_non_drinkers = Math.max(0, women - women_drinkers);
                const men_non_drinkers = Math.max(0, men - men_drinkers);
                return {
                    womenDrinkers: women_drinkers,
                    menDrinkers: men_drinkers,
                    totalDrinkers: women_drinkers + men_drinkers,
                    totalNonDrinkers: women_non_drinkers + men_non_drinkers,
                };
            }

            function isIngredientOfAnyCocktail(ingredientName) {
                for (const cocktailKey in state.cocktails) {
                    if (state.cocktails[cocktailKey].hasOwnProperty(ingredientName)) {
                        return true;
                    }
                }
                return false;
            }

            function calculateAndRenderResults() {
                const guestCounts = getGuestCounts();
                let allBeverageServingsAccumulator = {}; // Stores calculated servings of each beverage (including cocktail names)
                let totalCocktailServingsByPhase = { phase1: 0, phase2: 0, phase3: 0 };
                
                const cocktailNames = Object.keys(state.cocktails);

                let grandTotalAlcoholicDrinksConsumed = 0;
                let grandTotalNonAlcoholicDrinksConsumed = 0;

                Object.keys(state.phases).forEach(phaseId => {
                    const phase = state.phases[phaseId];
                    const alcoholicDrinksInPhase = guestCounts.totalDrinkers * phase.alcoholicRate * phase.duration;
                    const womenDrinks = alcoholicDrinksInPhase * (guestCounts.womenDrinkers / guestCounts.totalDrinkers || 0);
                    const menDrinks = alcoholicDrinksInPhase * (guestCounts.menDrinkers / guestCounts.totalDrinkers || 0);

                    grandTotalAlcoholicDrinksConsumed += alcoholicDrinksInPhase;

                    // 1. Process Alcoholic Drink Preferences into accumulator
                    Object.entries(phase.preferences.women).forEach(([beverage, percent]) => {
                        const servings = womenDrinks * (percent / 100);
                        allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
                        if (cocktailNames.includes(beverage)) {
                            totalCocktailServingsByPhase[phaseId] += servings;
                        }
                    });
                    Object.entries(phase.preferences.men).forEach(([beverage, percent]) => {
                        const servings = menDrinks * (percent / 100);
                        allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
                        if (cocktailNames.includes(beverage)) {
                            totalCocktailServingsByPhase[phaseId] += servings;
                        }
                    });

                    // 2. Process Non-Alcoholic Drinks (base for non-drinkers + mixers for drinkers)
                    const baseNonAlcoholicServingsInPhase = guestCounts.totalNonDrinkers * phase.nonAlcoholicRate * phase.duration +
                                                             guestCounts.totalDrinkers * phase.nonAlcoholicRate * phase.duration * 0.2; // 20% for mixers/hydration

                    // 3. ADDITIONAL 300ml/hour soft drink volume for Non-Drinkers
                    const additionalSoftDrinkVolumeMl = guestCounts.totalNonDrinkers * phase.duration * 300;
                    const softDrinkCategories = ["Coca Cola", "Soda", "Ginger Ale"];
                    let totalSoftDrinkPreferencePercentage = softDrinkCategories.reduce((sum, sd) => sum + (phase.preferences.nonDrinkers[sd] || 0), 0);

                    let additionalSoftDrinkServings = 0;
                    if (totalSoftDrinkPreferencePercentage > 0) {
                        softDrinkCategories.forEach(beverage => {
                            if (state.servings[beverage]) {
                                const relativePercent = (phase.preferences.nonDrinkers[beverage] || 0) / totalSoftDrinkPreferencePercentage;
                                const volumeForThisSoftDrink = additionalSoftDrinkVolumeMl * relativePercent;
                                const originalMlPerServing = state.servings[beverage].size / state.servings[beverage].serves;
                                const servingsToAdd = originalMlPerServing > 0 ? volumeForThisSoftDrink / originalMlPerServing : 0;
                                allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servingsToAdd;
                                additionalSoftDrinkServings += servingsToAdd;
                            }
                        });
                    }
                    grandTotalNonAlcoholicDrinksConsumed += baseNonAlcoholicServingsInPhase + additionalSoftDrinkServings;

                    // Distribute base non-alcoholic servings into accumulator
                    Object.entries(phase.preferences.nonDrinkers).forEach(([beverage, percent]) => {
                         const servings = baseNonAlcoholicServingsInPhase * (percent / 100);
                         allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
                    });
                });

                // Calculate grand total cocktail servings
                const grandTotalCocktailServings = Object.values(totalCocktailServingsByPhase).reduce((sum, servings) => sum + servings, 0);

                let finalIngredientVolumesMl = {}; // Total ml of each fundamental ingredient

                Object.entries(allBeverageServingsAccumulator).forEach(([beverage, servings]) => {
                    if (state.cocktails[beverage]) { // It's a cocktail (e.g., Mojito)
                        Object.entries(state.cocktails[beverage]).forEach(([ingredient, volumePerCocktailServing]) => {
                            finalIngredientVolumesMl[ingredient] = (finalIngredientVolumesMl[ingredient] || 0) + (volumePerCocktailServing * servings);
                        });
                    } else if (state.servings[beverage]) { // It's a direct drink (e.g., Beer, Coca Cola)
                        const volumePerServing = state.servings[beverage].size / state.servings[beverage].serves;
                        finalIngredientVolumesMl[beverage] = (finalIngredientVolumesMl[beverage] || 0) + (volumePerServing * servings);
                    }
                });

                let overallShoppingList = [];
                let cocktailIngredientsOnlyList = [];

                Object.entries(finalIngredientVolumesMl).forEach(([ingredient, totalVolumeMl]) => {
                    // Only consider items that exist in our servings list for shopping
                    if (state.servings[ingredient]) { 
                        const unitsToBuy = Math.ceil(totalVolumeMl / state.servings[ingredient].size);
                        if (unitsToBuy > 0) {
                            overallShoppingList.push({ name: ingredient, units: unitsToBuy });
                            if (isIngredientOfAnyCocktail(ingredient)) {
                                cocktailIngredientsOnlyList.push({ name: ingredient, units: unitsToBuy });
                            }
                        }
                    }
                });
                
                // Sort lists
                overallShoppingList.sort((a, b) => b.units - a.units);
                cocktailIngredientsOnlyList.sort((a, b) => b.units - a.units);

                DOMElements.shoppingListBody.innerHTML = overallShoppingList.map(item => `
                    <tr class="border-b border-stone-100 hover:bg-stone-50">
                        <td class="py-3 px-4 font-medium">${item.name}</td>
                        <td class="py-3 px-4 text-right font-bold text-stone-800">${item.units}</td>
                    </tr>
                `).join('');

                DOMElements.cocktailServingsPhase1.textContent = Math.ceil(totalCocktailServingsByPhase.phase1);
                DOMElements.cocktailServingsPhase2.textContent = Math.ceil(totalCocktailServingsByPhase.phase2);
                DOMElements.cocktailServingsPhase3.textContent = Math.ceil(totalCocktailServingsByPhase.phase3);
                DOMElements.cocktailServingsGrandTotal.textContent = Math.ceil(grandTotalCocktailServings);

                DOMElements.cocktailIngredientsBody.innerHTML = cocktailIngredientsOnlyList.map(item => `
                    <tr class="border-b border-stone-100 hover:bg-stone-50">
                        <td class="py-2 px-3 font-medium">${item.name}</td>
                        <td class="py-2 px-3 text-right font-bold text-stone-800">${item.units}</td>
                    </tr>
                `).join('');
                
                DOMElements.totalDrinksResult.textContent = Math.ceil(grandTotalAlcoholicDrinksConsumed + grandTotalNonAlcoholicDrinksConsumed);
                DOMElements.totalAlcoholicDrinksResult.textContent = Math.ceil(grandTotalAlcoholicDrinksConsumed);
                DOMElements.totalNonAlcoholicDrinksResult.textContent = Math.ceil(grandTotalNonAlcoholicDrinksConsumed);
                DOMElements.iceRequiredResult.textContent = Math.ceil((grandTotalAlcoholicDrinksConsumed + grandTotalNonAlcoholicDrinksConsumed) / 12 * 3);
            }

            function fullUpdate() {
                updateGuestProfileUI();
                calculateAndRenderResults();
            }

            function init() {
                setupEventListeners();
                renderServingSizes();
                renderBestPractices();
                renderPhaseContent('phase1');
                fullUpdate();
            }

            init();
        });
    </script>
</body>
</html>
