def function(input):
    n = input[0]
    ret = []
    flag = False
    visited = {}

    def dfs():
        if len(ret) == n and 1 in input[ret[-1]]:
            flag = True
            ret.append(1)

        if flag == True:
            return

        for i in range(1,n):
            if i not in visited:
                visited.add(i)
                ret.append(i)
                dfs()
                if flag:
                    return
                visited.remove(i)
                ret.remove(i)

    dfs()
    if flag:
        return ret
    else:
        print "No Solution"

def main():
    input = raw_input("")
    function(input)

if __name__ == "__main__":
    main()
