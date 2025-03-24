class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        day = 1
        meeting_pointer = 0
        count_day = 0
        while day <= days:
            if meeting_pointer >= len(meetings):
                break
            # within the range
            if meetings[meeting_pointer][0] <= day <= meetings[meeting_pointer][1]:
                count_day += meetings[meeting_pointer][1] - day + 1
                day = meetings[meeting_pointer][1] + 1
                print(day, count_day)
            elif meetings[meeting_pointer][0] > day:
                day += 1
            elif meetings[meeting_pointer][1] < day :
                meeting_pointer += 1
        print(count_day)
        return days - count_day

