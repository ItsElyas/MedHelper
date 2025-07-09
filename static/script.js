function showForm() {
    const form1 = document.getElementById("MedicineDiv");
    form1.style.display = "block";
    document.getElementById("addMedicine").style.display = "none";

    document.querySelectorAll("#yourMedicine #noMedicine").forEach(el => el.style.display = "none");
    
    const form2 = document.getElementById("medicineList");
    if (form2) {
        form2.style.display = "none";
    }
    // document.getElementById("addMedicine").style.display = "none";
}
//counter to tell user how many medications they are taken
let medCount = 0;

function cancelMedicine() {
}

// function submitMedicine() {
//     //Prevents page refreshing
//     event.preventDefault();

//     // Gets all the values of the inputs
//     const name = document.getElementById("medicineName").value;
//     const dose = document.getElementById("medicineDose").value;
//     const frequency = document.getElementById("Frequency").value;
//     const time = document.getElementById("timeToTake").value;

//     // Makes sure the user fills everything out
//     if(!name || !dose || !frequency || !time) {
//         alert("Please fill out all fields.");
//         return
//     }

//     medCount++;
    
//     const newMedDiv = document.createElement('div');
//     newMedDiv.className = "yourMedicineList";

//     newMedDiv.innerHTML = `
//         <strong>${name}</strong><br>
//         Dose: ${dose}mg<br>
//         Time: ${time}<br>`
//         ;
//            //querySelector accesses an id/class appendChild adds a new instance of a variable
//     document.querySelector(".yourMedicineList").appendChild(newMedDiv);

//     // Hide "No medications" message
//     document.querySelectorAll("#yourMedicine #noMedicine").forEach(el => el.style.display = "none");

    
//     document.querySelector(".medicineForm").reset();    // clears form
//     document.getElementById("MedicineDiv").style.display = "none";  //hides form
//     document.getElementById("addMedicine").style.display = "inline-block";  //reshows the add medicine btn

// }

