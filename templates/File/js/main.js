function lol(){
    window.resizeTo(300, 300); 
}

document.addEventListener('DOMContentLoaded', () => {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});

function open_new_windwo()
{
        eel.open_posl()
}

document.getElementById("posl").onclick = open_new_windwo

self.onload = lol
