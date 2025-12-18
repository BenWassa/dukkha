document.addEventListener('DOMContentLoaded', () => {
    // Check if the Neural Compass exists on this page
    const magnet = document.getElementById('magnet');
    if (!magnet) return; // Exit if not on Myths page

    // 1. MAGNET PHYSICS
    magnet.addEventListener('mousemove', (e) => {
        const rect = magnet.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        
        // Strength divisor (Higher = Less pull)
        magnet.style.transform = `translate(${x / 4}px, ${y / 4}px)`;
    });

    magnet.addEventListener('mouseleave', () => {
        magnet.style.transform = `translate(0px, 0px)`;
    });

    // 2. SCROLL PROGRESS RING
    const ringFill = document.getElementById('ringFill');
    const circumference = 238; // 2 * pi * 38

    const updateRing = () => {
        const collection = document.getElementById('myth-collection');
        if (!collection || !ringFill) return;
        const rect = collection.getBoundingClientRect();
        const top = window.scrollY;
        const start = collection.offsetTop;
        const total = Math.max(1, collection.offsetHeight - window.innerHeight);
        const scrolled = Math.max(0, Math.min(1, (window.scrollY - start) / total));
        const offset = circumference - (scrolled * circumference);
        ringFill.style.strokeDashoffset = offset;
    };

    window.addEventListener('scroll', () => requestAnimationFrame(updateRing));
    // initialize
    updateRing();

    // 3. SECTION TRACKING (Blur Reveal)
    const compassNum = document.getElementById('compassNum');
    const compassLabel = document.getElementById('compassLabel');
    
    // Target both the Hero (for Intro) and the Myth Cards
    const trackableSections = document.querySelectorAll('.myths-hero, .myth-card');
    
    let currentRoman = "0"; 

    const liveRegion = document.getElementById('compassLive');
    const mythsList = Array.from(document.querySelectorAll('.myth-card[data-roman]'));

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                // Get data attributes we added in Step 1
                const newRoman = entry.target.getAttribute('data-roman');
                const newTitle = entry.target.getAttribute('data-title');

                if(newRoman && newRoman !== currentRoman) {
                    currentRoman = newRoman;
                    
                    // Update Label
                    if(compassLabel && newTitle) compassLabel.innerText = newTitle;

                    // Blur Snap Animation
                    if(compassNum) {
                        compassNum.classList.add('blur-out');
                        setTimeout(() => {
                            compassNum.innerText = newRoman;
                            compassNum.classList.remove('blur-out');
                        }, 300); // Matches CSS transition time
                    }

                    // Accessibility: announce via live region
                    if (liveRegion) {
                        let announcement = newTitle || newRoman;
                        // If this is a myth card, compute its index among myths
                        if (newRoman !== '0') {
                            const idx = mythsList.findIndex(m => m === entry.target);
                            if (idx !== -1) {
                                announcement = `${newTitle}. Myth ${idx + 1} of ${mythsList.length}`;
                            }
                        } else {
                            announcement = `Introduction`;
                        }
                        liveRegion.innerText = announcement;
                    }
                }
            }
        });
    }, { threshold: 0.25 }); // Trigger when 25% of section is visible

    trackableSections.forEach(sec => observer.observe(sec));
});