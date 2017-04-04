function upload(event) {
event.preventDefault();
var data = new FormData($('#file-upload-form').get(0));

$.ajax({
    url: "analysisreport/import_file/",
    type: "POST",
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data) {
        alert("in upload")
        alert('success');
    }
});
return false;
}

$(function() {
    $('#file-upload-form').on("submit", upload);
});