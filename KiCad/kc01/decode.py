import base64, gzip, glob
parts = sorted(glob.glob('/Users/harinandanjv/Projects/01HackClub/Half Life/Palma/KiCad/kc01/sch_b64_*.txt'))
data = ''.join(open(f).read() for f in parts)
open('/Users/harinandanjv/Projects/01HackClub/Half Life/Palma/KiCad/kc01/kc01.kicad_sch','wb').write(gzip.decompress(base64.b64decode(data)))
print('Decoded OK')
