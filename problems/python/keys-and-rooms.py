class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        is_open = [0 for i in range(len(rooms))]
        def go(room):
            is_open[room] = True
            for new_room in rooms[room]:
                if not is_open[new_room]:
                    go(new_room)
        go(0)
        return not(False in is_open)