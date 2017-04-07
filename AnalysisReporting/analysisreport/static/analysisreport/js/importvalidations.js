$(document).ready(function() {
    $('#file-save-form').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            userfilename: {
                validators: {
                        stringLength: {
                        max: 16,
                        message:'Database name is too long, maximum allowed length is 16 characters.'
                    },
                        notEmpty: {
                        message: 'Database name cannot be empty'
                    },
                    regexp:{    
                    regexp:/^\S*$/,
                    message:"Database name cannot have space in it."
                    }


                }
            }
        }
    })

    .on('success.form.bv', function(e) {
        $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
        $('#file-save-form').data('bootstrapValidator').resetForm();

        e.preventDefault();

        var $form = $(e.target);

        var bv = $form.data('bootstrapValidator');

        $.post($form.attr('action'), $form.serialize(), function(result) {
            console.log(result);
        }, 'json');

    });

    //     <div data-alerts="alerts" data-titles='{"warning": "<em>Warning!</em>", "error": "<em>Error!</em>"}' data-ids="myid" data-fade="3000"></div>
    // <button id="warn-me" class="btn">Click to see a warning alert</button>
    // <script>
    // $("#warn-me").click(function() {
    //   $(document).trigger("add-alerts", [
    //     {
    //       "message": "This is a warning.",
    //       "priority": 'warning'
    //     }
    //   ]);
    // });
    // </script>

    bootstrap_alert = function() {}
    bootstrap_alert.warning = function(message) {
            $('#alert_placeholder').html('<div class="alert alert-danger"><a class="close" data-dismiss="alert">×</a><span>'+message+'</span></div>')
        }

    setTimeout(function() {

            $('.message').fadeOut('slow');
        }, 3000); // <-- time in milliseconds, 1000 =  1 sec

    $('#uploadFile').change(function(event) {
        console.log('event ==>', event);
        if (event.target.files.length) {
            if (Number(event.target.files[0].size) >= 10485760) {
                bootstrap_alert.warning('File size should not be more than 10 MB');
               
            }
            var ext = $('#uploadFile').val().split('.').pop().toLowerCase();
            // debugger;
            if (ext.length) {
                if ($.inArray(ext, ['csv', 'CSV']) == -1) {
                   bootstrap_alert.warning('The file you are trying to upload is not support, please try a CSV file only.');
                    event.target.files = [];
                }
                else {
                    console.log("sdfsdf");
                    $("#upload-btn").addClass("active");
                }
            }


        }
    });








});
