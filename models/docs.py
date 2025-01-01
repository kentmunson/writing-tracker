from typing import List, Optional

import yaml
from pydantic import BaseModel


class Document(BaseModel):
    google_doc_id: str
    user_id: int = 1  # placeholder for a future multi-user version
    title: Optional[str] = None
    status: Optional[str] = "Active"
    treatment_doc_id: Optional[str] = None


class Config(BaseModel):
    sa_email: str
    documents: List[Document]

    @classmethod
    def from_file(cls, fp: str):
        with open(fp, "r") as f:
            content = yaml.safe_load(f)
        return cls(**content)
