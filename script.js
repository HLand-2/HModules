const modules = [
    "Math Utils", "AI Engine", "Data Loader", "Visualizer", "Logger",
    "User Interface", "Security", "Google API", "Validator", "Config Manager"
];

const grid = document.getElementById('module-grid');

// Injecting the 10 modules into the site
modules.forEach((mod, index) => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `<h3>[${index + 1}] ${mod}</h3><p>System Node Operational</p>`;
    grid.appendChild(card);
});

function toggleSecurity() {
    const status = document.getElementById('status');
    status.innerText = status.innerText === "ENCRYPTED" ? "DECRYPTED" : "ENCRYPTED";
    status.style.color = status.innerText === "ENCRYPTED" ? "#00ffcc" : "#ff00ff";
}
function triggerPooPoo() {
    const body = document.body;
    const cards = document.querySelectorAll('.card');
    const symbols = "§±!@£$%^&*()_+=-¡€#¢∞§¶•ªº–≠⁄™‹›ﬁﬂ‡°·‚—±";
    const pooWords = ["LooLoo", "PooPoo", "ShooShoo", "WeeWee", "Flush!"];

    body.classList.toggle('poopoo-mode');

    cards.forEach((card, i) => {
        if (body.classList.contains('poopoo-mode')) {
            // Pick a random poo word and mix in symbols
            let randomWord = pooWords[Math.floor(Math.random() * pooWords.length)];
            let glitch = symbols[Math.floor(Math.random() * symbols.length)];
            card.innerHTML = `<h3>${glitch} ${randomWord} ${glitch}</h3><p>ERROR: SYSTEM STINKY</p>`;
        } else {
            // Restore original text
            card.innerHTML = `<h3>[${i + 1}] ${modules[i]}</h3><p>System Node Operational</p>`;
        }
    });

    console.log("💩 POO-POO PROTOCOL ACTIVATED 💩");
}
