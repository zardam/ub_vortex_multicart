# Patches for UNIBIOS 4.0

- UNIBIOS created by [Razoola](http://unibios.free.fr)
- Initial patch by [ArcadeTV](https://github.com/ArcadeTV/neogeo-menu)
- Multicart by [Vortex](https://github.com/xvortex/VTXCart)

## Patching

1. Obtain the [UNIBIOS 4.0 ROM](http://unibios.free.fr/download/uni-bios-40.zip).
2. Use the BPS patch file to patch your ROM. I recommend [FLIPS](https://dl.smwcentral.net/11474/floating.zip). 

## [uni-bios_4_0_BackToMenu.bps](uni-bios_4_0_BackToMenu.bps)

With this patch, keeping B pressed while soft rebooting from the in game menu will make the multicart boot on the menu.

## [uni-bios_4_0_PICKnMIX.bps](uni-bios_4_0_PICKnMIX.bps)

This patch enables PICKnMIX feature for a custom 161in1 cart, with some limitations:
- Always boots to PICKnMIX, even with a normal game cartridge.
- Works on MVS only (backup RAM used to store soft dips).
- No high score save.
- Tested on a MV1A only.
- Game list (titles and order) is hardcoded. The custom 161in1 cart must have been created with this one: [uni-bios_4_0_PICKnMIX.csv](uni-bios_4_0_PICKnMIX.csv).
- Use at your own risk!