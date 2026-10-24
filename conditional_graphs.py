from typing import TypedDict
from langgraph.graph import StateGraph,START , END 



class AgentState(TypedDict):
    name:str
    age:int
    field:str
    result:str


def It_departement_State(state:AgentState) -> AgentState:
    """welcoming to IT departement"""
    state["result"] = state["name"] + " welcoming to it departement"
    return state

def gestion_departement_State(state:AgentState) -> str :
    """welcoming to gestion departement"""
    state["result"] =  "welcoming to gestion departement " + state["name"] 
    return state 

def decide_greeting(state:AgentState) -> str :
    if state["field"] == "it" :
        return "It_departement_State"
    elif state["field"] == "gestion" :
        return "gestion_departement_State"
        
graph = StateGraph(AgentState)

graph.add_node("It_departement_State",It_departement_State)
graph.add_node("gestion_departement_State",gestion_departement_State)
graph.add_node("router",lambda state:state)

graph.add_edge(START,"router")
graph.add_conditional_edges(
    'router',
    decide_greeting,
    {
        "It_departement_State" : "It_departement_State",
        "gestion_departement_State" : "gestion_departement_State",
    }
)


graph.add_edge("It_departement_State",END)
graph.add_edge("gestion_departement_State",END)

bot = graph.compile()

input_data = {
    "name": "mohamed",
    "field": "gestion",
    "age": 20,

}


response = bot.invoke(input_data)

print(response['result'])



