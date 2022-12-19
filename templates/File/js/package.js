const appPackage = new Vue({
    el: "#appPackage",
    data: {
        answers: [],
        dptWindow: []
    },
    methods: {
        loadsAnswers(answers){
            this.answers = []
            for(let answer of answers){
                this.answers.push(answer)
            }
        },
        loadReport(id_answer){
            eel.load_report_package(id_answer)
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
            this.dptWindow.push(newWin)
        },
    }
})

function loadsAnswersPackage(answers){
    appPackage.loadsAnswers(answers)
}

function loadsReportsPackage(report){
    appPackage.openWindowReport(report)
}

window.onmouseout = ()=>{window.onbeforeunload = ConfirmLeave};
window.onmouseover = ()=>{window.onbeforeunload = null;}

function ConfirmLeave() {
    window.close()
}

document.addEventListener('DOMContentLoaded', () => {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    eel.load_answer_package()
});

var prevKey="";
document.onkeydown = function (e) {            
    if (e.key=="F5") {
        window.onbeforeunload = ConfirmLeave;
    }
    else if (e.key.toUpperCase() == "W" && prevKey == "CONTROL") {                
        window.onbeforeunload = ConfirmLeave;   
    }
    else if (e.key.toUpperCase() == "R" && prevKey == "CONTROL") {
        window.onbeforeunload = ConfirmLeave;
    }
    else if (e.key.toUpperCase() == "F4" && (prevKey == "ALT" || prevKey == "CONTROL")) {
        window.onbeforeunload = ConfirmLeave;
    }
    prevKey = e.key.toUpperCase();
}

eel.expose(loadsAnswersPackage)
eel.expose(loadsReportsPackage)