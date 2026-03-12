from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_llm(model_path: str):
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        dtype="auto",
        device_map="cuda:0",
    )

    gen_pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        do_sample=True,
        repetition_penalty=1.0,
        return_full_text=False,
    )

    llm = HuggingFacePipeline(pipeline=gen_pipe)
    return ChatHuggingFace(llm=llm)

# def load_llm(model_id, model_path):
#    llm = HuggingFacePipeline.from_model_id(
#        model_id=model_id,
#        task="text-generation",
#        model_kwargs={
#            "cache_dir": model_path,
#            "dtype": "auto",
#            "device_map": "cuda:0"
#        },
#        pipeline_kwargs=dict(
#            max_new_tokens=512,
#            do_sample=False,
#            repetition_penalty=1.0,
#            return_full_text=False,
#        ),
#    )
#    return ChatHuggingFace(llm=llm)


def load_embeddings(model_id:str, cache_dir:str):
    return HuggingFaceEmbeddings(
        model_name= model_id,
        cache_folder= cache_dir,
        model_kwargs={"device": "cuda:0", 
                      "local_files_only": True},
        encode_kwargs={"normalize_embeddings": True},
    )


def load_docs(path="data"):
    loader = DirectoryLoader(
        path=path,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True
    )
    return loader.load()

def load_eval_model():
    # OPENAI_IP = "104.18.6.162"
    # SNI_HOST = "api.openai.com"

    llm = ChatOpenAI(model="gpt-4o-mini",
                     temperature=0,
                     timeout=36000,
                     # base_url=f"https://{OPENAI_IP}/v1",
                     # default_headers={"Host": SNI_HOST},
                     )
    evaluator_llm = LangchainLLMWrapper(llm)

    return evaluator_llm

if __name__ == "__main__":
    llm = load_eval_model()
    print("yes")