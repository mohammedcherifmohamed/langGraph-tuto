from langgraph.graph import StateGraph , START , END 
from typing import TypedDict , List 
import random


class AgentState(TypedDict):
    name:str
    number:List[int]
    counter:int

def greeting_node(state:AgentState) -> AgentState :
    """greeting node which says hi to a person"""
    state['name']

def random_node(state:AgentState) -> AgentState : 
    state['number'].append(random.randint(0,10))
    state['counter'] += 1
    return state

def decision_node(state:AgentState) -> str : 
    """function to decide where to go """ 
    if state['counter'] < 5 :
        print(f"Enter Loop , {state["counter"]}")
        return 'loop'
    else : 
        print(f"Exit Loop , {state['counter']}")
        print(f"Exit Loop , {state['number']}")
        return 'exit'


graph= StateGraph(AgentState)
graph.add_node("greet",greeting_node)
graph.add_node("random",random_node)

graph.add_edge(START,"greet")
graph.add_edge("greet","random")

graph.add_conditional_edges(
    "random",
    decision_node,
    {
        "loop":"random",
        "exit" : END
    }
)

graph.add_edge("random",END)
bot = graph.compile()
input_data = {
    "name" : "mohamed",
    "number" : [],
    "counter" : 0
}
response = bot.invoke(input_data)