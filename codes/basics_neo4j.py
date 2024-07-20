import os
from typing import Any

from llama_index.core import SimpleDirectoryReader, PropertyGraphIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.anthropic import Anthropic
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.core.query_engine import RetrieverQueryEngine
from app_settings import settings

import nest_asyncio
nest_asyncio.apply()

# Set api keys
os.environ["OPENAI_API_KEY"] = settings.openai_api_key
os.environ["ANTHROPIC_API_KEY"] = settings.anthropic_api_key

# Initialize LLM and Embedding models
llm = Anthropic(model=settings.llm_model_name)
embed_model = OpenAIEmbedding(model=settings.embed_model_name)

# Load data into index
documents = SimpleDirectoryReader("./data/paul_graham/").load_data()
graph_store = Neo4jPropertyGraphStore(
    username=settings.neo4j_username,
    password=settings.neo4j_password,
    url=settings.neo4j_uri,
)
graph_store.refresh_schema()

# Check if the graph store has any nodes using a custom Cypher query
exists = True if graph_store.get() else False

if exists:
    index = PropertyGraphIndex.from_existing(
        llm=llm,
        embed_model=embed_model,
        property_graph_store=graph_store,
        show_progress=True,
    )
else:
    index = PropertyGraphIndex.from_documents(
        documents,
        llm=llm,
        embed_model=embed_model,
        property_graph_store=graph_store,
        show_progress=True,
    )

query_engine = index.as_query_engine(include_text=True)
response = query_engine.query("What did author do at Interleaf?")
print(response.response)

