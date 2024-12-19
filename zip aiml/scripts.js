document.addEventListener('DOMContentLoaded', function() {
    const apiKey = '337dc0b0d67f56a733ffa34d638fe1e0'; 
    const apiUrl = `https://gnews.io/api/v4/search?q=agriculture&country=in&token=${apiKey}&lang=en`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const newsContainer = document.getElementById('news-container');
            const articles = data.articles;

            if (articles.length === 0) {
                newsContainer.innerHTML = '<p>No agricultural news found.</p>';
                return;
            }

            articles.forEach(article => {
                const articleElement = document.createElement('div');
                articleElement.classList.add('article');
                
                articleElement.innerHTML = `
                    <img src="${article.image || 'https://via.placeholder.com/400x180'}" alt="${article.title}">
                    <h2>${article.title}</h2>
                    <p>${article.description || 'No description available.'}</p>
                    <a href="${article.url}" target="_blank">Read more</a>
                `;
                
                newsContainer.appendChild(articleElement);
            });
        })
        .catch(error => {
            console.error('Error fetching news:', error);
            document.getElementById('news-container').innerHTML = '<p>Failed to load news. Please try again later.</p>';
        });
});
