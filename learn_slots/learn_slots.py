
from timeit import timeit
from typing import NamedTuple

import attr,sys
from pympler import asizeof

# use NamedTuple
Message = NamedTuple("Message", [("sender", str), ("recipient", str), ("body", str)])

if sys.version_info.minor >=7:
    import dataclasses
    @dataclasses.dataclass
    class DataClassMessage:
        sender: str
        recipient: str
        body: str


    @dataclasses.dataclass
    class SlotMessage:
        __slots__ = ["sender", "recipient", "body"]
        sender: str
        recipient: str
        body: str


@attr.s(auto_attribs=True, slots=True, weakref_slot=False)
class AttrsMessage:
    sender: str
    recipient: str
    body: str


if __name__ == "__main__":
    pos = Message(
        sender="sender@exmaple.com",
        recipient="recipient.example.com",
        body="Hello, World!",
    )
    if sys.version_info.minor >=7:
        simple = DataClassMessage(
            sender="sender@exmaple.com",
            recipient="recipient.example.com",
            body="Hello, World!",
        )
        slotted = SlotMessage(
            sender="sender@exmaple.com",
            recipient="recipient.example.com",
            body="Hello, World!",
        )
        print(
            "Dataclass %d, Slotted dataclass %d"
            % asizeof.asizesof(simple, slotted)
        )
    attrs = AttrsMessage(
        sender="sender@exmaple.com",
        recipient="recipient.example.com",
        body="Hello, World!",
    )
    print(            
        "NamedTuple %d,  Attrs %d"
        % asizeof.asizesof(pos, attrs)
    )

    print(
        timeit(
            """m = Message(sender="sender@exmaple.com",
                recipient="recipient.example.com",body="Hello, World!",)
            """,
            globals=globals(),
        )
    )
    if sys.version_info.minor >=7:

        print(
            timeit(
                """dm = DataClassMessage(sender="sender@exmaple.com",
                    recipient="recipient.example.com",body="Hello, World!",)
                """,
                globals=globals(),
            )
        )
        print(
            timeit(
                """sm = SlotMessage(sender="sender@exmaple.com",
                    recipient="recipient.example.com",body="Hello, World!",)
                """,
                globals=globals(),
            )
        )
    print(
        timeit(
            """am = AttrsMessage(sender="sender@exmaple.com",
                recipient="recipient.example.com",body="Hello, World!",)
            """,
            globals=globals(),
        )
    )
