// ======================================================
// COSMOSHIELD AI DASHBOARD
// Part 1
// ======================================================

// ==========================
// GLOBAL VARIABLES
// ==========================

let predictionHistory = [];

let currentHorizon = "45m";


// ==========================
// RADIATION CHART
// ==========================

const chartCanvas = document.getElementById("radiationChart");

const radiationChart = new Chart(chartCanvas, {

    type: "line",

    data: {

        labels: [],

        datasets: [

            {

                label: "Radiation (MeV)",

                data: [],

                borderColor: "#38BDF8",

                backgroundColor: "rgba(56,189,248,.15)",

                borderWidth: 3,

                pointRadius: 4,

                pointBackgroundColor: "#38BDF8",

                tension: .4,

                fill: true

            }

        ]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: false

            }

        },

        scales: {

            x: {

                ticks: {

                    color: "#94A3B8"

                },

                grid: {

                    color: "rgba(255,255,255,.05)"

                }

            },

            y: {

                ticks: {

                    color: "#94A3B8"

                },

                grid: {

                    color: "rgba(255,255,255,.05)"

                }

            }

        }

    }

});


// ==========================
// FORM
// ==========================

const form = document.getElementById("predictionForm");

const predictButton = document.querySelector(".predict-btn");


// ==========================
// SUBMIT EVENT
// ==========================

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    predictButton.disabled = true;

    predictButton.innerHTML = "Analyzing Space Weather...";


    const payload = {

        satellite: document.getElementById("satellite").value,

        energy: Number(document.getElementById("energy").value),

        imf: Number(document.getElementById("imf").value),

        bx: Number(document.getElementById("bx").value),

        by: Number(document.getElementById("by").value),

        bz: Number(document.getElementById("bz").value),

        speed: Number(document.getElementById("speed").value),

        density: Number(document.getElementById("density").value),

        temperature: Number(document.getElementById("temperature").value)

    };


    try {

        const response = await fetch("/api/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(payload)

        });


        if (!response.ok) {

            throw new Error("Server Error");

        }


        const result = await response.json();

        console.log(result);

        updateDashboard(result, payload);

    }

    catch (error) {

        console.error(error);

        alert("Prediction Failed.");

    }

    finally {

        predictButton.disabled = false;

        predictButton.innerHTML = "Analyze Space Weather";

    }

});


// ==========================
// SOLAR ACTIVITY
// ==========================

function calculateSolarActivity(speed, bz) {

    if (speed >= 650 || bz <= -10) {

        return "Extreme";

    }

    if (speed >= 550 || bz <= -5) {

        return "High";

    }

    if (speed >= 420) {

        return "Moderate";

    }

    return "Low";

}


// ==========================
// RISK COLOR
// ==========================

function applyRiskClass(element, risk) {

    element.classList.remove(

        "low",

        "medium",

        "high"

    );


    switch (risk) {

        case "LOW":

            element.classList.add("low");

            break;

        case "MEDIUM":

            element.classList.add("medium");

            break;

        default:

            element.classList.add("high");

            break;

    }

}


// ==========================
// ADD CHART POINT
// ==========================

function addChartPoint(value) {

    const time = new Date().toLocaleTimeString();

    radiationChart.data.labels.push(time);

    radiationChart.data.datasets[0].data.push(value);


    if (radiationChart.data.labels.length > 12) {

        radiationChart.data.labels.shift();

        radiationChart.data.datasets[0].data.shift();

    }

    radiationChart.update();

}
// ======================================================
// UPDATE DASHBOARD
// Part 2
// ======================================================

