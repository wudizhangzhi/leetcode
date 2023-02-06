class Solution:
    mem = {
        0: 0,
        1: 1,
    }

    def fib(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        a1 = self.fib(n - 1)
        self.mem[n - 1] = a1
        a2 = self.fib(n - 2)
        self.mem[n - 2] = a2
        return a1 + a2


if __name__ == "__main__":
    print(Solution().fib(4) == 3)
