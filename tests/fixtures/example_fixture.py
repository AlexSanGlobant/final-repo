"""Code for create fixtures."""

from uuid import uuid4

import pytest

from tests.const import PROJECT_DIR


@pytest.fixture(scope="session")
def test_session_id() -> str:
    """Create session id."""
    test_session_id = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
