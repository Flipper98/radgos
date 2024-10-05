// static/js/script.js
async function search() {
    const query = document.getElementById('searchInput').value;
    
    if (!query) {
        alert('Пожалуйста, введите запрос для поиска.');
        return;
    }

    const response = await fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    });

    if (response.ok) {
        const results = await response.json();
        displayResults(results);
    } else {
        console.error('Ошибка при получении данных');
    }
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>Ничего не найдено</p>';
        return;
    }

    results.forEach(result => {
        const resultItem = document.createElement('div');
        resultItem.className = 'result-item';
        resultItem.innerHTML = `
            <h2><a href="${result.link}" target="_blank">${result.title}</a></h2>
            <p>${result.content}</p>
        `;
        resultsDiv.appendChild(resultItem);
    });
}
