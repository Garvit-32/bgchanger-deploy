
/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL_fore(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult_fore')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function readURL_back(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult_back')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload_fore').on('change', function () {
        readURL_fore(input);
    });
});

$(function () {
    $('#upload_back').on('change', function () {
        readURL_back(input);
    });
});


/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input_fore = document.getElementById('upload_fore');
var infoArea_fore = document.getElementById('upload-label_fore');

input_fore.addEventListener('change', showFileName_fore);
function showFileName_fore(event) {
    var input = event.srcElement;
    var fileName = input.files[0].name;
    infoArea_fore.textContent = 'File name: ' + fileName;
}


var input_back = document.getElementById('upload_back');
var infoArea_back = document.getElementById('upload-label_back');

input_back.addEventListener('change', showFileName_back);
function showFileName_back(event) {
    var input = event.srcElement;
    var fileName = input.files[0].name;
    infoArea_back.textContent = 'File name: ' + fileName;
}
