
import requests
from bs4 import BeautifulSoup
import re

# Base URL

BASE_URL = "https://subslikescript.com/series/Little_House_on_the_Prairie-71007"
sub_url = BASE_URL[26:]
folder = "little_trans"
showTitle = sub_url[8]

# Function to get all episode links

def get_episode_links():
    responce = requests.get(BASE_URL)
    soup = BeautifulSoup(responce.text, "html.parser")


    # FInd all links to episodes
    links = []

    for link in soup.select(f"a[href^='{sub_url}']"):
        episode_url = "https://subslikescript.com" + link["href"]
        links.append(episode_url)

    print(f"{len(links)} Episodes")
    return links

# Function to extract transcript from an episode page
def get_transcript(episode_url):
    responce = requests.get(episode_url)
    soup = BeautifulSoup(responce.text, "html.parser")

    title = soup.find("h1").text.strip() # Extract episode title
    script = soup.find("div", class_="full-script")

    if script:
        transcript_text = script.get_text(separator=" ").strip()
        return {"title": title, "transcript": transcript_text}

    return {"title": title, "transcript": "No transcript found"}

def save_transcript(episode_url):
    responce = requests.get(episode_url)
    soup = BeautifulSoup(responce.text, "html.parser")

    title = soup.find("h1").text.strip() # Extract episode title
    script = soup.find("div", class_="full-script")

    if script:
        transcript_text = script.get_text(separator="\n").strip()

    else: 
        transcript_text = "No transcript found"

    # Clean the fifle to create a valid filename
    fullFilename = f"{folder}/{title.replace(' ', '_').replace('/', '_').replace(',','')}.txt"

    filename = re.sub(rf"{showTitle}.*:_","", fullFilename)

    # Save to a file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n\n")
        file.write(transcript_text)

    print(f"Saved: {filename}")


# Main execution
if __name__== "__main__":
    episode_links = get_episode_links()

    ## Output Information
    
    #for link in episode_links[:5]: # Limit to 5 episodes for testing
    #   transcript_data = get_transcript(link)
    #   print(f"Title: {transcript_data['title']}\n")
    #   print(f"Transcript:\n{transcript_data['transcript']}***")
    #   print("=" * 80)
    
    ## Save to File

    for link in episode_links[5:30]:
        save_transcript(link)
    
    #get_episode_links()
