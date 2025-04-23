
# 🎥 Video Progress Tracker

An intelligent lecture video player that tracks actual learning progress by recording **unique watched segments**, preventing skip-based completion, and resuming automatically.

## 🌟 Features

- ✅ Tracks unique parts of the video watched
- ✅ Resumes video from last position (like YouTube)
- ✅ Fancy visual progress bar
- ✅ "Clear Progress" button to reset
- ✅ Prevents cheating via skipping
- ✅ Real-time progress saving with localStorage

## 🛠 Tech Stack

- HTML, CSS, JavaScript (Frontend)
- Python + Flask (Backend)
- Browser localStorage (for now)

## 🚀 Setup Instructions

1. Install Python (if not installed)
2. Install Flask:
   ```bash
   pip install flask


#Run the app:
python app.py

# Open browser at: http://127.0.0.1:5000

*How It Works*

--Tracking Intervals
Captures time segments while user watches the video.

Uses a custom merging algorithm to calculate unique seconds watched.

Displays progress as a percentage based on total video length.

--Resume Playback
Last watched position is saved in localStorage.

On next visit, the video resumes from that point.

--Challenges Solved
Skipping ahead doesn't count as progress.

Watching the same part twice doesn’t increase percentage.

Data saved without a backend (localStorage).



