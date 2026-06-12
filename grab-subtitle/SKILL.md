---
name: grab-subtitle
description: >
  Download subtitles from a YouTube video and convert them into a clean timestamped transcript.
  Use this skill whenever the user wants to grab, download, fetch, or extract subtitles or a transcript
  from a YouTube video. Also trigger when the user pastes a YouTube URL and asks for subtitles,
  captions, or a transcript, or says things like "get the subs for this video",
  "download captions", "transcribe this YouTube video", or "grab subtitle".
---

# Grab Subtitle

Download YouTube subtitles via yt-dlp and convert them into a clean, timestamped plain-text transcript.

## Workflow

### 1. Gather inputs

Ask the user for:
- **YouTube URL** (if not already provided)
- **Subtitle language code** (e.g., `en`, `fr`, `de` — default to `en` if the user doesn't specify)

### 2. Check available subtitles

List what's available for the video:

```bash
yt-dlp --list-subs "<URL>" 2>&1
```

Look at the output to determine:
- Whether **manual (human-written) subtitles** exist for the requested language
- Whether **auto-generated subtitles** exist for the requested language

### 3. Download subtitles

Prefer manual subtitles; fall back to auto-generated if manual aren't available.

**Manual subtitles:**
```bash
yt-dlp --write-sub --sub-lang <lang> --sub-format srt --skip-download -o "%(title)s" "<URL>"
```

**Auto-generated subtitles (fallback):**
```bash
yt-dlp --write-auto-sub --sub-lang <lang> --sub-format srt --skip-download -o "%(title)s" "<URL>"
```

Note: yt-dlp writes the subtitle file as `<title>.<lang>.srt` in the current directory.

### 4. Convert SRT to clean transcript

Run the bundled conversion script on the downloaded SRT file:

```bash
python3 ~/.claude/skills/grab-subtitle/scripts/srt_to_transcript.py "<path-to-srt-file>" "<output-name>.txt"
```

The script handles:
- Stripping SRT sequence numbers and timing arrows
- Converting timestamps from `HH:MM:SS,mmm` to `[M:SS]` / `[MM:SS]` format
- Grouping subtitle entries into paragraphs (new paragraph roughly every 30 seconds)
- Writing clean plain text output

### 5. Clean up

Remove the intermediate `.srt` file after conversion. Tell the user where the final `.txt` file was saved and whether manual or auto-generated subs were used.
