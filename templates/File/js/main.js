const menuContest = document.getElementById("menu_contest")


function updateMenuContest(contests){
    menuContest.innerHTML = ""

    for(let i=0; i < contests.contests.length; i++){
        menuContest.innerHTML += `<div class="col s12 m4">
                                    <div class="card blue-grey darken-1">
                                        <a href="${contests.contests[i].id}">
                                            <div class="card-content white-text">
                                                <span class="card-title center-align">${contests.contests[i].name_contest}</span>
                                            </div>
                                        </a>
                                    </div>
                                </div>`
    }
    //selectRowContest()
}

eel.expose(updateMenuContest)


function lol(){
    window.resizeTo(300, 300);
    eel.load_menu_contest()
}


self.onload = lol
