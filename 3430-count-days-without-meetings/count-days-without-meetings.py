class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()
        merged_meetings = []
        prev = meetings[0]

        # merge intervals
        for i in range(1, len(meetings)):
            if meetings[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], meetings[i][1])]
            else:
                merged_meetings.append(prev)
                prev = meetings[i]
        merged_meetings.append(prev)

        free_days = merged_meetings[0][0] - 1  # Days before first meeting
        for i in range(1, len(merged_meetings)):
            free_days += merged_meetings[i][0] - merged_meetings[i - 1][1] - 1
        free_days += days - merged_meetings[-1][1]  # Days after last meeting

        return free_days
    