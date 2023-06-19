import sys

input = sys.stdin.readline


# 미세먼지 확산
def spread():
    room_cpy = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if room_org[r][c] > 0:
                count = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (
                        0 <= nr < R
                        and 0 <= nc < C
                        and room_org[r + dr[i]][c + dc[i]] != -1
                    ):
                        count += 1
                        room_cpy[nr][nc] += room_org[r][c] // 5
                room_org[r][c] -= (room_org[r][c] // 5) * count

    for r in range(R):
        for c in range(C):
            if room_org[r][c] != -1:
                room_org[r][c] += room_cpy[r][c]


# 공기청정기 위쪽 이동
def air_up():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    direct = 0
    before = 0
    r, c = air, 1
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == air and c == 0:
            break
        if not (0 <= nr < R and 0 <= nc < C):
            direct += 1
            continue
        room_org[r][c], before = before, room_org[r][c]
        r = nr
        c = nc


# 공기청정기 아래쪽 이동
def air_down():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direct = 0
    before = 0
    r, c = air + 1, 1
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == air + 1 and c == 0:
            break
        if not (0 <= nr < R and 0 <= nc < C):
            direct += 1
            continue
        room_org[r][c], before = before, room_org[r][c]
        r = nr
        c = nc


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C, T = map(int, input().split())

room_org = []
for _ in range(R):
    room_org.append(list(map(int, input().rstrip().split())))

for r in range(R):
    if room_org[r][0] == -1:
        air = r
        break

for _ in range(T):
    spread()
    air_up()
    air_down()

print(sum([sum(x) for x in room_org]) + 2)