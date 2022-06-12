const listTasks = document.getElementById("list_tasks")
const nameContest = document.getElementById("name_contest")
const timeRegistration = document.getElementById("time_registration")
const timeStart = document.getElementById("time_start")
const timeEnd = document.getElementById("time_end")
const timeСontinuation = document.getElementById("time_continuation")
const timerShow = document.getElementById("timer_show")

const packageButton = document.getElementById("packageButton")
const closeContestButton = document.getElementById("closeContestButton")

let dptWindow = 0

closeContestButton.addEventListener("click", function(){
    eel.close_contest()
})

packageButton.addEventListener("click", function(){
    eel.open_package_window()
})


let dataEndDate = ""
let nowSeconds = 0
let planeSeconds = 0

let numberShipments = 0

let timerIntervalId = 0


document.addEventListener('DOMContentLoaded', () => {
    eel.load_main_window_contest()
    eel.user_load_tasks()

    eel.is_close()((isClose)=>{
         if(isClose)
             closeContest()
    })
    window.setInterval(intervalLoadAnswer, 20000)
});

function updateNumberShipments(num=0){
    const countAnswer = document.getElementById("countAnswer")
    countAnswer.innerHTML = `осталось ${numberShipments - num} попыток`
}

function closeContest(){
    for(let buttonFile of document.querySelectorAll(".select_file")){
        buttonFile.classList.add("disabled")
    }

    for(let button of document.querySelectorAll(".sendAnswer")){
        button.classList.add("disabled")
    }
    closeContestButton.classList.add("disabled")
}

function loadsTasks(tasks){
    listTasks.innerHTML = ""

    for(let i=0; i < tasks.length; i++){

        listTasks.innerHTML += `<a href="#" id="select_tasks">
                                    <li class="collection-item">
                                        <input value=${tasks[i].id} type="hidden">
                                        <span class="secondary-content" id="total">-</span>${tasks[i].type_task}.${tasks[i].name_test}
                                    </li>
                                </a>`
    }
    for(let task of document.querySelectorAll("#select_tasks")){
        task.addEventListener("click", (event)=>{
            const id_task = event.target.querySelectorAll("input")[0].value
            eel.user_select_task(parseInt(id_task))
        })
    }
    eel.user_select_task(parseInt(tasks[0].id))
}


function loadsLeftInformation(contest){
    nameContest.innerHTML = contest.name_contest
    timeRegistration.innerHTML = "Зарегестрированн: " + contest.datetime_registration
    timeStart.innerHTML = "Старт: " + contest.datetime_start
    timeEnd.innerHTML = "Финишь: " + contest.datetime_end

    console.log(contest)

    const dateStart = new Date(contest.datetime_start)
    const dateEnd = new Date(contest.datetime_end)

    let dateNow = dateEnd - dateStart
    planeSeconds = dateNow

    let hours = parseInt(dateNow / 1000 / 60 / 60)

    if(hours.toString().length < 2){
        hours = "0" + hours.toString()
    }

    dateNow = dateNow - hours * 60 * 60 * 1000

    let minuts = parseInt(dateNow / 1000 / 60)

    if(minuts.toString().length < 2){
        minuts = "0" + minuts.toString()
    }

    dateNow = dateNow - minuts * 60 * 1000

    let seconds = parseInt(dateNow / 1000)

    if(seconds.toString().length < 2){
        seconds = "0" + seconds.toString()
    }

    dataEndDate = dateEnd
    milliseconds = Date.now()
    nowSeconds = (dataEndDate - milliseconds) / 1000


    timerIntervalId = window.setInterval(timer, 1000)
    
    timeСontinuation.innerHTML = `Длительность: ${hours}:${minuts}:${seconds}`

    let strTimer = `${hours}:${minuts}:${seconds}`;
    timerShow.innerHTML = strTimer;

}



function timer(){

    let strSeconds = nowSeconds

    let hours = parseInt(strSeconds / 60 / 60)

    if(hours.toString().length < 2){
        hours = "0" + hours.toString()
    }

    strSeconds = strSeconds - hours * 60 * 60

    let minuts = parseInt(strSeconds / 60)

    if(minuts.toString().length < 2){
        minuts = "0" + minuts.toString()
    }

    strSeconds = strSeconds - minuts * 60

    let seconds = parseInt(strSeconds)

    if(seconds.toString().length < 2){
        seconds = "0" + seconds.toString()
    }

    if (nowSeconds <= 0) {
        timerShow.innerHTML = "00:00:00"
        eel.close_contest()
        window.clearInterval(timerIntervalId)
    }else{
        let strTimer = `${hours}:${minuts}:${seconds}`;
        timerShow.innerHTML = strTimer;
        --nowSeconds;        
    }
}


function loadAnswers(answers){
    const totalColor = {"OK": "green"}
    let types = {1: "Python"}
    const tabelAnswers = document.getElementById("answeBody");
    tabelAnswers.innerHTML = ""
    for(let i=0; i < answers.length; i++){
        const row = tabelAnswers.insertRow(-1)
        row.innerHTML = ` <tr>
                              <td>${answers[i].date_send}</td>
                              <td>${answers[i].id}</td>
                              <td>${answers[i].user.name}</td>
                              <td>${answers[i].task.id}</td>
                              <td>${types[answers[i].type_compiler]}</td>
                              <td><span color="${totalColor[answers[i].total]}">${answers[i].total}</span></td>
                              <td>${answers[i].time}</td>
                              <td>${answers[i].memory_size}</td>
                              <td>${answers[i].number_test}</td>
                              <td>${answers[i].points}</td>
                              <td><span class="light-blue darken-4" id="aReport" id_report=${answers[i].id}>отчет</span></td>
                          </tr>`
    }
    for(let report of document.querySelectorAll("#aReport")){
        report.addEventListener("click", openWindowReport)
    }
    updateNumberShipments(answers.length)
    
}


