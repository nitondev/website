    fetch('https://api.github.com/repos/nitondev/website/commits')
      .then(response => response.json())
      .then(data => {
        const fullSha = data[0].sha;
        const shortSha = fullSha.substring(0, 7);
        const commitUrl = `https://github.com/nitondev/website/commit/${fullSha}`;
        
        // Update the version display with link
        const versionElement = document.getElementById('version');
        versionElement.innerHTML = `site version: <a href="${commitUrl}" target="_blank">${shortSha}</a>`;
      })
      .catch(error => {
        console.error('Error fetching commit:', error);
        document.getElementById('version').textContent = 'site version: unknown';
      });
