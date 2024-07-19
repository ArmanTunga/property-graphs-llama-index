import os

from llama_index.core import (
    SimpleDirectoryReader, PropertyGraphIndex,
    StorageContext, load_index_from_storage
)
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.core.indices.property_graph import (
    ImplicitPathExtractor,
    SimpleLLMPathExtractor,
    CypherTemplateRetriever,

)

from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.openai import OpenAIEmbedding

from app_settings import settings

# Set api keys
os.environ["OPENAI_API_KEY"] = settings.openai_api_key
os.environ["ANTHROPIC_API_KEY"] = settings.anthropic_api_key

# Initialize LLM and Embedding models
llm = Anthropic(model=settings.llm_model_name)
embed_model = OpenAIEmbedding(model=settings.embed_model_name)

# Load data into index
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader('data/paul_graham/').load_data()

    # Create a node parser
    node_parser = SemanticSplitterNodeParser(
        buffer_size=4, breakpoint_percentile_threshold=95, embed_model=embed_model
    )

    # Parse the documents into nodes
    nodes = node_parser.get_nodes_from_documents(documents)

    index = PropertyGraphIndex.from_documents(
        documents,
        # llm=llm,
        embed_model=embed_model,
        kg_extractors=[
            ImplicitPathExtractor(),  # Creates previous-next relation
            SimpleLLMPathExtractor(  # Creates more complex or semantic relationship
                llm=llm,
                num_workers=4,
                max_paths_per_chunk=10,
            ),
        ],
        show_progress=True,
    )
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./storage")
    )

index.property_graph_store.save_networkx_graph(name="./pg.html") # IF PACKAGE "pyvis" not installed, then it Raises ModuleNotFoundError: No module named 'pyvis'

# Retrieval
retriever = index.as_retriever(
    include_text=False,  # include source text, default True
    # sub_retrievers=[CypherTemplateRetriever,] # Also we can add sub retrievers
)

nodes = retriever.retrieve("What happened at Interleaf and Viaweb?")

for node in nodes:
    print(node.text)
"""
Interleaf -> Added -> Scripting language
Viaweb -> Demonstrated -> Web apps future
Viaweb -> Had -> 70 stores
Viaweb -> Had -> 500 stores
Dan giffin -> Worked for -> Viaweb
Interleaf -> Crushed by -> Moore's law
Interleaf -> Made -> Document software
Viaweb -> Charged -> $300 per month
Author -> Worked at -> Interleaf
Viaweb -> Charged -> $100 per month
Paulgraham.com -> Created using -> Viaweb
Viaweb -> Grew -> 7x per year
Interleaf -> Used -> Lisp dialect
Viaweb -> Had -> Code editor
Viaweb -> Named after -> Working via web
Yahoo -> Bought -> Viaweb
Viaweb -> Founded by -> Authors
Julian -> Received -> 10% of company
Work choice -> Impacts -> Attention allocation
Print era -> Had -> Narrow channel to readers
Rich draves -> Studied at -> Cmu
"""


# Query
query_engine = index.as_query_engine(
    include_text=True
)

response = query_engine.query("What happened at Interleaf and Viaweb?")

print(response.response)
"""
Interleaf was involved in developing document software and used a Lisp dialect.
It was ultimately crushed by Moore's Law.
On the other hand, Viaweb demonstrated the future of web apps, had a significant number of stores, charged varying amounts per month, and grew rapidly.
It also had a code editor and was named after working via the web. Viaweb was eventually bought by Yahoo.
"""
