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
