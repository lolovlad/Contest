const appUser = new Vue({
    el: "#user",
    data: {
        error: "",
        users: [],
        reversTypeUser: {
            1: 'Администратор',
            2: 'Пользователь'
        },
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
        userFilde: {
            sename: "",
            name: "",
            secondname: "",
            data: {
                type_education: 1,
                name_organization: "",
                learning_stage: '8 класс'
            },
            login: "",
            password: "",
            type: ""
        },
        targetEdu: [],
        targetLearningStage: [],
        typeEdu: 1,
        updateMode: false
    },
    methods: {
        updateUsers(value){
            this.users.length = 0
            for(let user of value){
                this.users.push(user)
            }
        },
        openPageForm(){
            eel.load_user_form()
            this.updateMode = false
        },

        openPageFormUpdate(idUser){
            this.updateMode = true
            eel.load_user_form_update(idUser)
        },

        switchSelectEdu(event) {
            const value = event.target.value
            this.selectUpdateLearningStage(value)
            this.selectUpdateTargetEdu(value)
        },
        selectUpdateLearningStage(value){
            this.targetLearningStage.length = 0
            for(let select of this.selectLearningStage[value]){
                this.targetLearningStage.push(select)
            }
        },
        selectUpdateTargetEdu(value){
            eel.load_organization(value)((edu)=>{
                this.targetEdu.length = 0
                for(let organization of edu){
                    this.targetEdu.push({text: organization.name_organizations, 
                                         value: organization.name_organizations})
                }
            })
        },

        addUser(){
            eel.button_add_user(this.userFilde)
            this.clearForm()       
        },

        deleteUser(id_user){
            eel.button_delete_user(id_user)
        },

        updateUser(){
            eel.button_update_user(this.userFilde)            
        },

        clearForm(){
           this.userFilde = {
                                sename: "",
                                name: "",
                                secondname: "",
                                data: {
                                    type_education: 1,
                                    name_organization: "",
                                    learning_stage: '8 класс'
                                },
                                login: "",
                                password: "",
                                type: ""
                            }
            this.updateMode = false
        },

        loadFormUser(user){
            console.log(user, "loadForm")

            this.selectUpdateLearningStage(user.data.type_education)
            this.selectUpdateTargetEdu(user.data.type_education)

            this.userFilde = user

            /*for (const [key, value] of Object.entries(user)) {
                this.userFilde[key] = value
            }*/
        },
        /*
       
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
        }*/
    
    },
    watch: {
        login: function(val){
            this.login = val
            eel.update_select_user({login: this.login})
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
    eel.load_user()
    eel.get_user_mode_update()((val) => {
        if(val){
            eel.load_form_user()
            appUser.updateMode = true
        }else{
            appUser.updateMode = false
            appUser.selectUpdateLearningStage(1)
            appUser.selectUpdateTargetEdu(1)
        }
    })
})

function updateUserTable(users){
    appUser.updateUsers(users)
}


function loadFormUser(user){
    appUser.loadFormUser(user)
}

function errorUpdateFieldUser(val){
    console.log(val)
    appUser.error = val
}


eel.expose(updateUserTable)
eel.expose(loadFormUser)
eel.expose(errorUpdateFieldUser)
