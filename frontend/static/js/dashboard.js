const ctx = document.getElementById("radiationChart");

new Chart(ctx,{

type:"line",

data:{

labels:["00","04","08","12","16","20","24"],

datasets:[{

label:"Radiation (MeV)",

data:[0.22,0.31,0.29,0.45,0.38,0.41,0.36],

borderColor:"#38BDF8",

backgroundColor:"rgba(56,189,248,.15)",

fill:true,

tension:.4,

borderWidth:3,

pointRadius:4,

pointBackgroundColor:"#38BDF8"

}]

},

options:{

responsive:true,

plugins:{

legend:{

display:false

}

},

scales:{

x:{

grid:{

color:"rgba(255,255,255,.05)"

},

ticks:{

color:"#94A3B8"

}

},

y:{

grid:{

color:"rgba(255,255,255,.05)"

},

ticks:{

color:"#94A3B8"

}

}

}

}

});
const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const button = document.querySelector(".predict-btn");

    button.disabled = true;
    button.innerHTML = "Analyzing Space Weather...";

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

    try{

        const response = await fetch("/api/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(payload)

        });

        const result = await response.json();

        updateDashboard(result);

    }

    catch(error){

        alert("Prediction Failed");

        console.log(error);

    }

    finally{

        button.disabled = false;

        button.innerHTML = "Analyze Space Weather";

    }

});
function updateDashboard(data){

    if(data.status !== "success"){

        alert(data.message);

        return;

    }

    document.getElementById("predictionValue").innerHTML =
    Number(data.radiation).toFixed(3);

    document.getElementById("predictionModel").innerHTML =
    data.model;

    document.getElementById("predictionTime").innerHTML =
    new Date().toLocaleTimeString();

    document.getElementById("radiationValue").innerHTML =
    Number(data.radiation).toFixed(3);

    document.getElementById("modelValue").innerHTML =
    data.model;

    document.getElementById("riskValue").innerHTML =
    data.risk;

    document.getElementById("predictionRisk").innerHTML =
    data.risk;

    const risk=document.getElementById("predictionRisk");

    risk.className="prediction-risk";

    if(data.risk==="LOW")
        risk.classList.add("low");

    else if(data.risk==="MEDIUM")
        risk.classList.add("medium");

    else
        risk.classList.add("high");

}
async function loadPredictionHistory(){

    try{

        const response = await fetch("/api/history");

        const result = await response.json();

        if(result.status !== "success") return;

        const tbody = document.getElementById("historyBody");

        tbody.innerHTML = "";

        result.data.forEach(item=>{

            tbody.innerHTML += `
            <tr>

                <td>${item.time}</td>

                <td>${item.satellite}</td>

                <td>${Number(item.radiation).toFixed(3)} MeV</td>

                <td>${item.risk}</td>

                <td>LSTM</td>

            </tr>
            `;

        });

        if(result.data.length===0){

            tbody.innerHTML=`
            <tr>

            <td colspan="5">

            No prediction available.

            </td>

            </tr>
            `;

        }

    }

    catch(error){

        console.log(error);

    }

}
