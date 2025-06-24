import ollama

response = ollama.generate(
    model="deepseek-r1:1.5b",
    prompt="How far is earth from the moon"
)

print(response["response"])