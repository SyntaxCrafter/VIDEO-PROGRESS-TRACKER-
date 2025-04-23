
# 🎥 Video Progress Tracker

An intelligent lecture video player that tracks actual learning progress by recording **unique watched segments**, preventing skip-based completion, and resuming automatically.

#LIVE LINK - https://video-progress-tracker-l9l6.onrender.com

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



📂 Project Structure

video-progress-tracker/
├── static/                # Contains sample video and CSS files
├── templates/             # HTML templates (rendered using Flask)
├── app.py                 # Main Flask backend
├── data.json              # Stores progress data
├── README.md              # You're here!
├── DESIGN DOCUMENTATION(...) # In-depth explanation of logic & approach
├── .gitignore             # Files and folders to ignore
├── .gitattributes         # Git config for encoding & diff behavior


🛠️ Setup Instructions 
> Ensure you have Python 3.7+ installed.
1. Clone the Repository

git clone https://github.com/SyntaxCrafter/video-progress-tracker.git
cd video-progress-tracker

2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux

3. Install Required Dependencies
pip install flask
4. Run the Application
python app.py
> 🟢 Your app will be live at http://127.0.0.1:5000


✨ How It Works (Design Breakdown)
1. Watched Interval Tracking:
- Tracks video timeupdate events every second.
- Logs timestamps in [start, end] pairs.
- Finalizes and stores them on pause/skip.
2. Persistent Storage:
- Stores intervals in localStorage.
- Automatically resumes from the last watched position.
3. Progress Calculation:
- Merges overlapping intervals.
- Sums them to calculate actual watched percentage.
- Updates a live visual progress bar.
4. Data Management:
- Optional server-side data fallback via data.json.



🧠 Challenges Solved
See DESIGN DOCUMENTATION(...) for details on:
- GitHub large file issues and LFS workaround
- Debugging resume logic
- Managing merged watch intervals


-- Author
Made  by SyntaxCrafter
[https://github.com/SyntaxCrafter]



📌 Future Enhancements
•	User login & cloud sync (instead of just localStorage)
•	Admin dashboard to monitor video stats
•	Responsive UI improvements




