# Save response to Google Drive
output_file = "/content/drive/My Drive/CultrA.I. Files/ai_response.txt"
with open(output_file, "w") as f:
    f.write(tokenizer.decode(outputs[0], skip_special_tokens=True))
print(f"Response saved to: {output_file}")
