$(document).ready(function() {


    jQuery.validator.addMethod("user_chk", function(value, element) {
        

        if (/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+(?:\S{5,10})$/.test(value)) {
            return true;

        } else {
            return false;

        };
    }, ' Please enter a valid username between 5 to 10 characters.\n');



    jQuery.validator.addMethod("email_chk", function(value, element) {

        if (/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@(?:\S{1,63})$/.test(value)) {
            return true;

        } else {
            return false;

        };
    }, 'Please enter a valid email.suggestions:Prefer Active mail 2.no spaces');

    jQuery.validator.addMethod("pass_chk", function(value, element) {

        if (/^[A-Za-z0-9!@#$%^&*()_]{3,3}$/i.test(value)) {
            return true;

        } else {
            return false;

        };
    }, 'Please enter a valid password between with 8 charaters.');

     


    $('#myform').validate({
        rules: {
           
            username:
             {
                user_chk: true,
                required: true
            },
            password:
            { 
                required:true,
                pass_chk:true
            },

             
            password_again: 
            {
                equalTo: "#id_password",
                required:true
            },

            email: {
                email_chk: true,
                required: true
            }
        }
    });


}); 
 