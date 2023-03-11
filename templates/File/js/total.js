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
            for(const value of col){
                this.nameColumn.push(value)
            }
            this.report = []
            n = 1
            for(const value of total){
                const tdNew = []
                for(const [keyNew, valueNew] of Object.entries(value.total)){
                    tdNew.push(valueNew)
                }
                value.name = value.name
                value.total = tdNew
                value.num = n
                this.report.push(value)
                ++n
            }
        },
        loadContest(contests){
            this.contests = []
            for(let contest of contests){
                this.contests.push(contest)
            }
        },
        openReportTotal(idContest){
            eel.select_contest_total(idContest)((total)=>{
                this.loadTotalReport(total)
            })
        }
    }
})

document.addEventListener('DOMContentLoaded', function() {
    eel.load_contest_to_total()((contest)=>{
        appTotal.loadContest(contest)
    })
})


function loadContest(contest){
    appTotal.loadContest(contest)
}


function loadTotalContest(total){
    appTotal.loadTotalReport(total)
}

eel.expose(loadTotalContest)
eel.expose(loadContest)