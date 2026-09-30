from bs4 import BeautifulSoup
import pandas as pd

with open("job_listings.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

print("Page Title:", soup.title.text)

jobs = soup.find_all("div", class_="job-card")

print("Number of jobs found:", len(jobs))

data = []

for job in jobs:
    title_tag = job.select_one(".job-title")
    company_tag = job.select_one(".company")
    location_tag = job.select_one(".location")
    skills_tag = job.select_one(".skills")
    link_tag = job.select_one(".job-link")

    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    company = company_tag.get_text(strip=True) if company_tag else "N/A"
    location = location_tag.get_text(strip=True) if location_tag else "N/A"
    skills = skills_tag.get_text(strip=True) if skills_tag else "N/A"
    link = link_tag.get("href", "") if link_tag else ""

    data.append({
        "job_title": title,
        "company": company,
        "location": location,
        "skills": skills,
        "job_link": link
    })

df = pd.DataFrame(data)

print("\nJob Summary:")
print("Total Jobs:", len(df))
print("Remote Jobs:", (df["location"].str.lower() == "remote").sum())
print("Unique Locations:", df["location"].nunique())

from collections import Counter

all_skills = []

for skills in df["skills"]:
    skill_list = [skill.strip() for skill in skills.split(",")]
    all_skills.extend(skill_list)

skill_counts = Counter(all_skills)

print("\nSkill Frequency:")
for skill, count in skill_counts.most_common():
    print(skill, ":", count)

print("\nScraped Job Data:")
print(df)