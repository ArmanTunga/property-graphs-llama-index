# Property Graph Analysis with LlamaIndex

This project demonstrates the use of property graphs for data analysis and querying using LlamaIndex.

## Overview

Property graphs are a powerful way to represent and analyze complex, interconnected data. This project leverages LlamaIndex to create, manipulate, and query property graphs, enabling efficient exploration of relationships within the data.

## Features

- Create property graphs from various data sources
- Perform graph-based queries and analyses
- Visualize graph structures and query results
- Integrate with other LlamaIndex components for advanced data processing

## Knowledge Graph vs Property Graph
Knowledge graphs use a triple structure (subject, predicate, object) for representing relationships and excel in semantic reasoning. Property graphs use labeled nodes, relationships, and properties attached to both, offering more flexible data modeling and efficient querying. While knowledge graphs are ideal for large-scale knowledge representation, property graphs shine in scenarios requiring high-performance graph traversals and analytics. 

![knowledge-property-graphs.png](src%2Fknowledge-property-graphs.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

## PropertyGraph Construction
![property-graph-construction.png](src%2Fproperty-graph-construction.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

### Graph Extractors

#### ImplicitPathExtractor
Divides the whole text into chunks and every chunk becomes a label. The relationships are implicit and are based on the order of the chunks.

![implicit-path-extractor.png](src%2Fimplicit-path-extractor.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

#### SimpleLLMExtractor
An LLM is used to extract labels and relationships from the data.
![simple-llm-extractor.png](src%2Fsimple-llm-extractor.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

#### SchemaLLMExtractor
LLM is restricted to use labels and relationships that are predefined in a schema.
In the example below, we don't see the label "Mat" that was present in the previous(SimpleLLMExtractor) example. 
![schema-llm-extractor.png](src%2Fschema-llm-extractor.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

### Graph Retrievers

### LLMSynonymRetriever
Uses LLM and generates synonyms to retrieve the data.

![llm-synonym-retriever.png](src%2Fllm-synonym-retriever.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

### VectorContextRetriever
Uses embeddings to retrieve the data.
![vector-context-retriever.png](src%2Fvector-context-retriever.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

### Text2Cypher

Generates Cypher statement using LLM.
![text2cypher.png](src%2Ftext2cypher.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>

### Cypher Template Retriever
Extracts relevant parameter and runs the cypher template.
![cypher-template-retriever.png](src%2Fcypher-template-retriever.png)
<p align="center">Source: <a href="https://docs.google.com/presentation/d/15qKwdOVoobnIuGDVN0qNl7hDO3nPwLAdETpCoBAKqfQ/edit#slide=id.g2ea0c8b6842_0_7">LlamaIndex - Introduction To Property Graphs</a></p>
