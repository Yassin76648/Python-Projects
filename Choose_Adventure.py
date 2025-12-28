# Combined and integrated code: GUI + backend logic
import os
import tkinter as tk
from tkinter import messagebox

# Sample knowledge base
knowledge_base = {
    "HTML": {"description": "Structure web pages", "prerequisites": [], "duration_hours": 10, "sources": ["FreeCodeCamp", "MDN"]},
    "CSS": {"description": "Style web pages", "prerequisites": ["HTML"], "duration_hours": 15, "sources": ["FreeCodeCamp", "MDN"]},
    "JavaScript": {"description": "Make web pages interactive", "prerequisites": ["HTML", "CSS"], "duration_hours": 25, "sources": ["JavaScript.info"]},
    "React.js": {"description": "Frontend framework", "prerequisites": ["JavaScript"], "duration_hours": 25, "sources": ["React.dev"]},
    "Python": {"description": "General-purpose programming", "prerequisites": [], "duration_hours": 30, "sources": ["W3Schools"]},
    "SQL": {"description": "Work with databases", "prerequisites": [], "duration_hours": 20, "sources": ["Khan Academy"]},
    "Git": {"description": "Version control", "prerequisites": [], "duration_hours": 10, "sources": ["GitHub Docs"]},
    "GitHub": {"description": "Code hosting platform", "prerequisites": ["Git"], "duration_hours": 6, "sources": ["GitHub Docs"]},
    "Excel": {"description": "Spreadsheets and data analysis", "prerequisites": [], "duration_hours": 12, "sources": ["Microsoft Learn"]},
    "Power BI": {"description": "Interactive data dashboards", "prerequisites": ["Excel"], "duration_hours": 20, "sources": ["LinkedIn Learning"]},
    "Linux Basics": {"description": "Command line and OS basics", "prerequisites": [], "duration_hours": 18, "sources": ["LinuxJourney"]},
    "Networking Basics": {"description": "Networking fundamentals", "prerequisites": [], "duration_hours": 20, "sources": ["Cisco"]},
}

career_paths = {
    "web development": ["HTML", "CSS", "JavaScript", "React.js", "Git", "GitHub"],
    "data analysis": ["Excel", "SQL", "Python", "Power BI"],
    "software engineering": ["Python", "Git", "GitHub", "SQL"],
    "cybersecurity": ["Linux Basics", "Python", "Git", "Networking Basics"],
}

# Logic for generating learning plan
def generate_learning_plan(user_skills_str, has_certificates, daily_hours, career_goal):
    try:
        user_skills = [s.strip().lower() for s in user_skills_str.split(',') if s.strip()]
        daily_hours = float(daily_hours)
    except ValueError:
        return "❌ Please enter a valid number for daily hours."

    if career_goal.lower() not in career_paths:
        return "❌ Sorry, this career path is not supported."

    required_skills = career_paths[career_goal.lower()]
    missing_skills = [skill for skill in required_skills if skill.lower() not in user_skills]

    output = []
    total_hours = 0

    if not missing_skills:
        return "✅ You already have all the required skills!"

    output.append(f"📋 You need to learn {len(missing_skills)} skills:")
    for skill in missing_skills:
        data = knowledge_base.get(skill)
        if data:
            output.append(f"\n🔹 {skill}\n  Description: {data['description']}\n  Estimated time: {data['duration_hours']} hrs\n  Sources: {', '.join(data['sources'])}")
            total_hours += data['duration_hours']

    days_needed = round(total_hours / daily_hours, 1) if daily_hours > 0 else 'N/A'
    output.append(f"\n🕒 Total hours: {total_hours}")
    output.append(f"📆 Estimated duration: {days_needed} days at {daily_hours} hrs/day")
    return "\n".join(output)

# ============ GUI START ============
main = tk.Tk()
main.title(" Expert Career Advisor System ")
main.config(bg="#E4E2E2")
main.geometry("874x650")

label = tk.Label(master=main, text="Current Skills ")
label.config(bg="#897e7e", fg="#fff5f5")
label.place(x=64, y=27, height=37)

entry = tk.Entry(master=main)
entry.config(bg="#fff", fg="#000")
entry.place(x=63, y=73, width=316, height=91)

label1 = tk.Label(master=main, text="Professional Certificates")
label1.config(bg="#9e9797", fg="#ffffff")
label1.place(x=66, y=184, height=40)

entry1 = tk.Entry(master=main)
entry1.config(bg="#fff", fg="#000")
entry1.place(x=70, y=235, width=335, height=40)

label2 = tk.Label(master=main, text="Daily Study Hours")
label2.config(bg="#2b2b2b", fg="#ffffff")
label2.place(x=495, y=16, height=40)

entry2 = tk.Entry(master=main)
entry2.config(bg="#fff", fg="#000")
entry2.place(x=493, y=70, width=116, height=59)

label3 = tk.Label(master=main, text="Desired Career Path")
label3.config(bg="#a6a6a6", fg="#ffffff")
label3.place(x=495, y=176, height=40)

entry3 = tk.Entry(master=main)
entry3.config(bg="#fff", fg="#000")
entry3.place(x=493, y=233, width=366, height=44)

output = tk.Text(master=main)
output.place(x=70, y=500, width=730, height=120)

# Action on button press
def on_generate():
    skills = entry.get()
    certs = entry1.get().strip().lower()
    hours = entry2.get()
    goal = entry3.get()

    has_certs = certs in ['yes', 'true', '1']
    plan = generate_learning_plan(skills, has_certs, hours, goal)

    output.delete("1.0", tk.END)
    output.insert(tk.END, plan)

button = tk.Button(master=main, text="Generate Learning Plan", command=on_generate)
button.config(bg="#4dcae6", fg="#000")
button.place(x=387, y=419, height=40)

main.mainloop()