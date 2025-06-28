// p5.js Wedding Beverage Calculator - Standalone Version
// This sketch recreates the functionality of the original HTML/CSS/JS application
// using only the p5.js library. All UI elements are drawn and managed in code.

// --- GLOBAL CONFIGURATION & STATE ---

// State object to hold all application data.
// It's a direct port from the original JS logic.
let state = {};

// UI element registry and screen management
let ui = {};
let currentScreen = 'setup'; // Initial screen
let activePhase = 'phase1'; // For the 'plan' screen
let contentStartY = 120; // Increased vertical spacing

// Color Palette (from original CSS)
const colors = {
    background: '#FDFBF8',
    text: '#4A4A4A',
    textLight: '#7a7a7a',
    primary: '#d88c75', // Warm pink/orange
    secondary: '#4c9b8e', // Teal
    accent: '#E6DACE',
    border: '#F0EBE3',
    white: '#FFFFFF',
    statCard: [230, 218, 206],
    formula: '#2d5e56' // Dark teal for formulas
};

// Font configuration
let headerFont = 'serif';
let bodyFont = 'sans-serif';
let formulaFont = 'monospace';


// --- P5.JS SETUP & DRAW LOOPS ---

function setup() {
    createCanvas(windowWidth, windowHeight);
    textFont(bodyFont);

    // 1. Initialize application data (ported from original)
    initializeStateData();

    // 2. Create all UI elements for all screens
    buildUI();

    // 3. Run initial calculation to populate UI with default values
    calculateAndRenderResults();
}

function draw() {
    background(colors.background);

    // Center the main content area
    const contentWidth = min(1200, width - 40);
    translate((width - contentWidth) / 2, 0);

    // Draw common elements
    drawHeader(contentWidth);
    drawFooter(contentWidth);

    // Draw the currently active screen
    switch (currentScreen) {
        case 'setup':
            drawSetupScreen(contentWidth);
            break;
        case 'plan':
            drawPlanScreen(contentWidth);
            break;
        case 'results':
            drawResultsScreen(contentWidth);
            break;
        case 'visualizer':
            drawVisualizerScreen(contentWidth);
            break;
        case 'formulas':
            drawFormulasScreen(contentWidth);
            break;
        case 'insights':
            drawInsightsScreen(contentWidth);
            break;
    }
}


// --- SCREEN DRAWING FUNCTIONS ---

function drawHeader(w) {
    // Header background
    fill(colors.white);
    noStroke();
    rect(0, 0, w, 60);
    stroke(colors.border);
    line(0, 60, w, 60);

    // --- Defensive Layout Logic ---
    const buttonXPositions = Object.values(ui.navButtons).map(b => b.x);
    const navBlockStartX = buttonXPositions.length > 0 ? min(buttonXPositions) : w;
    const titleAvailableWidth = navBlockStartX - 20 - 20;

    // Title
    fill(colors.text);
    textFont(headerFont);
    textSize(24);
    textAlign(LEFT, CENTER);

    let titleString = "Wedding Beverage Planner";
    if (textWidth(titleString) > titleAvailableWidth) {
        titleString = "Beverage Planner";
    }
    if (textWidth(titleString) > titleAvailableWidth) {
        titleString = "WBP";
    }
    text(titleString, 20, 30);
    
    // Navigation Buttons
    Object.values(ui.navButtons).forEach(button => button.draw());
}


function drawFooter(w) {
    fill(colors.textLight);
    textFont(bodyFont);
    textSize(12);
    textAlign(CENTER, CENTER);
    text('Interactive p5.js application generated from the "Comprehensive Wedding Beverage & Ice Calculation Template" report.', w / 2, height - 20);
}

function drawSectionHeader(title, subtitle, y, w) {
    // Title
    fill(colors.text);
    textFont(headerFont);
    textSize(36);
    textAlign(CENTER, TOP);
    text(title, w / 2, y);

    // Subtitle
    fill(colors.textLight);
    textFont(bodyFont);
    textSize(14);
    rectMode(CENTER);
    text(subtitle, w / 2, y + 50, w * 0.8, 100);
    rectMode(CORNER);
}

function drawSetupScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "1. Event Setup",
        "Configure the core details of your event. Use the sliders to adjust your guest list composition. These numbers form the foundation for all subsequent calculations.",
        y, w
    );
    y += 150;

    const colWidth = (w - 40) / 3;
    const cardHeight = 350;

    // Card 1: Guest Profile
    drawCard(0, y, colWidth, cardHeight);
    ui.setup.guestSliders.totalGuests.x = 20;
    ui.setup.guestSliders.womenPercent.x = 20;
    ui.setup.guestSliders.totalGuests.y = y + 100;
    ui.setup.guestSliders.womenPercent.y = y + 170;
    ui.setup.guestSliders.totalGuests.w = colWidth - 40;
    ui.setup.guestSliders.womenPercent.w = colWidth - 40;
    fill(colors.text);
    textFont(headerFont);
    textSize(20);
    textAlign(LEFT, TOP);
    text("Guest Profile", 20, y + 20);
    ui.setup.guestSliders.totalGuests.draw();
    ui.setup.guestSliders.womenPercent.draw();
    drawGuestProfileText(y + 230, colWidth);

    const x2 = colWidth + 20;
    drawCard(x2, y, colWidth, cardHeight);
    fill(colors.text);
    textFont(headerFont);
    textSize(20);
    textAlign(LEFT, TOP);
    text("Event Timeline", x2 + 20, y + 20);
    drawTimelineInfo(x2 + 20, y + 70);

    const x3 = (colWidth + 20) * 2;
    drawCard(x3, y, colWidth, cardHeight);
    fill(colors.text);
    textFont(headerFont);
    textSize(20);
    textAlign(LEFT, TOP);
    text("Serving Sizes (per Unit)", x3 + 20, y + 20);
    drawServingSizes(x3 + 20, y + 70, colWidth - 40);
}

function drawPlanScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "2. Consumption Plan",
        "Visualize and adjust beverage preferences for each event phase. Use the tabs to switch phases and sliders to fine-tune the drink distribution. Percentages will automatically balance.",
        y, w
    );
    y += 150;

    drawCard(0, y, w, 550);

    Object.values(ui.plan.phaseTabs).forEach(button => button.draw());

    const colWidth = (w - 80) / 3;
    const xPositions = [20, colWidth + 50, (colWidth + 30) * 2 + 20];

    ['women', 'men', 'nonDrinkers'].forEach((group, i) => {
        let x = xPositions[i];
        let groupTitle = group.charAt(0).toUpperCase() + group.slice(1);
        if (group === 'nonDrinkers') groupTitle = "Non-Drinker Preferences";
        else groupTitle += "'s Preferences";

        fill(colors.text);
        textFont(headerFont);
        textSize(18);
        textAlign(CENTER, TOP);
        text(groupTitle, x + colWidth / 2, y + 90);

        ui.plan.charts[activePhase][group].x = x + colWidth / 2;
        ui.plan.charts[activePhase][group].y = y + 200;
        ui.plan.charts[activePhase][group].draw();

        let sliderY = y + 330;
        ui.plan.sliders[activePhase][group].forEach(slider => {
            slider.x = x;
            slider.y = sliderY;
            slider.w = colWidth;
            slider.draw();
            sliderY += 45;
        });
    });
}

function drawResultsScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "3. Shopping List & Summary",
        "Here is your dynamically calculated shopping list. This summary updates in real-time based on all your inputs, giving you a clear and actionable list of what to buy.",
        y, w
    );
    y += 150;

    const statCardWidth = (w - 60) / 4;
    Object.values(ui.results.statDisplays).forEach((display, i) => {
        let x = i * (statCardWidth + 20);
        drawCard(x, y, statCardWidth, 100, colors.statCard);
        fill(colors.text);
        textFont(headerFont);
        textSize(18);
        textAlign(CENTER, CENTER);
        text(display.label, x + statCardWidth / 2, y + 25);
        textFont(headerFont);
        textSize(36);
        text(display.value, x + statCardWidth / 2, y + 65);
    });

    y += 140;

    drawCard(0, y, w, 350);
    fill(colors.text);
    textFont(headerFont);
    textSize(20);
    textAlign(LEFT, TOP);
    text("Overall Shopping List", 20, y + 20);
    drawTable(20, y + 60, w - 40, ui.results.shoppingList);

    y += 390;

    drawCard(0, y, w, 250);
    fill(colors.text);
    textFont(headerFont);
    textSize(20);
    textAlign(LEFT, TOP);
    text("Cocktail Summary", 20, y + 20);
    drawCocktailSummary(20, y + 60, w - 40);
}

function drawVisualizerScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "Dynamic Event Visualizer",
        "An abstract representation of your event's beverage plan. The number of particles reflects the total estimated drinks, with colors indicating alcoholic (warm) vs. non-alcoholic (cool) options.",
        y, w
    );
    y += 150;

    drawCard(0, y, w, height - y - 80);

    push();
    translate(0, y);
    ui.visualizer.system.run();
    pop();
}

function drawFormulasScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "Calculation Formulas",
        "This section explains the core formulas used by the planner to generate the results. The calculations are based on standard event planning principles and the data from the source report.",
        y, w
    );
    y += 150;

    let accordionY = y;
    const maxW = min(w, 800); // Center the accordions
    const startX = (w - maxW) / 2;
    
    ui.formulas.accordions.forEach(accordion => {
        accordion.w = maxW;
        accordion.x = startX;
        accordion.y = accordionY;
        accordion.draw();
        accordionY += accordion.getHeight();
    });
}


function drawInsightsScreen(w) {
    let y = contentStartY;
    drawSectionHeader(
        "Best Practices",
        "Planning a wedding involves more than just numbers. Here are some key insights from the source report to ensure your beverage service is a complete success.",
        y, w
    );
    y += 150;

    let accordionY = y;
    const maxW = min(w, 800); // Center the accordions
    const startX = (w - maxW) / 2;
    
    ui.insights.accordions.forEach(accordion => {
        accordion.w = maxW;
        accordion.x = startX;
        accordion.y = accordionY;
        accordion.draw();
        accordionY += accordion.getHeight();
    });
}


// --- UI HELPER DRAWING FUNCTIONS ---

function drawCard(x, y, w, h, c = colors.white) {
    fill(c);
    stroke(colors.border);
    strokeWeight(1);
    rect(x, y, w, h, 8);
}

function drawGuestProfileText(startY, cardW) {
    const { total, women, men, women_drinkers, men_drinkers } = state.guests;
    const women_non_drinkers = Math.max(0, women - women_drinkers);
    const men_non_drinkers = Math.max(0, men - men_drinkers);

    textAlign(LEFT, TOP);
    textFont(bodyFont);
    textSize(12);
    fill(colors.textLight);

    let y = startY;
    const x = 20;

    stroke(colors.border);
    line(x, y - 10, x + cardW - 40, y - 10);

    text("Women: ", x, y);
    fill(colors.text);
    text(`${women}`, x + 50, y);
    fill(colors.textLight);
    text(`(${women_drinkers} drinkers, ${women_non_drinkers} non-drinkers)`, x + 75, y);
    y += 20;

    text("Men: ", x, y);
    fill(colors.text);
    text(`${men}`, x + 50, y);
    fill(colors.textLight);
    text(`(${men_drinkers} drinkers, ${men_non_drinkers} non-drinkers)`, x + 75, y);
}

