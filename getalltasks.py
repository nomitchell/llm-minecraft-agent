import minedojo

print(minedojo.tasks.ALL_PROGRAMMATIC_TASK_IDS)

task_prompt, task_guidance = minedojo.tasks.ALL_PROGRAMMATIC_TASK_INSTRUCTIONS["harvest_milk"]

print(task_prompt)

print(task_guidance)