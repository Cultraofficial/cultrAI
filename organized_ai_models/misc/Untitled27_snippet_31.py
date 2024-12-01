import schedule
import time

def generate_task():
    prompt = "Describe how AI can automatically build the front-end of an interactive platform."
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=100, pad_token_id=tokenizer.pad_token_id)
    generated_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated Output:")
    print(generated_output)
    # Save to file for tracking
    with open("/content/drive/My Drive/CultrA.I. Files/generated_output.txt", "a") as file:
        file.write(generated_output + "\n")

# Schedule the task to run every hour
schedule.every(1).hours.do(generate_task)

print("Starting the scheduler...")
while True:
    schedule.run_pending()
    time.sleep(1)
