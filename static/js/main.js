function contactFormSend(contact) {
    emailjs.send("service_sd2xyge","Contact-Form", {
        "from_name": contact.fname.value,
        "from_email": contact.contactemail.value,
        "message": contact.message.value
    })
    .then(
        function(response) {
            console.log("Well Done", response);
        },
        function(error) {
            console.log("Unfortunately, it has not worked", error);
        });
}