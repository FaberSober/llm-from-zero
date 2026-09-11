"""Feature 05: manually backpropagate through a small computation graph."""


def forward(
    weight: float, input_value: float, bias: float, target: float
) -> tuple[float, float, float, float]:
    """Run the forward pass and return the saved intermediate values."""
    a = weight * input_value
    b = a + bias
    prediction = b + a  # a reaches the prediction through two paths.
    error = prediction - target
    loss = error * error
    return a, b, prediction, loss


def backpropagate(
    weight: float, input_value: float, bias: float, target: float
) -> dict[str, float]:
    """Run a reverse pass and add both gradient contributions for ``a``."""
    a, b, prediction, loss = forward(weight, input_value, bias, target)

    d_loss_d_prediction = 2 * (prediction - target)

    # prediction = b + a
    d_loss_d_b = d_loss_d_prediction * 1.0
    d_loss_d_a_direct = d_loss_d_prediction * 1.0

    # b = a + bias; this is the second path from a to the loss.
    d_loss_d_a_through_b = d_loss_d_b * 1.0
    d_loss_d_a = d_loss_d_a_direct + d_loss_d_a_through_b
    d_loss_d_bias = d_loss_d_b * 1.0

    # a = weight * input
    d_loss_d_weight = d_loss_d_a * input_value

    return {
        "a": a,
        "b": b,
        "prediction": prediction,
        "loss": loss,
        "d_loss_d_prediction": d_loss_d_prediction,
        "d_loss_d_b": d_loss_d_b,
        "d_loss_d_a_direct": d_loss_d_a_direct,
        "d_loss_d_a_through_b": d_loss_d_a_through_b,
        "gradient_wrt_a": d_loss_d_a,
        "gradient_wrt_weight": d_loss_d_weight,
        "gradient_wrt_bias": d_loss_d_bias,
    }


def loss_for_parameters(
    weight: float, input_value: float, bias: float, target: float
) -> float:
    """Return the loss for a given pair of parameters."""
    return forward(weight, input_value, bias, target)[3]


def finite_difference_weight_gradient(
    weight: float, input_value: float, bias: float, target: float, epsilon: float = 1e-5
) -> float:
    """Estimate d(loss) / d(weight) with a small change in the weight."""
    loss_plus = loss_for_parameters(weight + epsilon, input_value, bias, target)
    loss_minus = loss_for_parameters(weight - epsilon, input_value, bias, target)
    return (loss_plus - loss_minus) / (2 * epsilon)


def finite_difference_bias_gradient(
    weight: float, input_value: float, bias: float, target: float, epsilon: float = 1e-5
) -> float:
    """Estimate d(loss) / d(bias) with a small change in the bias."""
    loss_plus = loss_for_parameters(weight, input_value, bias + epsilon, target)
    loss_minus = loss_for_parameters(weight, input_value, bias - epsilon, target)
    return (loss_plus - loss_minus) / (2 * epsilon)


def main() -> None:
    weight = 1.5
    input_value = 2.0
    bias = 0.5
    target = 10.0

    values = backpropagate(weight, input_value, bias, target)
    weight_gradient = finite_difference_weight_gradient(
        weight, input_value, bias, target
    )
    bias_gradient = finite_difference_bias_gradient(
        weight, input_value, bias, target
    )

    # Finite differences provide a small, runnable check of the reverse pass.
    assert abs(values["gradient_wrt_weight"] - weight_gradient) < 1e-6
    assert abs(values["gradient_wrt_bias"] - bias_gradient) < 1e-6

    print(f"weight = {weight}")
    print(f"input = {input_value}")
    print(f"bias = {bias}")
    print(f"a = {values['a']:.1f}")
    print(f"b = {values['b']:.1f}")
    print(f"prediction = {values['prediction']:.1f}")
    print(f"target = {target}")
    print(f"loss = {values['loss']:.2f}")
    print(f"d_loss_d_prediction = {values['d_loss_d_prediction']:.2f}")
    print(f"d_loss_d_b = {values['d_loss_d_b']:.2f}")
    print(f"d_loss_d_a_direct = {values['d_loss_d_a_direct']:.2f}")
    print(f"d_loss_d_a_through_b = {values['d_loss_d_a_through_b']:.2f}")
    print(f"gradient_wrt_a = {values['gradient_wrt_a']:.2f}")
    print(f"gradient_wrt_weight = {values['gradient_wrt_weight']:.2f}")
    print(f"gradient_wrt_bias = {values['gradient_wrt_bias']:.2f}")
    print(f"finite_difference_weight_gradient = {weight_gradient:.6f}")
    print(f"finite_difference_bias_gradient = {bias_gradient:.6f}")


if __name__ == "__main__":
    main()
