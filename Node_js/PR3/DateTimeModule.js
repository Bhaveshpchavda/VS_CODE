// DateTimeModule.js
module.exports = {
    getCurrentDateTime: function () {
    const currentDate = new Date();
    const formattedDate = currentDate.toLocaleDateString();
    const formattedTime = currentDate.toLocaleTimeString();
    return `${formattedDate} ${formattedTime}`;
    }
    };
    