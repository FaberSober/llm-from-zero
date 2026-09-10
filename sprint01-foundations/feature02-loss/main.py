"""Feature 02: calculate mean squared error from scratch."""


def mean_squared_error(predictions, targets):
    """Return the average squared difference between predictions and targets."""
    if not predictions:
        raise ValueError("predictions and targets must not be empty")
    if len(predictions) != len(targets):
        raise ValueError("predictions and targets must have the same length")

    squared_errors = []
    for prediction, target in zip(predictions, targets):
        error = prediction - target
        squared_errors.append(error * error)

    return sum(squared_errors) / len(squared_errors)


if __name__ == "__main__":
    targets = [2.0, 2.0, 5.0]
    predictions = [1.5, 3.0, 4.0]
    closer_predictions = [1.9, 2.1, 4.9]

    errors = [prediction - target for prediction, target in zip(predictions, targets)]
    squared_errors = [error * error for error in errors]
    loss = mean_squared_error(predictions, targets)
    closer_loss = mean_squared_error(closer_predictions, targets)

    print(f"predictions = {predictions}")
    print(f"targets = {targets}")
    print(f"errors = {errors}")
    print(f"squared_errors = {squared_errors}")
    print(f"mse_loss = {loss:.2f}")
    print(f"closer_predictions = {closer_predictions}")
    print(f"closer_loss = {closer_loss:.2f}")
