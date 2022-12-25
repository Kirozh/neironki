import numpy as np


def act(x):
    return 1 if (x >= 0.5) else 0


def go(house: int, rock: int, attr: int):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])
    weight2 = np.array([-1, 1])

    sum_hidden = np.dot(weight1, x)
    print("sum in hidden sloi = " + str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("sum in hidden sloi = " + str(out_hidden))
    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Itogo: " + str(y))
    return y


def main(house=0, rock=1, attr=1):
    if go(house, rock, attr) >= 0.5:
        print("I like you")
    else:
        print("Call me later")


if __name__ == "__main__":
    main()
