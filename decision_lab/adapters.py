"""Only a uniform demonstration adapter is implemented."""
from __future__ import annotations
from typing import Any, Mapping, Protocol

class ChoiceAdapter(Protocol):
    def predict(self, state: Any, question: str, options: Mapping[str, str]) -> dict[str, float]:
        """Return a probability for every semantic option ID, without seeing labels."""
        ...

class UniformAdapter:
    """Non-learned infrastructure baseline. It does not understand the input."""
    model_id = "uniform-demo"
    revision = "v1"

    def predict(self, state: Any, question: str, options: Mapping[str, str]) -> dict[str, float]:
        if len(options) < 2:
            raise ValueError("At least two options are required")
        return {key: 1.0 / len(options) for key in sorted(options)}
