$(document).ready(function() {


    jQuery.validator.addMethod("user_chk", function(value, element) {
        debugger;

        if (/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+(?:\S{5,10})$/.test(value)) {
            return true;

        } else {
            return false;

        };
    }, 'Please enter a valid password.');



    jQuery.validator.addMethod("email_chk", function(value, element) {

        if (/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@(?:\S{1,63})$/.test(value)) {
            return true;

        } else {
            return false;

        };
    }, 'Please enter a valid email.');

    jQuery.validator.addMethod("pass_chk", function(value, element) {

        if (/^[A-Za-z0-9!@#$%^&*()_]{2,3}$/i.test(value)) {
            return true;

        } else {
            return false;

        };
    }, 'Please enter a valid password.');


    $('#myform').validate({
        rules: {
            username: {
                user_chk: true,
                required: true
            },
            password:
            { 
                required:true,
                pass_chk:true
            },
            password_again: {
                equalTo: "#password"
            },
            email: {
                email_chk: true,
                required: true
            }
        }
    });


}); 





/*

$(document).ready(function() {
$jQuery.validator.addMethod("e_mail_chk", function(value, element)
{

return this.optional(element) || /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,5}$/i.test(value);
}, "Please enter a valid email address.");

$jQuery.validator.addMethod("Username_chk",function(value,element)
{
return this.optional(element) || /^[a-zA-Z0-9._-]{8,18}$/i.test(value);
},"Username are 3-15 characters");

$jQuery.validator.addMethod("password1_chk",function(value,element)
{
return this.optional(element) || /^[A-Za-z0-9!@#$%^&*()_]{8,8}$/i.test(value);
},"Passwords are 8 characters");

// Validate signup form
$("#myform").validate({
rules: {
e_mail_chk: "required email",
Username_chk: "required Username",
password1_chk: "required password",
password_again_chk:"required password_again"
},
*/
