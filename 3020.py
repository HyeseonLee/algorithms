import sys

n,h = map(int, sys.stdin.readline().strip().split())

up = [0] * (h+1) # 1부터 채워짐
down = [0] * (h+1)

for n_step in range(n):
    obs_h = int(sys.stdin.readline().strip())

    if n_step % 2 == 0: #석순
        up[obs_h] += 1
    else:
        down[obs_h] += 1

for i in range(h-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]

min_obs_value = float("inf")
count = 0

for h_step in range(1,h+1):
    hit = up[h_step] + down[h-h_step+1]
    if hit<min_obs_value:
        min_obs_value = hit
        count = 1
    elif hit == min_obs_value:
        count += 1

print(min_obs_value, count)