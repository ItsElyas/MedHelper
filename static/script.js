function showForm() {
    const form = document.getElementById("MedicineDiv");
    form.style.display = "block";
    document.getElementById("addMedicine").style.display = "none";
    
}
//counter to tell user how many medications they are taken
let medCount = 0;

function submit() {
    // Gets all the values of the inputs
    const name = document.getElementById("medicineName").value;
    const dose = document.getElementById("medicineDose").value;
    const frequency = document.getElementById("Frequency").value;
    const time = document.getElementById("timeToTake").value;

    // Makes sure the user fills everything out
    if(!name || !dose || !frequency || !time) {
        alert("Please fill out all fields.");
        return
    }

    medCount++;
}