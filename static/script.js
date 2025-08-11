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
const progressBar = document.getElementById('progressInnerBar');
const progressNumber = document.getElementById('progress');

function updateProgress() {
    let checkedCount = 0;
    
    medicineCheckBox.forEach(checkbox => {
        if(checkbox.checked) {
            checkedCount += 1;
        }
    });

    let percentage = 0;
    
    if (totalMeds > 0){
        percentage = (checkedCount / totalMeds) * 100;

        if (percentage > 89){
            progressBar.style.backgroundColor= '#009c15ff';
            progress.style.color = '#009c15ff';
        }

        else if (percentage < 90 && percentage >= 80){
            progressBar.style.backgroundColor= '#94ec06ff';
            progress.style.color = '#94ec06ff';
        }

        else if (percentage < 80 && percentage >= 70){
            progressBar.style.backgroundColor= '#acf855ff';
            progress.style.color = '#acf855ff';
        }

        else if (percentage < 70 && percentage >= 60){
            progressBar.style.backgroundColor= '#f7b526ff';
            progress.style.color = '#f7b526ff';
        }

        else if (percentage < 60){
            progressBar.style.backgroundColor= '#f5150eff';
            progress.style.color = '#f5150eff';
        }

    progressBar.style.width = percentage + '%';
    progressDisplay.textContent = percentage.toFixed(0) + '%';
    }
}


medicineCheckBox.forEach(checkbox => {
    checkbox.addEventListener('change',updateProgress)
});
updateProgress();
//!DOES NOT FULLY WORK:
//TODO: make it check if it has been checked already today and if so keep it checked even after refreshing the page
medicineCheckBox.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const medName = this.parentElement.querySelector('.medName');
        const medDose = this.parentElement.querySelector('.medDose');
        const medTime = this.parentElement.querySelector('.medTime');
        const isMissed =this.parentElement.classList.contains("missed"); 
        const medId = parseInt(this.parentElement.id.replace('med-', ''));

        const timeNow = new Date();
  

        

        if (this.checked) {
            medName.style.textDecoration = 'line-through';
            medName.style.color = '#48bb78';
            medName.style.opacity = '0.7';
            medId.taken = true;

            medDose.style.textDecoration = 'line-through';
            medDose.style.color = '#48bb78';
            medDose.style.opacity = '0.7';

            medTime.style.textDecoration = 'line-through';
            medTime.style.color = '#48bb78';
            medTime.style.opacity = '0.7';
        }
        //NOT WORKING
        else if (medTime < timeNow) {
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
        
    });
});

function upcomingMeds () {
    
}

