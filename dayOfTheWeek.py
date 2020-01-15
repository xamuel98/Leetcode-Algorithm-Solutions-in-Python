class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_the_week = {
          0: "Friday",
          1: "Saturday",
          2: "Sunday",
          3: "Monday",
          4: "Tuesday",
          5: "Wednesday",
          6: "Thursday",
        }

        leap_count = 0
        for y in range(1971, year):
            if self.checkLeapYear(y):
                leap_count += 1  # Count extra days added on leap year

        total_days = year * 365 + leap_count + self.getMonth(month - 1, year) + day
        base_days = 1971 * 365 + self.getMonth(1 - 1, 1971) + 1
        # print(total_days, base_days)
        diff = total_days - base_days
        # print(diff % 7)
        
        return days_of_the_week[diff % 7]
        
    def checkLeapYear(self, year):
        if ((year % 400) == 0 or (year % 4 == 0 and year % 100 != 0)):
            return True
        else:
            return False

    def getMonth(self, month, year):
        months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
         }

        total_days = 0
        for mon in range(1, month + 1):
            if mon == 2 and self.checkLeapYear(year):
                total_days += 1

            total_days += months[mon]

        return total_days
