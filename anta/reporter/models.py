#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: skip-file

"""Models related to anta.result_manager module."""

from rich.text import Text
from pydantic import BaseModel, validator
from ..result_manager.models import RESULT_OPTIONS


class ColorManager(BaseModel):
    """Color mangement for status report."""
    level: str
    color: str

    @validator('level', allow_reuse=True)
    def name_must_be_in(cls, v: str) -> str:
        """
        Status validator

        Validate status is a supported one

        Args:
            v (str): User defined level

        Raises:
            ValueError: If level is unsupported

        Returns:
            str: level value
        """
        if v not in RESULT_OPTIONS:
            raise ValueError(f'must be one of {RESULT_OPTIONS}')
        return v

    def style_rich(self) -> Text:
        """
        Build a rich Text syntax with color

        Returns:
            Text: object with level string and its associated color.
        """
        return Text(self.level, style=self.color)

    def string(self) -> str:
        """
        Build an str with color code

        Returns:
            str: String with level and its associated color
        """
        return f'[{self.color}]{self.level}'
