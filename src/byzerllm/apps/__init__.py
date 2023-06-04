from dataclasses import dataclass

@dataclass
class ClientParams:
    owner:str="admin"
    llm_embedding_func: str = "chat" 
    llm_chat_func: str = "chat"  

@dataclass
class BuilderParams:
    batch_size:int = 0
    chunk_size:int=600
    chunk_overlap: int = 30
    local_path_prefix: str = "/tmp/byzer-llm-qa-model"

@dataclass
class QueryParams:    
    local_path_prefix: str = "/tmp/byzer-llm-qa-model" 