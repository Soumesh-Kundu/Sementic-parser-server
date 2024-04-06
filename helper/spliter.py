from llama_index.core.node_parser import (
    SemanticSplitterNodeParser,
)
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
from functools import reduce
import os
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")
embed_model = OpenAIEmbedding()
splitter = SemanticSplitterNodeParser(
buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
)
def spliter(data:list[str])->list[str]:
    finalData=reduce(lambda acc,item:acc+item,data)
    documents:Document=Document(text=finalData)
    nodes=splitter.get_nodes_from_documents([documents])
    return list(map(lambda x:x.get_content(),nodes))