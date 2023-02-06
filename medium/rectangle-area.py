class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        xl = max(ax1, bx1)
        xr = min(ax2, bx2)
        dx = xr - xl

        yb = max(ay1, by1)
        yt = min(ay2, by2)
        dy = yt - yb
        common = 0
        if dx > 0 and dy > 0:
            common = dy * dx

        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)
        return a + b - common


if __name__ == "__main__":
    print(
        Solution().computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=3, by1=3, bx2=4, by2=4)
    )
