function updateTitle(title){
    console.log(title)
    const titleElem = document.getElementsByTagName("title")
    if(titleElem.length > 0){
        titleElem[0].innerHTML = title
    }else{
        const titleElem = document.createElement("title")
        titleElem.innerHTML = title
        const header = document.getElementsByTagName("head")
        header[0].appendChild(titleElem)
    }
}

document.addEventListener('DOMContentLoaded', () => {
    eel.title_window()((title)=>{
        updateTitle(title)
    })
})