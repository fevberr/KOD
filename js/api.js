window.a1 = async function() {
    try {
        const b1 = await fetch(`https://raw.githubusercontent.com/${window.r1}/${window.r2}/display/banner.py`);
        if (!b1.ok) throw new Error('Failed to fetch banner');
        const b2 = await b1.text();
        const b3 = b2.match(/b2\s*=\s*r("""|''')([\s\S]*?)\1/);
        if (b3) {
            let b4 = b3[2];
            const b5 = b4.split('\n');
            const b6 = Math.min(...b5.filter(l => l.trim()).map(l => l.match(/^\s*/)[0].length));
            const b7 = b5.map(l => l.slice(b6)).join('\n');
            document.getElementById('b2').textContent = b7;
        } else {
            const b8 = b2.match(/r("""|''')([\s\S]*?)\1/);
            if (b8) {
                document.getElementById('b2').textContent = b8[2];
            } else {
                throw new Error('Banner not found');
            }
        }
    } catch (e) {
        document.getElementById('b2').innerHTML = `
banner
        `;
    }
};

window.a2 = async function() {
    try {
        const c1 = await fetch(`https://raw.githubusercontent.com/${window.r1}/${window.r2}/config.py`);
        if (!c1.ok) throw new Error('Failed to fetch config');
        const c2 = await c1.text();
        const c3 = c2.match(/TABS\s*=\s*\{([^}]*)\}/s);
        if (!c3) return {};
        const c4 = c3[1];
        const c5 = {};
        const c6 = /["']([^"']+)["']\s*:\s*\[([^\]]*)\]/g;
        let c7;
        while ((c7 = c6.exec(c4)) !== null) {
            const c8 = c7[1];
            const c9 = c7[2].split(',').map(m => m.trim().replace(/["']/g, '')).filter(m => m);
            c5[c8] = c9;
        }
        return c5;
    } catch (e) {
        return {};
    }
};

window.a3 = async function() {
    try {
        const d1 = await fetch(`https://raw.githubusercontent.com/${window.r1}/${window.r2}/data/version.txt`);
        if (!d1.ok) throw new Error('Failed to fetch version');
        return (await d1.text()).trim();
    } catch {
        return '0.0.0';
    }
};

window.a4 = async function() {
    try {
        const e1 = await fetch(`https://api.github.com/repos/${window.r1}/commits/${window.r2}`);
        if (!e1.ok) throw new Error('Failed to fetch commit');
        const e2 = await e1.json();
        return {
            sha: e2.sha.substring(0, 7),
            date: new Date(e2.commit.committer.date).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            })
        };
    } catch {
        return { sha: '—', date: '—' };
    }
};
