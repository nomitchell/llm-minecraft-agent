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
prompt = "please give me step by step instructions to find a diamond in minecraft"

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