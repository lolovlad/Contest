let dptWindow = 0


function loadsAnswersPackage(answers){
    const totalColor = {"OK": "green"}
    let types = {1: "Python"}
    const tabelAnswer = document.getElementById("answerBody");
    tabelAnswer.innerHTML = ""
    for(let i=0; i < answers.length; i++){
        const row = tabelAnswer.insertRow(-1)
        row.innerHTML = `<tr>
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
                            <td><span class="light-blue darken-4" id="aReportPackage" id_report=${answers[i].id}>отчет</span></td>
                        </tr>`
    }
    for(let report of document.querySelectorAll("#aReportPackage")){
        report.addEventListener("click", openWindowReportPackage)
    }
}

function loadsReportsPackage(report){
    const newWin = window.open("about:blank", report.id, "width=600,height=600")
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

function openWindowReportPackage(event){
    if(dptWindow.closed == false)
        dptWindow.close()
    console.log(dptWindow)
    eel.load_report_package(parseInt(event.target.getAttribute("id_report")))
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