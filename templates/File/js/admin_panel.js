
document.addEventListener('DOMContentLoaded', () => {
    let element = document.querySelector('.tabs');
    let instance = M.Tabs.init(element);

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});

let tabel = document.getElementById("tabel");
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
    }
}

async function appdateTable(rowsTabel){
    console.log(rowsTabel)
}

async function add_user(){
    eel.button_add_user()
}

document.getElementById("add_user").onclick = add_user
eel.expose(appdateTable)