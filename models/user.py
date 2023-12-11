#!/bin/bash/python3
""" class User that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class representation of User

    Attributes:
        email :   user email.
        password :  user password.
        first_name : first name of the user.
        last_name : last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
