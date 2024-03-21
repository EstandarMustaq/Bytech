document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('searchForm');
    const queryInput = document.getElementById('query');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const query = queryInput.value;

        fetch('/search', {
            method: 'POST',
            body: JSON.stringify({ query: query }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            return response.text();
        })
        .then(data => {
            // Redireciona para a página de resultados
            window.location.href = `/results?query=${encodeURIComponent(query)}`;
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });
});

// Função para enviar o formulário de contato
document.getElementById('contactForm').addEventListener('submit', function(event) {
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  // Verifica se todos os campos estão preenchidos
  if (!name || !email || !message) {
    alert('Por favor, preencha todos os campos.');
    event.preventDefault();
  }
});


