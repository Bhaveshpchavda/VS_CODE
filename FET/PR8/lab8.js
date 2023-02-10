// lab8.js
let kayoPromise = new Promise(function(Resolve,Reject) {
     let health = prompt("Are you healthy or not? [Y/N]")
     
     if (health == 'y') {
     let numOfCakes = prompt("How many cakes can you bake?");
     Resolve("I have " + numOfCakes + " cakes and I'm happy!! : )");
     } 
     else if(health == 'n') {
     Reject("There is no cake and I'm sad! : (");
     }
     else {
     alert("Invalid Input, Try Again!");
     location.reload();
    }
    });
    kayoPromise.then(result => {alert(result);})
    .catch(error => {alert(error);})
    .finally(() => {alert('I still have party');})
   
    