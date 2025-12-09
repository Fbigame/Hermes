from dataclasses import dataclass
from pathlib import Path

from unity3d import AssetManifest


@dataclass
class Context:
    input: Path
    output: Path
    asset_manifest: AssetManifest
    locale_options: tuple[str, ...]
    card_id: str


def get_guid(source: str) -> str | None:
    if isinstance(source, str) and len(parts := source.split(':')) > 1:
        return parts[1]
    return None
