training_script = """
import argparse

def main(training_steps, learning_rate):
    print(f"Training for {training_steps} steps with learning rate {learning_rate}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--training_steps", type=int, default=1000)
    parser.add_argument("--learning_rate", type=float, default=0.001)
    args = parser.parse_args()
    main(args.training_steps, args.learning_rate)
"""

# Write the training script to file
with open("main_script.py", "w") as file:
    file.write(training_script)
