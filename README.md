
## Disclaimer
I am in no way affiliated with "Quel Solaar" http://www.quelsolaar.com/ministry_of_flat/ and just build and shared this python addon for blender for my own use. If you want to actually make use of this addon, then you'll also have to acquire a license from Quel Solaar for Ministry Of Flat. The dev behind the company is a really nice guy and cares about his product, so it's really money well spent.

## Description
This is a simple bridge to use MinistryOfFlat console variant http://www.quelsolaar.com/ministry_of_flat/ directly in blender and quickly and automatically unwrap meshes.
Currently Blender 3.0 is not supported yet but 2.8x and 2.9x should all work.

## How it works
The plugin simply exports the currently selected objects, then starts the UnwrapConsole3.exe with the exported files as the target, then reimports, transfers the uv channel and deletes the intermediary export/import object again.
It's super basic, but it works pretty reliably. It doesn't have any options to control the unwrapping process yet.
You also need the more expensive license of MinistryOfFlat though, to get the console variant of the program.

## Installation
To install the Addon just copy the MinistryOfFlatBridge folder into your blender addons directory and activate it in the Blender Addon Menu.
Then put the .exe file of the console variant of MOF into the folder called "mof" of the addon folder. The config file for MOF that i have in the repo might be outdated for your version of MOF.

And there's one possible issue to look out for and that's the license file that MoF uses, which needs to be in the correct folder. This is also different depending on wether you use the portable version of blender or the installed one.

I use windows 10 and the portable version of blender which i save in my documents folder (this is important!) and the license file sits next to the blender.exe. If you use the installed version of blender you need to put the license file next to the python.exe in blenders install directory.

You can then see the panel when selecting an object in object mode:

![Screenshot](AutoUVPanelScreenshot.png)
