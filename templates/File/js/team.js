const appTeam = new Vue({
    el: "#team",
    data: {
        error: "",
        teams: [],
        selectUsers: [],
        modeUpdate: false,
        team: {
            name_team: "",
            users: []
        },
        notActive: false
    },
    methods:{
        openPageForm(){
            eel.load_team_form()
        },
        openPageFormUpdate(idTeam){
            eel.load_team_form_update(idTeam)
        },
        updateTeams(value){
            console.log(value, "teamrr")
            this.teams.length = 0
            this.teams.splice(0)
            for(let team of value){
                this.teams.push(team)
            }
        },

        openViewUsers(){
            modelWindowUser.open()
        },

        closeViewUsers(){

        },
        selectRowUserTeam(user){
            const id_name = this.team.users.map(el => el.id)
            if (!id_name.includes(user.id)){
                this.team.users.push(user)

                const id_team = this.selectUsers.map(el => el.id)
                const i = id_team.indexOf(user.id)
                
                this.selectUsers.splice(i, 1)
            }
            if(this.team.users.length == 0){
                this.notActive = true
            }else{
                this.notActive = false
            }
        },
        deleteUserTeam(user){
            const id_name = this.team.users.map(el => el.id)
            const i = id_name.indexOf(user.id)
            this.selectUsers.push(user)
            this.team.users.splice(i, 1)

            if(this.team.users.length == 0){
                this.notActive = true
            }else{
                this.notActive = false
            }
        },
        updateViewUser(users){
            this.selectUsers.length = 0
            for(let user of users){
                this.selectUsers.push(user)
            }
        },
        addTeam(){
            eel.button_add_team(this.team)
        },
        updateTeam(){
            eel.button_update_team(this.team)
        },
        deleteTeam(idTeam){
            eel.button_delete_team(idTeam)
        },
        loadFormTeam(team){
            this.modeUpdate = true
            this.team = team

            eel.load_user_in_team(this.team.id)((users)=>{
                this.updateViewUser(users)
            })
        },
        /*
        clearForm(){
            this.id = -1
            this.nameTeam = ""
            this.isSolo = false
            this.error = ""
            this.users = []
            this.isSelect = false
            eel.clear_select_team()
        },
        selectRowTeam(team){
            eel.select_team(team)
        },
        deleteUserTeam(user){
            const id_name = this.users.map(el => el.id)
            const i = id_name.indexOf(user.id)
            this.selectUsers.push(user)
            this.users.splice(i, 1)
            eel.update_select_team({users: this.users})
        },
        addTeam(){
            if(this.fieldValidete(this.nameTeam, "название команды обязательна"))
                if(this.fieldValidete(this.users, "кол-во участников должно быть больше 0"))    
                    eel.button_add_team()
        },
        updateTeam(){
            if(this.id != -1)
                if(this.fieldValidete(this.nameTeam, "название команды обязательна"))
                    if(this.fieldValidete(this.users, "кол-во участников должно быть больше 0")) 
                        eel.button_update_team()
        },
        deleteTeam(){
            if(this.id != -1)
                eel.button_delete_team()
        },
        loadFormTeam(team){
            this.id = team.id
            this.nameTeam = team.name_team
            this.isSolo = team.is_solo
            this.users = team.users
            this.isSelect = true
            eel.load_user_in_team(this.id)((users)=>{
                this.updateViewUser(users)
            })
        },
        fieldValidete(value, error, len=0){
            if(value.length <= len){
                this.error = error
                return false
            }
            return true
        }*/

    },
    filters: {
        convertUsers(val){
            let mapping = val.map((el)=>{
                return `${el.sename} ${el.name[0]}. ${el.secondname[0]}.`
            })
            return mapping.join(" ")
        }
    }
})

let modelWindowUser

document.addEventListener('DOMContentLoaded', () => {
    modelWindowUser = document.querySelector('#modalSelectUser')

    if(modelWindowUser != null){
        M.Modal.init(modelWindowUser, {onCloseEnd: appTeam.closeViewUsers})
        modelWindowUser = M.Modal.getInstance(modelWindowUser)
    }
    eel.get_team_mode_update()((val) => {
        if(val){
            eel.load_form_team()
            appTeam.updateMode = true
        }else{
            eel.load_user_in_team(appTeam.team.id)((users)=>{
                appTeam.updateViewUser(users)
            })
            appTeam.updateMode = false
        }
    })
    eel.load_teams()
})


function updateTeamTabel(teams){
    appTeam.updateTeams(teams)
}

function errorUpdateFieldTeam(val){
    appTeam.error = val
}

function loadFormTeam(team){
    appTeam.loadFormTeam(team)
}

eel.expose(updateTeamTabel)
eel.expose(errorUpdateFieldTeam)
eel.expose(loadFormTeam)
