const analyzeBtn = document.getElementById("analyzeBtn");
const loading = document.getElementById("loading");
const resultsDiv = document.getElementById("results");

analyzeBtn.addEventListener("click", async () => {
    const jobDescription = document.getElementById("job_description").value;
    const resumes = document.getElementById("resumes").files;

    if (!jobDescription || resumes.length === 0) {
        alert("Please add job description and upload resumes");
        return;
    }

    const formData = new FormData();
    formData.append("job_description", jobDescription);

    for (let i = 0; i < resumes.length; i++) {
        formData.append("resumes", resumes[i]);
    }

    loading.classList.remove("hidden");
    resultsDiv.innerHTML = "";

    try {
        const response = await fetch("http://localhost:8000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        loading.classList.add("hidden");

        renderResults(data.results);

    } catch (error) {
        loading.classList.add("hidden");
        alert("Error connecting to backend");
        console.error(error);
    }
});

function renderResults(results) {
    results.forEach((res, index) => {
        const card = document.createElement("div");
        card.className = "result-card";

        card.innerHTML = `
            <div class="rank">Rank #${index + 1}</div>
            <h3>${res.filename}</h3>
            <div class="match">Match Score: <strong>${res.match_percentage}%</strong></div>

            <h4>Top Matching Skills</h4>
            ${res.matched_skills.map(skill =>
                `<span class="skill matched">${skill}</span>`
            ).join("")}

            <h4>Missing Skills</h4>
            ${res.missing_skills.map(skill =>
                `<span class="skill missing">${skill}</span>`
            ).join("")}
        `;

        resultsDiv.appendChild(card);
    });
}
