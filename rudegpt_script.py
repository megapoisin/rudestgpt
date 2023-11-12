from openai import OpenAI
client = OpenAI(api_key="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")
my_assistant = client.beta.assistants.retrieve("asst_n2YNcMBAYvP5Gw56jXv5U1Q3")
print(my_assistant)
