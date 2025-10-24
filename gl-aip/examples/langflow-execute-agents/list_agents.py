from glaip_sdk import Client

client = Client()

# Maybe try to find Langflow_Interview_Availability_Checker Agent ID in AIP Demo
for agent in client.agents.list_agents():
    print(agent.id, agent.name)
