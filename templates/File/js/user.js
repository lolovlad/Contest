const appUser = new Vue({
    el: "#user",
    data: {
        id: -1,
        login: "",
        name: "",
        sename: "",
        secondname: "",
        placeOfStudy: "",
        learningStage: "8 класс",
        password: "",
        type: 1,
        users: [],
        organizations: [],
        error: "",
        selectTypeEdu: [
            { text: 'Школа', value: 1 },
            { text: 'Вуз', value: 2 },
            { text: 'Колледж', value: 3 },
            { text: 'Иные', value: 4 }
        ],
        selectTypeUser: [
            { text: 'Администратор', value: 1 },
            { text: 'Пользователь', value: 2 }
        ],
        reversTypeUser: {
            1: 'Администратор',
            2: 'Пользователь'
        },
        selectLearningStage: {
            1: [
                { text: '8 класс', value: '8 класс' },
                { text: '9 класс', value: '9 класс' },
                { text: '10 класс', value: '10 класс' },
                { text: '11 класс', value: '11 класс' }
            ],
            2: [
                { text: '1 курс', value: '1 курс' },
                { text: '2 курс', value: '2 курс' },
                { text: '3 курс', value: '3 курс' },
                { text: '4 курс', value: '4 курс' }
            ],
            3: [
                { text: '1 курс', value: '1 курс' },
                { text: '2 курс', value: '2 курс' },
                { text: '3 курс', value: '3 курс' },
                { text: '4 курс', value: '4 курс' }
            ],
            4: [
                { text: 'Обучение', value: 'Обучение' },
            ],
        },
        targetEdu: [],
        targetLearningStage: [],
        typeEdu: 1,
        isSelect: false
    },
    methods: {
        updateUsers(value){
            this.clearForm()
            this.users.length = 0
            for(let user of value){
                this.users.push(user)
            }
            console.log(this.users)
        },
        selectRowUser(user){
            eel.select_user(user)
            this.isSelect = true
        },
        updateOrganization(value){
            this.organizations.length = 0
            for(let organization of value){
                this.organizations.push(organization)
            }

            this.selectUpdateTargetEdu()
            this.selectUpdateLearningStage()
            
        },
        selectUpdateTargetEdu(){
            this.targetEdu.length = 0
            for(let organization of this.organizations){
                if(organization.type_organizations == this.typeEdu){
                    this.targetEdu.push({text: organization.name_organizations, 
                                         value: organization.name_organizations})
                }
            }
            this.placeOfStudy = this.targetEdu[0].value
        },
        selectUpdateLearningStage(){
            this.targetLearningStage.length = 0
            for(let select of this.selectLearningStage[this.typeEdu]){
                this.targetLearningStage.push(select)
            }
        },
        loadFormUser(user){
            console.log(user, "loadForm")
            this.id = user.id
            this.login = user.login
            this.name = user.name
            this.sename = user.sename
            this.secondname = user.secondname
            this.typeEdu = user.type_learning
            this.placeOfStudy = user.place_of_study
            
            this.password = user.password
            this.type = user.type

            this.learningStage = user.learning_stage
        },
        addUser(){
            if(this.fieldValidete(this.login, "Поле логина обязательное"))
                if(this.fieldValidete(this.password, "Поле пароля обязательное"))
                    if(this.fieldValidete(this.name, "Поле имени обязательное"))
                        if(this.fieldValidete(this.sename, "Поле фамилии обязательное"))
                            if(this.fieldValidete(this.secondname, "Поле отчества обязательное")){
                                eel.update_select_user({
                                    type_learning: this.typeEdu,
                                    place_of_study: this.placeOfStudy,
                                    learning_stage: this.learningStage,
                                    
                                })
                                eel.button_add_user()
                            }
        },
        deleteUser(){
            eel.button_delete_user()
        },
        updateUser(){
            if(this.fieldValidete(this.login, "Поле логина обязательное"))
                if(this.fieldValidete(this.name, "Поле имени обязательное"))
                    if(this.fieldValidete(this.sename, "Поле фамилии обязательное"))
                        if(this.fieldValidete(this.secondname, "Поле отчества обязательное")){
                            eel.update_select_user({
                                type_learning: this.typeEdu,
                                place_of_study: this.placeOfStudy,
                                learning_stage: this.learningStage,
                                
                            })
                            eel.button_update_user()
                        }
        },
        clearForm(){
            this.id = -1
            this.login = ""
            this.name = ""
            this.sename = ""
            this.secondname = ""
            this.password = ""
            this.error = ""
            this.type = 1
            this.typeEdu = 1
            this.isSelect = false
            eel.clear_select_user()
        },
        fieldValidete(value, error){
            if(value.length == 0){
                this.error = error
                return false
            }
            return true
        }
    },
    watch: {
        login: function(val){
            this.login = val
            eel.update_select_user({login: this.login})
        },
        password: function(val){
            this.password = val
            eel.update_select_user({password: this.password})
        },
        name: function(val){
            this.name = val
            eel.update_select_user({name: this.name})
        },
        sename: function(val){
            this.sename = val
            eel.update_select_user({sename: this.sename})
        },
        secondname: function(val){
            this.secondname = val
            eel.update_select_user({secondname: this.secondname})
        },
        type: function(val){
            this.type = val
            eel.update_select_user({type: this.type})
        },
        selectUser: function(val){
            this.selectUser = val
            console.log(val)
        },
        typeEdu: function(val){
            this.typeEdu = val
            this.selectUpdateTargetEdu()
            this.selectUpdateLearningStage()
            eel.update_select_user({type_learning: this.typeEdu})
        },
        placeOfStudy: function(val){
            this.placeOfStudy = val
            this.selectUpdateLearningStage()
            eel.update_select_user({place_of_study: this.placeOfStudy})
        },
        learningStage: function(val){
            this.learningStage = val
            eel.update_select_user({learning_stage: this.learningStage})
        }
    },
    filters: {
        typeUser(val){
            if(val == 1){
                return "Администратор"
            }else{
                return "Пользователь"
            }
        },
        isNoneFild(val){
            if(val.length == 0)
                return "None"
            return val
        }
    }
})

document.addEventListener('DOMContentLoaded', () => {
    eel.load_organization()((edu)=>{
        appUser.updateOrganization(edu)
    })
    eel.load_user()
})

function updateUserTable(users){
    appUser.updateUsers(users)
}


function loadFormUser(user){
    console.log(user)
    appUser.loadFormUser(user)
}

function errorUpdateFieldUser(val){
    console.log(val)
    appUser.error = val
}


eel.expose(updateUserTable)
eel.expose(loadFormUser)
eel.expose(errorUpdateFieldUser)
