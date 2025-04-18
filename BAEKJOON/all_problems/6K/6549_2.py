# divide_and_conquer and binary_search
# trying
def divide_and_conquer(n, ns, lo, hi):
    if(lo > hi): return 0
    if(lo == hi): return ns[lo]

    mid = (lo+hi)//2
    l, r = mid, mid
    while((lo <= l) and (r <= hi)):
        if(((lo+1) <= l) and (ns[l-1] >= ns[mid])):
            l -= 1
        elif(((r+1) <= hi) and (ns[r+1] >= ns[mid])):
            r += 1
        else:
            break

    ans = max((r-l+1)*ns[mid],\
                divide_and_conquer(n, ns, lo, mid-1),\
                divide_and_conquer(n, ns, mid+1, hi))
    return ans

def solve():
    ns = list(map(int, input().split()))
    while ns[0] != 0:
        n, ns = ns[0], ns[1:]
        ans = divide_and_conquer(n, ns, 0, n-1)
        print(ans)
        ns = list(map(int, input().split()))

solve()