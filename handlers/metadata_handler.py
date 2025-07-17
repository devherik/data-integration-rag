from agno.document.base import Document as AgnoDocument
from langchain_core.documents.base import Document
from typing import Any, Dict, List, Union

def metadata_handler(data: Union[Dict, List, Any], parent_key: str = "") -> Dict[str, Any]:
    """
    Handles metadata retrieval for documents.

    Returns:
        List[Document]: A list of Document objects containing metadata.
    """
    # This is a placeholder implementation. Replace with actual logic to retrieve metadata.
    if not data:
        return {}
    # Example logic to convert Document to AgnoDocument
    cleaned_data = {}
    if isinstance(data, (str, int, float, bool)) or data is None:
        if parent_key:
            cleaned_data[parent_key] = data
            return cleaned_data
    if isinstance(data, dict):
        # Special handling for Notion-style date objects
        if 'start' in data or 'end' in data:
            start_date = data.get('start')
            end_date = data.get('end')
            if start_date:
                cleaned_data[f"{parent_key}_start"] = str(start_date)
            if end_date:
                cleaned_data[f"{parent_key}_end"] = str(end_date)
            return cleaned_data

        # Generic dictionary flattening
        for key, value in data.items():
            new_key = f"{parent_key}_{key}" if parent_key else key
            cleaned_data.update(metadata_handler(value, new_key))
        return cleaned_data
    elif isinstance(data, list):
        # Handle lists by recursively processing each item
        for index, item in enumerate(data):
            new_key = f"{parent_key}_{index}" if parent_key else str(index)
            cleaned_data.update(metadata_handler(item, new_key))
        return cleaned_data
    return cleaned_data