const appContest = new Vue({
    el: "#contest",
    data: {
        id: -1,
        dateStart: "",
        dateEnd: "",
        timeStart: "",
        timeEnd: "",
        type: 1,
        nameContest: "",
        stateContest: 0,
        users: [],
        teams: [],

        dateStartNotStr: new Date(ms=0),
        dateEndNotStr: new Date(ms=0),
        
        

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

        typeReport: ["Exel", "Word", "PDF"]

    },
    methods: {
        padTo2Digits(num) {
            return num.toString().padStart(2, '0');
        },
        formatDate(date) {
            return [
              this.padTo2Digits(date.getDate()),
              this.padTo2Digits(date.getMonth() + 1),
              date.getFullYear()
            ].join('.');
        },

        selectRowContest(contest){
            this.isSelect = false
            appNav.setSelect(true)

            eel.select_contest(contest)
        },
        loadFormContest(contest){
            const datetimeStartStr = contest.datetime_start.split(", ")
            const datetimeEndStr = contest.datetime_end.split(", ")


            this.id = contest.id,
            this.dateStart = datetimeStartStr[0]
            this.dateEnd = datetimeEndStr[0]
            this.timeStart = datetimeStartStr[1]
            this.timeEnd = datetimeEndStr[1]
            this.typeSelectedContes = contest.type
            this.nameContest = contest.name_contest
            this.stateContest = contest.state_contest
            this.users = contest.users

            const dateStart = datetimeStartStr[0].split(".").map(el=>parseInt(el))
            const dateEnd = datetimeEndStr[0].split(".").map(el=>parseInt(el))

            const timeStart = datetimeStartStr[1].split(":").map(el=>parseInt(el))
            const timeEnd = datetimeEndStr[1].split(":").map(el=>parseInt(el))

            this.dateStartNotStr = new Date(year=dateStart[2], month=dateStart[1], day=dateStart[0], 
                hour=timeStart[0], minute=timeStart[1])
            this.dateEndNotStr = new Date(year=dateEnd[2], month=dateEnd[1], day=dateEnd[0], 
                hour=timeEnd[0], minute=timeEnd[1])

            if(this.typeSelectedContes == 1){
                this.isTeam = false
            }else{
                this.isTeam = true
            }
            appTask.idContest = contest.id
        },
        registrationUsers(){
            if(this.typeSelectedContes == 1){
                eel.load_user_in_contest(this.id)((users)=>{
                    this.updateViewUser(users)
                })
            }else{
                eel.load_team_in_contest(this.id)((teams)=>{
                    this.updateViewUserTeam(teams)
                })
            }

            modelWindowContest.open()
        },
        updateViewUser(users){
            this.selectUsers.length = 0
            for(let user of users){
                this.selectUsers.push(user)
            }
        },
        updateViewUserTeam(teams){
            this.selectTeams.length = 0
            this.teams.length = 0
            console.log(teams, "teams")
            for(let team of teams.team_not_in_contest){
                this.selectTeams.push(team)
            }
            for(let team of teams.team_in_contest){
                this.teams.push(team)
            }
        },
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
        updateContests(value){
            this.clearForm()
            this.contests.length = 0
            for(let contest of value){
                this.contests.push(contest)
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
        deleteContest(){

            eel.button_delete_contest()
        },
        updateContest(){
            eel.button_update_contest()
        },
        selectRowUserContest(user){
            const id_name = this.users.map(el => el.id)
            if (!id_name.includes(user.id)){
                this.users.push(user)

                const id_team = this.selectUsers.map(el => el.id)
                const i = id_team.indexOf(user.id)
                
                this.selectUsers.splice(i, 1)

                eel.update_select_contest({users: this.users})
            }
        },
        deleteUserContest(user){
            const id_name = this.users.map(el => el.id)
            const i = id_name.indexOf(user.id)
            this.selectUsers.push(user)
            this.users.splice(i, 1)
            eel.update_select_contest({users: this.users})
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
        agreaRegUsers(){
            eel.registration_users_contest()
            modelWindowContest.close()
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
        }
        
    },
    watch: {
        dateStart: function(val){
            try{
                this.dateStartNotStr.setMonth(val.getMonth())
                this.dateStartNotStr.setFullYear(val.getFullYear())
                this.dateStartNotStr.setDate(val.getDate())
                this.dateStart = this.formatDate(val)

                eel.update_select_contest({datetime_start: this.dateStartNotStr})
            }catch (err){
                this.dateStart = val
            }
        },
        dateEnd: function(val){
            try{
                this.dateEndNotStr.setMonth(val.getMonth())
                this.dateEndNotStr.setFullYear(val.getFullYear())
                this.dateEndNotStr.setDate(val.getDate())
                this.dateEnd = this.formatDate(val)

                eel.update_select_contest({datetime_end: this.dateEndNotStr})
            }catch (err){
                this.dateEnd = val
            }
        },
        timeStart: function(val){
            this.timeStart = val

            eel.update_select_contest({datetime_start: this.dateStartNotStr})
        },
        timeEnd: function(val){
            this.timeEnd = val

            eel.update_select_contest({datetime_end: this.dateEndNotStr})
        },
        nameContest: function(val){
            this.nameContest = val
            eel.update_select_contest({name_contest: this.nameContest})
        },
        stateContest: function(val){
            this.stateContest = val

            eel.update_select_contest({state_contest: this.stateContest})
        },
        type: function(val){
            this.type = val

            eel.update_select_contest({type: this.type})
        },
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

const appNav = new Vue({
    el: "#navApp",
    data: {
        isSelect: false
    },
    methods: {
        setSelect(val){
            this.isSelect = val
            console.log(val)
        },
        loadsTasks(){
            console.log(this.isSelect, "loadsTasks")
            if(this.isSelect)
                eel.load_tasks()
        }
    }
})

let modelWindowContest = NaN
let modelWindowReport = NaN

document.addEventListener("DOMContentLoaded", ()=>{
    modelWindowContest = document.querySelector('#teamModel')
    modelWindowReport = document.querySelector('#modalSelectReport')

    M.Modal.init(modelWindowContest, {onCloseEnd: appContest.closeViewContest})
    modelWindowContest = M.Modal.getInstance(modelWindowContest)
    
    M.Modal.init(modelWindowReport, {onCloseEnd: appContest.closeViewContest})
    modelWindowReport = M.Modal.getInstance(modelWindowReport)

    M.textareaAutoResize(document.getElementById("description"))

    eel.load_contests()
})

function updateContestTable(contests){
    appContest.updateContests(contests)
}

function loadFormContest(contest){
    appContest.loadFormContest(contest)
}

eel.expose(updateContestTable)
eel.expose(loadFormContest)