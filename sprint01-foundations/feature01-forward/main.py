"""Feature 01: the smallest forward computation."""


def forward(x, w, b):
    """Compute the output of one linear unit: y_hat = x · w + b."""
    weighted_sum = 0.0
    for x_i, w_i in zip(x, w):
        weighted_sum += x_i * w_i
    return weighted_sum + b


if __name__ == "__main__":
    x = [2.0, 3.0]
    w = [0.5, -1.0]
    b = 1.0

    y_hat = forward(x, w, b)
    print(f"x = {x}")
    print(f"w = {w}")
    print(f"b = {b}")
    print(f"y_hat = {y_hat}")
