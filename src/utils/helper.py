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


def load_emote_type(input_path: Path):
    import pythonnet
    pythonnet.load()
    # 导入C#环境
    import System  # noqa
    import System.Reflection as SR  # noqa
    asm = SR.Assembly.LoadFile((input_path / r"Hearthstone_Data\Managed\Assembly-CSharp.dll").as_posix())
    name = 'EmoteType'
    enum_type = asm.GetType(name)
    if enum_type is None:
        raise ValueError(f"Enum '{name}' not found in DLL")
    
    names = System.Enum.GetNames(enum_type)
    values = [System.Enum.Parse(enum_type, n).value__ for n in names]
    
    return {v: n for n, v in zip(names, values)}


def get_guid(source: str) -> str | None:
    if isinstance(source, str) and len(parts := source.split(':')) > 1:
        return parts[1]
    return None
