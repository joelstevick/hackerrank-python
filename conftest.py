# conftest.py
import pytest

def pytest_collection_modifyitems(config, items):
    if config.getoption("--only"):
        selected = [item for item in items if item.get_closest_marker("only")]
        if selected:
            items[:] = selected

def pytest_addoption(parser):
    parser.addoption(
        "--only", action="store_true", default=False, help="Run only tests marked with @pytest.mark.only"
    )