import pytest
from commitizen.config.base_config import BaseConfig

from commitizen_galaxy_provider.provider import GalaxyProvider

GALAXY_YML = """\
namespace: my_namespace
name: my_collection
version: 1.0.0
readme: README.md
authors:
  - Someone <someone@example.com>
"""


@pytest.fixture
def galaxy_file(tmp_path, monkeypatch):
    path = tmp_path / "galaxy.yml"
    path.write_text(GALAXY_YML)
    monkeypatch.chdir(tmp_path)
    return path


def test_get_version(galaxy_file):
    provider = GalaxyProvider(BaseConfig())
    assert provider.get_version() == "1.0.0"


def test_set_version_persists_to_disk(galaxy_file):
    provider = GalaxyProvider(BaseConfig())
    provider.set_version("2.0.0")

    assert GalaxyProvider(BaseConfig()).get_version() == "2.0.0"


def test_set_version_preserves_other_fields(galaxy_file):
    provider = GalaxyProvider(BaseConfig())
    provider.set_version("2.0.0")

    content = GalaxyProvider(BaseConfig()).content
    assert content["namespace"] == "my_namespace"
    assert content["name"] == "my_collection"


def test_get_and_set_document_helpers():
    provider = object.__new__(GalaxyProvider)
    document = {"version": "1.2.3"}
    assert provider.get(document) == "1.2.3"

    provider.set(document, "1.2.4")
    assert document["version"] == "1.2.4"
