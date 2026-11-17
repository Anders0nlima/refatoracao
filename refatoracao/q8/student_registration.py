from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Address:
    city: str | None
    zip_code: str | None

    def is_valid(self) -> bool:
        if self.zip_code is None or not re.fullmatch(r"\d{5}-\d{3}", self.zip_code):
            return False
        return True
    
    def format(self) -> str:
        return f"{self.city} - {self.zip_code}"

@dataclass(frozen=True)
class ContactInfo:
    email: str | None
    phone: str | None

    def is_valid(self) -> bool:
        if self.email is None or "@" not in self.email:
            return False
        if self.phone is None or len(self.phone) < 10:
            return False
        return True
    
    def format(self) -> str:
        return f"{self.email} | {self.phone}"

class StudentRegistration:

    def __init__(self, name: str | None, email: str | None, phone: str | None,
                 city: str | None, zip_code: str | None, contact: ContactInfo | None = None, address: Address | None = None,):
        self._name = name
        self._contact = contact if contact is not None else ContactInfo(email, phone)
        self._address = address if address is not None else Address(city, zip_code)

    @property
    def contact(self) -> ContactInfo:
        return self._contact

    @property
    def address(self) -> Address:
        return self._address

    def is_valid(self) -> bool:
        if self._name is None or self._name.strip() == "":
            return False
        return self._contact.is_valid() and self._address.is_valid()

    def formatted_contact(self) -> str:
        return f"{self._name} | {self._contact.format()} | {self._address.format()}"
