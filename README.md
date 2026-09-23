# commitizen-galaxy-provider

A [commitizen](https://commitizen-tools.github.io/commitizen/) version provider for Ansible Collections. It reads and writes the `version` field in your collection's `galaxy.yml`, so `cz bump` can manage your collection version alongside your changelog and git tags.

## Installation

Install alongside commitizen, e.g. with `uv`:

```sh
uv add commitizen commitizen-galaxy-provider
```

or with `pip`:

```sh
pip install commitizen commitizen-galaxy-provider
```

## Usage

Set `galaxy` as the `version_provider` in your commitizen configuration, typically in `pyproject.toml`:

```toml
[tool.commitizen]
version_provider = "galaxy"
```

By default, the provider looks for `galaxy.yml` in the current directory. Given:

```yaml
namespace: my_namespace
name: my_collection
version: 1.0.0
readme: README.md
authors:
  - Someone <someone@example.com>
```

running `cz bump` updates the `version` field in place, preserving every other field in the file.

## How it works

`GalaxyProvider` extends commitizen's `FileProvider` and targets `galaxy.yml`. It parses the file as YAML, exposes `get_version`/`set_version` to read and persist the `version` key, and implements the `get`/`set` document helpers commitizen uses internally, without disturbing the rest of the collection metadata.

## Development

```sh
uv sync
uv run pytest
```
