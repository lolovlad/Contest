const appMenu = new Vue({
    el: "#menu",
    data: {
        contests: [],
        selectContest: null
    },
    methods: {
        updateContests(value){
            console.log(value)
            this.contests.length = 0
            for(let contest of value){
                this.contests.push(contest)
            }
        },
        selectRowContest(contest){
            //eel.user_load_contest(contest)
            eel.open_window_contest_user(contest.id)
        }
    }
})

function updateMenuContest(contests){
    appMenu.updateContests(contests)
}


const menuContest = document.getElementById("menuContest")

document.addEventListener("DOMContentLoaded", ()=>{
    intervalMenuContestr()
})

function intervalMenuContestr(){
    eel.load_menu_contest()((contests) => {
        appMenu.updateContests(contests)
    })
}

eel.expose(updateMenuContest)



