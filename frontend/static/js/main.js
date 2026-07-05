fetch("/api/home")

.then(response => response.json())

.then(data => {

document.getElementById("status").innerHTML =
`
Project : ${data.project}<br>

Status : ${data.status}<br>

Team : ${data.team}
`;

});