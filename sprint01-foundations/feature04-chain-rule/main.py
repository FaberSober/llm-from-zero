"""Feature 04: calculate a parameter gradient with the chain rule."""


def linear_prediction(weight: float, input_value: float) -> float:
    """Return the output of a one-parameter linear function."""
    return weight * input_value


def squared_loss(prediction: float, target: float) -> float:
    """Return the squared error for one prediction."""
    error = prediction - target
    return error * error


def loss_for_weight(weight: float, input_value: float, target: float) -> float:
    """Return the loss after changing only the weight."""
    prediction = linear_prediction(weight, input_value)
    return squared_loss(prediction, target)


def chain_rule_gradient(
    weight: float, input_value: float, target: float
) -> float:
    """Return d(loss) / d(weight) by multiplying local derivatives."""
    prediction = linear_prediction(weight, input_value)
    d_loss_d_prediction = 2 * (prediction - target)
    d_prediction_d_weight = input_value
    return d_loss_d_prediction * d_prediction_d_weight


def finite_difference_gradient(
    weight: float, input_value: float, target: float, epsilon: float = 1e-5
) -> float:
    """Estimate d(loss) / d(weight) with a small change in the weight."""
    loss_plus = loss_for_weight(weight + epsilon, input_value, target)
    loss_minus = loss_for_weight(weight - epsilon, input_value, target)
    return (loss_plus - loss_minus) / (2 * epsilon)


def main() -> None:
    weight = 1.5
    input_value = 2.0
    target = 5.0
    step = 0.1

    prediction = linear_prediction(weight, input_value)
    loss = squared_loss(prediction, target)
    d_loss_d_prediction = 2 * (prediction - target)
    d_prediction_d_weight = input_value
    gradient = chain_rule_gradient(weight, input_value, target)
    approximate_gradient = finite_difference_gradient(weight, input_value, target)

    # A finite-difference estimate provides a runnable check of the chain rule.
    assert abs(gradient - approximate_gradient) < 1e-6

    print(f"weight = {weight}")
    print(f"input = {input_value}")
    print(f"prediction = {prediction}")
    print(f"target = {target}")
    print(f"loss = {loss:.2f}")
    print(f"d_loss_d_prediction = {d_loss_d_prediction:.2f}")
    print(f"d_prediction_d_weight = {d_prediction_d_weight:.2f}")
    print(f"gradient_wrt_weight = {gradient:.2f}")
    print(f"finite_difference_gradient = {approximate_gradient:.6f}")
    print(
        "loss_if_weight_plus_0.1 = "
        f"{loss_for_weight(weight + step, input_value, target):.2f}"
    )
    print(
        "loss_if_weight_minus_0.1 = "
        f"{loss_for_weight(weight - step, input_value, target):.2f}"
    )


if __name__ == "__main__":
    main()
