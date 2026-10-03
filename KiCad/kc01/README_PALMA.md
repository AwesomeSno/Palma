# Palma KiCad Files - READ ME

## What was done

1. Complete schematic (kc01.kicad_sch) - 80 components, all connected
2. PCB layout (kc01_pcb.kicad_pcb) - Basic placement, needs routing
3. BOM (bom.csv) - Bill of materials
4. Journal draft (journal_draft.md) - Edit and publish to Half Life app

## To get the schematic

Run in Terminal:
```
cd "/Users/harinandanjv/Projects/01HackClub/Half Life/Palma/KiCad/kc01"
python3 decode.py
```
Creates kc01_new.kicad_sch (complete schematic).

## To get the PCB

Run in Terminal:
```
cd "/Users/harinandanjv/Projects/01HackClub/Half Life/Palma/KiCad/kc01"
python3 decode_pcb.py
```
Creates kc01_pcb.kicad_pcb (PCB layout).

## Then

1. Backup: cp kc01.kicad_sch kc01_backup.kicad_sch
2. Replace schematic: mv kc01_new.kicad_sch kc01.kicad_sch
3. Open kc01.kicad_sch in KiCad - run ERC
4. Open kc01_pcb.kicad_pcb in KiCad - route the board
5. Take 9-10 screenshots
6. Edit journal_draft.md and publish

## Screenshots (9-10)

1. Full schematic overview
2. ESP32-S3 section
3. BNO085 section
4. Power/charger section
5. USB-C section
6. Motor driver section
7. BOM
8. PCB layout
9. PCB 3D view
10. ERC clean (0 errors)

## Files

- sch_b64_*.txt - Schematic chunks (delete after decode)
- pcb_b64_*.txt - PCB chunks (delete after decode)
- decode.py, decode_pcb.py - Decoders (delete after use)
- bom.csv, journal_draft.md - Keep these
