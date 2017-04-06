function getCookie(name) {
    var cookieValue = null;
        if (document.cookie && document.cookie != '') 
        { 
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function upload(event) {
    debugger;
    event.preventDefault();
    var data = new FormData($('#file-upload-form'));
    console.log(data);
    debugger;
    $.ajax({
        url: "/analysisreport/get_file_data/",
        type: "POST",
        data: data,
        cache : false,
        processData: false,
        dataType: "JSON",
        success: function() {
            console.log();
            alert("in success");
        
        },
        error: function(data1) {
            console.log(data1);
            alert("in error");
        }
    });
    return false;
}

function savefile(event) {
event.preventDefault();
var data2 = new FormData($('#file-save-form').get(0));
$.ajax({
    url: "analysisreport/save_file/",
    type: "POST",
    data: data2,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data2) {
        alert("in savefile");
        alert('success');
    }
});
return false;
}


$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
        }
    });
    // $('#file-upload-form').on("submit", upload);
    $('#save-to-databse').on("submit",savefile);
});