from dataclasses import dataclass
from typing import List

@dataclass
class UserInputs:
    plex_url: str
    plex_token: str
    openai_key: str
    library_names: List[str]  # Change from a single string to a list of strings
    collection_title: str
    history_amount: int
    recommended_amount: int
    minimum_amount: int
    wait_seconds: int
