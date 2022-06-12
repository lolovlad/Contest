const menuContest = document.getElementById("menuContest")


function updateMenuContest(contests){
    menuContest.innerHTML = ""
    console.log(contests)
    for(let i=0; i < contests.length; i++){
        let tm = ""
        console.log(contests[i])
        if(contests[i].state_contest == 0 || contests[i].state_contest == 2){
            tm = `<div class="no_active">
            </div>`
        }

        menuContest.innerHTML += `<div class="col s12 m4">
                                        <div class="card blue-grey darken-1">
                                            ${tm}
                                            <div class="card-content white-text">
                                                <span class="card-title center-align">${contests[i].name_contest}</span>
                                                <input value="${contests[i].id}" type="hidden">
                                            </div>
                                            <div class="card-action">
                                                <a href="#" id="uploadContest">перейти в контест</a>
                                            </div>
                                        </div>
                                </div>`
        
    }

    for(menu of document.querySelectorAll("#uploadContest")){
        menu.addEventListener("click", (event)=>{
            const id_contest = event.path[2].querySelectorAll("input")[0].value
            eel.user_load_contest(parseInt(id_contest))
        })
    }
}

eel.expose(updateMenuContest)


document.addEventListener("DOMContentLoaded", ()=>{
    eel.load_menu_contest()
})

function intervalMenuContestr(){
    eel.load_menu_contest()
}

//window.setInterval(intervalMenuContestr, 10000) 

