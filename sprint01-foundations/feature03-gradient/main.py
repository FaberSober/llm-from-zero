"""Feature 03: use a gradient to describe how loss changes."""


def mean_squared_error(prediction: float, target: float) -> float:
    """Return the squared error for one prediction."""
    error = prediction - target
    return error * error


def gradient_wrt_prediction(prediction: float, target: float) -> float:
    """Return d(loss) / d(prediction) for the squared error."""
    return 2 * (prediction - target)


def finite_difference_gradient(
    prediction: float, target: float, epsilon: float = 1e-5
) -> float:
    """Estimate the gradient by measuring a small change in both directions."""
    loss_plus = mean_squared_error(prediction + epsilon, target)
    loss_minus = mean_squared_error(prediction - epsilon, target)
    return (loss_plus - loss_minus) / (2 * epsilon)


def main() -> None:
    prediction = 1.5
    target = 2.0
    step = 0.1

    loss = mean_squared_error(prediction, target)
    gradient = gradient_wrt_prediction(prediction, target)
    approximate_gradient = finite_difference_gradient(prediction, target)

    # A finite-difference estimate provides a small, runnable check of the formula.
    assert abs(gradient - approximate_gradient) < 1e-6

    print(f"prediction = {prediction}")
    print(f"target = {target}")
    print(f"loss = {loss:.2f}")
    print(f"gradient = {gradient:.2f}")
    print(f"finite_difference_gradient = {approximate_gradient:.6f}")
    print(
        "loss_if_prediction_plus_0.1 = "
        f"{mean_squared_error(prediction + step, target):.2f}"
    )
    print(
        "loss_if_prediction_minus_0.1 = "
        f"{mean_squared_error(prediction - step, target):.2f}"
    )


if __name__ == "__main__":
    main()
