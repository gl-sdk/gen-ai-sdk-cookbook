from glaip_sdk import Client

client = Client()

# Maybe try to find Langflow_Interview_Availability_Checker Agent ID in AIP Demo
agent_id = "your-agent-id-here"

agent = client.agents.get_agent_by_id(agent_id)
print(agent.agent_config)

prompt = "your-prompt-here"
# Prompt example for Langflow_Interview_Availability_Checker : 
# I have a meeting at 13.30 until 14.00 Jakarta Time Zone, Check my availability to attend an interview today at 13.00 until 21.00 Jakarta Time Zone
response = client.agents.run_agent(agent_id, prompt)
print(response)
