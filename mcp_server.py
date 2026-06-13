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
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
