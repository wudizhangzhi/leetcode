from typing import List
import random


def fastSort(l: List[int]) -> List[int]:
    def partition(nums, l, r):
        print(f"partition: {nums} {l} {r}")
        low = l
        while l < r:
            if nums[l] < nums[r]:
                print(f"{l} <-> {low}")
                nums[l], nums[low] = nums[low], nums[l]
                print(nums)
                low += 1
            l += 1
        print(f"{low} <-> {r}")
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def quick(arr: List[int], l: int, r: int):
        if l < r:
            pos = partition(arr, l, r)
            quick(arr, l, pos - 1)
            quick(arr, pos + 1, r)

    quick(l, 0, len(l) - 1)
    return l


if __name__ == "__main__":
    arr = [2, 1, 3]
    print(fastSort(arr))
    # for _ in range(100):
    #     arr = list([random.randint(1, 10) for _ in range(10)])
    #     print(arr)
    #     ans = sorted(arr)
    #     myAns = fastSort(arr)
    #     result = myAns == ans
    #     if not result:
    #         print(myAns)
    #         print(ans)
    #         print("=" * 100)
