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
                        message:'Username should be unique and at least 6 digit long.'
                    },
                        notEmpty: {
                        message: 'Username cannot be empty'
                    }
                }
            },
            
            email: {
                validators: {
                    notEmpty: {
                        message: 'Email cannot be empty'
                    },
                    emailAddress: {
                        message: 'Please provide valid email address'
                    }
                }
            },
        
      password: {
        
            

            validators:{
                 
                 notEmpty: {
                        message: 'Password cannot be empty'
                    },

            //     stringLength: {
            //         min: 8,
            //         max: 16,
            //         message: 'Password should have length'
                   
            // },

                regexp:{    
                    regexp:/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
                           // 
                           ///^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-z\d]$/,
                   message:'Please provide minimum 8 characters long alphanumeric password, with minimum one character in uppercase'
                
             },
            
        
        
            // identical:{
            //     field:"password_again",
            //     message:"Password and re-entered passwords are not matching"
            //     }
            }
        },

        password_again: {
            validators: {
                 notEmpty: {
                        message: 'Retype Password cannot be empty'
                    },

                    identical:{
                        field:"password",
                        message:"Password and re-entered passwords are not matching"
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

