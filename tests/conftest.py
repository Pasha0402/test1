from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    baseline = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(baseline))


@pytest.fixture
def client():
    return TestClient(app)
