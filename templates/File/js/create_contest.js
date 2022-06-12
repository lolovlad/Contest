const datepickerStart = document.getElementById('datepickerStart');
const datepickerStop = document.getElementById('datepickerStop');
const timepickerStart = document.getElementById('timepickerStart');
const timepickerStop = document.getElementById('timepickerStop');

const nameContest = document.getElementById('nameContest');
const typeSelectedContes = document.getElementById('typeSelectedContes');
const formContest = document.getElementById("formContest")

const selectTypeContest = createObjectToSelect(typeSelectedContes)

const buttonAddContest = document.getElementById("addContest")
const buttonUpdateContest = document.getElementById("updateContest")
const buttonDeleteContest = document.getElementById("deleteContest")
const buttonCreatingReport = document.getElementById("creatingReport")

//const selectColTest = document.getElementById('select_col_test');

let datepickerStartInit
let timepickerStartInit
let timepickerStopInit
let datepickerStopInit
//let selectColTestInit



let selectContest = {
    id: -1,
    nameContest: "",
    typeSelectedContes: 1,
    dateStart: {day: 1,
                month: 1,
                year: 2014},
    dateEnd: {day: 1,
              month: 1,
              year: 2014},
    timeStart: {hours: 1,
                min: 1},
    timeEnd:  {hours: 1,
               min: 1},

}

const datapickerRu = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок',
    months: [ 'Январь',
              'Февраль',
              'Март',
              'Апрель',
              'Май',
              'Июнь',
              'Июль',
              'Август',
              'Сентябрь',
              'Октябрь',
              'Ноябрь',
              'Декабрь'],

    monthsShort: ['Янв', 
                  'Фев', 
                  'Мар', 
                  'Апр', 
                  'Май', 
                  'Июн', 
                  'Июл', 
                  'Авг', 
                  'Сен', 
                  'Окт', 
                  'Ноя', 
                  'Дек'],
           
    weekdays: ['Понедельник',
               'Вторник',
               'Среда',
               'Четверг',
               'Пятница',
               'Суббота',
               'Воскресенье'],

    weekdaysShort: ['Вс',
                    'Пн',
                    'Вт',
                    'Ср',
                    'Чт',
                    'Пт',
                    'Сб',],  

    weekdaysAbbrev: ['В','П','В','С','Ч','П','С']
}

const timepickerRu = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок'
}


document.addEventListener('DOMContentLoaded', () => {

    M.textareaAutoResize(document.getElementById("description"))

    const dateNow = new Date()

    datepickerStartInit = M.Datepicker.init(datepickerStart, {i18n: datapickerRu, 
                                                          onSelect(date){
                                                            selectContest.dateStart.day = this.date.getDate(), 
                                                            selectContest.dateStart.month = this.date.getMonth() + 1, 
                                                            selectContest.dateStart.year = this.date.getFullYear()
                                                            eel.select_contest(selectContest)
                                                         },
                                                         onClose(){
                                                            activeInput()
                                                         },
                                                         format: 'yyyy-mm-dd',
                                                         minDate: dateNow,
                                                         });
    timepickerStartInit = M.Timepicker.init(timepickerStart, {i18n: timepickerRu,
                                                          twelveHour: false,
                                                          onSelect(hours, min){
                                                            selectContest.timeStart.hours = hours
                                                            selectContest.timeStart.min = min
                                                            eel.select_contest(selectContest)},
                                                          default: "00:00",
                                                          onCloseEnd(){
                                                            activeInput()
                                                         }
                                                    })
    timepickerStopInit = M.Timepicker.init(timepickerStop, {i18n: timepickerRu,
                                                        twelveHour: false,
                                                        onSelect(hours, min){
                                                            selectContest.timeEnd.hours = hours
                                                            selectContest.timeEnd.min = min
                                                            eel.select_contest(selectContest)
                                                            return},
                                                        default: "00:00"})

});


nameContest.addEventListener('input', (e)=>{
    selectContest.nameContest = e.target.value
    eel.select_contest(selectContest)});


typeSelectedContes.onchange = function(){
    let btnValue = this.options[this.selectedIndex].value;
    selectContest.typeSelectedContes = parseInt(btnValue)
    eel.select_contest(selectContest)
}

