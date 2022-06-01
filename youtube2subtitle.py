import sys
from youtube_transcript_api import YouTubeTranscriptApi
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Command instruction: youtube2subtitle.py <video-id> <lang>')
        sys.exit()
        
    # Example YT Link: 'https://youtu.be/lWso7m97W0I'
    # then video_id: 'lWso7m97W0I'
    scripts = YouTubeTranscriptApi.get_transcript(
        video_id=sys.argv[1],
        languages=[sys.argv[2]]
    )

    # write subtitle to file
    subtitle = ' '.join([item['text'] for item in scripts])
        
    with open('subtitle.txt', 'w', encoding='utf-8') as fs:
        fs.write(subtitle)
