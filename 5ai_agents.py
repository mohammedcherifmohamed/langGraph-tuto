from typing import TypedDict , List
from langgraph.graph import StateGraph , START , END
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

class AgentState(TypedDict) : 
    messages:List[HumanMessage]


def process(state:AgentState) -> AgentState:
    response =model.invoke(state['messages'])
    state['messages'].append(response)
    print("AI: ",response.content)
    print("\n")
    return state

graph = StateGraph(AgentState)
graph.add_node('process',process)

graph.add_edge(START,"process")
graph.add_edge("process",END)

bot = graph.compile()

response = bot.invoke({"messages": [HumanMessage(content="how are you")]})

print(response)

 