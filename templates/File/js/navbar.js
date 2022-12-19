const appNav = new Vue({
    el: "#nav",
    data: {

    },
    methods: {
        OpenWindowTotal(){
            eel.open_window_total()
        },
        openWindowContest(){
            eel.open_window_contest()
        },
        ExitMenu(){
            eel.button_exit_menu()
        }
    }
})