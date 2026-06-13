from pydoc import doc

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
        name="read_doc",
        description="Read the contents of a document by its ID."
)
def read_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found")


@mcp.tool(
        name="edit_doc",
        description="Edit the contents of a document by its ID."
)
def edit_doc(doc_id: str, new_content: str) -> str:
    if doc_id in docs:
        docs[doc_id] = new_content
        return "Document updated successfully"
    return "Document not found"

# TODO: Write a resource to return all doc id's
@mcp.resource(
        name="list_docs",
        description="List all available document IDs."
)
def list_docs() -> list:
    return list(docs.keys())

# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
        url="docs://documents",
        mimetype="application/json",
        name="get_doc",
        description="Get the contents of a document by its ID."
)
def get_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found")

@mcp.prompt(
        name="rewrite_doc",
        description="Rewrite a document in markdown format."
)
def rewrite_doc(doc_id: str) -> str:
    doc = docs.get(doc_id, "Document not found")
    if doc == "Document not found":
        return doc
    # Here you might want to implement the actual rewriting logic
    prompt = f"Rewrite the following document in markdown format:\n\n{doc}"
    # Here you might want to call an LLM to perform the rewriting
    return doc

@mcp.prompt(
        name="summarize_doc",
        description="Summarize the contents of a document."
)

def summarize_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found")


if __name__ == "__main__":
    mcp.run(transport="stdio")