function activeInput(){
    if(timepickerStartInit.time != undefined && datepickerStartInit.date != undefined){
        datepickerStop.removeAttribute("disabled")
        datepickerStopInit = M.Datepicker.init(datepickerStop, {i18n: datapickerRu, 
            onSelect(date){
                selectContest.dateEnd.day = this.date.getDate(), 
                selectContest.dateEnd.month = this.date.getMonth() + 1, 
                selectContest.dateEnd.year = this.date.getFullYear()
                timepickerStop.removeAttribute("disabled")
                eel.select_contest(selectContest)
            },
            format: 'yyyy-mm-dd',
            minDate: datepickerStartInit.date})
    }
}

function clearSelctContest(){
    selectUser = {
        id: -1,
        nameContest: "",
        typeSelectedContes: 1,
        dateStart: {day: 1,
                    month: 1,
                    year: 2001},
        dateEnd: {day: 1,
                  month: 1,
                  year: 2001},
        timeStart: {hours: 1,
                    min: 1},
        timeEnd:  {hours: 1,
                   min: 1},
    }

    buttonUpdateContest.classList.add("disabled")
    buttonDeleteContest.classList.add("disabled")
    buttonCreatingReport.classList.add("disabled")
    tabTask.classList.add("disabled")
}

function selectedContest(id, nameContest, type, datetimeStart, datetimeStop){
    selectContest.id = parseInt(id)
    selectContest.nameContest = nameContest
    selectContest.typeSelectedContes = type

    let dateStart = datetimeStart[0].split("-")
    let dateEnd = datetimeStop[0].split("-")

    selectContest.dateStart.year = parseInt(dateStart[0])
    selectContest.dateStart.month = parseInt(dateStart[1])
    selectContest.dateStart.day = parseInt(dateStart[2])

    selectContest.dateEnd.year = parseInt(dateEnd[0])
    selectContest.dateEnd.month = parseInt(dateEnd[1])
    selectContest.dateEnd.day = parseInt(dateEnd[2])


    let timeStart = datetimeStart[1].split(":")
    let timeEnd =  datetimeStop[1].split(":")


    selectContest.timeStart.hours = parseInt(timeStart[0])
    selectContest.timeStart.min = parseInt(timeStart[1])

    selectContest.timeEnd.hours = parseInt(timeEnd[0])
    selectContest.timeEnd.min = parseInt(timeEnd[1])
}


function updateContestTable(contests){
    const types = reverseObject(selectTypeContest)
    const tabelContest = document.getElementById("tbodyContest");
    tabelContest.innerHTML = ""
    for(let i=0; i < contests.length; i++){
        const row = tabelContest.insertRow(-1)
        row.innerHTML = `<tr>
                            <td>${contests[i].id}</td>
                            <td>${contests[i].name_contest}</td>
                            <td>${types[contests[i].type]}</td>
                            <td>${contests[i].datetime_registration}</td>
                            <td>${contests[i].datetime_start}</td>
                            <td>${contests[i].datetime_end}</td>
                        </tr>`
        row.addEventListener("click", selectRowContest)
    }
}

function selectRowContest(event){
    const data = event.path[1].cells

    const datetimeStartString = data[4].innerHTML.split(" ")
    const datetimeStopString = data[5].innerHTML.split(" ")

    datepickerStartInit.date = new Date(datetimeStartString[0])
    timepickerStartInit.time = datetimeStartString[1]
    
    let dataInputs = {
        nameContest: data[1].innerHTML,
        datepickerStart: datetimeStartString[0],
        timepickerStart: datetimeStartString[1],
        datepickerStop: datetimeStopString[0],
        timepickerStop: datetimeStopString[1]

    }
    let dataSelect = [data[2].innerHTML]

    const inputs = formContest.querySelectorAll("input")
    const selects = formContest.querySelectorAll("select")

    for(let i = 0; i < inputs.length; i++){
        if(!inputs[i].hasAttribute("data-target")){
            const rargetId = inputs[i].id
            inputs[i].labels[0].classList.add("active")
            inputs[i].value = dataInputs[rargetId]
        }
    }

    for(let i = 0; i < selects.length; i++){
        const rargetId = selects[i].id
        selects[i].value = selectTypeContest[dataSelect[i]]
    }

    selectedContest(parseInt(data[0].innerHTML), dataInputs.nameContest, parseInt(selectTypeContest[dataSelect[0]]), datetimeStartString, datetimeStopString)
    updateSelectContest()
}


