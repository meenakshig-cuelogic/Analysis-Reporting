$(document).ready(function() {
    $('#myform').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
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
                        message: 'Please provide non empty username'
                    }
                }
            },
            
            email: {
                validators: {
                    notEmpty: {
                        message: 'Please provide nonempty email address'
                    },
                    emailAddress: {
                        message: 'Please provide a hrlloo valid email address'
                    }
                }
            },
        
      password: {
        
            

            validators:{
                 notEmpty: {
                        message: 'Please provide password'
                    },

                stringLength: {
                    min: 8,
                    max: 16,
                    message:'password must be more than 8 character and less than 16 character long'
                
            },

                regexp:{    
                    regexp:/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-z\d]+$/,
                    message:"Password must contain atleast 1 number and 1 letter Uppercase"
            },
            
        
        
            identical:{
                field:"password_again",
                message:"Confirm your password below"
                }
            }
        },

        password_again: {
            validators: {
                 notEmpty: {
                        message: 'Please provide password'
                    },

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

            
            e.preventDefault();

            var $form = $(e.target);

            var bv = $form.data('bootstrapValidator');

          
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});

