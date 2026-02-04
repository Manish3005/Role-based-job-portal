function openTab(event,tabID){
    document.querySelectorAll(".tab-btn").forEach(btn =>{
        btn.classList.remove("active");
    });
    document.querySelectorAll(".content").forEach(btn=>{
        btn.classList.remove("active");
    })
    document.getElementById(tabID).classList.add("active");
    event.target.classList.add("active");
    if(tabID === "users") loadUsers();
    if(tabID === "companies") loadCompanies();
    if(tabID === "jobs") loadJobs();
}
function loadUsers() {
    fetch("/admin/users")
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector("#users-table tbody");
        tbody.innerHTML = "";

        data.forEach(user => {
            const row = `
                <tr>
                    <td>${user.id}</td>
                    <td>${user.email}</td>
                    <td>${user.role}</td>
                    <td>${user.is_active ? "Active" : "Inactive"}</td>
                    <td>${user.created_at}</td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
    });
}

function loadCompanies(){
    fetch("/admin/companies")
    .then(response => response.json())
    .then(data =>{
        const tbody = document.querySelector("#companies-table tbody");
        tbody.innerHTML = "";
        
        data.forEach(company => {
            const row = `
               <tr>
                  <td>${company.id}</td>
                  <td>${company.name}</td>
                  <td>${company.website}</td>
                  <td>${company.email}</td>
                  <td>${company.contact_number}</td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
    });
}

function loadJobs(){
    fetch("/admin/jobs")
    .then(response => response.json())
    .then(data =>{
        const tbody = document.querySelector("#jobs-table tbody");
        tbody.innerHTML="";

        data.forEach(job => {
            const row = `
                <tr>
                   <td>${job.id}</td>
                   <td>${job.title}</td>
                   <td>${job.location}</td>
                   <td>${job.salary}</td>
                   <td>${job.posted_date}</td>
                   <td>${job.name}</td>
                </tr>
            `
            tbody.innerHTML += row;
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    loadUsers();
    loadCompanies();
    loadJobs();
});