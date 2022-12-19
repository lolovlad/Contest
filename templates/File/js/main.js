const appMain = new Vue({
    el: "#main",
    data: {
        contest: {
            nameContest: "",
            timeRegistration: "",
            timeStart: "",
            timeEnd: "",
            id: 0
        },
        selectTask: {
            id: 0,
            nameTask: "",
            timeWork: "",
            sizeRaw: "",
            typeInput: "",
            typeOutput: "",
            nameTask: "",
            description: "",
            descriptionInput: "",
            descriptionOutput: "",

            pathTestFile: "",

            descriptionOutput: "",
            numberShipments: 100,
            taskView: {
                example: {
                    filling_type_variable: [],
                    answer: []
                },
                test: [{
                    str_limited: "",
                    necessary_test: ""
                }]
            }
        },
        tasks: [],
        answers: [],
        selectCompilation: [],
        planeSeconds: 0,
        numberShipments: 100,
        timerIntervalId: NaN,

        loadAnswerId: NaN,

        timeСontinuation: "",
        timerShow: "",
        nowSeconds: 0,
        compilations: [],

        file: "",
        compileter: 1,
        isSend: false,
        isClose: false,

        menu: {}
    }, 
    methods: {
        loadLeftInformation(contest){
            	
            this.loadsTask(contest.tasks)
            const dateStart = new Date(contest.datetime_start)
            const dateEnd = new Date(contest.datetime_end)
            const dateRegistration = new Date(contest.datetime_registration)

            this.contest.id = contest.id
            this.contest.nameContest = contest.name_contest
            this.contest.timeRegistration = this.formatDate(dateRegistration)
            this.contest.timeStart = this.formatDate(dateStart)
            this.contest.timeEnd = this.formatDate(dateEnd)
        
            let dateNow = dateEnd - dateStart
            this.planeSeconds = dateNow
            

            let hours = this.padTo2Digits(parseInt(dateNow / 1000 / 60 / 60))

                     
            dateNow = dateNow - hours * 60 * 60 * 1000
            let minuts = this.padTo2Digits(parseInt(dateNow / 1000 / 60))
        
            dateNow = dateNow - minuts * 60 * 1000
            let seconds =  this.padTo2Digits(parseInt(dateNow / 1000))
        
            const milliseconds = Date.now()
            this.nowSeconds = (dateEnd - milliseconds) / 1000
        
            this.timerIntervalId = window.setInterval(this.timer, 1000)
            
            this.timeСontinuation = `${hours}:${minuts}:${seconds}`
            this.timer()
        
        },
        padTo2Digits(num) {
            return num.toString().padStart(2, '0')
        },
        formatDate(date) {
            return [
              this.padTo2Digits(date.getDate()),
              this.padTo2Digits(date.getMonth() + 1),
              date.getFullYear()
            ].join('.')
        },
        timer(){
            let strSeconds = this.nowSeconds
            let hours = this.padTo2Digits(parseInt(strSeconds / 60 / 60))
        
            strSeconds = strSeconds - hours * 60 * 60
            let minuts = this.padTo2Digits(parseInt(strSeconds / 60))
        
            strSeconds = strSeconds - minuts * 60
            let seconds = this.padTo2Digits(parseInt(strSeconds))
        
            if (this.nowSeconds <= 0) {
                this.timerShow = "00:00:00"
                eel.close_contest()
                window.clearInterval(this.timerIntervalId)
            }else{
                this.timerShow = `${hours}:${minuts}:${seconds}`
                --this.nowSeconds
            }
        },
        loadsTask(tasks){
            this.tasks = []
            for(let task of tasks){
                this.menu[task.id] = "-"
                this.tasks.push(task)
            }
            this.selectRowTask(tasks[0])
        },
        selectRowTask(task){
            window.clearInterval(this.loadAnswerId)

            this.selectTask.id = task.id
            this.selectTask.nameTask = task.name_task
            this.selectTask.timeWork = task.time_work
            this.selectTask.sizeRaw = task.size_raw
            this.selectTask.typeInput = task.type_input
            this.selectTask.typeOutput = task.type_output
            this.selectTask.description = task.description
            this.selectTask.descriptionInput = task.description_input
            this.selectTask.descriptionOutput = task.description_output
            this.selectTask.numberShipments = task.number_shipments
            this.selectTask.pathTestFile = task.path_test_file
            this.selectTask.taskView.test = task.task_view.test
            this.selectTask.taskView.example = task.task_view.example
            
            this.updateNumberShipments(task.number_shipments)
            eel.select_answer({id_contest: this.contest.id, id_task: this.selectTask.id})
            eel.load_answer({
                id_contest: this.contest.id, 
                id_task: task.id
            })
            this.loadAnswerId = window.setInterval(this.loadAnswersInterval, 5000)
        },
        loadAnswersInterval(){
            eel.load_answer({
                id_contest: this.contest.id, 
                id_task: this.selectTask.id
            })
            this.updateNumberShipments(this.selectTask.numberShipments)
        },
        updateNumberShipments(num=0){
            this.numberShipments = num - this.answers.length
        },
        loadsCompilation(compilations){
            this.compilations = []
            for(let compilation of compilations){
                this.compilations.push(compilation)
            }
        },
        openFile(){
            eel.file_programme()((fileName)=>{
                this.file = fileName
                const pathSplit = this.file.split(".")
                eel.upload_file({
                    file_name: this.file,
                    extension_file: pathSplit.pop()
                })
                this.isSend = true
            })
        },
        addAnswer(){
            eel.button_send_answer()
            this.isSend = false
            this.file = ""
            this.compileter = 1
        },
        loadsAnswers(answers){
            this.answers = []
            for(let answer of answers){
                this.answers.push(answer)
            }
        },
        loadMenu(menu){
            this.menu = {}
            for(let key in menu) {
                if(menu[key].points != 0)
                    this.menu[key] = menu[key].points
                else
                    this.menu[key] = menu[key].total
            }
            this.tasks.push(0)
            this.tasks.pop()
        },
        menuView(id_task){
            return this.menu[parseInt(id_task)]
        },
        loadReport(id_answer){
            eel.load_report(id_answer)
        },
        openWindowReport(report){
            console.log(report, "report vue")
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
        },
        openPackageWindow(){
            eel.open_package_window()
        },
        closeContest(){
            console.log("cera")
            this.isClose = true
        },
        buttonCloseContest(){
            eel.close_contest()
        },
        ExitContest(){
            eel.open_window_menu()
        },
        examplePrint(val){
            const new_val = val.replaceAll("\n", "<br />")
            return new_val
        }
    },
    filters: {
        typeTaskFilter(val){
            const info = {
                1: "A",
                2: "B",
                3: "C",
                4: "D",
                5: "I",
                6: "F",
            }
            return info[val]
        },
        typeInputFilter(val){
            const info = {
                1: "стандартный ввод",
                2: "файл input.txt"
            }
            return info[val]
        },
        typeOutputFilter(val){
            const info = {
                1: "стандартный вывод",
                2: "файл output.txt"
            }
            return info[val]
        },
        namePrint(name){
            return name.sename
        },
        datePrint(val){
            const date = new Date(val)
            return date.toLocaleString()
        },
        examplePrint(val){
            const new_val = val.replace("\n", "<br />")
            return new_val
        }
    },
    watch: {
        compileter: function(val){
            this.compileter = val

            eel.select_answer({type_compilation: this.compileter})
        }
    }
    
})

document.addEventListener('DOMContentLoaded', () => {
    eel.load_main_window_contest()

    eel.load_compilation()((compilations)=>{
        appMain.loadsCompilation(compilations)
    })

    eel.is_close()((isClose)=>{
        console.log(isClose)
         if(isClose)
             appMain.closeContest()
    })
});

function closeContest(){
    appMain.closeContest()
}

function loadMenu(menu){
    appMain.loadMenu(menu)
}

function loadsReports(report){
    console.log(report, "report")
    appMain.openWindowReport(report)
}


function loadsLeftInformation(contest){
    appMain.loadLeftInformation(contest)
}

function loadAnswers(answers){
    appMain.loadsAnswers(answers)
}

function locationReplace(path){
    window.location.replace(`/${path}`);
}

eel.expose(loadsLeftInformation)
eel.expose(loadsReports)
eel.expose(loadMenu)
eel.expose(loadAnswers)
eel.expose(closeContest)
eel.expose(locationReplace)