eel.expose(updateContestTable)

function updateSelectContest(){
    console.log(selectContest)
    eel.select_contest(selectContest)

    buttonUpdateContest.classList.remove("disabled")
    buttonDeleteContest.classList.remove("disabled")
    buttonCreatingReport.classList.remove("disabled")

    timepickerStop.removeAttribute("disabled")
    datepickerStop.removeAttribute("disabled")
    activeInput()
    tabTask.classList.remove("disabled")
}

function clearInputsContest(){
    for(input of formContest.querySelectorAll("input")){
        input.value = ""
        try{
            input.labels[0].classList.remove("active")
        }catch{
        }
    }
    
    for(select of formUser.querySelectorAll("select")){
        select.value = ""
    }

    timepickerStop.setAttribute("disabled", "disabled")
    datepickerStop.setAttribute("disabled", "disabled")

    
    clearSelctContest()
}

async function addContest(){
    await eel.button_add_contest()
    clearInputsContest()
}

async function updateContest(){
    await eel.button_update_contest()
    clearInputsContest()
}


async function deleteContest(){
    await eel.button_delete_contest()
    clearInputsContest()
}

buttonAddContest.onclick = addContest
buttonUpdateContest.onclick = updateContest
buttonDeleteContest.onclick = deleteContest
buttonCreatingReport.onclick = createReport
/************************************* */

const buttonDeleteTask = document.getElementById("deleteTask")
const buttonUpdateTask = document.getElementById("updateTask")
const buttonAddTask = document.getElementById("addTask")
const buttonClearTask = document.getElementById("clearTask")

const timeWork = document.getElementById("time_work")
const typeInput = document.getElementById("type_input")
const typeOutput = document.getElementById("type_output")
const typeTask = document.getElementById("type_task")

const descriptionInput = document.querySelectorAll("textarea")[0]
const textTestFile = document.getElementById("text_test_file")

const selectTypeTime = createObjectToSelect(timeWork)
const selectTypeInput = createObjectToSelect(typeInput)
const selectTypeOutput = createObjectToSelect(typeOutput)
const selectTypeTask = createObjectToSelect(typeTask)

const formTask = document.getElementById("taskForm")

buttonDeleteTask.onclick = deleteTask
buttonUpdateTask.onclick = updateTask
buttonAddTask.onclick = addTask
buttonClearTask.onclick = clearTask

let selectTask = { 
    id: -1,
    time_work: 0,
    size_raw: 0,
    type_input: 0,
    type_output: 0,
    name_test: "",
    description: "",
    description_input: "",
    description_output: "",

    path_test_file: "",

    type_task: 1
}

function addTask(){
    eel.button_add_task()
    clearInputsTask()
}

function deleteTask(){
    eel.button_delete_task()
    clearInputsTask()
}

function updateTask(){
    eel.button_update_task()
    clearInputsTask()
}

function clearTask(){
    clearInputsTask()
}

function createReport(){
    eel.button_contest_create_report()
}

function clearSelectTask(){
    selectTask = { 
        id: -1,
        time_work: 0,
        size_raw: 0,
        type_input: 0,
        type_output: 0,
        name_test: "",
        description: "",
        description_input: "",
        description_output: "",
    
        path_test_file: "",
    
        type_task: 1
    }
}

