window.f1 = function() {
    const f1 = [
        {
            category: "General",
            questions: [
                { q: "How do I download 23 KOD?", a: "You can download it only from our <span class='highlight'>Discord</span> community Join and go to the <span class='highlight'>#downloads</span> channel to get the latest version" },
                { q: "What license is 23 KOD released under?", a: "23 KOD is open-source and licensed under the <span class='highlight'>MIT License</span> This means you can use modify and distribute it freely even for commercial purposes" },
                { q: "What operating systems does 23 KOD support?", a: "23 KOD is designed to be cross-platform It runs on<br><ul><li><span class='highlight'>Windows</span> via PowerShellCMD</li><li><span class='highlight'>Linux</span> through GNOME Terminal</li><li><span class='highlight'>Termux</span> on Android</li><li><span class='highlight'>iSH</span> on iOS</li></ul>" }
            ]
        },
        {
            category: "Technical",
            questions: [
                { q: "What Python version is required to run 23 KOD?", a: "23 KOD requires <span class='highlight'>Python 3.6</span> or a higher version to function correctly" }
            ]
        }
    ];

    function f2(filter = '') {
        const container = document.getElementById('d4');
        const noResults = document.getElementById('d5');
        let html = '';
        let total = 0;
        const searchTerm = filter.toLowerCase().trim();

        f1.forEach(category => {
            let categoryHtml = '';
            let hasVisible = false;

            category.questions.forEach(item => {
                const match = searchTerm === '' ||
                    item.q.toLowerCase().includes(searchTerm) ||
                    item.a.toLowerCase().includes(searchTerm);
                if (match) {
                    hasVisible = true;
                    total++;
                    const id = `faq-${total}`;
                    categoryHtml += `
                        <div class="faq-item" id="${id}">
                            <div class="faq-question" onclick="window.f3('${id}')">
                                <i class="fas fa-chevron-right"></i>
                                ${item.q}
                                <span class="arrow"><i class="fas fa-chevron-right"></i></span>
                            </div>
                            <div class="faq-answer">${item.a}</div>
                        </div>
                    `;
                }
            });

            if (hasVisible) {
                html += `
                    <div class="faq-category">
                        <div class="faq-category-title">${category.category}</div>
                        ${categoryHtml}
                    </div>
                `;
            }
        });

        container.innerHTML = html;
        document.getElementById('d2').textContent = `${total} questions`;

        if (total === 0 && searchTerm !== '') {
            noResults.classList.add('show');
        } else {
            noResults.classList.remove('show');
        }
    }

    window.f3 = function(id) {
        const item = document.getElementById(id);
        if (item) {
            item.classList.toggle('open');
            document.querySelectorAll('.faq-item').forEach(other => {
                if (other.id !== id) {
                    other.classList.remove('open');
                }
            });
        }
    };

    document.getElementById('d3').addEventListener('input', function() {
        f2(this.value);
    });

    f2();
};
