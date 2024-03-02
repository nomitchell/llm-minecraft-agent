from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"
# To use a different branch, change revision
# For example: revision="gptq-4bit-32g-actorder_True"   gptq-4bit-32g-actorder_True
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)
prompt = "Tell me about AI"
prompt_template=f'''<s>[INST] {prompt} [/INST]
'''

sys_prompt = "You are a helpful assistant, who always provide explanation. Think like you are answering to a five year old."
prompt = "give me step by step instructions to find a diamond in minecraft"

prefix = "<|im_start|>"
suffix = "<|im_end|>\n"
sys_format = prefix + "system\n" + sys_prompt + suffix
user_format = prefix + "user\n" + prompt + suffix
assistant_format = prefix + "assistant\n"
prompt_template = sys_format + user_format + assistant_format

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.1
)
print(pipe(prompt_template)[0]['generated_text'])
tok = tokenizer("prompt_template")
tokens = len(tok['input_ids'])
print(f"Number of tokens: {tokens}")

class model:
    def __init__(self):
        self.model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name_or_path,
            device_map="auto",
            trust_remote_code=False,
            revision="main"
        )
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            top_k=40,
            repetition_penalty=1.1
        )

        self.prefix = "<|im_start|>"
        self.suffix = "<|im_end|>\n"

    def formatPrompt(systemText, userText):
        sys_format = prefix + "system\n" + sys_prompt + suffix
        user_format = prefix + "user\n" + prompt + suffix
        prompt_template = sys_format + user_format 

        return prompt

    def decomposeGoal(self, objectName, objectQuantity, objectInfo):
        systemText = \
        '''SYSTEM:
        You are an assistant for the game Minecraft.
        I will give you some target object and some knowledge related to the object. Please write the
        obtaining of the object as a goal in the standard form.
        The standard form of the goal is as follows:
        {
        "object": "the name of the target object",
        "count": "the target quantity",
        "material": "the materials required for this goal, a dictionary in the form {material_name:
        material_quantity}. If no material is required, set it to None",
        "tool": "the tool used for this goal. If multiple tools can be used for this goal, only write
        the most basic one. If no tool is required, set it to None",
        "info": "the knowledge related to this goal"
        }
        The information I will give you:
        Target object: the name and the quantity of the target object
        Knowledge: some knowledge related to the object.
        Requirements:
        1. You must generate the goal based on the provided knowledge instead of purely depending
        on your own knowledge.
        2. The "info" should be as compact as possible, at most 3 sentences. The knowledge I give you
        may be raw texts from Wiki documents. Please extract and summarize important information
        instead of directly copying all the texts.
        Goal Example:
        { "object": "iron_ore",
        "count": 1,
        "material": None,
        "tool": "stone_pickaxe",
        "info": "iron ore is obtained by mining iron ore. iron ore is most found in level 53. iron ore
        can only be mined with a stone pickaxe or better; using a wooden or gold pickaxe will yield
        nothing."
        }
        {
        "object": "wooden_pickaxe",
        "count": 1,
        "material": {"planks": 3, "stick": 2},
        "tool": "crafting_table",
        "info": "wooden pickaxe can be crafted with 3 planks and 2 stick as the material and
        crafting table as the tool."
        }''' 

        userText = \
        f'''Target object: {objectQuantity} {objectName}
        Information: {objectInfo}
        '''

        prompt = self.formatPrompt(systemText, userText)

        response = pipe(prompt)[0]['generated_text']

        return response


