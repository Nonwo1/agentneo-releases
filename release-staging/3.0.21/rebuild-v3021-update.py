from __future__ import annotations
import sys, zipfile, json, struct, binascii
from pathlib import Path

def write_stored_zip(entries, out_path: Path):
    local=bytearray(); central=bytearray()
    dostime=0; dosdate=0x21
    for name,data in entries:
        nb=name.encode("utf-8")
        flag=0x800 if any(b>=128 for b in nb) else 0
        crc=binascii.crc32(data)&0xffffffff
        size=len(data); off=len(local)
        local += struct.pack("<IHHHHHIIIHH",0x04034b50,20,flag,0,dostime,dosdate,crc,size,size,len(nb),0)
        local += nb; local += data
        central += struct.pack("<IHHHHHHIIIHHHHHII",0x02014b50,20,20,flag,0,dostime,dosdate,crc,size,size,len(nb),0,0,0,0,0,off)
        central += nb
    cd_off=len(local); cd_size=len(central)
    local += central
    local += struct.pack("<IHHHHIIH",0x06054b50,0,0,len(entries),len(entries),cd_size,cd_off,0)
    out_path.write_bytes(local)

def main():
    if len(sys.argv)!=4:
        raise SystemExit("usage: rebuild.py OLD_UPDATE DELTA_ZIP OUTPUT")
    oldp, deltap, outp = map(Path, sys.argv[1:])
    with zipfile.ZipFile(oldp) as zo, zipfile.ZipFile(deltap) as zd:
        order=json.loads(zd.read("order.json"))
        dnames=set(zd.namelist())
        entries=[]
        for name in order:
            dp="files/"+name
            if dp in dnames:
                data=zd.read(dp)
            else:
                data=zo.read(name)
            entries.append((name,data))
    write_stored_zip(entries,outp)

if __name__=="__main__":
    main()