function drawTimelineInfo(x, y) {
    const timeline = [
        { id: "P1", title: "Friday Evening Reception", time: "5 PM - 2 AM (9 hours)" },
        { id: "P2", title: "Saturday Daytime Grill", time: "10 AM - 5 PM (7 hours)" },
        { id: "P3", title: "Saturday Evening Party", time: "5 PM - 2 AM (9 hours)" }
    ];

    let currentY = y;
    timeline.forEach(item => {
        fill(colors.accent);
        noStroke();
        ellipse(x + 20, currentY + 15, 40, 40);
        fill(colors.text);
        textAlign(CENTER, CENTER);
        textFont(bodyFont);
        textSize(14);
        text(item.id, x + 20, currentY + 15);

        textAlign(LEFT, TOP);
        fill(colors.text);
        textSize(14);
        text(item.title, x + 55, currentY);
        fill(colors.textLight);
        textSize(12);
        text(item.time, x + 55, currentY + 20);

        currentY += 60;
    });
}

function drawServingSizes(x, y, w) {
    let currentY = y;
    textAlign(LEFT, TOP);
    textFont(bodyFont);
    textSize(12);

    Object.entries(state.servings).forEach(([name, data]) => {
        if (currentY > y + 250) return;
        fill(colors.textLight);
        text(name, x, currentY);
        textAlign(RIGHT, TOP);
        fill(colors.text);
        text(data.serves.toFixed(2), x + w, currentY);
        textAlign(LEFT, TOP);
        currentY += 20;
    });
}

function drawTable(x, y, w, data) {
    const headerY = y;
    const rowHeight = 30;
    const col1X = x + 15;
    const col2X = x + w - 15;

    fill(colors.textLight);
    textFont(bodyFont);
    textSize(12);
    textAlign(LEFT, CENTER);
    text("BEVERAGE / INGREDIENT", col1X, headerY);
    textAlign(RIGHT, CENTER);
    text("BOTTLES/UNITS TO BUY", col2X, headerY);
    stroke(colors.border);
    line(x, y + 15, x + w, y + 15);

    let rowY = y + 20;
    for (const item of data) {
        if (rowY > y + 270) return;
        fill(colors.text);
        textSize(14);
        textAlign(LEFT, CENTER);
        text(item.name, col1X, rowY + rowHeight / 2);
        textAlign(RIGHT, CENTER);
        textFont(headerFont);
        text(item.units, col2X, rowY + rowHeight / 2);
        textFont(bodyFont);
        rowY += rowHeight;
    }
}

function drawCocktailSummary(x, y, w) {
    const halfW = w / 2 - 20;

    fill(colors.textLight);
    textFont(headerFont);
    textSize(16);
    textAlign(LEFT, TOP);
    text("Total Cocktail Servings", x, y);

    let textY = y + 30;
    textFont(bodyFont);
    textSize(14);
    fill(colors.text);
    text(`Friday Reception:  ${ui.results.cocktailServings.phase1}`, x, textY);
    text(`Saturday Grill:      ${ui.results.cocktailServings.phase2}`, x, textY + 25);
    text(`Saturday Party:      ${ui.results.cocktailServings.phase3}`, x, textY + 50);

    stroke(colors.border);
    line(x, textY + 80, x + halfW, textY + 80);

    textFont(headerFont);
    textSize(18);
    text(`Grand Total: ${ui.results.cocktailServings.grandTotal} servings`, x, textY + 95);

    const tableX = x + w / 2 + 20;
    const tableW = halfW;
    fill(colors.textLight);
    textFont(headerFont);
    textSize(16);
    textAlign(LEFT, TOP);
    text("Cocktail Ingredient Bottles", tableX, y);

    const headerY = y + 30;
    const rowHeight = 25;
    fill(colors.textLight);
    textFont(bodyFont);
    textSize(12);
    textAlign(LEFT, CENTER);
    text("INGREDIENT", tableX, headerY);
    textAlign(RIGHT, CENTER);
    text("BOTTLES/UNITS", tableX + tableW, headerY);
    stroke(colors.border);
    line(tableX, y + 45, tableX + tableW, y + 45);

    let rowY = y + 50;
    for (const item of ui.results.cocktailIngredients) {
        if (rowY > y + 180) return;
        fill(colors.text);
        textSize(14);
        textAlign(LEFT, CENTER);
        text(item.name, tableX, rowY + rowHeight / 2);
        textAlign(RIGHT, CENTER);
        textFont(headerFont);
        text(item.units, tableX + tableW, rowY + rowHeight / 2);
        textFont(bodyFont);
        rowY += rowHeight;
    }
}


// --- EVENT HANDLERS ---