function updateDashboard(data, payload) {

    // -----------------------------
    // Backend Validation
    // -----------------------------

    if (data.status !== "success") {

        alert(data.message || "Prediction Failed");

        return;

    }

    const radiation = Number(data.radiation).toFixed(3);

    // -----------------------------
    // LIVE PREDICTION PANEL
    // -----------------------------

    document.getElementById("predictionValue").textContent =
        radiation;

    document.getElementById("predictionModel").textContent =
        data.model;

    document.getElementById("predictionTime").textContent =
        new Date().toLocaleTimeString();

    // -----------------------------
    // RISK BADGE
    // -----------------------------

    const predictionRisk =
        document.getElementById("predictionRisk");

    predictionRisk.textContent =
        data.risk;

    applyRiskClass(predictionRisk, data.risk);

    // -----------------------------
    // OVERVIEW
    // -----------------------------

    const overviewMission =
        document.getElementById("overviewMission");

    if (overviewMission) {

        overviewMission.textContent =
            payload.satellite;

    }

    const currentMission =
        document.getElementById("currentMission");

    if (currentMission) {

        currentMission.textContent =
            payload.satellite;

    }

    const overviewRadiation =
        document.getElementById("overviewRadiation");

    if (overviewRadiation) {

        overviewRadiation.textContent =
            radiation + " MeV";

    }

    // -----------------------------
    // SOLAR ACTIVITY
    // -----------------------------

    const activity =
        calculateSolarActivity(
            payload.speed,
            payload.bz
        );

    const solarCard =
        document.getElementById("solarActivity");

    if (solarCard) {

        solarCard.textContent =
            activity;

    }

    // -----------------------------
    // UPDATE HISTORY ARRAY
    // -----------------------------

    predictionHistory.unshift({

        time: new Date().toLocaleTimeString(),

        satellite: payload.satellite,

        radiation: radiation,

        risk: data.risk,

        model: data.model

    });

    if (predictionHistory.length > 20) {

        predictionHistory.pop();

    }

    // -----------------------------
    // LIVE CHART
    // -----------------------------

    addChartPoint(Number(radiation));

    // -----------------------------
    // RELOAD HISTORY
    // -----------------------------

    loadPredictionHistory();

}
// ======================================================
// HISTORY
// ======================================================

async function loadPredictionHistory() {

    try {

        const response = await fetch("/api/history");

        if (!response.ok) return;

        const result = await response.json();

        if (result.status !== "success") return;

        const tbody = document.getElementById("historyBody");

        tbody.innerHTML = "";

        if (result.data.length === 0) {

            tbody.innerHTML = `
            <tr>
                <td colspan="5">
                    No prediction available.
                </td>
            </tr>
            `;

            return;

        }

        result.data.forEach(item => {

            tbody.innerHTML += `

            <tr>

                <td>${item.time}</td>

                <td>${item.satellite}</td>

                <td>${Number(item.radiation).toFixed(3)} MeV</td>

                <td>

                    <span class="history-risk ${item.risk.toLowerCase()}">

                        ${item.risk}

                    </span>

                </td>

                <td>LSTM</td>

            </tr>

            `;

        });

    }

    catch (error) {

        console.log(error);

    }

}

// ======================================================
// PREDICTION HORIZON BUTTONS
// ======================================================

const horizonButtons =
    document.querySelectorAll(".horizon-buttons button");

horizonButtons.forEach(button => {

    button.addEventListener("click", () => {

        horizonButtons.forEach(btn =>
            btn.classList.remove("active")
        );

        button.classList.add("active");

        currentHorizon = button.innerText;

        console.log(
            "Prediction Horizon:",
            currentHorizon
        );

    });

});

// ======================================================
// NUMBER ANIMATION
// ======================================================

function animateValue(element, start, end, duration) {

    let startTime = null;

    function animation(currentTime) {

        if (!startTime)
            startTime = currentTime;

        const progress = Math.min(
            (currentTime - startTime) / duration,
            1
        );

        const value =
            progress * (end - start) + start;

        element.textContent =
            value.toFixed(3);

        if (progress < 1) {

            requestAnimationFrame(animation);

        }

    }

    requestAnimationFrame(animation);

}

// ======================================================
// AUTO REFRESH HISTORY
// ======================================================

setInterval(() => {

    loadPredictionHistory();

}, 30000);

// ======================================================
// PAGE LOAD
// ======================================================

window.onload = () => {

    loadPredictionHistory();

    radiationChart.update();

    console.log("CosmoShield Dashboard Ready 🚀");

};

// ======================================================
// FUTURE NOAA API PLACEHOLDER
// ======================================================

// Future:
//
// async function fetchNOAAData(){
//
// }
//
// async function updateRealtimeSolarWeather(){
//
// }
//
// async function updateLiveSatelliteData(){
//
// }
//
// These will be connected later.