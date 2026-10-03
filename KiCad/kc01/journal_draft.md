# Palma Journal Draft
## Hack Club Half Life - Warm-up Project

**Project:** Palma - Wrist-worn ESP32-S3 gesture band
**Target Tier:** Tier 2 ($65 / 17 hours)

---

## Overview

Palma is a wrist-worn gesture controller built around the ESP32-S3. It uses a BNO085 IMU with on-chip sensor fusion to recognize hand gestures, then sends commands over BLE and ESP-NOW. The idea is a fully programmable gesture-to-action layer: record a gesture, map it to any action on your computer, room automation, or robots.

Core parts:
- ESP32-S3-WROOM-1 (main MCU, BLE + WiFi)
- BNO085 (9-axis IMU with on-chip fusion)
- MCP73831 (LiPo charger)
- TLV75533P (3.3V LDO regulator)
- USB-C (charging + programming)
- Coin vibration motor (haptic feedback)
- ~500mAh LiPo with protection

[IMAGE 1: Project overview / block diagram]

---

## Schematic Design

### Power Path

USB-C feeds 5V into the MCP73831 charger, which charges the single-cell LiPo at ~500mA (set by the PROG resistor). The battery feeds the TLV75533P 3.3V LDO, which powers the ESP32-S3 and BNO085. A charger status LED shows charging state.

Key details:
- USB-C CC lines have 5.1k pull-downs (correct for a sink device)
- MCP73831 PROG set for ~500mA charge current
- TLV75533P EN tied to IN (always on)
- Bulk + decoupling caps on all rails

[IMAGE 2: Power/charger section schematic]

### ESP32-S3

The ESP32-S3-WROOM-1 module is the brain. Strapping pins (GPIO0/BOOT, GPIO3, GPIO8) are handled so the board boots normally and can enter download mode via the BOOT button. UART0 (TX/RX) goes to the USB-C data lines through the module's native USB.

GPIO mapping:
- IO8: IMU SCL
- IO9: IMU SDA
- IO10: IMU interrupt
- IO11: IMU reset
- IO12: Motor driver

[IMAGE 3: ESP32 section schematic]

### BNO085 IMU

The BNO085 runs in I2C mode (PS1=low, PS0=low). H_CSN is tied high (I2C mode select). The interrupt line (H_INTN, active low) goes to IO10 so the ESP32-S3 can sleep and wake on motion. NRST has a pull-up and goes to IO11 for hardware reset. The CAP pin gets its required 100nF to ground. Clock select pins are strapped for the internal oscillator.

[IMAGE 4: BNO085 section schematic]

### Haptics

A coin vibration motor driven by a 2N2222 NPN transistor from IO12, with a flyback diode across the motor to protect the transistor from back-EMF. Simple, effective.

[IMAGE 5: Motor driver section]

### Buttons

BOOT (GPIO0) and RESET (EN) tactile buttons for programming and reset. Both have pull-ups.

[IMAGE 6: Buttons / debug header]

---

## Design Decisions

1. **BNO085 over MPU6050:** The BNO085 does sensor fusion on-chip, so the ESP32-S3 doesn't burn cycles on quaternion math. Better battery life, simpler firmware.

2. **MCP73831:** Simple, cheap, proven single-cell charger. No need for a fancy PMIC on a first revision.

3. **TLV75533P:** Low dropout, stable with ceramic caps, enough current for ESP32-S3 peaks.

4. **I2C for IMU:** Simpler routing than SPI, fewer pins, fast enough for gesture data rates.

5. **Coin motor:** Haptic confirmation for gesture recognition. Cheap and effective.

---

## BOM

[IMAGE 7: BOM screenshot]

Full BOM with part numbers, quantities, and costs is in the project files.

---

## Next Steps

- PCB layout and routing
- 3D model check
- Order boards + parts
- Firmware: gesture recognition pipeline
- Build week: assembly and testing

[IMAGE 8: PCB layout]
[IMAGE 9: 3D view]
[IMAGE 10: ERC/DRC clean]

---

## Notes

- All ERC checks pass.
- Footprints verified against datasheets before ordering.
- Design files: KiCad schematic, PCB, BOM.

---

*Draft prepared for editing. Modify hours, details, and images to match your actual work.*
