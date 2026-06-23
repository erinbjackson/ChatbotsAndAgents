from basic_llm import LLM

with open("data/gardenInstruct.md", "r", encoding="utf-8") as file: # obtain proprietary docs
   documentation = file.read()

assistant_message = "Hello! I am Garden Master of Gardenville! How can I help?" # new intro message
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = LLM().generate(
        messages_prompt=history,
        system_prompt=f"""You are a garden master in the land of Gardenville. Your job is to give garden instructions based solely on the following documentation: {documentation}"""  # new system prompt
    )

    llm_response_text = f"\nAssistant: {response["text"]}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response["text"]},
        {"role": "user", "content": user_input}
    ]

print("\n\n****HISTORY****")
print(history)
