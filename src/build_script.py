import os
import subprocess
import sys
from pathlib import Path


def build():
    project_root = Path(__file__).resolve().parent.parent
    entry = project_root / "src" / "cli.py"
    os.chdir(project_root)
    
    # 虚拟环境的 Python
    python_exe = Path(sys.executable)
    
    # Nuitka 打包参数
    output_dir = project_root / 'dist'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "hearth-card-asset.exe"
    
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root / "src") + os.pathsep + env.get("PYTHONPATH", "")
    
    cmd = [
        python_exe.as_posix(),
        "-m", "nuitka",
        "--standalone",
        "--onefile",
        "--follow-imports",
        "--output-dir=" + output_dir.as_posix(),
        "--output-filename=" + output_file.as_posix(),
        "--include-package=UnityPy.resources",
        "--user-package-configuration-file=hearth-card-asset.nuitka-package.config.yml",
        entry.as_posix()
    ]
    
    subprocess.check_call(cmd, env=env)


if __name__ == "__main__":
    build()