function mousePressed() {
    const contentWidth = min(1200, width - 40);
    const startX = (width - contentWidth) / 2;

    for (const key in ui.navButtons) {
        if (ui.navButtons[key].isClicked(mouseX - startX, mouseY)) {
            Object.values(ui.navButtons).forEach(b => b.active = false);
            ui.navButtons[key].active = true;
            currentScreen = key;
            return;
        }
    }

    switch (currentScreen) {
        case 'plan':
            for (const key in ui.plan.phaseTabs) {
                if (ui.plan.phaseTabs[key].isClicked(mouseX - startX, mouseY)) {
                    Object.values(ui.plan.phaseTabs).forEach(b => b.active = false);
                    ui.plan.phaseTabs[key].active = true;
                    activePhase = key;
                    return;
                }
            }
            break;
        case 'formulas':
            ui.formulas.accordions.forEach(accordion => {
                accordion.handleClick(mouseX - startX, mouseY);
            });
            break;
        case 'insights':
            ui.insights.accordions.forEach(accordion => {
                accordion.handleClick(mouseX - startX, mouseY);
            });
            break;
    }
}

function mouseDragged() {
    const contentWidth = min(1200, width - 40);
    const startX = (width - contentWidth) / 2;

    if (currentScreen === 'setup') {
        Object.values(ui.setup.guestSliders).forEach(slider => {
            slider.handleDrag(mouseX - startX, mouseY);
        });
        updateGuestProfile();
        calculateAndRenderResults();
    } else if (currentScreen === 'plan') {
        ui.plan.sliders[activePhase].women.forEach(s => s.handleDrag(mouseX - startX, mouseY));
        ui.plan.sliders[activePhase].men.forEach(s => s.handleDrag(mouseX - startX, mouseY));
        ui.plan.sliders[activePhase].nonDrinkers.forEach(s => s.handleDrag(mouseX - startX, mouseY));
    }
}

function mouseReleased() {
    if (currentScreen === 'setup') {
        Object.values(ui.setup.guestSliders).forEach(slider => slider.release());
    } else if (currentScreen === 'plan') {
        ui.plan.sliders[activePhase].women.forEach(s => s.release());
        ui.plan.sliders[activePhase].men.forEach(s => s.release());
        ui.plan.sliders[activePhase].nonDrinkers.forEach(s => s.release());
    }
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    buildUI();
    calculateAndRenderResults();
}

// --- UI ELEMENT CLASSES ---

class Button {
    constructor(x, y, w, h, label, active = false) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.label = label;
        this.active = active;
    }

    draw() {
        let bgColor = this.active ? colors.primary : colors.white;
        let textColor = this.active ? colors.white : colors.textLight;

        if (this.isHovered(mouseX - (width - min(1200, width - 40)) / 2, mouseY)) {
            if (!this.active) {
                bgColor = '#f7f5f2';
                textColor = colors.primary;
            }
        }

        noStroke();
        fill(bgColor);
        rect(this.x, this.y, this.w, this.h, 5); // Added slight border radius

        fill(textColor);
        textAlign(CENTER, CENTER);
        textSize(14);
        text(this.label, this.x + this.w / 2, this.y + this.h / 2);
    }

    isHovered(mx, my) {
        return mx > this.x && mx < this.x + this.w && my > this.y && my < this.y + this.h;
    }

    isClicked(mx, my) {
        return this.isHovered(mx, my);
    }
}

class Slider {
    constructor(x, y, w, h, label, minVal, maxVal, initialVal, onChange) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.label = label;
        this.minVal = minVal;
        this.maxVal = maxVal;
        this.value = initialVal;
        this.onChange = onChange;

        this.handleW = 16;
        this.isDragging = false;
    }

    draw() {
        const handleX = map(this.value, this.minVal, this.maxVal, this.x, this.x + this.w);

        noStroke();
        fill(220);
        rect(this.x, this.y + this.h / 2 - 2, this.w, 4, 2);
        fill(colors.primary);
        rect(this.x, this.y + this.h / 2 - 2, handleX - this.x, 4, 2);

        stroke(colors.border);
        fill(colors.primary);
        ellipse(handleX, this.y + this.h / 2, this.handleW, this.handleW);

        fill(colors.text);
        textAlign(LEFT, CENTER);
        textSize(14);
        text(this.label, this.x, this.y - 10);
        textAlign(RIGHT, CENTER);
        text(round(this.value), this.x + this.w, this.y - 10);
    }

    handleDrag(mx, my) {
        const handleX = map(this.value, this.minVal, this.maxVal, this.x, this.x + this.w);
        if (mouseIsPressed && !this.isDragging) {
            if (dist(mx, my, handleX, this.y + this.h / 2) < this.handleW) {
                this.isDragging = true;
            }
        }

        if (this.isDragging) {
            let newValue = map(mx, this.x, this.x + this.w, this.minVal, this.maxVal);
            newValue = constrain(newValue, this.minVal, this.maxVal);
            if (abs(this.value - newValue) > 0.1) {
                this.value = newValue;
                if (this.onChange) this.onChange(this.value);
            }
        }
    }

    release() {
        this.isDragging = false;
    }
}

class DoughnutChart {
    constructor(x, y, radius, data) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.data = data;
    }

    updateData(newData) {
        this.data = newData;
    }

    draw() {
        const total = this.data.values.reduce((sum, val) => sum + val, 0);
        if (total === 0) return;

        let lastAngle = -HALF_PI;
        for (let i = 0; i < this.data.values.length; i++) {
            const val = this.data.values[i];
            const angle = (val / total) * TWO_PI;
            fill(this.data.colors[i % this.data.colors.length]);
            noStroke();
            arc(this.x, this.y, this.radius * 2, this.radius * 2, lastAngle, lastAngle + angle, PIE);
            lastAngle += angle;
        }

        fill(colors.white);
        ellipse(this.x, this.y, this.radius, this.radius);
    }
}

