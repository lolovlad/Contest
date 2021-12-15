

window.onmouseout = ()=>{window.onbeforeunload = ConfirmLeave};
window.onmouseover = ()=>{window.onbeforeunload = null;}

function ConfirmLeave() {
    window.close()
}

document.addEventListener('DOMContentLoaded', () => {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});

function lol(){
    window.resizeTo(900, 600); 
}

self.onload = lol

var prevKey="";
document.onkeydown = function (e) {            
    if (e.key=="F5") {
        window.onbeforeunload = ConfirmLeave;
    }
    else if (e.key.toUpperCase() == "W" && prevKey == "CONTROL") {                
        window.onbeforeunload = ConfirmLeave;   
    }
    else if (e.key.toUpperCase() == "R" && prevKey == "CONTROL") {
        window.onbeforeunload = ConfirmLeave;
    }
    else if (e.key.toUpperCase() == "F4" && (prevKey == "ALT" || prevKey == "CONTROL")) {
        window.onbeforeunload = ConfirmLeave;
    }
    prevKey = e.key.toUpperCase();
}