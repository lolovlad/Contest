const tabContest = document.getElementById("tab_contest")
const tabTask = document.getElementById("tab_task")



tabContest.onclick = () => {
    eel.load_contest()
}

tabTask.onclick = () => {
    eel.load_tasks()
}


let datepickerStart = document.getElementById('datepicker_start');
let datepickerStop = document.getElementById('datepicker_stop');
let timepickerStart = document.getElementById('timepicker_start');
let timepickerStop = document.getElementById('timepicker_stop');
let selectColTest = document.getElementById('select_col_test');


let selectContest = {
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

const datapicker_ru = {
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

    weekdaysShort: ['Пн',
                    'Вт',
                    'Ср',
                    'Чт',
                    'Пт',
                    'Сб', 
                    'Вс'],  

    weekdaysAbbrev: ['П','В','С','Ч','П','С','В']
}

const timepicker_ru = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок'
}


document.addEventListener('DOMContentLoaded', () => {

    M.textareaAutoResize(document.getElementById("description"))
    selectColTest = M.FormSelect.init(selectColTest, {});



    datepickerStart = M.Datepicker.init(datepickerStart, {i18n: datapicker_ru, 
                                                          onSelect(date){
                                                            selectContest.dateStart.day = this.date.getDate(), 
                                                            selectContest.dateStart.month = this.date.getMonth() + 1, 
                                                            selectContest.dateStart.year = this.date.getFullYear()
                                                            eel.select_contest(selectContest)  
                                                        },
                                                          format: 'dd/mm/yyyy'});
    datepickerStop = M.Datepicker.init(datepickerStop, {i18n: datapicker_ru, 
                                                        onSelect(date){
                                                            selectContest.dateEnd.day = this.date.getDate(), 
                                                            selectContest.dateEnd.month = this.date.getMonth() + 1, 
                                                            selectContest.dateEnd.year = this.date.getFullYear()
                                                            eel.select_contest(selectContest)
                                                        },
                                                        format: 'dd/mm/yyyy',})
    timepickerStart = M.Timepicker.init(timepickerStart, {i18n: timepicker_ru,
                                                          twelveHour: false,
                                                          onSelect(hours, min){
                                                            selectContest.timeStart.hours = hours
                                                            selectContest.timeStart.min = min
                                                            eel.select_contest(selectContest)},
                                                          default: "00:00"
                                                    })
    timepickerStop = M.Timepicker.init(timepickerStop, {i18n: timepicker_ru,
                                                        twelveHour: false,
                                                        onSelect(hours, min){
                                                            selectContest.timeEnd.hours = hours
                                                            selectContest.timeEnd.min = min
                                                            eel.select_contest(selectContest)},
                                                        default: "00:00"})

});


const nameContest = document.getElementById('name_contest');
const typeSelectedContes = document.getElementById('name');


nameContest.addEventListener('input', (e)=>{
    selectContest.nameContest = e.target.value
    eel.select_contest(selectContest)});


typeSelectedContes.onchange = function(){
    let btnValue = this.options[this.selectedIndex].value;
    selectContest.type = parseInt(btnValue)
    eel.select_contest(selectContest)
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

    tabTask.classList.add("disabled")
}

function selectRowContest(){
    let tabel = document.getElementById("tbody_contest");
    let rIndex = 0
    
    for(let i = 0; i < tabel.rows.length; i++)
    {
        tabel.rows[i].onclick = function(){
            rIndex = this.rowIndex;
            nameContest.labels[0].classList.add("active")
            nameContest.value = this.cells[1].innerHTML;
            
            let datetimeStart = this.cells[4].innerHTML.split(",")
            let datetimeStop = this.cells[5].innerHTML.split(",")


            datepickerStart.setDate(new Date(datetimeStart[0]))
            datepickerStop.setDate(new Date(datetimeStop[0]))
            datepickerStart.setInputValue()
            datepickerStop.setInputValue()

            let ts = document.getElementById('timepicker_start');
            let tsp = document.getElementById('timepicker_stop');
            
            ts.value = datetimeStart[1]
            ts.labels[0].classList.add("active")

            tsp.value = datetimeStop[1]
            tsp.labels[0].classList.add("active")



            let types = {"олимпиада": 1, "хакатон": 2}
            typeSelectedContes.value = types[this.cells[2].innerHTML];
            
            selectedContest(this.cells[0].innerHTML, this.cells[1].innerHTML, parseInt(typeSelectedContes.value), datetimeStart, datetimeStop)
        }
    }
}

