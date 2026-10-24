from typing import TypedDict,Dict ,List
from langgraph.graph import StateGraph, START,END




class AgentState(TypedDict):
    name:str
    skills:List[str]
    age:str
    result:str


def first_node(state: AgentState) -> AgentState:
    """simple node that adds greeting message to the state"""
    state['result'] = "hello " + state["name"] + " Welcome to LangGraph"
    return state

def second_node(state: AgentState) -> AgentState:
    """simple node that adds greeting message to the state"""
    skills = ", ".join(state['skills'])
    state['result'] =  state["result"] + f"your skills are {skills}"
    return state

def third_node(state: AgentState) -> AgentState:
    """simple node that adds greeting message to the state"""
    state['result'] = state['result'] + "you are" + state["age"] + "years old"
    return state

graph= StateGraph(AgentState)
graph.add_node("first_node",first_node)
graph.add_node("second_node",second_node)
graph.add_node("third_node",third_node)

graph.add_edge(START,"first_node")
graph.add_edge("first_node","second_node")
graph.add_edge("second_node","third_node")

graph.add_edge("third_node",END)

bot=graph.compile()
# print(bot)
input_data = {
    "name" : "mohamed",
    "age" : "20" , 
    "skills" : ["python","LangGraph","LangChain"],
}
reponse = bot.invoke(input_data)

print(reponse)
