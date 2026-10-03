#!/bin/bash
# Combine schematic parts
cd "/Users/harinandanjv/Projects/01HackClub/Half Life/Palma/KiCad/kc01"
cat sch_part_*.txt > kc01_new.kicad_sch
echo "Combined into kc01_new.kicad_sch"
ls -lh kc01_new.kicad_sch
