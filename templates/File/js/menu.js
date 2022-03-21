const menuContest = document.getElementById("menu_contest")


function updateMenuContest(contests){
    menuContest.innerHTML = ""

    for(let i=0; i < contests.contests.length; i++){
        menuContest.innerHTML += `<div class="col s12 m4">
                                    <div class="card blue-grey darken-1">
                                        <div class="card-content white-text">
                                            <span class="card-title center-align">${contests.contests[i].name_contest}</span>
                                            <input value="${contests.contests[i].id}" type="hidden">
                                        </div>
                                        <div class="card-action">
                                            <a href="#" id="upload_contest">перейти в контест</a>
                                      </div>
                                    </div>
                                </div>`
    }

    for(menu of document.querySelectorAll("#upload_contest")){
        menu.addEventListener("click", (event)=>{
            const id_contest = event.path[2].querySelectorAll("input")[0].value
            eel.user_load_contest(parseInt(id_contest))
        })
    }
}

eel.expose(updateMenuContest)


function lol(){
    window.resizeTo(300, 300);
    eel.load_menu_contest()
}


self.onload = lol
