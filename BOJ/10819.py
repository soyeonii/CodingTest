import bisect

n = int(input())
n_card = sorted(list(map(int, input().split())))
m = int(input())
m_card = list(map(int, input().split()))

for card in m_card:
    print(bisect.bisect_right(n_card, card) - bisect.bisect_left(n_card, card), end=' ')
