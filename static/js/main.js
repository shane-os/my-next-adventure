// Contact Form
const formRef = document.querySelector("#contactus")
const firstNameRef = document.querySelector("#fname")
formRef.addEventListener("submit", contactFormSend)

// Successful Submission Pop-Up Message
function contactFormSend(event) {
    event.preventDefault()
    emailjs.send("service_sd2xyge","Contact-Form", {
        "from_name": formRef.fname.value,
        "from_email": formRef.contactemail.value,
        "message": formRef.message.value
    })
    .then(
        function(response) {
            swal({
                    title: "Form Sent Successfully!",
                    text: "Thank you for submitting the Form",
                    icon: "success",
                    button: 'Close',
                });
            console.log("It worked!", response);
        });
}