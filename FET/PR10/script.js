var nameError = document.getElementById('name-error');
var emailError = document.getElementById('email-error');
var contactError = document.getElementById('contact-error');
var passError = document.getElementById('passwd-error');
var subError = document.getElementById('sub-error');
var p = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$/;
function validate_name(){
    var n = document.getElementById('id-name').value;
    if (n.length == 0) {
        nameError.innerHTML = "Name is required"; 
        return false;   
    }
    if(!n.match(/^[a-zA-Z]*\s{1}[a-zA-Z]*$/)){
        nameError.innerHTML = "Oops! Invalid Input"; 
        return false; 
    }
    else{
        nameError.innerHTML = '';
        return true;
    }
}

function validate_mail(){
    var em = document.getElementById('id-mail').value;
    if (em.length == 0) {
        emailError.innerHTML = "Email is required"; 
        return false;   
    }
    if(!em.match(/^[^ ]+@[^ ]+\.[a-z]{2,3}$/)){
        emailError.innerHTML = "Email is not a valid"
        return false;
    }
    else{
        emailError.innerHTML = ' ';
        return true;
    }
}

function validate_phone(){
    var ph = document.getElementById('id-phone').value;
    if (ph.length == 0) {
        contactError.innerHTML = "Contact no. is required"; 
        return false;   
    }
    if (ph.length !== 10) {
        contactError.innerHTML = "Number must be 10 digits"; 
        return false;   
    }
    if (!ph.match(/^[0-9]{10}$/)) {
        contactError.innerHTML = "Oops! Invalid Input"; 
        return false;   
    }
    else{
        contactError.innerHTML = ' ';
        return true; 
    }
}

function validate_passwd(){
    var pass = document.getElementById('id-passwd').value;
    if(pass.length == 0){
        passError.innerHTML = "Password required";
        return false;
    }
    else if(!pass.match(p)){
        passError.innerHTML = "Oops! Invalid Password";
        return false;
    }
    else{
        passError.innerHTML = ' ';
        return true;
    }

}

function validate_form(){
    if(!validate_name() || !validate_mail() || !validate_phone() || !validate_passwd()){
        alert("Oop's something went wrong! ⚠️")
        return false;
    }
    else{
        alert("Validate successfully 🔐")
    }
}