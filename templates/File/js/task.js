const appTask = new Vue({
    el: "#task",
    data: {
        tasks: [],
        filseTest: {
            pathTestFile: "",
            listNameFilse: [],

        },

        task: {
            name_task: "",
            content: "",
            type_task: 1,
        },

        typeTask: 1,
        numberShipments: 100,

        selectTypeTask: [
            {text: "A", value: 1},
            {text: "B", value: 2},
            {text: "C", value: 3},
            {text: "D", value: 4},
            {text: "I", value: 5},
            {text: "F", value: 6}
        ],
        error: "",
        updateMode: false
    },
    methods: {
        updateTasks(value){
            this.tasks = []
            for(let task of value){
                this.tasks.push(task)
            }
            
        },
        openPageForm(){
            eel.open_task_form()
        },
        saveFileTest(){

        },
        addTask(){
            this.task.description = tinymce.get("contentTask").getContent();
            this.task.description_input = tinymce.get("contentInput").getContent();
            this.task.description_output = tinymce.get("contentOutput").getContent();
            eel.button_add_task(this.task)
        },

        updateTask(){
            this.task.description = tinymce.get("contentTask").getContent();
            this.task.description_input = tinymce.get("contentInput").getContent();
            this.task.description_output = tinymce.get("contentOutput").getContent();
            eel.button_update_task(this.task)
        },
        
        openPageFormUpdate(idTask){
            eel.open_task_update_form(idTask)
        },
        openPageFormSettings(idTask){
            eel.open_task_settings_form(idTask)
        },
        loadForm(task){
            tinymce.get("contentTask").setContent(task.description);
            tinymce.get("contentInput").setContent(task.description_input);
            tinymce.get("contentOutput").setContent(task.description_output);
            this.task.id = task.id
            this.task.name_task = task.name_task
            this.task.type_task = task.type_task
        },
        deleteTask(idTask){
            eel.button_delete_task(idTask)
        },
        /*clearForm(){
            this.id = -1
            this.timeWork = 1
            this.sizeRaw = 32
            this.typeInput =  1
            this.typeOutput = 1
            this.nameTask = ""
            this.description = ""
            this.descriptionInput = ""
            this.descriptionOutput = ""

            this.pathTestFile = ""

            this.typeTask = 1
            this.numberShipments = 100

            this.isSelect = false

            eel.clear_select_task()
            setTimeout(autoResize, 10)
        },
        addTask(){
            eel.update_select_task({id_contest: this.idContest})
            eel.button_add_task()
        },
        updateTask(){
            eel.update_select_task({id_contest: this.idContest})
            eel.button_update_task()
        },
        deleteTask(){
            eel.update_select_task({id_contest: this.idContest})
            eel.button_delete_task()
        },
        selectRowTask(task){
            this.isSelect = true
            eel.select_task(task)
        },
        loadFormTask(task){
            console.log(task)
            this.id = task.id
            this.timeWork = task.time_work
            this.sizeRaw = task.size_raw
            this.typeInput =  task.type_input
            this.typeOutput = task.type_output
            this.nameTask = task.name_task
            this.description = task.description
            this.descriptionInput = task.description_input
            this.descriptionOutput = task.description_output

            this.pathTestFile = task.path_test_file

            this.typeTask = task.type_task
            this.numberShipments = task.number_shipments
            setTimeout(autoResize, 10)
        },*/

    },
    filters: {
        typeTaskFilter(val){
            const info = {
                1: "A",
                2: "B",
                3: "C",
                4: "D",
                5: "I",
                6: "F",
            }
            return info[val]
        },
        typeInputFilter(val){
            const info = {
                1: "стандартный ввод",
                2: "файл input.txt"
            }
            return info[val]
        },
        typeOutputFilter(val){
            const info = {
                1: "стандартный вывод",
                2: "файл output.txt"
            }
            return info[val]
        },
        shortDescription(val){
            if(val.length > 100){
                return val.split(0, 100) + "..."
            }
            return val
        },
        shortDescription(val){
            if(val.length > 100){
                return val.split(0, 100) + "..."
            }
            return val
        },
    }

})


document.addEventListener("DOMContentLoaded", ()=>{
    eel.get_task_mode_update()((val) => {
        if(val){
            appTask.updateMode = true
            eel.load_form_task()((task) => {
                appTask.loadForm(task)
            })
        }else{
            //eel.load_user_in_team(appTeam.team.id)((users)=>{
            //    appTeam.updateViewUser(users)
            //})
            //appTeam.updateMode = false
        }
    })

    eel.get_list_task()((tasks)=>{
        console.log(tasks)
        appTask.updateTasks(tasks)
    })
})

function updateTaskTable(tasks){
    appTask.updateTasks(tasks)
}

function loadFormTask(task){
    appTask.loadFormTask(task)
}


eel.expose(updateTaskTable)
eel.expose(loadFormTask)
