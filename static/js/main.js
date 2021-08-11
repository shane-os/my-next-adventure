import swal from 'sweetalert';
const formRef = document.querySelector("#contactus")
formRef.addEventListener("submit", contactFormSend)


function contactFormSend(event, contact) {
    event.preventDefault()
    emailjs.send("service_sd2xyge","Contact-Form", {
        "from_name": contact.fname.value,
        "from_email": contact.contactemail.value,
        "message": contact.message.value
    })
    .then(
        function(response) {
            swal({
                    title: "Form Sent Successfully!",
                    text: "Thank you for submitting the Form",
                    icon: "success",
                    confirmButtonText: 'Close',
                });
            console.log("It worked!", response);
        },
        function(error) {
            console.log("Unfortunately, it has not worked", error);
        });
}