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




//     $(document).ready(function() {
//       $('#reg_form').bootstrapValidator({

// feedbackIcons: {
//   valid: 'glyphicon glyphicon-ok',
//   invalid: 'glyphicon glyphicon-remove',
//   validating: 'glyphicon glyphicon-refresh'
// },
// fields: {
//   username: {
//     validators: {
//       notEmpty: {
//         message: 'The username is required and can\'t be empty'
//       },
//       stringLength: {
//         min: 6,
//         max: 30,
//         message: 'The username must be more than 6 and less than 30 characters long'
//       },
//       regexp: {
//         regexp: /^[a-zA-Z0-9_\.]+$/,
//         message: 'The username can only consist of alphabetical, number, dot and underscore'
//       }
//     }
//   },

//   email: {
//     validators: {
//       notEmpty: {
//         message: 'Please supply your email address'
//       },
//       emailAddress: {
//         message: 'Please supply a valid email address'
//       }
//     }
//   },

//   password: {
//     validators: {
//       stringLength: {
//         min: 8,
//         max: 30,
//         message: 'The password must be more than 8 and less than 30 characters long'
//       },
//       regexp: {
//         regexp: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
//         message: 'Password must contain Minimum 8 characters at least 1 Alphabet and 1 Number:'
//       },

//       identical: {
//         field: 'confirmPassword',
//         message: 'Confirm your password below - type same password please'
//       }
//     }
//   },
//   confirmPassword: {
//     validators: {
//       identical: {
//         field: 'password',
//         message: 'The password and its confirm are not the same'
//       }
//     }
//   },
// }
// })
      
//       .on('success.form.bv', function(e) {
// $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
// $('#reg_form').data('bootstrapValidator').resetForm();

// e.preventDefault();

// var $form = $(e.target);

// var bv = $form.data('bootstrapValidator');

// $.post($form.attr('action'), $form.serialize(), function(result) {
//   console.log(result);
// }, 'json');
// });
// });