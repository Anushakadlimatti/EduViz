const options = [
    { value: 'option1', label: 'GRE' },
    { value: 'option2', label: 'TOEFL' },
    { value: 'option3', label: 'University rating' },
    { value: 'option4', label: 'SOP' },
    { value: 'option5', label: 'LOR' },
    { value: 'option6', label: 'CGPA' },
    { value: 'option7', label: 'Research' },
    { value: 'option8', label: 'Chance of Admit' },
];
const sidebar = document.getElementById('sidebar');
const doneButton = document.getElementById('doneButton');
const selectedOptions = [];
options.forEach(option => {
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = option.value;
    checkbox.value = option.value;
    checkbox.addEventListener('change', handleCheckboxChange);
    const label = document.createElement('label');
    label.htmlFor = option.value;
    label.textContent = option.label;
    sidebar.appendChild(checkbox);
    sidebar.appendChild(label);
});
doneButton.addEventListener('click', handleDoneButtonClick);
function handleCheckboxChange(event) {
    const { value, checked } = event.target;
    if (checked) {
        selectedOptions.push(value);
    } else {
        const index = selectedOptions.indexOf(value);
        if (index !== -1) {
            selectedOptions.splice(index, 1);
        }
    }
}
function handleDoneButtonClick() {
    console.log('Selected options:', selectedOptions); // Log selected options
}