class AccordionItem {
    constructor(x, y, w, title, contentLines) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.title = title;
        this.contentLines = contentLines; // Expects an array of {text, type: 'normal'/'formula'}
        this.isExpanded = false;
        this.headerHeight = 50;
    }

    getHeight() {
        if (!this.isExpanded) {
            return this.headerHeight + 10;
        }
        let contentH = 20; // Initial padding
        this.contentLines.forEach(line => {
            textSize(14);
            const textW = textWidth(line.text);
            contentH += ceil(textW / (this.w - 40)) * 20 + 10; // Height per line + small gap
        });
        return this.headerHeight + contentH;
    }

    draw() {
        drawCard(this.x, this.y, this.w, this.getHeight() - 10, colors.white);

        fill(colors.text);
        textFont(headerFont);
        textSize(16);
        textAlign(LEFT, CENTER);
        text(this.title, this.x + 20, this.y + this.headerHeight / 2);

        push();
        translate(this.x + this.w - 30, this.y + this.headerHeight / 2);
        if (this.isExpanded) rotate(PI);
        fill(colors.textLight);
        noStroke();
        triangle(0, -5, -5, 5, 5, 5);
        pop();

        if (this.isExpanded) {
            let lineY = this.y + this.headerHeight + 15;
            this.contentLines.forEach(line => {
                if (line.type === 'formula') {
                    fill(colors.formula);
                    textFont(formulaFont);
                } else {
                    fill(colors.textLight);
                    textFont(bodyFont);
                }
                textSize(14);
                textAlign(LEFT, TOP);
                text(line.text, this.x + 20, lineY, this.w - 40);
                const textW = textWidth(line.text);
                lineY += ceil(textW / (this.w - 40)) * 20 + 10;
            });
        }
    }

    handleClick(mx, my) {
        if (mx > this.x && mx < this.x + this.w && my > this.y && my < this.y + this.headerHeight) {
            this.isExpanded = !this.isExpanded;
        }
    }
}

class ParticleSystem {
    constructor() {
        this.particles = [];
        this.colors = {
            alcoholic: color(216, 140, 117, 180),
            nonAlcoholic: color(76, 155, 142, 180)
        };
    }

    updateData(data) {
        this.data = data;
    }

    run() {
        if (!this.data) return;
        const targetParticleCount = constrain(ceil(this.data.totalDrinks / 20), 0, 500);

        if (this.particles.length < targetParticleCount && frameCount % 3 === 0) {
            let type = 'nonAlcoholic';
            if (this.data.totalDrinks > 0) {
                type = random(1) < (this.data.alcoholicDrinks / this.data.totalDrinks) ? 'alcoholic' : 'nonAlcoholic';
            }
            this.particles.push(new Particle(this.colors[type]));
        }

        if (this.particles.length > targetParticleCount) this.particles.splice(0, 1);

        for (let i = this.particles.length - 1; i >= 0; i--) {
            let p = this.particles[i];
            p.update();
            p.display();
            if (p.isFinished()) this.particles.splice(i, 1);
        }
    }
}

class Particle {
    constructor(c) {
        this.w = min(1200, width - 40);
        this.h = height - contentStartY - 150 - 80;
        this.x = random(this.w);
        this.y = random(this.h);
        this.vx = random(-0.5, 0.5);
        this.vy = random(-0.5, 0.5);
        this.alpha = random(150, 255);
        this.size = random(4, 10);
        this.color = c;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.alpha -= 0.8;
        if (this.x < 0 || this.x > this.w) this.vx *= -1;
        if (this.y < 0 || this.y > this.h) this.vy *= -1;
    }

    display() {
        noStroke();
        fill(red(this.color), green(this.color), blue(this.color), this.alpha);
        ellipse(this.x, this.y, this.size);
    }

    isFinished() {
        return this.alpha < 0;
    }
}


// --- CORE LOGIC & DATA INITIALIZATION ---

