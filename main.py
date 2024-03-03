import minedojo
from menu import Menu
from model import Model

task_id_options = [i[8:].replace("_", " ") for i in minedojo.tasks.ALL_PROGRAMMATIC_TASK_IDS if "harvest_1" in i or "harvest_8" in i]

with open("items.txt", 'r') as f:
    items = f.readlines()
    items = [i.replace("\\n", "") for i in items]

task_id = "harvest_" + Menu.openMenu(task_id_options).replace(" ", "_")

model = Model()

print(model.decomposeGoal(task_id.replace("-", " "), minedojo.tasks.ALL_PROGRAMMATIC_TASK_INSTRUCTIONS[task_id]))

env = minedojo.make(task_id="Playthrough", image_size=(160, 256))

#print(mcwiki.retrieveKnowledge("https://minecraft.fandom.com/wiki/Diamond"))




while True:
    obs = env.reset()  # Reset the environment
    action = env.action_space.no_op()
    action[0] = 1
    next_obs, reward, done, info = env.step(action)  # Take an action and observe the next state
    print(info)


'''


ask for goal done

create environment done

load knowledge to do

load model

call decomposer on goal, knowledge, and format, save goal tree

construct action interface

load reference to text memory storage, store goal object and reference plan

while loop
    
    construct feedback from previous action, inventory, environment, observations

    give planner goal tree, memory, structured action list, feedback, returns a ordered list of actions

    give action to agent

    get observation from environment afterward

if success update memory
    


'''