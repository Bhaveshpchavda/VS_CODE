// Get the download button and video URL input field
const downloadBtn = document.getElementById('downloadBtn');
const videoUrlInput = document.getElementById('url');

// Add an event listener to the download button
downloadBtn.addEventListener('click', () => {
    // Get the video ID from the URL
    const videoId = extractVideoId(videoUrlInput.value);
    // Make a request to the YouTube API to get information about the video
    fetch(`https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=YOUR_API_KEY`)
        .then(response => response.json())
        .then(data => {
            // Get the video title and URL from the API response
            const videoTitle = data.items[0].snippet.title;
            const videoUrl = `https://www.youtube.com/watch?v=${videoId}`;
            // Display the video title and download link to the user
            alert(`Video title: ${videoTitle}\nDownload URL: ${videoUrl}`);
        })
        .catch(error => {
            // Handle errors if the API request fails
            console.error(error);
            alert('Error fetching video information.');
        });
});

// Function to extract the video ID from a YouTube video URL
function extractVideoId(url) {
    const videoIdRegex = /(?:\?v=|&v=|youtu\.be\/)(.*?)(?:\?|&|$)/;
    const match = url.match(videoIdRegex);
    return match[1];
}
