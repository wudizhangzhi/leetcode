def pratice_22_1_3():
    """转置链表和矩阵"""

    def transfer_list():
        pass

    def transfer_matrix():
        pass

    pass


def bellman_ford(G: list, S: tuple):
    pass


def pratice_24_1_1():
    pass


def test():
    class Chan:
        def __init__(self, val, next=None) -> None:
            self.val = val
            self.next = next

    a = [
        Chan(1, next=Chan(2, next=Chan(3))),
        Chan(2, next=Chan(1, next=Chan(4, next=Chan(5)))),
        Chan(3, next=Chan(1, next=Chan(6, next=Chan(7)))),
        Chan(4, next=Chan(2)),
        Chan(5, next=Chan(2)),
        Chan(6, next=Chan(3)),
        Chan(7, next=Chan(3)),
    ]
    # V=7 E=12
    count = 0
    for u in a:
        while u:
            count += 1
            u = u.next
    print(count)


if __name__ == "__main__":
    test()
