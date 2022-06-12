const tabContest = document.getElementById("tabContest")
const tabTask = document.getElementById("tabTask")
const tabTeam = document.getElementById("tabTeam")

const selectContes = document.getElementById("id_contest")
const selectModelContes = document.getElementById("id_contest_model")

const buttonAgree = document.getElementById("agreeButton")

const buttonExit = document.getElementById("buttonExit")

console.log(buttonExit)

buttonExit.addEventListener("click", ()=>{
    console.log(1111)
    eel.button_exit_window()
})


tabContest.onclick = (e) => {
    //eel.load_contest("all")
}

tabTask.onclick = (e) => {
    if(!e.path[1].classList.contains("disabled"))
        eel.load_tasks()
}

tabTeam.onclick = (e) => {
    eel.load_teams()
}

let modelWindowContest = NaN
let modelWindowUser = NaN


document.addEventListener('DOMContentLoaded', () => {
    let element = document.querySelector('.tabs');
    let instance = M.Tabs.init(element);

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    var elems = document.querySelectorAll('.modal');
    modelWindowContest = M.Modal.init(elems[0]);
    modelWindowContest = M.Modal.getInstance(elems[0]);

    modelWindowUser = M.Modal.init(elems[1], {onCloseEnd: closeModel});
    modelWindowUser = M.Modal.getInstance(elems[1]);

    eel.load_user()
    eel.load_contest("all")
});


function createObjectToSelect(selector){
    const data = {}
    for(let option of selector.querySelectorAll("option")){
        if(option.value != "")
            data[option.innerHTML] = option.value
    }
    return data
}

function reverseObject(obj){
    const data = {}
    for(const [key, value] of Object.entries(obj)){
        data[value] = key
    }
    return data
}


function loadSelectContest(contests){
    console.log(contests)
    selectModelContes.innerHTML = '<option value="" disabled selected>Выбрать команду</option>'
    selectContes.innerHTML = '<option value="" disabled selected>Зарегестрированны на соревнование</option> <option value="soloTeam" disabled selected>Одиночное соревнование</option>'
    for(let i=0; i < contests.length; i++){
        const opt = document.createElement('option')
        opt.value = parseInt(contests[i].id)
        opt.innerHTML = contests[i].name_contest
        console.log(opt)
        if(contests[i].type == 1){
            selectModelContes.appendChild(opt.cloneNode(true))
        }else{
            selectContes.appendChild(opt)
        }
    }
}

buttonAgree.addEventListener("click", ()=>{

    if(selectModelContes.value != ""){
        const data = {id_user: selectUser.id,
                      id_contest: parseInt(selectModelContes.value)}
        eel.registration_user_event(data)
        selectModelContes.value = ""
        modelWindowContest.close()
    }
})

function alert(message){
     M.toast({html: message})
}

eel.expose(alert)
eel.expose(loadSelectContest)