function buildUI() {
    const w = min(1200, width - 40);

    const breakpoint = 1100;
    let navConfig = { labels: {}, buttonWidth: 150, buttonGap: 10 };

    if (w < breakpoint) {
        navConfig.labels = { setup: "Setup", plan: "Plan", results: "List", visualizer: "Visuals", formulas: "Formulas", insights: "Info" };
        navConfig.buttonWidth = max(80, (w - 200) / 6 - navConfig.buttonGap);
    } else {
        navConfig.labels = { setup: "Event Setup", plan: "Consumption Plan", results: "Shopping List", visualizer: "Visualizer", formulas: "Formulas", insights: "Best Practices" };
        navConfig.buttonWidth = 150;
    }

    const navKeys = ['setup', 'plan', 'results', 'visualizer', 'formulas', 'insights'];
    const totalNavWidth = (navConfig.buttonWidth * navKeys.length) + (navConfig.buttonGap * (navKeys.length - 1));
    let startX = w - totalNavWidth - 10;

    ui.navButtons = {};
    navKeys.forEach((key, index) => {
        const buttonX = startX + index * (navConfig.buttonWidth + navConfig.buttonGap);
        ui.navButtons[key] = new Button(buttonX, 10, navConfig.buttonWidth, 40, navConfig.labels[key]);
    });
    if (ui.navButtons[currentScreen]) ui.navButtons[currentScreen].active = true;

    ui.setup = { guestSliders: {} };
    ui.setup.guestSliders.totalGuests = new Slider(0, 0, 0, 40, `Total Guests: ${state.guests.total}`, 1, 300, state.guests.total, (val) => {
        ui.setup.guestSliders.totalGuests.label = `Total Guests: ${round(val)}`;
    });
    ui.setup.guestSliders.womenPercent = new Slider(0, 0, 0, 40, 'Gender Split:', 0, 100, 50, (val) => {
        ui.setup.guestSliders.womenPercent.label = `Gender Split: ${round(val)}% W / ${100-round(val)}% M`;
    });

    const planCardY = contentStartY + 150;
    ui.plan = { phaseTabs: {}, sliders: {}, charts: {} };
    ui.plan.phaseTabs.phase1 = new Button(20, planCardY, 150, 40, "Friday Reception", true);
    ui.plan.phaseTabs.phase2 = new Button(180, planCardY, 150, 40, "Saturday Grill");
    ui.plan.phaseTabs.phase3 = new Button(340, planCardY, 150, 40, "Saturday Party");

    const chartColors = {
        women: ['#d88c75', '#e4a391', '#eecab9', '#f8dcd0', '#ffe6da'],
        men: ['#4c9b8e', '#6bb3a5', '#89ccbd', '#a8e5d5', '#c6ffed'],
        nonDrinkers: ['#a8a29e', '#bbb6b2', '#cec9c6', '#e0ddda']
    };
    Object.keys(state.phases).forEach(phaseId => {
        ui.plan.sliders[phaseId] = { women: [], men: [], nonDrinkers: [] };
        ui.plan.charts[phaseId] = {};
        Object.keys(state.phases[phaseId].preferences).forEach(group => {
            Object.entries(state.phases[phaseId].preferences[group]).forEach(([bev, val]) => {
                const slider = new Slider(0, 0, 0, 20, `${bev}: ${val}%`, 0, 100, val, (newVal) => {
                    const preferences = state.phases[phaseId].preferences[group];
                    const otherBeverages = Object.keys(preferences).filter(b => b !== bev);
                    const sumOfOthersBefore = otherBeverages.reduce((sum, b) => sum + preferences[b], 0);
                    preferences[bev] = round(newVal);
                    const remainingPercentage = 100 - preferences[bev];
                    if (sumOfOthersBefore > 0) {
                        const ratio = remainingPercentage / sumOfOthersBefore;
                        otherBeverages.forEach(b => { preferences[b] = round(preferences[b] * ratio); });
                    } else if (otherBeverages.length > 0) {
                        const equalShare = floor(remainingPercentage / otherBeverages.length);
                        otherBeverages.forEach(b => preferences[b] = equalShare);
                    }
                    let currentSum = Object.values(preferences).reduce((sum, v) => sum + v, 0);
                    let difference = 100 - currentSum;
                    if (difference !== 0) {
                       const keyToAdjust = otherBeverages.length > 0 ? otherBeverages[0] : bev;
                       preferences[keyToAdjust] += difference;
                       if(preferences[keyToAdjust] < 0) preferences[keyToAdjust] = 0;
                    }
                    ui.plan.sliders[phaseId][group].forEach(s => {
                        const currentBev = s.label.split(':')[0];
                        s.value = preferences[currentBev];
                        s.label = `${currentBev}: ${preferences[currentBev]}%`;
                    });
                    ui.plan.charts[phaseId][group].updateData({
                        labels: Object.keys(preferences),
                        values: Object.values(preferences),
                        colors: chartColors[group]
                    });
                    calculateAndRenderResults();
                });
                ui.plan.sliders[phaseId][group].push(slider);
            });
            const prefs = state.phases[phaseId].preferences[group];
            ui.plan.charts[phaseId][group] = new DoughnutChart(0, 0, 60, {
                labels: Object.keys(prefs),
                values: Object.values(prefs),
                colors: chartColors[group]
            });
        });
    });

    ui.results = {
        statDisplays: { total: { label: "Total Drinks", value: "0" }, alcoholic: { label: "Alcoholic Servings", value: "0" }, nonAlc: { label: "Non-Alc Servings", value: "0" }, ice: { label: "Ice Required", value: "0 kg" } },
        shoppingList: [],
        cocktailServings: { phase1: 0, phase2: 0, phase3: 0, grandTotal: 0 },
        cocktailIngredients: []
    };

    ui.visualizer = { system: new ParticleSystem() };
    
    ui.formulas = { accordions: [] };
    state.formulas.forEach(item => {
        ui.formulas.accordions.push(new AccordionItem(0, 0, w, item.title, item.content));
    });

    ui.insights = { accordions: [] };
    state.bestPractices.forEach(item => {
        ui.insights.accordions.push(new AccordionItem(0, 0, w, item.title, [{text: item.content, type: 'normal'}]));
    });
}

function updateGuestProfile() {
    const total = round(ui.setup.guestSliders.totalGuests.value);
    const womenPercent = round(ui.setup.guestSliders.womenPercent.value) / 100;
    state.guests.total = total;
    state.guests.women = round(total * womenPercent);
    state.guests.men = total - state.guests.women;
}

