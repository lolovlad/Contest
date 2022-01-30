let selectUser = {
    "id": -1,
    "login": "",
    "name": "",
    "sename": "",
    "password": "",
    "type": 1
}

const login = document.getElementById('login');
const name = document.getElementById('name');
const sename = document.getElementById('sename');
const type = document.getElementById('selected');
const password = document.getElementById('password');


document.addEventListener('DOMContentLoaded', () => {
    let element = document.querySelector('.tabs');
    let instance = M.Tabs.init(element);

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    eel.load_user()
});

function selectRow(){
    let tabel = document.getElementById("tbody");
    let rIndex = 0
    
    for(let i = 0; i < tabel.rows.length; i++)
    {
        tabel.rows[i].onclick = function(){
            rIndex = this.rowIndex;
            let login = document.getElementById("login")
            login.labels[0].classList.add("active")
            login.value = this.cells[1].innerHTML;
    
            let name = document.getElementById("name")
            name.labels[0].classList.add("active")
            name.value = this.cells[2].innerHTML;
    
            let sename = document.getElementById("sename")
            sename.labels[0].classList.add("active")
            sename.value = this.cells[3].innerHTML;
    
            let types = {"админ": 1, "участник": 2}
            document.getElementById("selected").value = types[this.cells[4].innerHTML];
            
            selectedUser(this.cells[0].innerHTML, login.value, name.value, sename.value, "", types[this.cells[4].innerHTML])
        }
    }
}


function selectedUser(id, login, name, sename, password, type){
    selectUser.login = login
    selectUser.name = name
    selectUser.sename = sename
    selectUser.type = type
    selectUser.password = password
    selectUser.id = parseInt(id)
    eel.select_user(selectUser)
}


function updateTable(rowsTabel){
    let types = {1: "админ", 2: "участник"}
    const tabel = document.getElementById("tbody");
    tabel.innerHTML = ""
    console.log(tabel)

    for(let i=0; i < rowsTabel.users.length; i++){
        let row = tabel.insertRow(-1)
        row.innerHTML = `<tr>
                            <td>${rowsTabel.users[i].id}</td>
                            <td>${rowsTabel.users[i].login}</td>
                            <td>${rowsTabel.users[i].name}</td>
                            <td>${rowsTabel.users[i].sename}</td>
                            <td>${types[rowsTabel.users[i].type]}</td>
                        </tr>`
    }
    selectRow()
}

function clearSelctUser(){
    selectUser = {
        "id": -1,
        "login": "",
        "name": "",
        "sename": "",
        "password": "",
        "type": 1
    }
}

function clearInputs(){
    login.value = ""
    name.value = ""
    sename.value = ""
    password.value = ""
    type.value = 1

    login.labels[0].classList.remove("active")
    name.labels[0].classList.remove("active")
    sename.labels[0].classList.remove("active")
    password.labels[0].classList.remove("active")
    clearSelctUser()
}

async function add_user(){
    eel.button_add_user()
    clearInputs()
}

async function update_user(){
    eel.button_update_user()
    clearInputs()
}


async function delete_user(){
    if(selectUser.id != -1){
        eel.button_delete_user()
    }
    clearInputs()
}


login.addEventListener('input', (e)=>{
    selectUser.login = e.target.value
    eel.select_user(selectUser)});
name.addEventListener('input', (e)=>{
    selectUser.name = e.target.value
    eel.select_user(selectUser)});
sename.addEventListener('input', (e)=>{
    selectUser.sename = e.target.value
    eel.select_user(selectUser)});

type.onchange = function(){
    let btnValue = this.options[this.selectedIndex].value;
    console.log(btnValue)
    selectUser.type = parseInt(btnValue)
    eel.select_user(selectUser)
    
}
password.addEventListener('input', (e)=>{
    selectUser.password = e.target.value
    eel.select_user(selectUser)});


document.getElementById("add_user").onclick = add_user
document.getElementById("update_user").onclick = update_user
document.getElementById("delete_user").onclick = delete_user

eel.expose(updateTable)