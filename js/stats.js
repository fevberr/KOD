window.s1 = async function() {
    try {
        const tabs = await window.a2();
        const tabNames = Object.keys(tabs);

        const allModules = new Set();
        for (const modules of Object.values(tabs)) {
            for (const m of modules) {
                allModules.add(m);
            }
        }
        const totalModules = allModules.size;

        document.getElementById('b4').textContent = totalModules;
        document.getElementById('b4').className = 'num';
        document.getElementById('b5').textContent = tabNames.length;
        document.getElementById('b5').className = 'num';

        document.getElementById('b6').textContent =
            totalModules === 1 ? '1 module' : `${totalModules} modules`;

        const tabContent = document.getElementById('b7');
        if (tabNames.length > 0) {
            let html = '';
            for (const tabName of tabNames) {
                const modules = tabs[tabName] || [];
                html += `
                    <div class="tab-group">
                        <div class="tab-header">
                            <span class="tag">
                                <i class="fas fa-folder"></i>
                                ${tabName}
                                <span class="count">${modules.length}</span>
                            </span>
                        </div>
                        <ul class="module-list">
                            ${modules.map(m => {
                                const ext = m.includes('.') ? m.split('.').pop() : '';
                                return `<li>${m} <span class="ext">${ext}</span></li>`;
                            }).join('')}
                            ${modules.length === 0 ? '<li class="empty"><i class="fas fa-hourglass-half"></i> coming soon...</li>' : ''}
                        </ul>
                    </div>
                `;
            }
            tabContent.innerHTML = html;
        } else {
            tabContent.innerHTML = '<span style="color:#2a3b55; font-size:0.85rem;">Recon Tab · example · coming</span>';
        }

        // Discord stats
        const version = await window.a3();
        document.getElementById('a3').textContent = version;

        const commit = await window.a4();
        document.getElementById('e2').innerHTML = `
            <div class="discord-stat">
                <i class="fas fa-tag"></i>
                <div class="num">${version}</div>
                <span class="label">latest version</span>
            </div>
            <div class="discord-stat">
                <i class="fas fa-code-branch"></i>
                <div class="num">${commit.sha}</div>
                <span class="label">latest commit</span>
            </div>
            <div class="discord-stat">
                <i class="fas fa-calendar-alt"></i>
                <div class="num">${commit.date}</div>
                <span class="label">last update</span>
            </div>
            <div class="discord-stat">
                <i class="fas fa-database"></i>
                <div class="num">${totalModules}</div>
                <span class="label">total modules</span>
            </div>
        `;

        // Benefits
        document.getElementById('c2').innerHTML = `
            <div class="benefit">
                <div class="icon"><i class="fas fa-shield-alt"></i></div>
                <h4>100% Virus Free</h4>
                <p>Every release is thoroughly scanned and verified No malware no bloatware.</p>
            </div>
            <div class="benefit">
                <div class="icon"><i class="fas fa-check-circle"></i></div>
                <h4>Always Tested</h4>
                <p>Each update undergoes rigorous testing on all supported platforms before release.</p>
            </div>
            <div class="benefit">
                <div class="icon"><i class="fas fa-window-restore"></i></div>
                <h4>Cross-Platform</h4>
                <p>Works on <strong>Windows</strong>, <strong>Linux</strong>, <strong>Termux</strong>, and <strong>iSH</strong>.</p>
            </div>
            <div class="benefit">
                <div class="icon"><i class="fas fa-sync-alt"></i></div>
                <h4>Auto-Detection</h4>
                <p>Automatically detects your <strong>device</strong>, <strong>OS</strong>, <strong>IP</strong>, and <strong>ping</strong>.</p>
            </div>
            <div class="benefit">
                <div class="icon"><i class="fas fa-users"></i></div>
                <h4>Community Driven</h4>
                <p>Built with input from real users Features shaped by the community.</p>
            </div>
            <div class="benefit">
                <div class="icon"><i class="fas fa-sync-alt"></i></div>
                <h4>Always Updated</h4>
                <p>Regular updates with new features improvements and security patches.</p>
            </div>
        `;

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('b4').textContent = '?';
        document.getElementById('b4').className = 'num error';
        document.getElementById('b5').textContent = '?';
        document.getElementById('b5').className = 'num error';
        document.getElementById('b6').textContent = '—';
        document.getElementById('b7').innerHTML =
            '<span style="color:#2a3b55; font-size:0.85rem;">Recon Tab · example · coming</span>';
    }
};
