from typing import List, Optional

class VitalHistory:
    """Stores multiple medical readings and supports analysis."""

    def __init__(self, readings: Optional[List[float]]=None):
        # TODO: Implement logic
        pass

    def __len__(self) -> int:
        # TODO: Implement logic
        pass

    def __getitem__(self, index: int) -> float:
        # TODO: Implement logic
        pass

    def __iter__(self):
        # TODO: Implement logic
        pass

    def __sub__(self, other: 'VitalHistory') -> float:
        """Calculates difference in averages between two histories."""
        # TODO: Implement logic
        pass

    def __repr__(self) -> str:
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    h1 = VitalHistory([120, 125, 130])
    h2 = VitalHistory([110, 115, 120])
    # TODO: Implement logic
    pass