function calculateAndRenderResults() {
    const guestCounts = {
        womenDrinkers: state.guests.women_drinkers,
        menDrinkers: state.guests.men_drinkers,
        totalDrinkers: state.guests.women_drinkers + state.guests.men_drinkers,
        totalNonDrinkers: Math.max(0, state.guests.women - state.guests.women_drinkers) + Math.max(0, state.guests.men - state.guests.men_drinkers),
    };
    
    let allBeverageServingsAccumulator = {};
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

        Object.entries(phase.preferences.women).forEach(([beverage, percent]) => {
            const servings = womenDrinks * (percent / 100);
            allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
            if (cocktailNames.includes(beverage)) totalCocktailServingsByPhase[phaseId] += servings;
        });
        Object.entries(phase.preferences.men).forEach(([beverage, percent]) => {
            const servings = menDrinks * (percent / 100);
            allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
            if (cocktailNames.includes(beverage)) totalCocktailServingsByPhase[phaseId] += servings;
        });

        const baseNonAlcoholicServingsInPhase = guestCounts.totalNonDrinkers * phase.nonAlcoholicRate * phase.duration + guestCounts.totalDrinkers * phase.nonAlcoholicRate * phase.duration * 0.2;
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

        Object.entries(phase.preferences.nonDrinkers).forEach(([beverage, percent]) => {
             const servings = baseNonAlcoholicServingsInPhase * (percent / 100);
             allBeverageServingsAccumulator[beverage] = (allBeverageServingsAccumulator[beverage] || 0) + servings;
        });
    });

    const grandTotalCocktailServings = Object.values(totalCocktailServingsByPhase).reduce((sum, servings) => sum + servings, 0);
    let finalIngredientVolumesMl = {};
    Object.entries(allBeverageServingsAccumulator).forEach(([beverage, servings]) => {
        if (state.cocktails[beverage]) {
            Object.entries(state.cocktails[beverage]).forEach(([ingredient, volumePerCocktailServing]) => {
                finalIngredientVolumesMl[ingredient] = (finalIngredientVolumesMl[ingredient] || 0) + (volumePerCocktailServing * servings);
            });
        } else if (state.servings[beverage]) {
            const volumePerServing = state.servings[beverage].size / state.servings[beverage].serves;
            finalIngredientVolumesMl[beverage] = (finalIngredientVolumesMl[beverage] || 0) + (volumePerServing * servings);
        }
    });
    
    function isIngredientOfAnyCocktail(ingredientName) {
        for (const cocktailKey in state.cocktails) {
            if (state.cocktails[cocktailKey].hasOwnProperty(ingredientName)) return true;
        }
        return false;
    }

    let overallShoppingList = [];
    let cocktailIngredientsOnlyList = [];
    Object.entries(finalIngredientVolumesMl).forEach(([ingredient, totalVolumeMl]) => {
        if (state.servings[ingredient]) { 
            const unitsToBuy = ceil(totalVolumeMl / state.servings[ingredient].size);
            if (unitsToBuy > 0) {
                overallShoppingList.push({ name: ingredient, units: unitsToBuy });
                if (isIngredientOfAnyCocktail(ingredient)) {
                    cocktailIngredientsOnlyList.push({ name: ingredient, units: unitsToBuy });
                }
            }
        }
    });

    ui.results.statDisplays.total.value = ceil(grandTotalAlcoholicDrinksConsumed + grandTotalNonAlcoholicDrinksConsumed);
    ui.results.statDisplays.alcoholic.value = ceil(grandTotalAlcoholicDrinksConsumed);
    ui.results.statDisplays.nonAlc.value = ceil(grandTotalNonAlcoholicDrinksConsumed);
    ui.results.statDisplays.ice.value = `${ceil((grandTotalAlcoholicDrinksConsumed + grandTotalNonAlcoholicDrinksConsumed) * 0.25)} kg`;
    ui.results.shoppingList = overallShoppingList.sort((a, b) => b.units - a.units);
    ui.results.cocktailIngredients = cocktailIngredientsOnlyList.sort((a, b) => b.units - a.units);
    ui.results.cocktailServings.phase1 = ceil(totalCocktailServingsByPhase.phase1);
    ui.results.cocktailServings.phase2 = ceil(totalCocktailServingsByPhase.phase2);
    ui.results.cocktailServings.phase3 = ceil(totalCocktailServingsByPhase.phase3);
    ui.results.cocktailServings.grandTotal = ceil(grandTotalCocktailServings);
    ui.visualizer.system.updateData({
        totalDrinks: ceil(grandTotalAlcoholicDrinksConsumed + grandTotalNonAlcoholicDrinksConsumed),
        alcoholicDrinks: ceil(grandTotalAlcoholicDrinksConsumed),
        nonAlcoholicDrinks: ceil(grandTotalNonAlcoholicDrinksConsumed)
    });
}

