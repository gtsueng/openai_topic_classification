from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI  
from langchain.callbacks import get_openai_callback

def get_content_from_file(file_path):
    """Read and return content from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file: '{file_path}'")
    except Exception as e:
        raise e

# Path to the API key and prompt text files
api_key_file_path = "key.txt"
prompt_file_path = "prompt.txt"

# Read API key and prompt from files
api_key = get_content_from_file(api_key_file_path)
prompt = get_content_from_file(prompt_file_path)

llm = OpenAI(openai_api_key = api_key)
with get_openai_callback() as cb:
    result = llm(prompt)
    print(result)
    print(cb)
