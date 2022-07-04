from dataclasses import dataclass


@dataclass
class Mail:
    username: str
    domain: str
    mail: str

