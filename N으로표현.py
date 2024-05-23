import itertools

def solution(N, number):
    answer = 0
    dp = {i:set() for i in range(1,10)}
    # dp[1] = {N}
    # dp[2] = {int(str(N)*2), N+N, N-N, N*N, N//N}

    def check_ans(ans):
        if ans > 8: 
            return -1
        else:
            return ans
        
    for i in range(1,10):
        dp[i].add(int(str(N)*i)) # NNN 넣기
        if number in dp[i]:
            return check_ans(i)
        
        for n in range(1,i):
            # 1, 2, .. 3
            # 3,2,1 이어야 하니까
            # dp[n]이랑 dp[i-n]
            mix = list(itertools.product(dp[n], dp[i-n]))
            # mix에 있는 요소들을 +,-,*,// 해야해요
            for item in mix:
                dp[i].add(item[0]+item[1])
                dp[i].add(item[0]-item[1])
                dp[i].add(item[0]*item[1])
                if item[0] != 0 and item[1] != 0:
                    dp[i].add(item[0]//item[1])

        if number in dp[i]:
            answer = i
            return check_ans(answer)

    return -1

def solution2(N, number):
    dp = {i:set() for i in range(1,10)}

    def check_num(num1, num2, number, i):
        for res in [num1+num2, num1-num2, num1*num2]:
            if res == number:
                return True       
            else:  
                dp[i].add(res)

        if num1!=0 and num2!=0:
            if num1//num2 ==number:
                return True
            else:
                dp[i].add(num1//num2)
        
    def check_ans(ans):
        if ans > 8: 
            return -1
        else:
            return ans
        
    for i in range(1,10):
        dp[i].add(int(str(N)*i)) # NNN 넣기

        if number in dp[i]:
            return check_ans(i)
               
        for n in range(1,i):
            for item0 in dp[n]:
                for item1 in dp[i-n]:
                    if check_num(item0,item1,number,i)==True:
                        return check_ans(i)

    return -1

def solution3(N, number):
    dp = {i:set() for i in range(1,10)}

    def check_num(num1, num2, number, i):
        for res in [num1+num2, num1-num2, num1*num2]:
            if res == number:
                return True       
            else:  
                dp[i].add(res)

        if num1!=0 and num2!=0:
            if num1//num2 ==number:
                return True
            else:
                dp[i].add(num1//num2)
        
    def check_ans(ans):
        if ans > 8: 
            return -1
        else:
            return ans
        
    for i in range(1,10):
        dp[i].add(int(str(N)*i)) # NNN 넣기

        if number in dp[i]:
            return check_ans(i)
               
        for n in range(1,i):
            mix = itertools.product(dp[n], dp[i-n])
            for item in mix:
                if check_num(item[0], item[1], number, i) == True:
                    return check_ans(i)


    return -1

if __name__ == "__main__":
    print(solution(5,12)) # 4
    print(solution(2,11)) # 3
    print(solution(5,555)) # 3
    print(solution(5,5)) # 1
    print(solution(5,31168)) # -1