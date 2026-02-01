function openTab(tabID){
    document.querySelectorAll(".tab-btn").forEach(btn =>{
        btn.classList.remove("active");
    });
    document.querySelectorAll(".content").forEach(btn=>{
        btn.classList.remove("active");
    })
    event.target.classList.add("active");
    document.getElementById(tabID).classList.add("active");
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

document.addEventListener("DOMContentLoaded", () => {
    loadUsers();
});