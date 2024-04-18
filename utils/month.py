from datetime import datetime

def next_month(month):
    match month:
        case 1:
            return "февраля"
        case 2:
            return "марта"
        case 3:
            return "фпреля"
        case 4:
            return "мая"
        case 5:
            return "июня"
        case 6:
            return "июля"
        case 7:
            return "августа"
        case 8:
            return "сентября"
        case 9:
            return "октября"
        case 10:
            return "ноября"
        case 11:
            return "декабря"
        case 12:
            return "января"
        

def get_next_month():
    return next_month(datetime.now().month)
