<div align="center">

# <img src="images/icon-title (new).png" width="32" height="32" alt="Icon"> Bandcamp Player (Python Edition)

[![Download](images/download-button.png)](https://github.com/kameryn1811/Bandcamp-Player/releases/tag/Launcher_v3.0.0_Beanbagbeni_Edition)

</div>

A compact, Python-based mini player for streaming music directly from Bandcamp on Windows Desktop. 

Designed for previewing albums when deciding on new music you want to support. This player isn’t meant to replace traditional music software (Winamp, MusicBee, VLC, etc.), but to complement it by making album previews quick and convenient before purchasing, especially when you have a lot of albums to preview.  

## Key Features

* **Executable** - Available in .exe format, simply download and run (compatible with Windows 10 and 11).
* **Automatic Updates** - Select automatic updates or check now to be notified when there is a new update and accept to install it automatically.
* **Compact Interface** - Minimal design that stays out of your way and 4 modes to suit your style: Regular, Mini, Micro, and/or Nano.
* **Playlist Management** - Easily create and manage playlists of your favorite Bandcamp albums.
* **Adjustable Playlist** - Minimize, expand, resize or detach the playlist for flexible window management.
* **Always on Top** - Keep the player visible while working in other applications.
* **Keyboard Shortcuts** - Full keyboard control for play, pause, next, previous, volume, and more (customizable in the settings menu). Global keyboard shortcuts available with included `bandcamp_player_hotkeys.ahk` script ([Autohotkey v2 installation](https://www.autohotkey.com/v2/) required)
* **Autoplay** - Automatically start playback on launch and when switching albums. 
* **Shuffle & Repeat** - Multiple playback modes for varied listening.
* **Volume Control** - Adjustable volume.
* **Image Viewer** - Click on the magnifying glass in any mode to aoom and pan artwork and view it fullscreen, complete with player, playlist and visualization/particle effects. 
* **App Themes** - Choose from Light, Dark, Album and Custom! Album Mode uses the color from each URLs album page. Custom uses locally stored .css files that you can customize.
* **Account Menu** - Login to Bandcamp and access Follow Artist and Wishlist Album features directly from the Apps Account Menu! Easily Follow or Wishlist your favorite Artist/Album with this convenient feature.
* **Track Change Notifications** - Keep track of what you are listening to, especially helpful when the app is hidden via nano modes autohide, or minimized; adjust the notifications or turn them off in the settings. 


*The main player interface with compact playlist, regular/mini/micro and nano modes.*
*Note: Mini mode features optional player autohide so the artwork is fully viewable.*
*Note: Nano mode features optional autohide when docked to the top or bottom of the screen.*

<img alt="main-player-interface" src="images/main-v2.0.0.png" />

*The image viewer interface with fullscreen player playlist, visualizer and particles effects available.*
*Note: Click on magnfying glass icon in regular and mini mode to access the image viewer.*

<img width="720" alt="image-viewer-interface" src="images/image-viewer-v2.0.0.png" />



## Technology & Approach

Bandcamp doesn’t provide a public API for music playback, playlists, or track data (its official APIs are limited to sales and merchandise for artists and labels). 

As a work around Bandcamp Player loads Bandcamps native player in the backround and controls it via a Qt interface and DOM manipulation.

### Core Stack

- **PyQt6** – Cross-platform desktop framework for window management
- **PyQt6-WebEngine** – Embedded Chromium browser used to load Bandcamp’s mobile site with full DOM access
- **Qt-Painted Interface** - Fully customizable Qt interface used for reliability and extensibility
- **QtAwesome** – FontAwesome icons for consistency acroos platforms
  
## Quick Start

**Installation**

1. Download [BandcampPlayer.zip](https://github.com/kameryn1811/Bandcamp-Player/releases/tag/Launcher_v3.0.0_Beanbagbeni_Edition) extract it and run BandcampPlayer.exe.
2. **Note:** You may see a Windows Defender SmartScreen Warning, see [Troubleshooting](#troubleshooting) for more information. 
3. What it Does:
   - Downloads the latest `bandcamp_pl_gui.py` script from GitHub and Launches it
   - Checks for updates on startup
   - Self-contained - No Python installation needed
   - All dependencies included

## Usage

1. **Add URLs**: Drag and drop or Paste Bandcamp URLs into the main window (to load it right away) or into the playlist (to create a queue).
3. **Play Music**: Double click on an album in the playlist to load the url and start playing.
4. **Player Controls**: Use the Play controls or keyboard shortcuts to navigate albums and tracks, and adjust play modes (see [Shuffle & Repeat Modes](#shuffle--repeat-modes--)).
6. **Playlist**: Use the Playlist to manage Bandcamp albums, you can add/remove, reorder, load artist discography, save and load playlists and more. The playlist can act as a sidebar (attached to the main window) or be detached for more felxibility (the detached playlist can be resized, docked to the main window and will remember its state/position)
7. **Window Modes**: Switch between Regular, Mini, Micro, and Nano modes from the title bar.
8. **Image Viewer**: Click on the [Magnifying Glass Icon](#image-viewer-fullscreen-cover-art-with-player) in Regular or Mini mode to enter Image viewer - complete with player and effects for a fullscreen experience. 
10. **Settings Menu**: show the menu from the top right of regular, mini or micro mode and select the settings icon to view several additional settings like Autoplay settings, Update settings, [Keyboard Shortcuts](#keyboard-shortcuts) and More. 

## Image Viewer (Fullscreen Cover Art with player)  

**Image Viewer Button** - Click on the magnifying glass icon over the cover art in any mode to access the image viewer (full screen mode).

<img alt="image viewer button" src="images/Image viewer button.png" /> 

**Image Viewer Player Options** - Options to toggle player autohide, visualization, particle effects and more. (Note: Visualizations currently use simulated audio analysis (fake) since I haven't succeeded in analyzing the streamed audio in realtime yet)

<img alt="image viewer button" src="images/vis-menu.png" /> 

## Shuffle & Repeat Modes  <img alt="shuffle-repeat" src="images/shuffle-repeat.png" />

<img alt="shuffle-tracks" src="images/shuffle-tracks.png" /> **Shuffle Tracks** – shuffle tracks within the current album  
<img alt="shuffle-album" src="images/shuffle-album.png" /> **Shuffle Albums** – play albums in random order  
<img alt="super-shuffle" src="images/super-shuffle.png" /> **Super Shuffle** – completely random tracks and albums; avoids recent repeats  
<img alt="continuous" src="images/continuous.png" /> **Continuous Repeat** – plays through entire playlist (default)  
<img alt="repeat-album" src="images/repeat-album.png" /> **Repeat Album** – loops current album  
<img alt="repeat-1" src="images/repeat-1.png" /> **Repeat Track** – loops current track (shows "1" on button)  

**Combinations:** Shuffle and Repeat work together (e.g., *Shuffle Tracks + Repeat Album* loops shuffled tracks; *Super Shuffle + Repeat Off* plays random tracks without immediate repeats).

## Keyboard Shortcuts

* **Space** - Play/Pause
* **Play/Pause** - Ctrl + Alt + Space
* **Next Track** - Ctrl + Alt + Right
* **Previous Track** - Ctrl + Alt + Left
* **Next Album** - Ctrl + Shift + Alt + Right
* **Previous Album** - Ctrl + Shift + Alt + Left
* **Volume Up** - Ctrl + Shift + Up
* **Volume Down** - Ctrl + Shift + Down
* **Mute** - Ctrl + Shift + M
* **Toggle Playlist** - Ctrl + Alt + P
* **Expand/Collapse Playlist** - Ctrl + Shift + Alt + P
* **Cycle App Mode** - Ctrl + Alt + M
* **Save Playlist** - Ctrl + S
* And more... (see Settings > Keyboard Shortcuts)
* Note: Global keyboard shortcuts require ([Autohotkey v2](https://www.autohotkey.com/v2/) to be installed and the included `bandcamp_player_hotkeys.ahk` script to be running. 

## Troubleshooting

**Please Note**
- Documentation is still improving
- This should be a stable release but you may encounter bugs, please feel free to report any issues or suggestions. Issues can usually be resolved by loading another url, restarting the app, and if you're stuck rename or delete settings.json and/or Playlists folder to do a factory reset.

**Windows SmartScreen Warning**
- When you open BandcampPlayer.exe for the first time, Windows might say: "Windows protected your PC"
- This happens because the app isn't code-signed (certificates are pricey, and this is a free open-source project).
- No worries, it's safe to run. The EXE is the same code you can read on GitHub.
- **To continue:** Click "More info" and "Run anyway", Windows won't nag you again for the same .exe. 
- **Want extra peace of mind?** - You can review the code, build it yourself, or use the standalone Python script.

**Windows 7: Missing DLL or Failed to load Python Errors**
- If the app won't launch on Windows 7 and you see errors like "api-ms-win-core-path-l1-1-0.dll not found" or "Failed to load Python DLL," Windows 7 is missing a DLL required by Python 3.11+.
- Fix it with the latest compatibility patch from nalexandru: https://github.com/nalexandru/api-ms-win-core-path-HACK/releases
- Download the latest release and copy the DLLs to the following locations:
  - x86 → C:\Windows\SysWOW64
  - x64 → C:\Windows\System32 (Admin rights may be needed)
- Launch the app!
- Thanks to @alabx for this [fix](https://github.com/kameryn1811/Bandcamp-Downloader/issues/6)! 

**"Player not responding or sluggish"**
- Check your internet connection
- Verify the Bandcamp URL is valid and accessible
- Try refreshing the page
- VPNs, proxies, or ISP “secure connection” features can block or slow the CDN requests used to fetch artwork and metadata. Try turning these off or switching to a faster VPN location.
- Antivirus software with HTTPS/SSL scanning (Kaspersky, ESET, Dr.Web, etc.) may interfere with image requests — temporarily disable these features to test.If it helps, whitelist BandcampDownloader.exe and bandcamp.com.
- Bad DNS routing can also cause slow or missing images. Switching to 1.1.1.1, 8.8.8.8, or 9.9.9.9 may help.

**"Playlist not saving"**
- Check that the Playlists folder exists in the app directory
- Verify write permissions for the app directory

**Global Keyboard Shortcuts not working**
- Global keyboard shortcuts require ([Autohotkey v2](https://www.autohotkey.com/v2/) to be installed and the included `bandcamp_player_hotkeys.ahk` script to be running. 
- Try restarting the application

## Credits & Inspiration

This project was inspired by [Robert Golderbine's Companion Window | Always on Top](https://chromewebstore.google.com/detail/companion-window-always-o/hhneckfekhpegclkfhefepcjmcnmnpae) and [Yuki Eliot's Mobile View Switcher](https://chromewebstore.google.com/detail/mobile-view-switcher/ddfcjnekgmblacbpifjdmcbbhfcdekic). Prior to this project I was using a modified version of these Browser Extenstions to achieve a Mini BandCamp Player (It featured a compact bandcamp mode that stripped away everything but the player and playlist, and had 3 view modes - but needed to be launched for each album individually and sadly had many security limitations inherent in browser PIP implementations preventing automations e.g. automatic resizing of the player and playback manipulation which are made possible in this python project.

*Original Bandcamp Player using a modified version of Companion Window in combination with Mobile View Switcher:*

<img alt="main-player-interface" src="images/OGBandcampPlayer.png" />

## Legal & Ethical Use

This tool is designed for:
* Streaming freely available music from Bandcamp
* Personal use of music you own or have permission to stream
* Building a local playlist of new music you want to preview before buying

Please respect copyright laws and Bandcamp's terms of service. Support artists by purchasing music when possible.

## Disclaimer

This software is provided as-is for educational and personal use. The developers are not responsible for misuse. Please use responsibly and support the artists whose music you enjoy.
























