<div align="center">

# <img src="images/icon-title (new).png" width="32" height="32" alt="Icon"> Beni's Bandcamp Player

<p>
  <a href="https://github.com/bshurikan/Beni-BandcampPlayer">
    <img src="images/download-button.png" height="39">
  </a>
  <a href="https://ko-fi.com/B0B51LWFE" target="_blank">
    <img src="images/support_me_on_kofi_beige.png" height="39">
  </a>
</p>

</div>

**A compact, fully featured mini player for streaming music directly from Bandcamp on Windows 10/11.**

Preview new albums in a quick and convenient way before purchasing and playing the high quality downloads in your favorite music app like MusicBee, foobar2000, VLC, etc. 

<div align="center">

[Key Features](#key-features) &nbsp;&middot;&nbsp; [Quick Start](#quick-start) &nbsp;&middot;&nbsp; [Troubleshooting](#troubleshooting) &nbsp;&middot;&nbsp; [Disclaimer](#legal--ethical-use)

</div>
<br>

<img width="593" alt="main-player-interface" src="https://github.com/user-attachments/assets/f48c31c6-f8a2-4a93-825f-de62e7c23141" />

*The main player regular/mini/micro/nano modes and notification.*

<img width="593" alt="image viewer mode" src="https://github.com/user-attachments/assets/b05a39d4-084c-436c-b3d6-7b5c0bc8bc56" />

*The image viewer interface.*

<img width="593" alt="image viewer fullscreen" src="https://github.com/user-attachments/assets/ee3626d5-92ae-4c85-b3cf-6d27eede34ba" />

*The image viewer interface in fullscreen mode with player, playlist, visualizer and particles effects available.*

## Key Features

* **Minimal design** - that stays out of your way with 3 modes to suit your style:
  * **Regular Mode** - main window that can be rolled up into Mini or Micro modes to save screen space.
  * **Nano Mode** - An ultra-compact dockable player that can snap to the top or bottom of your screen and auto-hide (à la Winamp); and
  * **Image Viewer Mode** - a lightbox-style showcase (great if you have a second monitor). Zoom and pan artwork, go fullscreen, and enjoy visualization/particle effects.  
* **Volume Control** - Adjustable volume! Nuff said.  
* **Playlist Management** - Easily create and manage URLs and Save/Load separate lists.
* **Import URLs** - Easily Load Artist Discographies, Similar Artist or Import Collections. 
* **Shuffle & Repeat** - Multiple playback modes for varied listening.
* **App Themes** - Choose from Light, Dark, Album or Custom!
  * **Album Themes** - loads color palette from each URL for a unique look that matches the artists intent. Palettes can be saved and edited - with a Prefer Saved option to override the default palette! 
  * **Custom Themes** - Save an album theme you like or create your own with built in Theme editor!
* **Account Menu** - Login to Bandcamp to access **Follow Artist** and **Wishlist Album** features directly from the Apps Account Menu and unlock unlimited streaming of albums you've purchased with fancy icon and thank you messages. 
* **Track Change Notifications** - Keep track of what you are listening to, especially helpful in Nano Mode when autohidden; adjust the notifications or turn them off in the settings. 
* **Keyboard Shortcuts** - Full keyboard control for play, pause, next, previous, volume, and more (customizable in the settings menu). With Global Support. 

## Technology & Approach

Bandcamp doesn’t provide a public API for music playback, playlists, or track data (its official APIs are limited to sales and merchandise for artists and labels). 

As a work around Beni's Bandcamp Player loads Bandcamps native player in the backround and controls it via a Qt interface and DOM manipulation.

### Core Stack

- **PyQt6** – Cross-platform desktop framework for window management
- **PyQt6-WebEngine** – Embedded Chromium browser used to load Bandcamp’s site with full DOM access
- **Qt-Painted Interface** - Fully customizable Qt interface used for reliability and extensibility
- **QtAwesome** – FontAwesome icons for consistency across platforms
  
## Quick Start

**Installation**

1. Download [BandcampPlayer.zip](https://github.com/kameryn1811/Bandcamp-Player/releases/tag/Launcher_v3.0.0_Beanbagbeni_Edition) extract it and run BandcampPlayer.exe.
2. **Note:** You may see a Windows Defender SmartScreen Warning, see [Troubleshooting](#troubleshooting) for more information. 

## Usage

1. **Add URLs**: Drag and drop Bandcamp URLs into the main window (to load it right away) or into the playlist to create a queue (CTRL+V, Right click and select Paste URL also work).
3. **Play Music**: Double click on an album in the playlist to load the url and start playing.
4. **Player Controls**: Use the Play controls or keyboard shortcuts to navigate albums and tracks, and adjust play modes (see [Shuffle & Repeat Modes](#shuffle--repeat-modes--)).
6. **Album List**: Use the Album List to manage Bandcamp URL's, you can add/remove, reorder, load artist discography, save and load Album lists and more. The Album List can act as a sidebar (attached to the main window) or be detached for more felxibility (the detached Album List can be resized, docked to the main window and will remember its state/position)
7. **Window Modes**: Roll up the main window into in to Mini or Micro using the upward chevron or minimize to the separate Nano Player from the title bar.
8. **Image Viewer**: Click on the fullscreen button to enter Image viewer.
10. **Settings Menu**: Click on the cog icon to view several additional settings like Updates, Settings, Themes, and more. 

## Image Viewer (Fullscreen Cover Art with player)  

**Image Viewer Player Options** - Options to toggle player autohide, visualization, particle effects and more. (Note: Visualizations currently use simulated audio analysis (fake) since I haven't succeeded in analyzing the streamed audio in realtime yet despite several attempts)

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
* And more... (see Settings > Keyboard Shortcuts)

## Troubleshooting

**Please Note**
- Documentation is still improving
- This app has now received a decent amount of testing so it should be pretty stable but you may still encounter bugs, please feel free to report any issues or suggestions. Issues can usually be resolved by loading another url, restarting the app, or if you're really stuck renaming or deleting settings.json and it's Backup folder, and/or the Playlists folder. 

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
- Verify the Bandcamp URL is valid and accessible (sometimes artists remove access to an album or redirect it), check the album page to make sure its still there, remove the url and readd it. 
- Try refreshing the URL or switching to another URL. 
- VPNs, proxies, or ISP “secure connection” features can block or slow the CDN requests used to fetch artwork and metadata. Try turning these off or switching to a faster VPN location or Split tunnel and exclude the app. 
- Antivirus software with HTTPS/SSL scanning (Kaspersky, ESET, Dr.Web, etc.) may interfere with image requests — temporarily disable these features to test. If it helps, whitelist the app and bandcamp.com.
- Bad DNS routing can also cause slow or missing images. Switching to 1.1.1.1, 8.8.8.8, or 9.9.9.9 may help.

**"Playlist not saving"**
- Check that the Playlists folder exists in the app directory
- Verify write permissions for the app directory

## Credits & Inspiration

This project was inspired by [Robert Golderbine's Companion Window | Always on Top](https://chromewebstore.google.com/detail/companion-window-always-o/hhneckfekhpegclkfhefepcjmcnmnpae) and [Yuki Eliot's Mobile View Switcher](https://chromewebstore.google.com/detail/mobile-view-switcher/ddfcjnekgmblacbpifjdmcbbhfcdekic). 

Prior to this project I was using a **custom version of Companion Window** with **Mobile View Switcher** as a Mini BandCamp Player (It featured a compact bandcamp mode that stripped away everything but the player and playlist, and had roll up feature like the current app - but had to be launched separately for each album and had many security limitations inherent in browser PIP implementations preventing automations e.g. automatic resizing, playback manipulation, playlists+ which are made possible in this python project.

<img alt="main-player-interface" src="images/OGBandcampPlayer.png" />

*Original Bandcamp Player using a custom version of Companion Window with Mobile View Switcher*

Out of interest here is a screenshot from an early prototype of the current player that displayed the mobile webview directly instead of using a custom interface (an evolution of the original browser extension concept). However it also had a number of limitations and bugs that were difficult to surmout (the live webview could be unpredictable and fail to reliably inject css and js) *The live webview is still presented in the current app when logging in or out and fundamental to the app behind the scenes. 

<img width="560" height="711" alt="main-v1 0 0 2" src="https://github.com/user-attachments/assets/f37a89ad-e3cb-4de0-8e61-9d53db7458b3" />

*Early Protype that presented the bandcamp mobile webview directly*


## Legal & Ethical Use

This tool is designed for:
* Streaming freely available music from Bandcamp
* Personal use of music you own or have permission to stream
* Building a local playlist of new music you want to preview before buying

Please respect copyright laws and Bandcamp's terms of service. Support artists by purchasing music when possible.

## Disclaimer

This software is provided as-is for educational and personal use. The developers are not responsible for misuse. Please use responsibly and support the artists whose music you enjoy.
























