
import requests
from bs4 import BeautifulSoup

# Base URL

BASE_URL = "https://subslikescript.com/series/Leave_It_to_Beaver-50032"

# Function to get all episode links

def get_episode_links():
    responce = requests.get(BASE_URL)
    soup = BeautifulSoup(responce.text, "html.parser")

    # FInd all links to episodes
    links = []

    for link in soup.select("a[href^='/series/Leave_It_toBeaver-50032/']"):
        episode_url = "https://subslikescript.com" + link["href"]
        links.append(episode_url)

    return links

# Function to extract transcript from an episode page
def get_transcript(episode_url):
    responce = requiests.get(episode_url)
    soup = BeautifulSoup(responce.text, "html.parser")

    title = soup.find("h1").text.strip() # Extract episode title
    script = soup.find("div", class_="full-script")

    if script:
        transscript_text = script.get_text(separator="\n").strip()
        return {"title": title, "transcript": transcript_text}

    return {"title": title, "transcript": "No transcript found"}

# Main execution
if __name__== "__main__":
    episode_links = get_episode_links()

    for link in episode_links[:5]: # Limit to 5 episodes for testing
       transcript_data = get_transcript(link)
       print(f"Title: {transcript_data['title']}\n")
       print(f"Transcript:\n{transcript_data['transcript']}\n")
       print("=" * 80)


