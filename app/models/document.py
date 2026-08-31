"""Document Domain Model."""
from dataclasses import dataclass, field, asdict
from typing import Dict, Any
import time
import uuid

@dataclass
class Document:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = ""
    filename: str = ""
    original_name: str = ""
    file_type: str = "txt"
    file_size: int = 0
    checksum: str = ""
    upload_timestamp: float = field(default_factory=time.time)
    word_count: int = 0
    character_count: int = 0
    status: str = "uploaded"
    storage_path: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
