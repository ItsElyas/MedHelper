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
    const form1 = document.getElementById("MedicineDiv");
    form1.style.display = "none";
    document.getElementById("addMedicine").style.display = "block";

    document.querySelectorAll("#yourMedicine #noMedicine").forEach(el => el.style.display = "block");
    
    const form2 = document.getElementById("medicineList");
    if (form2) {
        form2.style.display = "block";
    }
}
const progressDisplay = document.getElementById('progress');
const totalMeds = parseInt(progressDisplay.dataset.totalMeds);   //SO COOL: parseInt makes it a int and  dataset grabs the stuff from flask i think
const medicineCheckBox = document.querySelectorAll(".MedicineCheckBox");

function updateProgress() {
    let checkedCount = 0;
    
    medicineCheckBox.forEach(checkbox => {
        if(checkbox.checked) {
            checkedCount += 1;
        }
    });

    let percentage = 0;
    
    if (totalMeds > 0)
        percentage = (checkedCount / totalMeds) * 100;
    progressDisplay.textContent = percentage.toFixed(0) + '%';
}


medicineCheckBox.forEach(checkbox => {
    checkbox.addEventListener('change',updateProgress)
});
updateProgress();

medicineCheckBox.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const medName = this.parentElement.querySelector('.medName');
        const medDose = this.parentElement.querySelector('.medDose');
        const medTime = this.parentElement.querySelector('.medTime');
        const isMissed =this.parentElement.classList.contains("missed"); 
        const medId = parseInt(this.parentElement.id.replace('med-', ''));


        if (this.checked) {
            medName.style.textDecoration = 'line-through';
            medName.style.color = '#48bb78';
            medName.style.opacity = '0.7';

            medDose.style.textDecoration = 'line-through';
            medDose.style.color = '#48bb78';
            medDose.style.opacity = '0.7';

            medTime.style.textDecoration = 'line-through';
            medTime.style.color = '#48bb78';
            medTime.style.opacity = '0.7';
        }

        //NOT WORKING
        else if (isMissed) {
            medName.style.textDecoration = 'none';
            medName.style.color = '#a10000';   // dark red
            medName.style.opacity = '1';
            medName.style.fontWeight = 'bold';

            medDose.style.textDecoration = 'none';
            medDose.style.color = '#a10000';
            medDose.style.opacity = '1';
            medDose.style.fontWeight = 'bold';

            medTime.style.textDecoration = 'none';
            medTime.style.color = '#a10000';
            medTime.style.opacity = '1';
            medTime.style.fontWeight = 'bold';
        }
         else {
            medName.style.textDecoration = 'none';
            medName.style.color = '#000000';
            medName.style.opacity = '1';

            medDose.style.textDecoration = 'none';
            medDose.style.color = '#000000';
            medDose.style.opacity = '1';

            medTime.style.textDecoration = 'none';
            medTime.style.color = '#000000';
            medTime.style.opacity = '1';
        }
       
    
    })
  });

//NEEDS TO BE FIXED I CANT TELL IF IT WORKS
function updateMedClasses () {
    fetch('/checkMedications')  //Makes a GET request to the backend
    .then(response => response.json()) //Convers the response to a json
    .then(data => {
        const missedMeds = data.missed.map(med => med.id); //Grabs the list of missed meds we made
        const takenMeds = data.taken.map(med => med.id); //Grabs the list of taken meds we made

        document.querySelectorAll('.medicineCheckList').forEach(div => {
            const id = parseInt(div.id.replace("med-",""));

            if(missedMeds.includes(id)) {
                div.classList.add("missed");
            }
            else {
                div.classList.remove("missed");
            } 
             if(takenMeds.includes(id)) {
                div.classList.add("taken");
            }
            else {
                div.classList.remove("taken");
            } 
        });
    });
}



window.onload = updateMedClasses;
setInterval(updateMedClasses, 30000)

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

