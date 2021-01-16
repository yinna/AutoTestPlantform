from datetime import timedelta,datetime

class timeUtils():
    def __init__(self):
        pass

    def currentDay(self):
        day = datetime.now().strftime('%Y-%m-%d')
        print(day)
        return day

    def currentDayString(self):
        day = datetime.timetz("utc").isoformat()
        print(day)
        return day

    def currentDayUTC(self):
        dayUTC_old = datetime.utcnow().isoformat()
        dayUTC_new = str(dayUTC_old)[:-3] + "T"
        print("UTC时间："+dayUTC_new)
        return dayUTC_new

    def dateAfterSomeDay(self,time_interval):
        start_date = datetime.strptime(timeUtils().currentDay(), '%Y-%m-%d')
        now_date = timedelta (days=time_interval)
        a = start_date + now_date
        newDay = a.strftime('%Y-%m-%d')
        print(newDay)
        return newDay

if __name__ == "__main__":
    timeUtils().currentDayUTC()