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
            eel.user_load_contest(contest)
        },
        isActive(contest){
            if(contest.contests.state_contest == 3)
                return true
            if(contest.state_user == 2)
                return true
            return false
        }
    }
})

function updateMenuContest(contests){
    appMenu.updateContests(contests)
}


const menuContest = document.getElementById("menuContest")

document.addEventListener("DOMContentLoaded", ()=>{
    eel.load_menu_contest()
})

function intervalMenuContestr(){
    eel.load_menu_contest()
}

function locationReplace(path){
    window.location.replace(`/${path}`);
}

eel.expose(updateMenuContest)
eel.expose(locationReplace)


