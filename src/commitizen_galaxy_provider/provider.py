from collections.abc import Mapping
from typing import Any

from commitizen.providers.base_provider import FileProvider
from yaml import safe_dump, safe_load


class GalaxyProvider(FileProvider):
    """
    Ansible galaxy.yml providers
    """

    filename = "galaxy.yml"

    __content: dict[str, Any] | None = None

    @property
    def content(self) -> dict[str, Any] | None:
        if self.__content is None:
            with open(self.file) as f:
                self.__content = safe_load(f)
        return self.__content

    def __write_galaxy_content(self) -> None:
        with open(self.file, "w") as f:
            safe_dump(self.content, f)

    def get_version(self) -> str:
        """
        Get the current version from galaxy.yml
        """

        if not self.content:
            return ""

        return str(self.content.get("version", ""))

    def set_version(self, version: str) -> None:
        """
        Set the version in galaxy.yml
        """
        if not self.content:
            return
        self.content["version"] = version
        self.__write_galaxy_content()

    def get(self, document: Mapping[str, str]) -> str:
        return document.get("version", "")

    def set(self, document: dict[str, Any], version: str) -> None:
        document["version"] = version
