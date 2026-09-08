import pytest

SYSTEM_VERSION = "1.3.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.3.0",
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.2.0",
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():
    ...