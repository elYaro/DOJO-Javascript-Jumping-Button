
function answerCheck(thisbutton) {
    var clickedbutton  = thisbutton.innerHTML;
    var question2 = document.getElementById('question2').getAttribute('data-question2');
    if (clickedbutton == question2){
        alert('I knew you selected this :)');
    } else {
        buttonjump(thisbutton);
    }
}

function buttonjump(thisbutton){
    
    thisbutton.style.position = 'absolute';
    let changeposition = Math.random() * 100;
    thisbutton.style.left = changeposition +'%';

}
    