import calendar, itertools
from utils import dayOfTheWeek

class CalendarManager:

    def weekly(self, month, year, week):
        '''Generate a weekly calendar
        
        Params:
            month (int)
            year (int)
            week (int)
        '''

        cal = calendar.Calendar()
        days = cal.itermonthdays4(year, month)
        result = ""

        try:
            end = (week*7) - 1
            start = end - 6

            for day in itertools.islice(days, start, end):
                result += "{} {}/{}/{} \n".format(dayOfTheWeek(day[3]), day[2], day[1], day[0])
            return result
        except Exception as e:
            return "Please, choose an existing year, month and week number \n {}".format(e)


    def montly(self, month, year, formatted = True):
        '''Generate a montly calendar
        
        Params:
            month (int)
            year (int)
            formatted (boolean) - Return a plain or formatted string
        '''

        try:
            if formatted:
                cal = calendar.TextCalendar()
                return cal.formatmonth(year,month)

            else:
                cal = calendar.Calendar()
                days = cal.itermonthdays4(year, month)
                result = ""

                for day in days:
                    result += "{} {}/{}/{} \n".format(dayOfTheWeek(day[3]), day[2], day[1], day[0])

                return result

        except Exception as e:
            return "Please, choose an existing year, month and week number \n{}".format(e)

    def yearly(self, year, formatted = True):
        '''Generate a montly calendar
        
        Params:
            month (int)
            year (int)
            formatted (boolean) - Return a plain or formatted string
        '''

        try:
            if formatted:
                cal = calendar.TextCalendar()
                return cal.formatyear(year)

            else:
                cal = calendar.Calendar()
                result = ""

                for month in range(1,13):
                    days = cal.itermonthdays4(year, month)
                    for day in days:
                        result += "{} {}/{}/{} \n".format(dayOfTheWeek(day[3]), day[2], day[1], day[0])

                return result

        except Exception as e:
            return "Please, choose an existing year, month and week number \n{}".format(e)