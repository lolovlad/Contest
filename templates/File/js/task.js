const appTask = new Vue({
    el: "#task",
    data: {
        tasks: [],
        newTask: [],
        id: -1,
        idContest: -1,
        timeWork: 1,
        sizeRaw: 32,
        typeInput: 1,
        typeOutput: 1,
        nameTask: "",
        description: "",
        descriptionInput: "",
        descriptionOutput: "",

        pathTestFile: "",

        typeTask: 1,
        numberShipments: 100,

        selectTimeWork: [
            {text: "1 секунда", value: 1},
            {text: "2 секунда", value: 2},
            {text: "3 секунда", value: 3},
            {text: "4 секунда", value: 4},
            {text: "5 секунда", value: 5}
        ],
        selectTypeInput: [
            {text: "стандартный ввод", value: 1},
            {text: "файл input.txt", value: 2}
        ],
        selectTypeOutput: [
            {text: "стандартный вывод", value: 1},
            {text: "файл output.txt", value: 2}
        ],
        selectTypeTask: [
            {text: "A", value: 1},
            {text: "B", value: 2},
            {text: "C", value: 3},
            {text: "D", value: 4},
            {text: "I", value: 5},
            {text: "F", value: 6}
        ],
        error: "",
        isSelect: false
    },
    watch: {
        timeWork: function(val){
            this.timeWork = val

            eel.update_select_task({time_work: this.timeWork})
        },
        sizeRaw: function(val){
           this.sizeRaw = val

           eel.update_select_task({size_raw: this.sizeRaw})
        },
        typeInput: function(val){
            this.typeInput = val

            eel.update_select_task({type_input: this.typeInput})
        },
        typeOutput: function(val){
            this.typeOutput = val

            eel.update_select_task({type_output: this.typeOutput})
        },
        description: function(val){
            this.description = val
            eel.update_select_task({description: this.description})
        },
        descriptionInput: function(val){
            this.descriptionInput = val

            eel.update_select_task({description_input: this.descriptionInput})
        },
        descriptionOutput: function(val){
            this.descriptionOutput = val

            eel.update_select_task({description_output: this.descriptionOutput})
        },
        pathTestFile: function(val){
            this.pathTestFile = val

            eel.update_select_task({path_test_file: this.pathTestFile})
        },
        typeTask: function(val){
            this.typeTask = val

            eel.update_select_task({type_task: this.typeTask})
        },
        numberShipments: function(val){
            this.numberShipments = val

            eel.update_select_task({number_shipments: this.numberShipments})
        },
        nameTask: function(val){
            this.nameTask = val

            eel.update_select_task({name_task: this.nameTask})
        },
        idContest: function(val){
            this.idContest = val

            eel.update_select_task({id_contest: this.idContest})
        },
    },
    methods: {
        clearForm(){
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
        openFile(){
            eel.file()((pathFile)=>{
                this.pathTestFile = pathFile
            })
        },
        updateTasks(value){
            this.clearForm()
            this.tasks = []
            for(let task of value){
                this.tasks.push(task)
            }
            
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
        }

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


function updateTaskTable(tasks){
    appTask.updateTasks(tasks)
}

function loadFormTask(task){
    appTask.loadFormTask(task)
}

function autoResize(){
    const textArea = document.getElementById("description")
    M.textareaAutoResize(textArea)
}

eel.expose(updateTaskTable)
eel.expose(loadFormTask)
