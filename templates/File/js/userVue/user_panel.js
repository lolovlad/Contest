const appNav = new Vue({
    el: "#nav",
    data: {
        isView: true
    },
    methods: {
        openWindowTotal(){
            eel.open_window_total()
        },
        openWindowContest(){
            eel.open_window_menu()
        },
        exitMenu(){

        }
    }

})

function locationReplace(path){
    window.location.replace(`/${path}`);
}
eel.expose(locationReplace)