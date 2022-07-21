from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Mail:
    username: str
    domain: str
    mail: str

