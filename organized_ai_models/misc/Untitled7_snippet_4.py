from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
import os

# Define model names
brain_model_name = "EleutherAI/gpt-neox-20b"       # Main "brain" for high-level reasoning
support_model_name = "EleutherAI/gpt-j-6B"         # Support model for task-specific generation
directive_model_name = "google/flan-t5-xxl"        # Instruction-following model for structured directives

# Load Tokenizers and Models
# Brain Model: GPT-NeoX-20B
brain_tokenizer = AutoTokenizer.from_pretrained(brain_model_name)
brain_model = AutoModelForCausalLM.from_pretrained(brain_model_name)
brain_pipeline = pipeline("text-generation", model=brain_model, tokenizer=brain_tokenizer)

# Support Model: GPT-J-6B
support_tokenizer = AutoTokenizer.from_pretrained(support_model_name)
support_model = AutoModelForCausalLM.from_pretrained(support_model_name)
support_pipeline = pipeline("text-generation", model=support_model, tokenizer=support_tokenizer)

# Directive Model: FLAN-T5-XXL
directive_tokenizer = AutoTokenizer.from_pretrained(directive_model_name)
directive_model = AutoModelForSeq2SeqLM.from_pretrained(directive_model_name)
directive_pipeline = pipeline("text2text-generation", model=directive_model, tokenizer=directive_tokenizer)

# Functions for generating responses from each model
def generate_brain_response(prompt, max_length=100):
    response = brain_pipeline(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]["generated_text"]

def generate_support_response(prompt, max_length=100):
    response = support_pipeline(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]["generated_text"]

def generate_directive_response(prompt, max_length=100):
    response = directive_pipeline(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]["generated_text"]

# Example Workflow: Collaborative Task Generation
def collaborative_task_generation(task_prompt):
    # Brain Model generates high-level instructions
    brain_directive = generate_brain_response(f"High-level directive for: {task_prompt}")

    # Support Model breaks down tasks into actionable steps
    support_steps = generate_support_response(f"Break down into steps: {brain_directive}")

    # Directive Model provides a structured instruction based on support model output
    final_instructions = generate_directive_response(f"Structured directive for steps: {support_steps}")

    return {
        "Brain Directive": brain_directive,
        "Support Steps": support_steps,
        "Final Instructions": final_instructions
    }

# Example task to demonstrate collaborative generation
task_prompt = "Set up an adaptive storytelling AI platform"
collaborative_response = collaborative_task_generation(task_prompt)

print("Collaborative Task Output:")
for key, value in collaborative_response.items():
    print(f"{key}:\n{value}\n")
