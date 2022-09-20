const app = new Vue({
        el: "#app",
        data: {
                login: "",
                password: "",
                error: ""
        },
        methods: {
                setResult(){
                        eel.button_login()
                },
                clear(){
                        this.login = ""
                        this.password = ""
                        this.error = ""
                },
                setError(errorVal){
                        this.error = errorVal
                }
        },
        watch: {
                login: function(val){
                        this.login = val
                        eel.update_field_login({"login": this.login, 
                                                "password": this.password})
                },
                password: function(val){
                        this.password = val
                        eel.update_field_login({"login": this.login, 
                                                "password": this.password})
                }
        }
})

function update_error(errorVal){
        app.setError(errorVal)
}

function locationReplace(path){
        console.log(111)
        window.location.replace(`/${path}`);
}


eel.expose(update_error)
eel.expose(locationReplace)