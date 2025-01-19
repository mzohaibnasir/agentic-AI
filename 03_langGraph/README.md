langGraph is a library for building steateful, multi-actor applications with LLMs, used to create agennt and multi-agent workflows.


Compared to other LLM frameworks it offers,
1. Cycles
2. controllability
3. persistence


It allows you to define flows that have cycles, differetating it from DAG-based solutions










1. state management: at what state, what what work it should do

Agent coordination: agent to might need agent'1 outputs

Srpoose our chatbot is using 3 agents
1. agent1(google search)
2. agent2(wiki search)
3. agent2(vectorDG search)



2. Flexibility
developershave the flexibility to define their own agent logic and communication protocols

3. Scalability

we can build large scale multi agent applications because it can handle high volume of interactions. Interaction can be between agents and complex workflows.

4. Fault tolerance
handle errors and still keeps the application running