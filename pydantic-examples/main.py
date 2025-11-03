from datetime import datetime

import json
import logfire

from pydantic import BaseModel, EmailStr, Field
from pydantic.config import ConfigDict
from typing_extensions import Annotated
from uuid import UUID, uuid4

# configure logfire
logfire.configure(token='pylf_v1_eu_xY08pQJdBfHGNsHzyBR4tyl3YKlyVpSxdSynlwXKhrwF')
logfire.instrument_pydantic()
    
class Identity(BaseModel):
    """
    This is the main identity model.
    """
    model_config = ConfigDict(title='Identity')

    id: Annotated[
        UUID,
        Field(
            title="Identifier",
            description="A unique identifier for the user.",
            default_factory=uuid4
        )
    ]
    name: Annotated[
        str,
        Field(
            title="Full Name",
            description="The full name of the user.",
            max_length=100
        )
    ]
    mail: Annotated[
        EmailStr,
        Field(
            title="Email Address",
            description="The email address of the user.",
            max_length=100
        )
    ] = None

def main():

    main_model_schema = Identity.model_json_schema()  # (1)!
    print(json.dumps(main_model_schema, indent=2))  # (2)!

    # this will record details of a successful validation to logfire
    user = Identity(name="John Doe")
    print(user.model_dump())

if __name__ == "__main__":
    main()
