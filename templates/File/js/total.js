const appTotal = new Vue({
    el: "#total",
    data: {
        contests: [],
        report: [],
        nameColumn: [],
    },
    methods: {
        loadTotalReport(total){
            const typeContest = total[0].type_contest
            const thNew = []
            const tdNew = []
            this.nameColumn = []
            let col = []
            let n = 1
            for(const [keyNew, valueNew] of Object.entries(total[0].total)){
                thNew.push(`Задание ${n}`)
                ++n
            }
            if(typeContest == 1){
                col = ["№", "Участник"].concat(thNew, ["Сумма баллов"])
            }else{
                col = ["№", "Название команды"].concat(thNew, ["Сумма баллов"])
            }
            for(let value of col){
                this.nameColumn.push(value)
            }
            this.report = []
            n = 1
            console.log(total)
            for(let value of total){
                const tdNew = []
                for(const [keyNew, valueNew] of Object.entries(value.total)){
                    tdNew.push(valueNew.points)
                }
                if(typeContest == 1){
                    value.name = value.name_user
                }else{
                    value.name = value.name_team
                }
                value.total = tdNew
                value.num = n
                this.report.push(value)
                ++n
            }
            console.log(this.report)
        },
        loadContest(contests){
            this.contests = []
            console.log(contests)
            for(let contest of contests){
                this.contests.push(contest)
            }
        },
        openReportTotal(idContest){
            eel.select_contest_total(idContest)
        }
    }
})

document.addEventListener('DOMContentLoaded', function() {
    eel.load_contest_to_total()
})


function loadContest(contest){
    appTotal.loadContest(contest)
}


function loadTotalContest(total){
    appTotal.loadTotalReport(total)
 /*   console.log(total)
    totalMenu.innerHTML = ""

    for(const [key, value] of Object.entries(total.reports_total)){
        console.log(key, value)
        let thNew = ``
        
        for(const [keyNew, valueNew] of Object.entries(value[0].total)){
            thNew += `<th>Задание ${keyNew}</th>`
        }

        totalMenu.innerHTML += `<table>
                                  <thead>
                                    <tr>
                                        <th>№</th>
                                        <th>Название команды</th>
                                        <th>Участники</th>
                                        ${thNew}
                                        <th>Сумма баллов</th>
                                    </tr>
                                  </thead>
                        
                                  <tbody id="totalBody">
                                  </tbody>
                                </table>`
        const tabel = totalMenu.querySelectorAll("#totalBody")[0]
        tabel.innerHTML = ""
        
        for(let i=0; i < value.length; i++){
            let thNew = ``
        
            for(const [keyNew, valueNew] of Object.entries(value[i].total)){
                thNew += `<th>${valueNew.points}</th>`
            }
            let row = tabel.insertRow(-1)
            row.innerHTML = `<tr>
                                <th>${i+1}</th>
                                <th>${value[i].name_team}</th>
                                <th>${value[i].name_team}</th>
                                ${thNew}
                                <th>${value[i].sum_point}</th>
                            </tr>`
        }
    }*/ 
}

eel.expose(loadTotalContest)
eel.expose(loadContest)