from re import X


def main():
    ans = []
    x = 0
    for i in range(0,10):
        f(i,ans,x)

    print(ans)
    print(x)

def f(n,an_array,a_value):
    an_array.append(n)
    a_value += 1

main()