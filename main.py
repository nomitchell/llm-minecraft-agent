import minedojo
from Menu import Menu

task_id = Menu.openMenu(minedojo.tasks.ALL_PROGRAMMATIC_TASK_IDS)

env = minedojo.make(task_id=task_id, image_size=(160, 256))

#print(mcwiki.retrieveKnowledge("https://minecraft.fandom.com/wiki/Diamond"))




while True:
    obs = env.reset()  # Reset the environment
    action = env.action_space.no_op()
    action[0] = 1
    next_obs, reward, done, info = env.step(action)  # Take an action and observe the next state
    print(info)


'''


ask for goal

create environment

load knowledge

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