function updateTaskTable(tasks){
    let typesTime = reverseObject(selectTypeTime)
    let typesInput = reverseObject(selectTypeInput)
    let typesOutput = reverseObject(selectTypeOutput)
    let typesTask = reverseObject(selectTypeTask)
    const tabelTask = document.getElementById("tbodyTask");
    tabelTask.innerHTML = ""
    for(let i=0; i < tasks.length; i++){
        const row = tabelTask.insertRow(-1)
        row.innerHTML = `<tr>
                            <td>${tasks[i].id}</td>
                            <td>${typesTime[tasks[i].time_work]}</td>
                            <td>${tasks[i].size_raw}</td>
                            <td>${typesInput[tasks[i].type_input]}</td>
                            <td>${typesOutput[tasks[i].type_output]}</td>

                            <td>${tasks[i].name_test}</td>
                            <td>${tasks[i].description.slice(0, 30)}...</td>
                            <td>${tasks[i].description_input.slice(0, 30)}...</td>
                            <td>${tasks[i].description_output.slice(0, 30)}...</td>

                            <td>${tasks[i].path_test_file}</td>
                            <td>${typesTask[tasks[i].type_task]}</td>
                        </tr>`
        row.addEventListener("click", selectRowTask)
    }
}

eel.expose(updateTaskTable)
eel.expose(loadFormTask)

function selectRowTask(event){
    let newSelectTask = {}
    const data = event.path[1].cells
    newSelectTask.id = parseInt(data[0].innerHTML)
    newSelectTask.type_response = "selectChange"
    eel.select_task(newSelectTask)
}

function loadFormTask(task){
    const inputs = formTask.querySelectorAll("input")
    const selects = formTask.querySelectorAll("select")
    for(let i = 0; i < inputs.length - 1; i++){
        if(inputs[i].type != "hidden"){
            const rargetId = inputs[i].id
            inputs[i].labels[0].classList.add("active")
            inputs[i].value = task[rargetId]
        }
    }

    for(let i = 0; i < selects.length; i++){
        const rargetId = selects[i].id
        selects[i].value = task[rargetId]
    }

    descriptionInput.labels[0].classList.add("active")
    descriptionInput.value = task.description
    M.textareaAutoResize(description)
    textTestFile.value = task.path_test_file

    selectTask = task

    buttonUpdateTask.classList.remove("disabled")
    buttonDeleteTask.classList.remove("disabled")
    buttonClearTask.classList.remove("disabled")
}

function clearInputsTask(){
    descriptionInput.value = ""
    descriptionInput.labels[0].classList.remove("active")

    textTestFile.value = ""


    for(input of formTask.querySelectorAll("input")){
        input.value = ""
        try{
            input.labels[0].classList.remove("active")
        }catch{
        }
    }
    
    for(select of formTask.querySelectorAll("select")){
        select.value = ""
    }

    buttonUpdateTask.classList.add("disabled")
    buttonDeleteTask.classList.add("disabled")
    buttonClearTask.classList.add("disabled")
    clearSelectTask()
}


function openSelectFile(event){
    eel.file()((pathFile)=>{
        let div = event.path[2]
        div.querySelectorAll(".file-path")[0].value = pathFile
        const id_file = div.querySelectorAll(".select_file")[0].id
        selectTask[`path_${id_file}`] = pathFile
        updateTasks(selectTask)
    })
}

function updateInput(event){
    const targetId = event.target.id
    if(targetId == "size_raw"){
        selectTask[targetId] = parseInt(event.target.value)
    }else{
        selectTask[targetId] = event.target.value
    }
    updateTasks(selectTask)
}

function updateSelector(event){
    let name_id = event.target.id
    selectTask[name_id] = parseInt(event.target.value)
    updateTasks(selectTask)
}

function updateTasks(val){
    selectTask = val
    buttonUpdateTask.classList.remove("disabled")
    buttonDeleteTask.classList.remove("disabled")
    buttonClearTask.classList.remove("disabled")
    eel.select_task(val)
}

descriptionInput.addEventListener("input", updateInput)


for(buttonFile of formTask.querySelectorAll(".select_file")){
    buttonFile.onclick = openSelectFile
}


for(input of formTask.querySelectorAll("input")){
    input.addEventListener("input", updateInput)
}

for(select of formTask.querySelectorAll("select")){
    select.addEventListener("change", updateSelector)
}

/*как сделать конфетку
когда вводяться данные надо просто добавлять в структуру ключ и значение
если оно было созданно то просто обновлять
если там пусто то блокировать кнопки*/