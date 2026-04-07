from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class ContactEntity:
	id: Optional[int]
	first_name: str
	last_name: str
	email: Optional[str]
	phone: Optional[str]
	contact_type: str
	company: Optional[str]
	position: Optional[str]
	notes: Optional[str]
	is_active: bool
	created_at: Optional[datetime]
	updated_at: Optional[datetime]
