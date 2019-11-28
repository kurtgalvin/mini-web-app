console.log('Thank you for taking the time to look over my project!')

function indexFormSubmit(e) {
  e.preventDefault()
  const elems = e.target.elements
  const responseElem = document.getElementById('index-main-form-response')

  let formData = new FormData()
  console.log(e.target.elements)
  for(i = 0; i < elems.length-1; i++) {
    formData.append([elems[i].name], elems[i].value)
  }

  const xmlHttp = new XMLHttpRequest()
  xmlHttp.open("POST", '/api/employee')
  xmlHttp.onload = function() {
    const response = JSON.parse(this.response)
    if(response['complete']) {
      responseElem.innerHTML = '<span style="color: green;">Employee Created!</span>'
    } else if(response['error'] == 'IntegrityError') {
      responseElem.innerHTML = '<span style="color: red;">Employee NOT created, already exists</span>'
    } else {
      responseElem.innerHTML = '<span style="color: red;">Employee NOT created, Error</span>'
    }
  }
  xmlHttp.send(formData)
}