function selectedContest(id, nameContest, type, datetimeStart, datetimeStop){
    selectContest.id = parseInt(id)
    selectContest.nameContest = nameContest
    selectContest.typeSelectedContes = type

    let dateStart = datetimeStart[0].split("/")
    let dateEnd = datetimeStop[0].split("/")


    selectContest.dateStart.day = parseInt(dateStart[1])
    selectContest.dateStart.month = parseInt(dateStart[0])
    selectContest.dateStart.year = parseInt(dateStart[2])


    selectContest.dateEnd.day = parseInt(dateEnd[1])
    selectContest.dateEnd.month = parseInt(dateEnd[0])
    selectContest.dateEnd.year = parseInt(dateEnd[2])


    let timeStart = datetimeStart[1].split(":")
    let timeEnd =  datetimeStop[1].split(":")


    selectContest.timeStart.hours = parseInt(timeStart[0])
    selectContest.timeStart.min = parseInt(timeStart[1])

    selectContest.timeEnd.hours = parseInt(timeEnd[0])
    selectContest.timeEnd.min = parseInt(timeEnd[1])

    tabTask.classList.remove("disabled")

    eel.select_contest(selectContest)
}


function updateTableContest(rowsTabel){
    let types = {1: "олимпиада", 2: "хакатон"}
    const tabel = document.getElementById("tbody_contest");
    tabel.innerHTML = ""

    for(let i=0; i < rowsTabel.contests.length; i++){
        let row = tabel.insertRow(-1)
        console.log(row)
        row.innerHTML = `<tr>
                            <td>${rowsTabel.contests[i].id}</td>
                            <td>${rowsTabel.contests[i].name_contest}</td>
                            <td>${types[rowsTabel.contests[i].type]}</td>
                            <td>${rowsTabel.contests[i].datetime_registration}</td>
                            <td>${rowsTabel.contests[i].datetime_start}</td>
                            <td>${rowsTabel.contests[i].datetime_end}</td>
                        </tr>`
    }
    selectRowContest()
}

eel.expose(updateTableContest)

function clearInputsContest(){
    nameContest.value = ""
    typeSelectedContes.value = 1

    nameContest.labels[0].classList.remove("active")
    typeSelectedContes.labels[0].classList.remove("active")

    let ts = document.getElementById('timepicker_start')
    let tsp = document.getElementById('timepicker_stop')
    
    ts.value = ""
    ts.labels[0].classList.remove("active")
    tsp.value = ""
    tsp.labels[0].classList.remove("active")


    ts = document.getElementById('datepicker_start')
    tsp = document.getElementById('datepicker_stop')
    
    ts.value = ""
    ts.labels[0].classList.remove("active")
    tsp.value = ""
    tsp.labels[0].classList.remove("active")

    clearSelctContest()
}

async function addContest(){
    eel.button_add_contest()
    clearInputsContest()
}

async function updateContest(){
    eel.button_update_contest()
    clearInputsContest()
}


async function deleteContest(){
    if(selectContest.id != -1){
        eel.button_delete_contest()
    }
    clearInputsContest()
}

document.getElementById("add_contest").onclick = addContest
document.getElementById("update_contest").onclick = updateContest
document.getElementById("delete_contest").onclick = deleteContest

/************************************* */

let selectTasks = { 
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
    path_programme_file: "",

    type_task: 1
}

