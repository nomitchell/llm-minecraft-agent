import minedojo

env = minedojo.make(task_id="harvest_milk", image_size=(160, 256))

while True:
    obs = env.reset()  # Reset the environment
    action = env.action_space.no_op()
    action[0] = 1
    next_obs, reward, done, info = env.step(action)  # Take an action and observe the next state
    print(info)