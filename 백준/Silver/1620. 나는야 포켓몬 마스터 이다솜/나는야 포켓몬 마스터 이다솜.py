import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_str = {}
pokemon_int = {}

for i in range(1, n+1):
    pokemon = input().rstrip()
    pokemon_str[pokemon] = i
    pokemon_int[i] = pokemon

for _ in range(m):
    Q = input().rstrip()
    if Q.isalpha():
        print(pokemon_str[Q])
    else:
        print(pokemon_int[int(Q)])