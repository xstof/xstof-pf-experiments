# Simple RAG

## Set up Cognitive Search

Leveraging the Azure Search OpenAI demo, we'll set up a cognitive search instance with some demo data.

```sh
mkdir openai-demo
cd openai-demo
azd init -t azure-search-openai-demo
```

## Install vector db tool

```sh
pip install promptflow-vectordb
```

## Test Questions

- What is included in my Northwind Health Plus plan that is not in standard?
- What happens in a performance review?
- What does a product manager do?
- follow up: how is this different from what a director of product management does? can you compare the two in a single table?
- What does a sales rep do?
- What does a director of product management do?

## Notes

This is a very naive implementation, intended for demonstration and learning purposes only.  Context for references to previous items might not be retrieved.