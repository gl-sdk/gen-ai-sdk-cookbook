from glaip_sdk import Client

client = Client()
agent = client.create_agent(
    name=f"hello-world-agent",
    instruction="You are a friendly AI assistant.",
)
agent.run("Hello! How are you today?")
agent.delete()