function updateTasks(val){
    selectTasks = val
    eel.update_tasks(val)
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

function clearSelectTask(){
    selectTasks = { 
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
        path_programme_file: "",
    
        type_task: 1
    }
}

function updateTableTasks(rowsTabel){
    let typesTime = {1: "1 секунда", 2: "2 секунда", 3: "3 секунда", 4: "4 секунда", 5: "5 секунда"}
    let typesInput = {1: "стандартный ввод", 2: "файл input.txt", 3: "стандартный ввод или input.txt"}
    let typesOutput = {1: "стандартный вывод", 2: "файл output.txt", 3: "стандартный вывод или output.txt"}
    let typesTask = {1: "A", 2: "B", 3: "C", 4: "D", 5: "I", 6: "F"}
    const tabel = document.getElementById("tbody_task");
    tabel.innerHTML = ""

    console.log(rowsTabel, tabel)

    for(let i=0; i < rowsTabel.tasks.length; i++){

        let row = tabel.insertRow(-1)
        row.innerHTML = `<tr>
                            <td>${rowsTabel.tasks[i].id}</td>
                            <td>${typesTime[rowsTabel.tasks[i].time_work]}</td>
                            <td>${rowsTabel.tasks[i].size_raw}</td>
                            <td>${typesInput[rowsTabel.tasks[i].type_input]}</td>
                            <td>${typesOutput[rowsTabel.tasks[i].type_output]}</td>

                            <td>${rowsTabel.tasks[i].name_test}</td>
                            <td>${rowsTabel.tasks[i].description.slice(0, 30)}...</td>
                            <td>${rowsTabel.tasks[i].description_input.slice(0, 30)}...</td>
                            <td>${rowsTabel.tasks[i].description_output.slice(0, 30)}...</td>

                            <td>${rowsTabel.tasks[i].path_test_file}</td>
                            <td>${rowsTabel.tasks[i].path_programme_file}</td>
                            <td>${typesTask[rowsTabel.tasks[i].type_task]}</td>
                        </tr>`
        console.log(row)
    }
    selectRowTask()
}

eel.expose(updateTableTasks)

function selectRowTask(){
    let tabel = document.getElementById("tbody_task");
    let rIndex = 0

    let typesTime = {"1 секунда": 1, "2 секунда": 2, "3 секунда": 3, "4 секунда": 4, "5 секунда": 5}
    let typesTask = {"A": 1, "B": 2, "C": 3, "D": 4, "I": 5, "F": 6}
    let typesInput = {"стандартный ввод": 1, "файл input.txt": 2, "стандартный ввод или input.txt": 3}
    let typesOutput = {"стандартный вывод": 1, "файл output.txt": 2, "стандартный вывод или output.txt": 3}
    
    for(let i = 0; i < tabel.rows.length; i++)
    {
        tabel.rows[i].onclick = function(){
            eel.select_task(parseInt(this.cells[0].innerHTML))((task)=>{
                let selectTasks = { 
                    id: task.id,
                    time_work: task.time_work,
                    size_raw: task.size_raw,
                    type_input: task.type_input,
                    type_output: task.type_output,
                    name_test: task.name_test,
                    description: task.description,
                    description_input: task.description_input,
                    description_output: task.description_output,
                
                    path_test_file: task.path_test_file,
                    path_programme_file: task.path_programme_file,
                
                    type_task: task.type_task
                }
    
                rIndex = this.rowIndex;
    
                console.log(selectTasks)
    
    
                const timeWork = document.getElementById("time_work")
                const typeTask = document.getElementById("type_task")
                const sizeRaw = document.getElementById("size_raw")
                const typeInput = document.getElementById("type_input")
                const typeOutput = document.getElementById("type_output")
                const nameTest = document.getElementById("name_test")
                const description = document.getElementById("description")
                const descriptionInput = document.getElementById("description_input")
                const descriptionOutput = document.getElementById("description_output")
                const textTestFile = document.getElementById("text_test_file")
                const textProgrammeFile = document.getElementById("text_programme_file")
    
                timeWork.value = selectTasks.time_work
    
                typeTask.value = selectTasks.type_task
    
                sizeRaw.labels[0].classList.add("active")
                sizeRaw.value = selectTasks.size_raw
    
                typeInput.value = selectTasks.type_input
                typeOutput.value = selectTasks.type_output
    
                nameTest.labels[0].classList.add("active")
                nameTest.value = selectTasks.name_test
    
                description.labels[0].classList.add("active")
                description.value = selectTasks.description
                M.textareaAutoResize(description)
    
                descriptionInput.labels[0].classList.add("active")
                descriptionInput.value = selectTasks.description_input
    
                descriptionOutput.labels[0].classList.add("active")
                descriptionOutput.value = selectTasks.description_output
    
                textProgrammeFile.value = selectTasks.path_programme_file
                textTestFile.value = selectTasks.path_test_file
                
                updateTasks(selectTasks)
            })

        }
    }
}

function clearInputsTask(){
    const textArea = document.querySelectorAll("textarea")[0]
    textArea.value = ""
    textArea.labels[0].classList.remove("active")

    const textTestFile = document.getElementById("text_test_file")
    const textProgrammeFile = document.getElementById("text_programme_file")

    textTestFile.value = ""
    textProgrammeFile.value = ""


    for(input of document.getElementById("task_form").querySelectorAll("input")){
        input.value = ""
        try{
            input.labels[0].classList.remove("active")
        }catch{
        }
    }
    
    for(select of document.querySelectorAll("select")){
        select.value = ""
    }

    clearSelectTask()
}


function openSelectFile(event){
    eel.file()((pathFile)=>{
        let div = event.path[2]
        div.querySelectorAll(".file-path")[0].value = pathFile
        const id_file = div.querySelectorAll(".select_file")[0].id
        selectTasks[`path_${id_file}`] = pathFile
        updateTasks(selectTasks)
    })
}

function updateInput(event){
    const targetId = event.target.id
    if(targetId == "size_raw"){
        selectTasks[targetId] = parseInt(event.target.value)
    }else{
        selectTasks[targetId] = event.target.value
    }
    updateTasks(selectTasks)
}

function updateSelector(event){
    let name_id = event.target.id
    selectTasks[name_id] = parseInt(event.target.value)
    updateTasks(selectTasks)
}

function createFormTest(){
}

document.getElementById("add_task").onclick = addTask
document.getElementById("update_task").onclick = updateTask
document.getElementById("delete_task").onclick = deleteTask
document.getElementById("clear_task").onclick = clearTask

document.querySelectorAll("textarea")[0].addEventListener("input", updateInput)



for(buttonFile of document.querySelectorAll(".select_file")){
    buttonFile.onclick = openSelectFile
}


for(input of document.getElementById("task_form").querySelectorAll("input")){
    input.addEventListener("input", updateInput)
}

for(select of document.querySelectorAll("select")){
    select.addEventListener("change", updateSelector)
}

