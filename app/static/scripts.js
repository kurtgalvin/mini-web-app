console.log('Thank you for taking the time to look over my project!')

function getFormData(event) {
  const elems = event.target.elements

  let formData = new FormData()
  for(i = 0; i < elems.length-1; i++) {
    formData.append([elems[i].name], elems[i].value)
  }
  return formData
}

function indexFormSubmit(e) {
  e.preventDefault()
  const formData = getFormData(e)
  const responseElem = document.getElementById('index-main-form-response')

  const xmlHttp = new XMLHttpRequest()
  xmlHttp.open("POST", '/api/employees')
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

function saveEmployee(e) {
  e.preventDefault()
  const formData = getFormData(e) 
  const responseElem = document.getElementById('employee-response-li')

  const xmlHttp = new XMLHttpRequest()
  xmlHttp.open("PUT", '/api/employees/'+formData.get('id'))
  formData.delete('id')
  xmlHttp.onload = function() {
    const response = JSON.parse(this.response)
    if(response['complete']) {
      responseElem.innerHTML = '<span style="color: green;">Employee Saved!</span>'
    } else {
      responseElem.innerHTML = '<span style="color: red;">Employee did NOT save</span>'
    }
  }
  xmlHttp.send(formData)
}

function deleteEmployee(empId) {
  const xmlHttp = new XMLHttpRequest()
  if(!confirm("Are you sure?")) {
    return false
  }
  xmlHttp.open("DELETE", '/api/employees/'+empId)
  xmlHttp.onload = function() {
    location.reload()
  }
  xmlHttp.send(null)
}