function set_result()
{
        let isLogin = eel.button_login()      
}


function update_error(error_val){
        console.log(123)
        error = document.getElementById("error")
        error.innerHTML = error_val
}


const login = document.getElementById('login');
const password = document.getElementById('password');

login.addEventListener('input', updateValue);
password.addEventListener('input', updateValue);

function updateValue(e){
        eel.update_date(login.value, password.value)
}

eel.expose(update_error)
document.getElementById("signin").onclick = set_result;