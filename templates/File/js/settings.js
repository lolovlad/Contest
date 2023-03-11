const appSettings = new Vue({
    el: "#settings",
    data: {
        settings: {
            type_work: 1,
            size_raw: 32,
            type_input: 1,
            type_output: 1,
            number_shipments: 100
        },

        filseTest: {
            pathTestFile: "",
            listNameFilse: []
        },

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
    },
    methods: {
        loadModelSettings(settings){
            this.settings = settings
        },
        updateSettings(){
            eel.button_update_settings(this.settings)
        },

        openAddFileWindow(){
            eel.get_setting_task()((settings) => {
                for(let fileName of settings.files){
                    const fileExt = fileName.split('.').pop();
                    if(fileExt == "json"){
                        this.filseTest.pathTestFile = fileName
                    }else{
                        this.filseTest.listNameFilse.push(fileName)
                    }
                }
            })
            modelWindowAddFile.open()
        },
        deleteFileInList(index){
            eel.delete_file(this.filseTest.listNameFiles[index])
            this.filseTest.listNameFilse.splice(index, 1);
        },
        addFileInList(){
            eel.files_test()((listFiles)=>{
                for(nameFile of listFiles){
                    this.filseTest.listNameFilse.push(nameFile)
                }
            })
        },
        closeModelWindowAddFile(){
            modelWindowAddFile.close()
        },
       
        openFile(){
            eel.file()((pathFile)=>{
                eel.upload_json_file(pathFile)((fileName)=>{
                    this.filseTest.pathTestFile = fileName
                })
            })
        },
    }
})

let modelWindowAddFile = NaN

document.addEventListener('DOMContentLoaded', () => {
    modelWindowAddFile = document.querySelector('#modalAddFilse')

    if(modelWindowAddFile != null){
        M.Modal.init(modelWindowAddFile, {onCloseEnd: appSettings.closeModelWindowAddFile})
        modelWindowAddFile = M.Modal.getInstance(modelWindowAddFile)
    }

    eel.get_setting_task()((settings)=>{
        appSettings.loadModelSettings(settings)
    })
})
