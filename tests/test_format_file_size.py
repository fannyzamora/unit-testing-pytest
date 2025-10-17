import pytest
from src.formatter import format_file_size

@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        pytest.param(0, "0B", id="test_format_file_size_returns_format_zero"),
        pytest.param(1, "1.00 B", id="test_format_file_size_returns_format_one_byte"),
        pytest.param(1024, "1.00 KB", id="test_format_file_size_returns_format_kb"),
        pytest.param(1024**2, "1.00 MB", id="test_format_file_size_returns_format_mb"),
        pytest.param(1024**3, "1.00 GB", id="test_format_file_size_returns_format_gb"),
        pytest.param(1024**4, "1.00 TB", id="test_format_file_size_returns_format_tb"),
    ],
)
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result