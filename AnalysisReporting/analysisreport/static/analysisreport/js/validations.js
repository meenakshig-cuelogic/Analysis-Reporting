$(document).ready(function() {
    $('#myform').bootstrapValidator({
        
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                validators: {
                        stringLength: {
                        min: 6,
                        message:'Username must be atleast 6 character long'
                    },
                        notEmpty: {
                        message: 'Please provide username'
                    }
                }
            },
         
            email: {
                validators: {
                    notEmpty: {
                        message: 'Please provide your email address'
                    },
                    emailAddress: {
                        message: 'Please provide a valid email address'
                    }
                }
            },
     
    password: 
            {
            validators:{
                notEmpty: {
                        message: 'Please provide a password'
                    },
            regexp:{    
            regexp:/^[0-9]+$/,
            message:"Password must contain atleast 1 number and 1 lowercase letter"
            },
         
         


            stringLength: {
                    min: 8,
                    max: 16,
                    message:'password must be more than 8 character and less than 16 character long'
             
                },
     
     
            identical:{
                field:"password_again",
                message:"Confirm your password below"
                }
            }
        },

        password_again: {
            validators: {
                    identical:{
                        field:"password",
                        message:"The password and retyped password are not same"
                    }
                }
            }
     
        }


    })

    .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#myform').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});



