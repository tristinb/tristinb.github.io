
function toggleContent() {
    var code = document.getElementById("code");
    var button = document.getElementById("toggle-button");
    code.classList.toggle('active');

    var isVisible = code.classList.contains('active');
    var buttonText = isVisible ? 'Hide Code' : 'Show Code';
    button.textContent = buttonText
}



// const handleCheckBox2 = (checkboxId) => {
//     const checks = document.querySelectorAll('#votingRuleTable input[type="checkbox"]');
//     const checkedBox = document.getElementById(checkboxId);

//     checks.forEach((checkbox) => {
//         if (checkbox.id!==checkboxId){
//             checkbox.checked = false;
//         }
//     })
//     ;
//     var checkedRow = checkedBox.parentNode.parentNode;
//     var checkedRule = Array.from(checkedRow.children).map( (cell) => {return cell.textContent});

//     console.log(checkedRule)
// }