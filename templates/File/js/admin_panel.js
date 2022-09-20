const windowUser = document.getElementById("windowUser")
const windowContest = document.getElementById("windowContest")
const windowTeam = document.getElementById("windowTeam")

windowContest.addEventListener("click", ()=>{
    eel.open_window_contest()
})

windowUser.addEventListener("click", ()=>{
    eel.open_window_user()
})

windowTeam.addEventListener("click", ()=>{
    eel.open_window_team()
})


let datepickerStartInit

const datapickerRu = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок',
    months: [ 'Январь',
              'Февраль',
              'Март',
              'Апрель',
              'Май',
              'Июнь',
              'Июль',
              'Август',
              'Сентябрь',
              'Октябрь',
              'Ноябрь',
              'Декабрь'],

    monthsShort: ['Янв', 
                  'Фев', 
                  'Мар', 
                  'Апр', 
                  'Май', 
                  'Июн', 
                  'Июл', 
                  'Авг', 
                  'Сен', 
                  'Окт', 
                  'Ноя', 
                  'Дек'],
           
    weekdays: ['Понедельник',
               'Вторник',
               'Среда',
               'Четверг',
               'Пятница',
               'Суббота',
               'Воскресенье'],

    weekdaysShort: ['Вс',
                    'Пн',
                    'Вт',
                    'Ср',
                    'Чт',
                    'Пт',
                    'Сб',],  

    weekdaysAbbrev: ['В','П','В','С','Ч','П','С']
}

const timepickerRu = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок'
}

const tabContest = document.getElementById("tabContest")
const tabTask = document.getElementById("tabTask")
const tabTeam = document.getElementById("tabTeam")

const buttonAgree = document.getElementById("agreeButton")



let datapickerElementStart = NaN
let datapickerElementEnd = NaN

document.addEventListener('DOMContentLoaded', () => {
    window.resizeTo(1500, 1100)
    let element = document.querySelector('.tabs');
    let instance = M.Tabs.init(element);

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    
    initDatePiker()

});


function reverseObject(obj){
    const data = {}
    for(const [key, value] of Object.entries(obj)){
        data[value] = key
    }
    return data
}

function alert(message){
     M.toast({html: message})
}

function initDatePiker(){
    const datepickerStart = document.getElementById('datepickerStart');
    const datepickerStop = document.getElementById('datepickerStop');
    const timepickerStart = document.getElementById('timepickerStart');
    const timepickerStop = document.getElementById('timepickerStop');
    const dateNow = new Date()

    datapickerElementStart = M.Datepicker.init(datepickerStart, {i18n: datapickerRu, 
                                               onSelect(date){
                                                   appContest.dateStart = this.date
                                               },
                                               format: 'dd.mm.yyyy',
                                               minDate: dateNow,
                                               firstDay: 1})
    M.Timepicker.init(timepickerStart, {i18n: timepickerRu,
                                        twelveHour: false,
                                        onSelect(hours, min){
                                            appContest.dateStartNotStr.setHours(hours)
                                            appContest.dateStartNotStr.setMinutes(min)
                                            appContest.timeStart = `${hours}:${min}`
                                        },
                                        default: "00:00"})
    M.Timepicker.init(timepickerStop, {i18n: timepickerRu,
                                        twelveHour: false,
                                        onSelect(hours, min){
                                            appContest.dateEndNotStr.setHours(hours)
                                            appContest.dateEndNotStr.setMinutes(min)
                                            appContest.timeEnd = `${hours}:${min}`
                                        },
                                        default: "00:00"})
    datapickerElementEnd = M.Datepicker.init(datepickerStop, {i18n: datapickerRu,
                                                              onSelect(date){
                                                                   appContest.dateEnd = this.date
                                                              },
                                                              format: 'dd.mm.yyyy',
                                                              minDate: dateNow,
                                                              firstDay: 1})
}

function locationReplace(path){
    console.log(path)
    window.location.replace(`/${path}`);
}

eel.expose(locationReplace)
eel.expose(alert)