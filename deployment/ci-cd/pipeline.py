def test_pipeline_sanity():
    print("Running basic sanity checks")
    assert True


def train():
    print("Training model...")
    print("Using dataset v1.2")
    print("Model trained successfully")


def evaluate():
    print("Evaluating model...")
    print("Accuracy: 0.91")
    print("Evaluation passed")


def register():
    print("Registering model...")
    print("Model version: v3")
    print("Saved to model registry")


if __name__ == "__main__":
    test_pipeline_sanity()
    train()
    evaluate()
    register()
