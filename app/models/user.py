"""User Domain Model."""
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any
import time
import uuid

@dataclass
class User:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    username: str = ""
    email: str = ""
    password_hash: str = ""
    role: str = "Analyst"
    full_name: str = ""
    created_at: float = field(default_factory=time.time)
    last_login: Optional[float] = None
    is_active: bool = True

    def to_dict(self, include_sensitive: bool = False) -> Dict[str, Any]:
        d = asdict(self)
        if not include_sensitive:
            d.pop("password_hash", None)
        return d
