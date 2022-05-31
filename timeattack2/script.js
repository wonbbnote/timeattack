function upload() {
    let file = $('#upload-file')[0].files[0]
    console.log(file)
    let title = $('#upload-title').val()
    let form_data = new FormData()

    form_data.append("file_give", file)
    form_data.append("title_give", title)

    $.ajax({
        type: "POST",
        url: "/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["result"])
        }
    });
  }

  function search() {
    let title = $('#search-title').val()
    let form_data = new FormData()

    form_data.append("title_give", title)

    $.ajax({
        type: "POST",
        url: "/search",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let predictions = response["predictions"]
            $('.result').remove()
            for (let i = 0; i < predictions.length; i++) {
                let path = predictions[i]['path']
                let result = predictions[i]['result']

                let temp_html = `<div class="result"><img src="${path}" width="100px"/>
                                <p>${result}</p></div>`
                $('.search').append(temp_html)
            }
        }
    });
  }

  function preview() {
    let frame = document.getElementById('frame');
    frame.src=URL.createObjectURL(event.target.files[0]);
    frame.style.display = 'block';
  }