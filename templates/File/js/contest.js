const appContest = new Vue({
    el: "#contest",
    data: {
        users: [],
        teams: [],
        contest: {
            name_contest: "",
            type: 1,
            state_contest: 0,
            datetime_start: Date(ms=0),
            datetime_end: Date(ms=0),
        },


        dateStartNotStr: new Date(ms=0),
        dateEndNotStr: new Date(ms=0),
        
        dateStart: "",
        dateEnd: "",
        timeStart: "",
        timeEnd: "",
        

        selectTypeContest: [
            {text: "Олимпида", value: 1},
            {text: "Командная олимпиада", value: 2},
            {text: "Хакатон", value: 3}
        ],
        selectStateContest: [
            {text: "Зарегестрированн", value: 0},
            {text: "Подтверждено", value: 1},
            {text: "Проходит", value: 2},
            {text: "Завершенно", value: 3}
        ],
        selectUsers: [],
        selectTeams: [],
        contests: [],
        error: "",
        isSelect: true,
        isTeam: false,

        isReport: false,

        genereteReport: {
            pathFile: "",
            nameFile: "",
            typeReport: ""
        },

        typeReport: ["Exel", "Word", "PDF"],
        updateMode: false

    },
    methods: {
        updateContests(value){
            this.contests.length = 0
            for(let contest of value){
                this.contests.push(contest)
            }
        },

        openPageForm(){
            eel.load_contest_form()
        },
        addContest(){
            if(this.dateEndNotStr.getTime() > this.dateStartNotStr.getTime()){
                const isAgree = confirm("Поле типа соревнования нельзя будет изменить. Вы согласны с ведеными данными?");
                if(isAgree){
                    this.contest.datetime_start = this.dateStartNotStr
                    this.contest.datetime_end = this.dateEndNotStr
                    eel.button_add_contest(this.contest)
                }
            }else{
                this.error = "Дата начала больше даты окончания"
            }
        },

        deleteContest(idContest){
            eel.button_delete_contest(idContest)
        },
        updateContest(){
            if(this.dateEndNotStr.getTime() > this.dateStartNotStr.getTime()){
                this.contest.datetime_start = this.dateStartNotStr
                this.contest.datetime_end = this.dateEndNotStr
                eel.button_update_contest(this.contest)
            }else{
                this.error = "Дата начала больше даты окончания"
            }
        },
        openPageFormUpdate(idContest){
            eel.load_contest_form_update(idContest)
        },

        loadFormContest(contest){
           this.contest = contest
           this.dateStartNotStr = new Date(contest.datetime_start + ".00Z")
           this.dateEndNotStr = new Date(contest.datetime_end + ".00Z")
           initDatePiker()
           this.timeStart = `${this.dateEndNotStr.getHours()}:${this.dateEndNotStr.getMinutes()}`
           this.timeEnd = `${this.dateEndNotStr.getHours()}:${this.dateEndNotStr.getMinutes()}`
        },

        registrationUsers(idContest, type){
            if(type == 1){
                eel.load_user_in_contest(idContest)((users)=>{
                    this.isTeam = false
                    this.updateViewUser(users)
                })
            }else{
                eel.load_team_in_contest(idContest)((teams)=>{
                    this.isTeam = true
                    this.updateViewUserTeam(teams)
                })
            }

            modelWindowContest.open()
        },

        updateViewUser(users){
            this.selectUsers.length = 0
            this.users.length = 0

            for(let user of users.user_not_in_contest){
                this.selectUsers.push(user)
            }
            for(let user of users.user_in_contest){
                this.users.push(user)
            }
        },

        updateViewUserTeam(teams){
            this.selectTeams.length = 0
            this.teams.length = 0
            for(let team of teams.team_not_in_contest){
                this.selectTeams.push(team)
                for(let user of team.users){
                    this.users.push(user)
                }
            }
            for(let team of teams.team_in_contest){
                this.teams.push(team)
            }
        },

        selectRowUserContest(user){
            const id_name = this.users.map(el => el.id)
            if (!id_name.includes(user.id)){
                this.users.push(user)

                const id_team = this.selectUsers.map(el => el.id)
                const i = id_team.indexOf(user.id)
            
                this.selectUsers.splice(i, 1)
            }
        },
        deleteUserContest(user){
            const id_name = this.users.map(el => el.id)
            const i = id_name.indexOf(user.id)
            this.selectUsers.push(user)
            this.users.splice(i, 1)
        },

        selectRowTeamContest(team){
            const id_team = this.teams.map(el => el.id)
            if (!id_team.includes(team.id)){
                let id_now_team = new Set(team.users.map(el => el.id))
                let id_all_team = new Set(this.users.map(el => el.id))
                let intersection = new Set(
                    [...id_now_team].filter(x => id_all_team.has(x)))
                
                console.log(id_now_team, id_all_team, intersection)
                if(intersection.size == 0){
                    this.teams.push(team)

                    const id_team = this.selectTeams.map(el => el.id)
                    const i = id_team.indexOf(team.id)
                    
                    this.selectTeams.splice(i, 1)
                    this.users = this.users.concat(team.users)
                }
            }
        },
        deleteTeamContest(team){
            const id_team = this.teams.map(el => el.id)
            const i = id_team.indexOf(team.id)
            this.selectTeams.push(team)
            this.teams.splice(i, 1)
            this.users.length = 0
            for(let team of this.teams){
                this.users = this.users.concat(team.users)
            }
        },

        agreaRegUsers(){
            eel.registration_users_contest(this.users)
            modelWindowContest.close()
        },
        openWindowTask(idContest){
            eel.open_window_task(idContest)
        }
        /*
        addContest(){
            eel.update_select_contest({datetime_registration: new Date(ms=0)})
            if(this.dateEndNotStr.getTime() > this.dateStartNotStr.getTime()){
                const isAgree = confirm("Поле типа соревнования нельзя будет изменить. Вы согласны с ведеными данными?");
                if(isAgree)
                    eel.button_add_contest()
                    this.clearForm()
            }else{
                this.error = "Дата начала больше даты окончания"
            }
        },
        clearForm(){
            this.id = -1
            this.dateStart = ""
            this.dateEnd = ""
            this.timeStart = ""
            this.timeEnd = ""
            this.typeSelectedContes = 1
            this.nameContest = ""
            this.stateContest = 0
            this.users = []
            this.teams = []

            this.isSelect = true
            appNav.setSelect(false)

            this.dateStartNotStr = new Date(ms=0)
            this.dateEndNotStr = new Date(ms=0)

            datapickerElementEnd.setDate()
            datapickerElementStart.setDate()
            eel.clear_select_contest()
        },
        closeViewContest(){

        },

        selectRowTeamContest(team){
            const id_team = this.teams.map(el => el.id)
            if (!id_team.includes(team.id)){
                let id_now_team = new Set(team.users.map(el => el.id))
                let id_all_team = new Set(this.users.map(el => el.id))
                let intersection = new Set(
                    [...id_now_team].filter(x => id_all_team.has(x)))
                if(intersection.size == 0){
                    this.teams.push(team)

                    const id_team = this.selectTeams.map(el => el.id)
                    const i = id_team.indexOf(team.id)
                    
                    this.selectTeams.splice(i, 1)
                    this.users = this.users.concat(team.users)
                    eel.update_select_contest({users: this.users})
                }
            }
        },
        deleteTeamContest(team){
            const id_team = this.teams.map(el => el.id)
            const i = id_team.indexOf(team.id)
            this.selectTeams.push(team)
            this.teams.splice(i, 1)
            this.users.length = 0
            for(let team of this.teams){
                this.users = this.users.concat(team.users)
            }
            console.log(this.users)
            eel.update_select_contest({users: this.users})
        },
      
        contestReport(){
            modelWindowReport.open()
            //eel.button_contest_create_report()
        },
        openPathFile(){
            eel.path_report()((pathFile) => {
                this.genereteReport.pathFile = pathFile
            })
        },
        selectTypeReport(typeReport){
            this.genereteReport.typeReport = typeReport
        },
        isSelectedTypeReport(typeReport){
            if(this.genereteReport.typeReport == typeReport)
                return "type__report__active"
            return ""
        },
        agreaReport(){
            if(this.genereteReport.pathFile && this.genereteReport.nameFile && this.genereteReport.typeReport){
                eel.button_contest_create_report(this.genereteReport)
                this.genereteReport = {
                    pathFile: "",
                    nameFile: "",
                    typeReport: ""
                }
            }else{
                alert("Не все поля заполнены")
            }
        }*/
        
    },
    filters: {
        typeSelectContest(val){
           const info = {
            1: "Олимпида",
            2: "Командная олимпиада",
            3: "Хакатон",
            }
            return info[val]
        },
        stateSelectContest(val){
            const info = {
                0: "Зарегестрированн",
                1: "Подтверждено",
                2: "Проходит",
                3: "Завершенно"
            }
            return info[val]
        },
        convertUsers(val){
            let mapping = val.map((el)=>{
                return `${el.sename} ${el.name[0]}. ${el.secondname[0]}.`
            })
            return mapping.join(" ")
        },
        dateFilter(val){
            return new Date(val).toLocaleString()
        }
    },
    computed: {
        isSelected(){
            if(this.isSelect){
                return "disabled"
            }
            return ""
        },
    }
})

let modelWindowContest = NaN
let modelWindowReport = NaN

document.addEventListener("DOMContentLoaded", ()=>{
    modelWindowContest = document.querySelector('#teamModel')
    modelWindowReport = document.querySelector('#modalSelectReport')

    if(modelWindowContest != null){
        M.Modal.init(modelWindowContest, {onCloseEnd: appContest.closeViewContest})
        modelWindowContest = M.Modal.getInstance(modelWindowContest)
    }

    if(modelWindowReport != null){    
        M.Modal.init(modelWindowReport, {onCloseEnd: appContest.closeViewContest})
        modelWindowReport = M.Modal.getInstance(modelWindowReport)
    }

    eel.get_contest_mode_update()((val) => {
        if(val){
            eel.load_form_contest()
            appContest.updateMode = true
        }else{
            //eel.load_user_in_team(appTeam.team.id)((users)=>{
            //    appTeam.updateViewUser(users)
            //})
            //appTeam.updateMode = false
        }
    })

    eel.load_contests()
    initDatePiker()
})

function updateContestTable(contests){
    appContest.updateContests(contests)
}

function loadFormContest(contest){
    appContest.loadFormContest(contest)
}

eel.expose(updateContestTable)
eel.expose(loadFormContest)