from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_prompt_context(search_result: list[dict]) -> str:
  retrieved_docs = []

  def format_single_doc(doc:dict):
    return f"Content: {doc['Content']} \n Source: {doc['Source']}"

  for item in search_result:
    retrieved_docs.append({
      "Content": item["text"],
      "Source": item["original_entity"]["sourcefile"]
    })

  doc_string = "\n\n".join([format_single_doc(doc) for doc in retrieved_docs])
  return doc_string