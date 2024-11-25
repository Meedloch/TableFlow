document.addEventListener("DOMContentLoaded", () => {
    const reservation = JSON.parse(localStorage.getItem("reservation"));
    const reservationId = localStorage.getItem("reservation_id");

    if (!reservation || !reservationId) {
        alert("Aucune réservation trouvée. Vous allez être redirigé vers la page d'accueil.");
        window.location.href = "/";
        return;
    }

    const detailsList = document.getElementById("reservationDetails");
    detailsList.innerHTML = `
        <li class="list-group-item"><strong>Numéro de réservation :</strong> ${reservationId}</li>
        <li class="list-group-item"><strong>Nombre de personnes :</strong> ${reservation["Nombre de personnes"]}</li>
        <li class="list-group-item"><strong>Option classique :</strong> ${reservation["Option classique (40€)"]}</li>
        <li class="list-group-item"><strong>Option dégustation :</strong> ${reservation["Option dégustation (60€)"]}</li>
        <li class="list-group-item"><strong>Supplément vin :</strong> ${reservation["Supplément vin (20€)"]}</li>
        <li class="list-group-item"><strong>Date :</strong> ${reservation["Date"]}</li>
        <li class="list-group-item"><strong>Heure :</strong> ${reservation["Heure"]}</li>
        <li class="list-group-item"><strong>Prénom :</strong> ${reservation["Prénom"]}</li>
        <li class="list-group-item"><strong>Nom :</strong> ${reservation["Nom"]}</li>
        <li class="list-group-item"><strong>Email :</strong> ${reservation["Email"]}</li>
        <li class="list-group-item"><strong>Téléphone :</strong> ${reservation["Téléphone"]}</li>
        <li class="list-group-item"><strong>Prix total (€) :</strong> ${reservation["Prix total (€)"]}</li>
    `;
});
