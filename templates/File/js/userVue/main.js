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

        tasks: {},
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

        menu: {},

    }, 
    methods: {
        loadLeftInformation(contest){
            	
            const dateStart = new Date(contest.datetime_start)
            const dateEnd = new Date(contest.datetime_end)
            const dateRegistration = new Date(contest.datetime_registration)
            
            this.loadsCompilation(contest.compilers)

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
                eel.close_contest()((message)=>{
                    websocket.send(message)
                })
                window.clearInterval(this.timerIntervalId)
            }else{
                this.timerShow = `${hours}:${minuts}:${seconds}`
                --this.nowSeconds
            }
        },
        loadsTask(tasks){
            this.tasks = tasks
            console.log(parseInt(Object.keys(tasks)[0]), tasks)
            this.selectRowTask(parseInt(Object.keys(tasks)[0]))
        },
        loadSelectTask(task){
            this.selectTask = task
            this.numberShipments = task.number_shipments
        },

        selectRowTask(IdTask){
            window.clearInterval(this.loadAnswerId)
            this.selectTask.id = parseInt(IdTask)
            eel.load_main_window_select_task(parseInt(IdTask))((task)=>{
                this.loadSelectTask(task)
            })
            this.getAnswers()
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
            eel.button_send_answer(this.selectTask.id, this.compileter)((message) => {
                websocket.send(message)
            })

            this.isSend = false
            this.file = ""
            this.compileter = 1
            //this.loadAnswerId = window.setInterval(this.getAnswers, 5000)
        },


        getAnswers(){
            eel.get_list_answers(this.selectTask.id)((answer)=>{
                this.loadsAnswers(answer)
            })
        },

        loadsAnswers(answers){
            this.answers = []
            for(let answer of answers){
                this.answers.push(answer)
            }

            this.updateNumberShipments(this.selectTask.number_shipments)
        },
        loadReport(id_answer){
            eel.get_report(id_answer)((report)=>{
                this.openWindowReport(report)
            })
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
            this.isClose = true
        },
        buttonCloseContest(){
            eel.close_contest()
            this.closeContest()
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
        }
    },
    watch: {
        compileter: function(val){
            this.compileter = val

            
        }
    }
    
})


let websocket

document.addEventListener('DOMContentLoaded', () => {
    appNav.isView = false

    eel.get_url_websocket()((url)=>{
        websocket = new WebSocket(url);

        websocket.onopen = function(e) {
            eel.load_main_window_contest()((contest) => {
                appMain.loadLeftInformation(contest)
            })
            eel.load_main_window_list_task()((tasks) => {
                appMain.loadsTask(tasks)
            })
        };
          
        websocket.onmessage = function(event) {
            const obj = JSON.parse(event.data);
            eel.parser_message(obj)
        };
          
        websocket.onclose = function(event) {
          if (event.wasClean) {
            alert(`[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`);
          } else {
            alert('[close] Соединение прервано');
          }
        };
          
        websocket.onerror = function(error) {
            alert(`[error]`);
        };
    })

});

function getListAnswer(){
    appMain.getAnswers()
}



eel.expose(getListAnswer)