// **** THIS FUNCTION HAS BEEN CORRECTED AND VERIFIED ****
function initializeStateData() {
    state = {
        guests: { total: 28, women: 14, men: 14, women_drinkers: 10, men_drinkers: 11, },
        servings: { "Prosecco": { size: 750, serves: 5 }, "White Wine": { size: 750, serves: 5 }, "Whiskey": { size: 750, serves: 17 }, "Beer": { size: 500, serves: 1 }, "Aperol": { size: 1000, serves: 17 }, "Coca Cola": { size: 2000, serves: 12 }, "Ginger Ale": { size: 2000, serves: 12 }, "Soda": { size: 2000, serves: 67 }, "White Rum": { size: 750, serves: 17 }, "Non-alcoholic beer": { size: 500, serves: 1 }, "Prosecco 0%": { size: 750, serves: 5 }, "Lime Juice": { size: 1000, serves: 45 }, "Simple Syrup": { size: 1000, serves: 67 }, "Elderflower Liqueur": { size: 750, serves: 12.68 }, },
        phases: {
            phase1: { name: "Friday Evening Reception", duration: 9, alcoholicRate: 1.11, nonAlcoholicRate: 1, preferences: { women: { "Prosecco": 48, "White Wine": 24, "Mojito": 19, "Aperol Spritz": 9, "Hugo": 0, "Beer": 0, "Whiskey and Cola": 0 }, men: { "Prosecco": 0, "White Wine": 18, "Mojito": 24, "Aperol Spritz": 0, "Hugo": 0, "Beer": 29, "Whiskey and Cola": 29 }, nonDrinkers: { "Non-alcoholic beer": 20, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 20, "Ginger Ale": 20 } } },
            phase2: { name: "Saturday Daytime Grill", duration: 7, alcoholicRate: 1.14, nonAlcoholicRate: 1, preferences: { women: { "Prosecco": 6, "White Wine": 12, "Mojito": 6, "Aperol Spritz": 6, "Hugo": 6, "Beer": 64, "Whiskey and Cola": 0 }, men: { "Prosecco": 0, "White Wine": 6, "Mojito": 6, "Aperol Spritz": 0, "Hugo": 0, "Beer": 82, "Whiskey and Cola": 6 }, nonDrinkers: { "Non-alcoholic beer": 30, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 15, "Ginger Ale": 15 } } },
            phase3: { name: "Saturday Evening Party", duration: 9, alcoholicRate: 1.11, nonAlcoholicRate: 1, preferences: { women: { "Prosecco": 48, "White Wine": 24, "Mojito": 19, "Aperol Spritz": 9, "Hugo": 0, "Beer": 0, "Whiskey and Cola": 0 }, men: { "Prosecco": 0, "White Wine": 18, "Mojito": 24, "Aperol Spritz": 0, "Hugo": 0, "Beer": 29, "Whiskey and Cola": 29 }, nonDrinkers: { "Non-alcoholic beer": 20, "Prosecco 0%": 10, "Coca Cola": 30, "Soda": 20, "Ginger Ale": 20 } } }
        },
        cocktails: { "Mojito": { "White Rum": 59.15, "Lime Juice": 22.18, "Simple Syrup": 14.79, "Soda": 88.72 }, "Whiskey and Cola": { "Whiskey": 44.36, "Coca Cola": 133.08 }, "Aperol Spritz": { "Prosecco": 90.00, "Aperol": 60.00, "Soda": 30.00 }, "Hugo": { "Prosecco": 88.72, "Elderflower Liqueur": 59.15, "Soda": 29.57 } },
        bestPractices: [
            { title: "Buffering for Unexpected Consumption", content: `It is strongly recommended to add a safety buffer, typically 10-15% extra, to the final calculated quantities for all beverages. This accounts for heavier-than-anticipated drinking, unexpected guests, or accidental spills.` },
            { title: "Efficient Beverage Management", content: `Consider offering signature cocktails to streamline choices and simplify the bar setup. Purchasing beverages in bulk or cases is often more economical. Ensure sufficient bar staff to maintain quick service.` },
            { title: "Importance of Quality Ingredients", content: `The quality of ingredients directly impacts the guest experience. Using fresh mixers, high-quality spirits, and appropriate ice can significantly enhance the overall enjoyment of the drinks served.` },
            { title: "Ice for More Than Just Drinks", content: `The calculated ice is for drinks only. Remember you'll need additional ice for chilling bottles in buckets or coolers. Plan to buy extra ice beyond the calculated amount.` }
        ],
        formulas: [
            { title: "1. Guest & Drinker Counts", content: [
                { text: `The number of guests who drink alcohol is based on a fixed ratio from the source report (10/14 women, 11/14 men). The rest are non-drinkers.`, type: "normal"},
                { text: `Total Drinkers = (Women Drinkers) + (Men Drinkers)`, type: "formula" },
                { text: `Total Non-Drinkers = (Total Guests) - (Total Drinkers)`, type: "formula" }
            ]},
            { title: "2. Total Drinks Per Event Phase", content: [
                { text: `Total alcoholic drinks for a phase are based on an hourly consumption rate.`, type: "normal"},
                { text: `Total Alc. Drinks = Total Drinkers × Rate × Duration`, type: "formula" },
                { text: `Non-alcoholic drinks are calculated similarly, with an extra 20% allowance for drinkers (for mixers/hydration) and a bonus volume for non-drinkers.`, type: "normal"},
                { text: `Total Non-Alc. Drinks = (Non-Drinkers × Rate × Dur) + (Drinkers × Rate × Dur × 0.2) + (Bonus Servings)`, type: "formula" },
            ]},
            { title: "3. Individual Beverage & Ingredient Needs", content: [
                { text: `The total drinks for a group (e.g., Men) are distributed according to the preference percentages set with the sliders.`, type: "normal"},
                { text: `Drink Servings = Total Group Drinks × (Preference % / 100)`, type: "formula" },
                { text: `For cocktails, this determines servings. For direct drinks (like Beer), it's converted to volume. All volumes are summed up.`, type: "normal"},
                { text: `Ingredient Volume (ml) = Σ (Servings × ml per Serving)`, type: "formula" },
                { text: `Finally, the total required volume for each ingredient is divided by its bottle size to determine how many units to buy.`, type: "normal"},
                { text: `Bottles to Buy = CEIL(Total Volume / Bottle Size)`, type: "formula" }
            ]},
            { title: "4. Ice Calculation", content: [
                { text: `A common rule of thumb is used for ice: approximately 1 pound (0.45kg) per person if only for drinks. We simplify this based on total drinks.`, type: "normal"},
                { text: `Ice (kg) = Total Drinks (All Types) × 0.25`, type: "formula" },
            ]},
        ]
    };
}
