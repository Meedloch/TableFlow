// Gestion de la soumission du formulaire de réservation
document.getElementById("reservationForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/api/submit-reservation", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Erreur ${response.status}: ${errorData.message}`);
        }

        const result = await response.json();
        if (result.reservation && result.reservation_id) {
            // Stocker les détails de la réservation et le numéro unique
            localStorage.setItem("reservation", JSON.stringify(result.reservation));
            localStorage.setItem("reservation_id", result.reservation_id);

            // Rediriger vers la page de résultats
            window.location.href = "/result";
        } else {
            throw new Error("Aucune réservation trouvée.");
        }
    } catch (error) {
        console.error("Erreur détectée :", error.message);
        alert(`Une erreur est survenue : ${error.message}`);
    }
});

// Gestion de la recherche de réservation par numéro
document.getElementById("searchForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    const reservationId = document.getElementById("reservationId").value;

    try {
        const response = await fetch(`/api/find-reservation/${reservationId}`);

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Erreur ${response.status}: ${errorData.message}`);
        }

        const result = await response.json();
        if (result.status === "success") {
            const reservation = result.reservation;
            document.getElementById("searchResult").innerHTML = `
                <h3>Résultats :</h3>
                <ul class="list-group">
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
                </ul>
            `;
        } else {
            document.getElementById("searchResult").innerHTML = `<p class="text-danger">${result.message}</p>`;
        }
    } catch (error) {
        console.error("Erreur détectée :", error.message);
        document.getElementById("searchResult").innerHTML = `<p class="text-danger">Une erreur est survenue lors de la recherche.</p>`;
    }
});
