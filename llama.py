import transformers
import torch

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
# First, define a tool
def get_current_temperature(location: str) -> float:
    """
    Get the current temperature at a location.
    
    Args:
        location: The location to get the temperature for, in the format "City, Country"
    Returns:
        The current temperature at the specified location in the specified units, as a float.
    """
    return 22.  # A real function should probably actually get the temperature!

# Next, create a chat and apply the chat template
messages = [
  {"role": "system", "content": "You are a bot that responds to weather queries."},
  {"role": "user", "content": "Hey, what's the temperature in Paris right now?"}
]

inputs = tokenizer.apply_chat_template(messages, tools=[get_current_temperature], add_generation_prompt=True)
