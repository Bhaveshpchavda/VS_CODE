// DateTimeModule.js
module.exports = {
    getCurrentDateTime: function () {
    var  currentDate = new Date();
    var  formattedDate = currentDate.toLocaleDateString();
    var  formattedTime = currentDate.toLocaleTimeString();
    return `${formattedDate} ${formattedTime}`;
    }
    };
    