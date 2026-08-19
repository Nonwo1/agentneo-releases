from pathlib import Path
import hashlib, io, json, shutil, subprocess, sys, zipfile

CUR_UPDATE=Path(sys.argv[1]); CUR_EXE=Path(sys.argv[2]); PATCH=Path(sys.argv[3]); OUT=Path(sys.argv[4]);OUT.mkdir(parents=True,exist_ok=True)
START=6330752;OLD_END=41139282;NEW_END=41145560;FIXED=(2026,8,19,12,0,0)
EXPECTED_OLD_UPDATE='7bb91128ac4875f858e31a4df74dc1247eca983bb27acd7b8c15861810028e56'
EXPECTED_OLD_EXE='ee23b685381040d95c9f77fc8c93df1be85aa643c6eab3776f230011408bbd08'
EXPECTED_UPDATE='5e7c39b8ad35aaffe26cee7e57d4f2803eeecb3a2605fb390996dec9c5de79cf'
EXPECTED_EXE='b99995f7137687ce8023d087bedcabdec151e3bbd0b1a8d474a9bf721f4daa0d'
def sha(b):return hashlib.sha256(b).hexdigest()
def shafile(p):return sha(Path(p).read_bytes())
cur_u=shafile(CUR_UPDATE);cur_e=shafile(CUR_EXE)
assert cur_u in {EXPECTED_OLD_UPDATE,EXPECTED_UPDATE},cur_u
assert cur_e in {EXPECTED_OLD_EXE,EXPECTED_EXE},cur_e
if cur_u==EXPECTED_UPDATE and cur_e==EXPECTED_EXE:
    shutil.copy2(CUR_UPDATE,OUT/'AgentNEO_v3.0.13_Update.zip')
    shutil.copy2(CUR_EXE,OUT/'AgentNEO_v3.0.13.exe')
    print(json.dumps({'updater':cur_u,'installer':cur_e,'state':'already-refreshed'},indent=2));raise SystemExit(0)

exe_bytes=CUR_EXE.read_bytes();payload_end=OLD_END if cur_e==EXPECTED_OLD_EXE else NEW_END
work=OUT/'tree';shutil.rmtree(work,ignore_errors=True);work.mkdir(parents=True)
with zipfile.ZipFile(io.BytesIO(exe_bytes[START:payload_end])) as z:
    assert z.testzip() is None;member_names=z.namelist();zip_comment=z.comment;z.extractall(work)
if cur_e==EXPECTED_OLD_EXE:
    subprocess.run(['patch','-p1','--batch','--forward','-i',str(PATCH.resolve())],cwd=work,check=True)

with zipfile.ZipFile(CUR_UPDATE) as z: current_manifest=json.loads(z.read('manifest.json'))
paths=[x['path'] for x in current_manifest['files'] if x.get('path')]
if 'app/agentneo/core/media_catalog.py' not in paths:
    try:i=paths.index('app/agentneo/core/media_workflows.py')
    except ValueError:i=len(paths)
    paths.insert(i,'app/agentneo/core/media_catalog.py')
paths=[p for p in paths if p!='config/settings.json']

def zwrite(z,name,data):
    zi=zipfile.ZipInfo(name,FIXED);zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=(0o100644<<16)
    z.writestr(zi,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

rows=[]
for rel in paths:
    b=(work/rel).read_bytes();rows.append({'path':rel,'action':'replace','size':len(b),'sha256':sha(b)})
notes=('AgentNEO v3.0.13 expands Media Studio ComfyUI integration: the main selector now lists all discovered model/support assets; dedicated Diffusion model, VAE and Text encoder selectors are auto-populated from local/server loader catalogues; normal ComfyUI saved/preset workflow JSON is converted to API prompt graphs (including native subgraphs); and AgentNEO scans ComfyUI workflow-template and user-workflow APIs to automatically match the selected model and support assets. Scroll-safe controls and long-running prompt-ID monitoring remain enabled.')
manifest={'format':'agentneo-update-v1','version':'3.0.13','channel':'stable','requires_restart':True,'release_notes':notes,'files':rows}
updater=OUT/'AgentNEO_v3.0.13_Update.zip'
with zipfile.ZipFile(updater,'w',zipfile.ZIP_DEFLATED,compresslevel=9,allowZip64=True) as z:
    zwrite(z,'manifest.json',(json.dumps(manifest,indent=2)+'\n').encode())
    for row in rows:zwrite(z,'payload/'+row['path'],(work/row['path']).read_bytes())
assert shafile(updater)==EXPECTED_UPDATE,(shafile(updater),EXPECTED_UPDATE)

installer=OUT/'AgentNEO_v3.0.13.exe'
if cur_e==EXPECTED_EXE:
    shutil.copy2(CUR_EXE,installer)
else:
    payload={n:(work/n).read_bytes() for n in member_names if n!='MANIFEST_SHA256.txt'}
    manifest_text=''.join(f'{sha(payload[n])}  {n}\n' for n in member_names if n!='MANIFEST_SHA256.txt').encode()
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,'w',zipfile.ZIP_DEFLATED,compresslevel=9,allowZip64=True) as z:
        z.comment=zip_comment;zwrite(z,'MANIFEST_SHA256.txt',manifest_text)
        for n in member_names:
            if n!='MANIFEST_SHA256.txt':zwrite(z,n,payload[n])
    new_payload=buf.getvalue();capacity=len(exe_bytes)-START
    assert len(new_payload)<=capacity
    installer.write_bytes(exe_bytes[:START]+new_payload+b'\0'*(capacity-len(new_payload)))
assert shafile(installer)==EXPECTED_EXE,(shafile(installer),EXPECTED_EXE)
print(json.dumps({'updater':shafile(updater),'installer':shafile(installer),'state':'rebuilt'},indent=2))
