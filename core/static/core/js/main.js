document.addEventListener('DOMContentLoaded', function () {

    // ---------- 1. Click-to-flip cards ----------
    const cards = document.querySelectorAll('.flip-card');
    cards.forEach(function (card) {
        card.addEventListener('click', function () {
            card.classList.toggle('flipped');
            playFlipSound();
        });
    });

    function playFlipSound() {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();

        if (ctx.state === 'suspended') {
            ctx.resume();
        }

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(500, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(800, ctx.currentTime + 0.1);

        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.15);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(ctx.currentTime);
        osc.stop(ctx.currentTime + 0.15);
    }

    // ---------- 3. Shuffle button ----------
    const shuffleBtn = document.querySelector('.shuffle-button');
    const grid = document.querySelector('.project-grid');

    if (shuffleBtn && grid) {
        shuffleBtn.addEventListener('click', function () {
            const cards = Array.from(grid.children);
            const gridRect = grid.getBoundingClientRect();
            const centerX = gridRect.width / 2;
            const centerY = gridRect.height / 2;

            playShuffleSound();

            // Phase 1: gather all cards toward the center
            cards.forEach(function (card) {
                const rect = card.getBoundingClientRect();
                const cx = rect.left - gridRect.left + rect.width / 2;
                const cy = rect.top - gridRect.top + rect.height / 2;
                const dx = centerX - cx;
                const dy = centerY - cy;

                card.style.transition = 'transform 0.35s ease, opacity 0.35s ease';
                card.style.transform = `translate(${dx}px, ${dy}px) scale(0.35) rotate(${(Math.random() * 30 - 15).toFixed(1)}deg)`;
                card.style.opacity = '0.6';
                card.style.zIndex = '10';
            });

            setTimeout(function () {
                // shuffle the actual order (Fisher-Yates)
                for (let i = cards.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [cards[i], cards[j]] = [cards[j], cards[i]];
                }
                cards.forEach(function (card) {
                    grid.appendChild(card);
                });

                // Phase 2: position cards back at center (no transition), ready to fly out
                cards.forEach(function (card) {
                    const newRect = card.getBoundingClientRect();
                    const cx = newRect.left - gridRect.left + newRect.width / 2;
                    const cy = newRect.top - gridRect.top + newRect.height / 2;
                    const dx = centerX - cx;
                    const dy = centerY - cy;

                    card.style.transition = 'none';
                    card.style.transform = `translate(${dx}px, ${dy}px) scale(0.35) rotate(${(Math.random() * 30 - 15).toFixed(1)}deg)`;
                    card.style.opacity = '0.6';
                });

                void grid.offsetWidth; // force reflow so the "none" transition actually applies first

                // Phase 3: fly out to final resting positions
                cards.forEach(function (card) {
                    card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
                    card.style.transform = 'translate(0, 0) scale(1) rotate(0deg)';
                    card.style.opacity = '1';
                    card.style.zIndex = '';
                });
            }, 350);
        });
    }

    function playShuffleSound() {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        if (ctx.state === 'suspended') ctx.resume();

        const duration = 0.6;
        const bufferSize = ctx.sampleRate * duration;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);

        for (let i = 0; i < bufferSize; i++) {
            const t = i / ctx.sampleRate;
            const flutter = Math.abs(Math.sin(t * 45)) > 0.3 ? 1 : 0.2; // pulsing = riffle flutter
            data[i] = (Math.random() * 2 - 1) * flutter * 0.35;
        }

        const noise = ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.value = 2500;
        filter.Q.value = 0.7;

        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);

        noise.start();
        noise.stop(ctx.currentTime + duration);
    }

    // ---------- 4. Confetti on contact form success ----------
    const successMessage = document.querySelector('.success-message');
    if (successMessage) {
        launchConfetti();
    }

    function launchConfetti() {
        const colors = ['#a8d8ea', '#f7b8d0', '#b8e6d0', '#ffe27a'];
        for (let i = 0; i < 40; i++) {
            const piece = document.createElement('div');
            piece.className = 'confetti-piece';
            piece.style.left = Math.random() * 100 + 'vw';
            piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            piece.style.animationDelay = Math.random() * 0.5 + 's';
            document.body.appendChild(piece);

            setTimeout(function () {
                piece.remove();
            }, 3000);
        }
    }

});