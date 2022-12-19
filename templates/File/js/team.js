const appTeam = new Vue({
    el: "#team",
    data: {
        id: -1,
        nameTeam: "",
        isSolo: false,
        users: [],
        error: "",
        teams: [],
        selectUsers: [],
        isSelect: false
    },
    methods:{
        updateTeams(value){
            this.clearForm()
            this.teams.length = 0
            for(let team of value){
                this.teams.push(team)
            }
        },
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
        selectRowUserTeam(user){
            const id_name = this.users.map(el => el.id)
            if (!id_name.includes(user.id)){
                this.users.push(user)

                const id_team = this.selectUsers.map(el => el.id)
                const i = id_team.indexOf(user.id)
                
                this.selectUsers.splice(i, 1)

                eel.update_select_team({users: this.users})
            }
        },
        openViewUsers(){
            modelWindowUser.open()
            eel.load_user_in_team(this.id)((users)=>{
                this.updateViewUser(users)
            })
        },
        closeViewUsers(){

        },
        updateViewUser(users){
            this.selectUsers.length = 0
            for(let user of users){
                this.selectUsers.push(user)
            }
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
        }

    },
    watch: {
        nameTeam: function(val){
            this.nameTeam = val
            eel.update_select_team({name_team: this.nameTeam})
        },
        isSolo: function(val){
            this.isSolo = val
            eel.update_select_team({is_solo: this.isSolo})
        }
    },
    filters: {
        typeTeam(val){
            if(val){
                return "Да"
            }else{
                return "Нет"
            }
        },
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
    M.Modal.init(modelWindowUser, {onCloseEnd: appTeam.closeViewUsers})
    modelWindowUser = M.Modal.getInstance(modelWindowUser)


    eel.load_teams()
})


function updateTeamTabel(teams){
    appTeam.updateTeams(teams)
}

function errorUpdateFieldTeam(val){
    console.log(val)
    appTeam.error = val
}

function loadFormTeam(team){
    appTeam.loadFormTeam(team)
}

eel.expose(updateTeamTabel)
eel.expose(errorUpdateFieldTeam)
eel.expose(loadFormTeam)
