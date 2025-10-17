from dataclasses import dataclass, field
import pytest
from src.formatter import format_file_size

@dataclass
class FileSizeTestCase:
    size_bytes: int
    expected_result: str
    id: str = field(init=False)

    def __post_init__(self):
        self.id = f"test_format_file_size_{self.size_bytes}_bytes"

test_cases = [
    FileSizeTestCase(0, "0B"),
    FileSizeTestCase(1, "1.00 B"),
    FileSizeTestCase(1024, "1.00 KB"),
    FileSizeTestCase(1024**2, "1.00 MB"),
    FileSizeTestCase(1024**3, "1.00 GB"),
    FileSizeTestCase(1024**4, "1.00 TB"),
]

@pytest.mark.parametrize("test_case", test_cases, ids=lambda tc: tc.id)
def test_format_file_size(test_case):
    assert format_file_size(test_case.size_bytes) == test_case.expected_result