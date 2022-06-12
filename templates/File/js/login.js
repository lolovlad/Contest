function setResult()
{
        let isLogin = eel.button_login()
        //window.close() 
}



function update_error(errorVal){
        error = document.getElementById("error")
        error.innerHTML = errorVal
}


const login = document.getElementById('login');
const password = document.getElementById('password');

login.addEventListener('input', updateValue);
password.addEventListener('input', updateValue);

function updateValue(e){
        eel.update_field_login(login.value, password.value)
}


eel.expose(update_error)
document.getElementById("signin").onclick = setResult;