
target = 1000000
divisor_sums = [0 for _ in range(target + 1)]
#past_in_prev_chain = [False for _ in range(target + 1)]
long_chain = [0, 0]


for index in range(target + 1):
    if index == 0:
        continue
    for i in range(index * 2, target + 1, index):
        divisor_sums[i] += index


for current_value, next_value in enumerate(divisor_sums):

    if current_value < 2:# or past_in_prev_chain[current_value]:
        continue 

    chain = []
    flag = False

    while current_value not in chain and current_value <= target:
        chain.append(current_value)

        try:
            current_value, next_value = next_value, divisor_sums[next_value]
        except IndexError:
            current_value, next_value = next_value, 0
            flag = True

    #for i in chain:
    #    past_in_prev_chain[i] = True

    if (not flag) and long_chain[0] < len(chain) - chain.index(current_value):
        long_chain = [len(chain), min(chain[chain.index(current_value):])]


print(long_chain)