function loadMenu(menu){
    if(Object.keys(menu).length > 0){
        for(let taskMenu of listTasks.querySelectorAll("a")){
            const id_task = parseInt(taskMenu.querySelectorAll("input")[0].value)
            let total = menu[id_task]
            if(total != undefined){
                if(total.points == 0){
                    total = total.total
                }else if(total.points == 0 && total.total == "-"){
                    total = "0"
                }else{
                    total = total.points
                }
            }else{
                total = "-"
            }
            taskMenu.querySelectorAll("span")[0].innerHTML = total
        }
    }
}



function loadSelectTask(task){
    let typesTime = {1: "1 секунда", 2: "2 секунда", 3: "3 секунда", 4: "4 секунда", 5: "5 секунда"}
    let typesInput = {1: "стандартный ввод", 2: "файл input.txt"}
    let typesOutput = {1: "стандартный вывод", 2: "файл output.txt"}
    
    const timeWork = document.getElementById("timeWork")
    const sizeRaw = document.getElementById("sizeRaw")
    const typeInput = document.getElementById("typeInput")
    const typeOutput = document.getElementById("typeOutput")
    const nameTest = document.getElementById("name_test")
    const description = document.getElementById("description")
    const descriptionInput = document.getElementById("description_input")
    const descriptionOutput = document.getElementById("description_output")
    const example = document.getElementById("example")

    const testTabel = document.getElementById("test_tabel")
    testTabel.innerHTML = ""

    for(let i=0; i < task.path_test_file.test.length; i++){
        let row = testTabel.insertRow(-1)
        row.innerHTML = `<tr>
                            <td>${task.path_test_file.test[i].str_limited}</td>
                            <td>${task.path_test_file.test[i].necessary_test}</td>
                        </tr>`
    }

    const descriptions = task.description.split("\n")

    description.innerHTML = ""
    timeWork.innerHTML = typesTime[task.time_work]
    sizeRaw.innerHTML = task.size_raw + "Mb"
    typeInput.innerHTML = typesInput[task.type_input]
    typeOutput.innerHTML = typesOutput[task.type_output]
    nameTest.innerHTML = task.name_test
    
    numberShipments = task.number_shipments
    
    for(let discr of descriptions){
        description.innerHTML += `<p class="op__task">${discr}</p>`
    }

    example.innerHTML = ""


    for(let i=0; i < task.path_test_file.example.answer.length; i++){
        example.innerHTML += `<div class="row">
                                <h5 class="h__task left-align">Пример ${i+1}</h5>
                                <div class="tabel__box">
                                    <table>
                                        <thead>
                                        <tr>
                                            <th>Ввод</th>
                                            <th>Вывод</th>
                                        </tr>
                                        </thead>

                                        <tbody>
                                        <tr>
                                            <td>${task.path_test_file.example.filling_type_variable[i]}</td>
                                            <td>${task.path_test_file.example.answer[i]}</td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>`
    }

    descriptionInput.innerHTML = task.description_input
    descriptionOutput.innerHTML = task.description_output
    eel.load_answer()
}

function intervalLoadAnswer(){
    eel.load_answer()
}


function openSelectFile(event){
    eel.file()((pathFile)=>{
        let div = event.path[2]
        div.querySelectorAll(".file-path")[0].value = pathFile
        const id_file = div.querySelectorAll(".select_file")[0].id
        eel.set_file(pathFile)
    })
}

function loadsReports(report){
    const newWin = window.open("about:blank", "hello", "width=600,height=600")
    const body = `<html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="./File/css/main.css"  media="screen,projection"/>
      <link type="text/css" rel="stylesheet" href="./File/css/materialize.min.css"  media="screen,projection"/>
  
      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>
  
        <body>
        </body>
    </html>`
    newWin.document.write(body)
    console.log(report.list_report)
    const bodyMain = newWin.document.body
    for(let i=0; i < report.list_report.length; i++){
        console.log(report.list_report[i])
        bodyMain.innerHTML += `<div class="row">
                                    <h5 class="h__task left-align">номер теска ${i + 1}</h5>
                                    <h6 class="h__task left-align">${report.list_report[i].name_test}</h6>
                                    <p class="op__task" id="description_output">${report.list_report[i].list_test_report.join(' ')}</p>
                                    <p class="op__task" id="description_output">time ${report.list_report[i].time}ms : memory ${report.list_report[i].memory}mb : points ${report.list_report[i].point_sum} : test number ${report.list_report[i].number_test}</p>
                                </div>
                                <div class="line">
                                </div>`
    }
    dptWindow = newWin
}

function openWindowReport(event){
    if(dptWindow.closed == false)
        dptWindow.close()
    eel.load_report(parseInt(event.target.getAttribute("id_report")))
}

for(buttonFile of document.querySelectorAll(".select_file")){
    buttonFile.onclick = openSelectFile
}

eel.expose(loadsLeftInformation)
eel.expose(loadsTasks)
eel.expose(loadSelectTask)
eel.expose(loadAnswers)
eel.expose(loadsReports)
eel.expose(closeContest)
eel.expose(loadMenu)

document.getElementById("sendAnswer").onclick = ()=>{
    eel.button_send_answer()
}
