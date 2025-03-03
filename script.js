function generateCodes() {
    fetch('http://localhost:5000/generate')
        .then(response => response.json())
        .then(data => {
            let codesList = document.getElementById('codes');
            codesList.innerHTML = "";
            data.codes.forEach(code => {
                let li = document.createElement('li');
                li.textContent = code;
                codesList.appendChild(li);
            });
        });
}
