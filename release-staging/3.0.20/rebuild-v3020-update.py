#!/usr/bin/env python3
import hashlib
import json
import sys
import zipfile
from pathlib import Path

FIXED_DT = (2026, 8, 21, 9, 28, 0)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_zip(path):
    with zipfile.ZipFile(path, "r") as z:
        return {name: z.read(name) for name in z.namelist() if not name.endswith("/")}


def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: rebuild-v3020-update.py BASE_3019_UPDATE.zip DELTA.zip OUTPUT.zip")
    base_path, delta_path, out_path = map(Path, sys.argv[1:])
    base = read_zip(base_path)
    delta = read_zip(delta_path)

    # Delta contains changed/new payload members plus authoritative 3.0.20 manifest.
    merged = dict(base)
    merged.update(delta)
    manifest = json.loads(merged["manifest.json"].decode("utf-8"))
    expected = [entry["path"] for entry in manifest["files"]]

    # Keep only the package contract files referenced by the new manifest plus manifest.json.
    allowed = {"manifest.json"} | {f"payload/{p}" for p in expected}
    merged = {k: v for k, v in merged.items() if k in allowed}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        # Reproduce local package member order exactly: manifest first, then manifest file order.
        order = ["manifest.json"] + [f"payload/{p}" for p in expected]
        for name in order:
            if name not in merged:
                raise RuntimeError(f"missing required member after merge: {name}")
            info = zipfile.ZipInfo(name, FIXED_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            info.create_system = 3
            z.writestr(info, merged[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    print(f"built={out_path}")
    print(f"sha256={sha256(out_path)}")


if __name__ == "__main__":
    main()
