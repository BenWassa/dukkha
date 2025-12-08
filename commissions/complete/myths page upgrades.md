Use the following code as inspiration for upgrades to myths page:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Decoding Dopamine & Desire - Project Dukkha</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&display=swap" rel="stylesheet">
    
    <style>
        /* --- CSS VARIABLES & RESET --- */
        :root {
            --color-accent: #C9A961;
            --color-accent-light: #E8DCC2;
            --color-accent-faint: rgba(201, 169, 97, 0.1);
            --color-bg: #FAFAF9;
            --color-surface: #FFFFFF;
            --color-border: #E7E5E4;
            --color-text-main: #1F2937;
            --color-text-muted: #6B7280;
            --color-text-light: #9CA3AF;
            --color-success: #10B981;
            --color-error: #EF4444;
            
            --font-sans: 'Inter', sans-serif;
            --font-serif: 'Merriweather', serif;
            
            --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --radius-lg: 1rem;
            --radius-full: 9999px;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        html { scroll-behavior: smooth; }

        body {
            background-color: var(--color-bg);
            font-family: var(--font-sans);
            color: var(--color-text-main);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }

        /* --- TYPOGRAPHY --- */
        h1, h2, h3 { font-family: var(--font-serif); }
        
        .text-accent { color: var(--color-accent); }
        .text-serif { font-family: var(--font-serif); }
        .font-bold { font-weight: 700; }
        .italic { font-style: italic; }
        .uppercase { text-transform: uppercase; }
        .tracking-wide { letter-spacing: 0.05em; }

        /* --- LAYOUT UTILS --- */
        .container {
            max-width: 64rem; /* approx 1024px */
            margin: 0 auto;
            padding: 0 1rem;
        }

        .flex { display: flex; }
        .flex-col { flex-direction: column; }
        .items-center { align-items: center; }
        .justify-center { justify-content: center; }
        .justify-between { justify-content: space-between; }
        .gap-2 { gap: 0.5rem; }
        .gap-3 { gap: 0.75rem; }
        .gap-4 { gap: 1rem; }
        
        /* --- HEADER --- */
        header {
            background: var(--color-surface);
            border-bottom: 1px solid var(--color-border);
            padding: 5rem 1rem 4rem;
            text-align: center;
        }

        .badge {
            display: inline-block;
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--color-text-muted);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            box-shadow: var(--shadow-sm);
            margin-bottom: 1.5rem;
        }

        h1 {
            font-size: 2.5rem;
            line-height: 1.2;
            margin-bottom: 1.5rem;
            color: #1C1917;
        }

        header p {
            font-size: 1.125rem;
            color: var(--color-text-muted);
            max-width: 42rem;
            margin: 0 auto;
        }

        /* --- NAVIGATION --- */
        .sticky-nav {
            position: sticky;
            top: 1rem;
            z-index: 100;
            display: none; /* Hidden on mobile */
            justify-content: center;
            gap: 1rem;
            margin-bottom: 4rem;
            padding: 1rem 0;
            background: rgba(250, 250, 249, 0.85);
            backdrop-filter: blur(8px);
        }

        .nav-pill {
            text-decoration: none;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--color-text-light);
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            padding: 0.5rem 1rem;
            border-radius: var(--radius-full);
            transition: all 0.2s ease;
        }

        .nav-pill:hover {
            color: var(--color-accent);
            border-color: var(--color-accent);
        }

        /* --- MYTH CARD --- */
        .myth-card {
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            overflow: hidden;
            margin-bottom: 3rem;
            box-shadow: var(--shadow-sm);
            scroll-margin-top: 6rem; /* for smooth scroll anchor positioning */
        }

        .card-grid {
            display: grid;
            grid-template-columns: 1fr;
        }

        /* Visual Column */
        .col-visual {
            background-color: #FAFAF9; /* Stone-50 */
            border-bottom: 1px solid var(--color-border);
            padding: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        
        .gold-gradient-line {
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, transparent, var(--color-accent), transparent);
            opacity: 0.5;
        }

        /* Content Column */
        .col-content {
            padding: 2rem;
            display: flex;
            flex-direction: column;
        }

        .myth-label {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1rem;
        }

        .myth-tag {
            background: var(--color-accent-faint);
            color: var(--color-accent);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-full);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .myth-line {
            height: 1px;
            background: var(--color-border);
            flex-grow: 1;
        }

        .myth-text {
            font-family: var(--font-serif);
            font-size: 1.5rem;
            color: var(--color-text-light);
            text-decoration: line-through;
            text-decoration-color: rgba(201, 169, 97, 0.6);
            text-decoration-thickness: 2px;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }

        .truth-text {
            font-family: var(--font-serif);
            font-size: 1.5rem;
            color: #1C1917; /* Stone 900 */
            font-weight: 700;
            line-height: 1.3;
        }

        .description {
            color: #4B5563; /* Stone 600 */
            margin-bottom: 2rem;
            font-size: 1rem;
        }
        
        .description p { margin-bottom: 1rem; }
        .description p:last-child { margin-bottom: 0; }

        /* Action Box */
        .action-box {
            background: var(--color-accent-faint);
            border-left: 4px solid var(--color-accent);
            padding: 1.5rem;
            border-radius: 0 0.5rem 0.5rem 0;
            margin-bottom: 1.5rem;
        }

        .protocol-label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
            color: #1C1917;
        }

        .protocol-title {
            font-family: var(--font-serif);
            font-size: 1.125rem;
            font-style: italic;
            color: #44403C;
            margin-bottom: 0.5rem;
        }

        .protocol-desc {
            font-size: 0.875rem;
            color: #57534E;
        }

        /* Citations (Details/Summary) */
        details {
            border-top: 1px solid var(--color-border);
            padding-top: 1rem;
            margin-top: auto;
        }

        summary {
            list-style: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--color-text-light);
            transition: color 0.2s;
        }

        summary:hover { color: var(--color-accent); }
        summary::-webkit-details-marker { display: none; } /* Hide default triangle */

        .citations-list {
            margin-top: 1rem;
            background: #FAFAF9;
            padding: 1rem;
            border-radius: 0.5rem;
            font-size: 0.75rem;
            color: var(--color-text-muted);
            animation: fadeIn 0.3s ease-out;
        }
        
        .citation-item { display: flex; gap: 0.5rem; margin-bottom: 0.5rem; }
        .cite-num { color: var(--color-accent); font-family: monospace; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* --- VISUALIZATIONS (CSS ART) --- */
        .visual-container { width: 100%; max-width: 280px; }
        
        /* 1. Dukkha */
        .dukkha-box {
            background: white;
            border: 2px solid var(--color-accent);
            padding: 1rem;
            border-radius: 0.75rem;
            position: relative;
            box-shadow: var(--shadow-md);
            text-align: center;
            z-index: 2;
        }
        .dukkha-arrow {
            position: absolute;
            top: -20px; left: 50%;
            transform: translateX(-50%) rotate(90deg);
            color: var(--color-accent);
        }
        .dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 6px; }
        .dot-red { background: #F87171; }
        .dot-orange { background: #FB923C; }
        .dot-yellow { background: #FACC15; }

        /* 2. Dopamine */
        .bar-container {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            height: 160px;
            gap: 1rem;
        }
        .bar-wrapper {
            width: 48%;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            height: 100%;
            cursor: pointer;
        }
        .bar {
            width: 100%;
            border-radius: 0.5rem 0.5rem 0 0;
            transition: all 0.3s;
        }
        .bar-wanting {
            height: 90%;
            background: var(--color-accent);
            position: relative;
            overflow: hidden;
        }
        .bar-pulse {
            position: absolute;
            inset: 0;
            background: rgba(255,255,255,0.3);
            animation: pulse 2s infinite;
        }
        .bar-liking {
            height: 30%;
            background: #D6D3D1;
        }
        .bar-wrapper:hover .bar-liking { background: #A8A29E; }
        .bar-wrapper:hover .bar-wanting { box-shadow: 0 0 15px rgba(201,169,97,0.4); }
        
        @keyframes pulse { 0% { opacity: 0; } 50% { opacity: 1; } 100% { opacity: 0; } }

        /* 3. Paths */
        .paths-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            width: 100%;
        }
        .path-col { display: flex; flex-direction: column; align-items: center; }
        .path-line-container {
            width: 100%; height: 2px; background: #D6D3D1;
            position: relative; margin-bottom: 1.5rem;
        }
        .branch-line {
            position: absolute; width: 50%; height: 100%;
            background: #D6D3D1; top: 0;
        }
        .branch-left { right: 0; transform-origin: left center; transform: rotate(-45deg) translateY(12px); }
        .branch-right { left: 0; transform-origin: right center; transform: rotate(45deg) translateY(12px); }
        
        .box-red { background: #FEF2F2; border: 1px solid #FECACA; color: #991B1B; padding: 0.75rem; border-radius: 0.5rem; width: 100%; text-align: center; }
        .box-green { background: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46; padding: 0.75rem; border-radius: 0.5rem; width: 100%; text-align: center; }

        /* 4. Tolerance */
        .tolerance-card {
            background: white;
            padding: 1rem;
            border-radius: 0.75rem;
            border: 1px solid var(--color-border);
            width: 100%;
        }
        .receptor-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .receptor-dots { display: flex; gap: 4px; }
        .rec-dot { width: 8px; height: 16px; border-radius: 2px; }
        .rec-active { background: var(--color-accent); opacity: 0.8; }
        .rec-burnt { background: #D6D3D1; }
        .rec-empty { border: 1px solid #E5E7EB; }

        /* 5. Middle Way */
        .arc-svg { width: 100%; height: auto; }
        .needle { transform-origin: bottom center; animation: wiggle 4s ease-in-out infinite; }
        @keyframes wiggle { 0%, 100% { transform: rotate(-10deg); } 50% { transform: rotate(10deg); } }


        /* --- RESPONSIVE MEDIA QUERIES --- */
        @media (min-width: 768px) {
            h1 { font-size: 3.5rem; }
            
            .sticky-nav { display: flex; }

            .card-grid {
                grid-template-columns: 4fr 8fr; /* 4 columns visual, 8 content */
            }

            .col-visual {
                border-bottom: none;
                border-right: 1px solid var(--color-border);
            }
            
            .col-content { padding: 2.5rem; }
        }
        
        /* Icons */
        .icon { width: 20px; height: 20px; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
        .icon-sm { width: 16px; height: 16px; }
        .icon-lg { width: 24px; height: 24px; }
        .icon-green { color: var(--color-success); }
        .icon-accent { color: var(--color-accent); }

        /* Footer */
        footer {
            border-top: 1px solid var(--color-border);
            padding: 3rem 1rem;
            text-align: center;
            background: white;
        }
        
        .footer-logo {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-serif);
            font-weight: 700;
            font-size: 1.25rem;
            color: #1C1917;
            margin-bottom: 1rem;
        }
        .logo-circle {
            width: 24px; height: 24px;
            border: 2px solid var(--color-accent);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .logo-dot { width: 8px; height: 8px; background: var(--color-accent); border-radius: 50%; }

    </style>
</head>
<body>

    <header>
        <div class="container">
            <span class="badge">Field Guide</span>
            <h1>Decoding <span class="italic text-accent">Dopamine</span> & Desire</h1>
            <p>We often suffer not because of reality, but because of our misconceptions about it. Here are the five most common myths about motivation and Buddhist psychology, debunked with science.</p>
        </div>
    </header>

    <main class="container">
        
        <!-- Navigation -->
        <nav class="sticky-nav">
            <a href="#myth-1" class="nav-pill">1. Suffering</a>
            <a href="#myth-2" class="nav-pill">2. Dopamine</a>
            <a href="#myth-3" class="nav-pill">3. Desire</a>
            <a href="#myth-4" class="nav-pill">4. Detox</a>
            <a href="#myth-5" class="nav-pill">5. Emotions</a>
        </nav>

        <!-- Myth 1 -->
        <article id="myth-1" class="myth-card">
            <div class="card-grid">
                <!-- Visual -->
                <div class="col-visual">
                    <div class="gold-gradient-line"></div>
                    <div class="visual-container">
                        <div style="text-align: center; margin-bottom: 1.5rem;">
                            <span class="text-serif italic" style="color:#9CA3AF; display:block; margin-bottom: 0.25rem;">Common Misconception</span>
                            <div style="background:#E7E5E4; color:#57534E; padding: 0.5rem; border-radius: 0.5rem; font-family: monospace; font-size: 0.875rem;">Dukkha = Pain ❌</div>
                        </div>
                        <div style="position: relative; padding-top: 2rem;">
                            <!-- Arrow Icon -->
                            <svg class="icon icon-lg dukkha-arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            
                            <div class="dukkha-box">
                                <div style="margin-bottom: 1rem;">
                                    <span class="text-serif font-bold" style="font-size: 1.25rem; display: block; color: #1C1917;">Unsatisfactoriness</span>
                                    <span class="uppercase" style="font-size: 0.7rem; color: #78716C; letter-spacing: 0.05em;">The Nuanced Reality</span>
                                </div>
                                <div style="text-align: left; font-size: 0.875rem; color: #57534E; display: flex; flex-direction: column; gap: 0.5rem;">
                                    <div class="flex items-center"><span class="dot dot-red"></span> Pain</div>
                                    <div class="flex items-center"><span class="dot dot-orange"></span> Change / Impermanence</div>
                                    <div class="flex items-center"><span class="dot dot-yellow"></span> Subtle Dissatisfaction</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Content -->
                <div class="col-content">
                    <div class="myth-label">
                        <span class="myth-tag">Myth #1</span>
                        <div class="myth-line"></div>
                    </div>
                    <h3 class="myth-text">"Buddhism says 'Life is Suffering,' so it's pessimistic."</h3>
                    <div class="flex items-center gap-3" style="margin-bottom: 1.5rem;">
                        <svg class="icon icon-lg icon-green" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                        <h3 class="truth-text">Dukkha signifies Unsatisfactoriness, not just Pain.</h3>
                    </div>
                    <div class="description">
                        <p>The First Noble Truth is often mistranslated. <em>Dukkha</em> refers to a profound sense of "unsatisfactoriness," "stress," or "inherent incompleteness" that pervades conditioned existence. It isn't a denial of happiness, but an observation that even pleasant experiences are fleeting.</p>
                        <p>When we cling to temporary states as if they were permanent, we create friction. The teaching is actually optimistic: it identifies the problem solely to offer a cure.</p>
                    </div>
                    <div class="action-box">
                        <div class="protocol-label">
                            <svg class="icon icon-accent" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                            Protocol
                        </div>
                        <p class="protocol-title">Practice Mindful Impermanence</p>
                        <p class="protocol-desc">When experiencing a pleasant moment, consciously appreciate it fully while acknowledging its temporary nature. This reduces the 'clinging' reflex.</p>
                    </div>
                    <details>
                        <summary>
                            <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                            View Evidence & Sources
                        </summary>
                        <div class="citations-list">
                            <div class="citation-item"><span class="cite-num">[1]</span> Rahula, W. (1974). What the Buddha Taught. Grove Press.</div>
                            <div class="citation-item"><span class="cite-num">[2]</span> Bodhi, B. (2000). The Connected Discourses of the Buddha. Wisdom Publications.</div>
                        </div>
                    </details>
                </div>
            </div>
        </article>

        <!-- Myth 2 -->
        <article id="myth-2" class="myth-card">
            <div class="card-grid">
                <div class="col-visual">
                    <div class="gold-gradient-line"></div>
                    <div class="visual-container">
                        <div class="bar-container">
                            <div class="bar-wrapper">
                                <div class="bar bar-wanting">
                                    <div class="bar-pulse"></div>
                                </div>
                                <div style="text-align:center; margin-top: 0.75rem;">
                                    <div class="font-bold text-serif" style="font-size: 0.875rem; color: #44403C;">WANTING</div>
                                    <div style="font-size: 0.65rem; color: #78716C; text-transform: uppercase;">Dopamine</div>
                                </div>
                            </div>
                            <div class="bar-wrapper">
                                <div class="bar bar-liking"></div>
                                <div style="text-align:center; margin-top: 0.75rem;">
                                    <div class="font-bold text-serif" style="font-size: 0.875rem; color: #44403C;">LIKING</div>
                                    <div style="font-size: 0.65rem; color: #78716C; text-transform: uppercase;">Opioids</div>
                                </div>
                            </div>
                        </div>
                        <div style="background: #FEF2F2; border: 1px solid #FECACA; padding: 0.75rem; border-radius: 0.5rem; margin-top: 1rem;">
                            <div class="flex justify-between items-center" style="color: #991B1B; font-weight: 500; font-size: 0.75rem;">
                                <span>The Addiction Gap</span>
                                <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-content">
                    <div class="myth-label">
                        <span class="myth-tag">Myth #2</span>
                        <div class="myth-line"></div>
                    </div>
                    <h3 class="myth-text">"Dopamine is the 'pleasure chemical'—more is better."</h3>
                    <div class="flex items-center gap-3" style="margin-bottom: 1.5rem;">
                        <svg class="icon icon-lg icon-green" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                        <h3 class="truth-text">Dopamine drives 'Wanting,' not necessarily 'Liking.'</h3>
                    </div>
                    <div class="description">
                        <p>Modern neuroscience reveals a crucial distinction: dopamine primarily mediates "incentive salience" (the drive to get) rather than "hedonic impact" (the joy of having).</p>
                        <p>It is entirely possible—and common in addiction—to intensely <em>want</em> something you no longer <em>like</em>. This disconnect creates a "hungry ghost" state: a compulsive pursuit that yields no satisfaction.</p>
                    </div>
                    <div class="action-box">
                        <div class="protocol-label">
                            <svg class="icon icon-accent" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                            Protocol
                        </div>
                        <p class="protocol-title">The Wanting vs. Liking Audit</p>
                        <p class="protocol-desc">Before acting on a compulsion (e.g., scrolling), ask: 'Am I expecting joy, or just relieving an itch?' Prioritize high-Liking activities over high-Wanting ones.</p>
                    </div>
                    <details>
                        <summary>
                            <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                            View Evidence & Sources
                        </summary>
                        <div class="citations-list">
                            <div class="citation-item"><span class="cite-num">[1]</span> Berridge, K. C., & Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. Neuron.</div>
                            <div class="citation-item"><span class="cite-num">[2]</span> Berridge, K. C., & Robinson, T. E. (1998). What is the role of dopamine in reward: hedonic impact, reward learning, or incentive salience?</div>
                        </div>
                    </details>
                </div>
            </div>
        </article>

        <!-- Myth 3 -->
        <article id="myth-3" class="myth-card">
            <div class="card-grid">
                <div class="col-visual">
                    <div class="gold-gradient-line"></div>
                    <div class="visual-container flex-col">
                        <div style="background:#1C1917; color:white; padding:0.5rem 1rem; border-radius:0.5rem; font-family: var(--font-serif); margin-bottom: 2rem; position: relative;">
                            Desire
                            <div style="position:absolute; bottom:-2rem; left:50%; width:2px; height:2rem; background:#D6D3D1; transform:translateX(-1px);"></div>
                        </div>
                        
                        <div class="paths-grid">
                            <!-- Bad Path -->
                            <div class="path-col">
                                <div class="path-line-container">
                                    <div class="branch-line branch-left"></div>
                                </div>
                                <div class="box-red">
                                    <span style="font-weight:bold; display:block; font-size:0.875rem;">Taṇhā</span>
                                    <span style="font-size:0.65rem; text-transform:uppercase;">Craving</span>
                                </div>
                                <svg class="icon" style="color:#A8A29E; margin:0.5rem 0; transform:rotate(90deg);" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                                <span style="font-size:0.75rem; color:#78716C; font-weight:500;">Suffering</span>
                            </div>

                            <!-- Good Path -->
                            <div class="path-col">
                                <div class="path-line-container">
                                    <div class="branch-line branch-right"></div>
                                </div>
                                <div class="box-green">
                                    <span style="font-weight:bold; display:block; font-size:0.875rem;">Chanda</span>
                                    <span style="font-size:0.65rem; text-transform:uppercase;">Aspiration</span>
                                </div>
                                <svg class="icon" style="color:#A8A29E; margin:0.5rem 0; transform:rotate(90deg);" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                                <span style="font-size:0.75rem; color:#78716C; font-weight:500;">Growth</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-content">
                    <div class="myth-label">
                        <span class="myth-tag">Myth #3</span>
                        <div class="myth-line"></div>
                    </div>
                    <h3 class="myth-text">"All desire is bad; I should want nothing."</h3>
                    <div class="flex items-center gap-3" style="margin-bottom: 1.5rem;">
                        <svg class="icon icon-lg icon-green" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                        <h3 class="truth-text">It is 'Craving' (Taṇhā) that causes suffering, not Aspiration (Chanda).</h3>
                    </div>
                    <div class="description">
                        <p>Buddhist psychology distinguishes between two types of drive. <strong>Taṇhā</strong> is the unwholesome, ego-driven thirst that demands reality be different than it is.</p>
                        <p><strong>Chanda</strong>, or wholesome desire/aspiration, is the intention to act, create, or help. Without Chanda, one could not even desire to become enlightened. The goal is to transmute craving into aspiration.</p>
                    </div>
                    <div class="action-box">
                        <div class="protocol-label">
                            <svg class="icon icon-accent" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                            Protocol
                        </div>
                        <p class="protocol-title">Discern Your Drive</p>
                        <p class="protocol-desc">Label your motivation. Is it 'Must Have' (contraction, fear, sticky) or 'Choose To' (expansive, clear, open)? Feed the latter.</p>
                    </div>
                    <details>
                        <summary>
                            <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                            View Evidence & Sources
                        </summary>
                        <div class="citations-list">
                            <div class="citation-item"><span class="cite-num">[1]</span> Harvey, P. (2012). An Introduction to Buddhist Ethics. Cambridge University Press.</div>
                            <div class="citation-item"><span class="cite-num">[2]</span> Bodhi, B. (2000). The Connected Discourses of the Buddha.</div>
                        </div>
                    </details>
                </div>
            </div>
        </article>

        <!-- Myth 4 -->
        <article id="myth-4" class="myth-card">
            <div class="card-grid">
                <div class="col-visual">
                    <div class="gold-gradient-line"></div>
                    <div class="visual-container">
                        <div class="tolerance-card">
                            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E7E5E4; padding-bottom:0.5rem; margin-bottom:1rem;">
                                <span style="font-size:0.75rem; font-weight:bold; color:#9CA3AF; text-transform:uppercase;">Receptor Sensitivity</span>
                                <svg class="icon icon-sm icon-accent" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                            </div>

                            <div class="receptor-row">
                                <span style="font-size:0.75rem; color:#78716C;">Baseline</span>
                                <div class="receptor-dots">
                                    <div class="rec-dot rec-active"></div><div class="rec-dot rec-active"></div><div class="rec-dot rec-active"></div><div class="rec-dot rec-active"></div><div class="rec-dot rec-active"></div>
                                </div>
                            </div>
                            
                            <div style="position: relative; margin: 1rem 0; text-align: center;">
                                <div style="position: absolute; top:50%; left:0; width:100%; border-top: 1px dashed #FCA5A5;"></div>
                                <span style="position:relative; background:#FEF2F2; color:#DC2626; font-size:0.65rem; font-weight:bold; padding:0.25rem 0.5rem; border-radius:99px; border:1px solid #FECACA;">OVERSTIMULATION</span>
                            </div>

                            <div class="receptor-row">
                                <div class="flex flex-col">
                                    <span style="font-size:0.75rem; color:#78716C;">Result</span>
                                    <span style="font-size:0.65rem; color:#A8A29E;">(Down-regulation)</span>
                                </div>
                                <div class="receptor-dots">
                                    <div class="rec-dot rec-burnt"></div><div class="rec-dot rec-burnt"></div>
                                    <div class="rec-dot rec-empty"></div><div class="rec-dot rec-empty"></div><div class="rec-dot rec-empty"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-content">
                    <div class="myth-label">
                        <span class="myth-tag">Myth #4</span>
                        <div class="myth-line"></div>
                    </div>
                    <h3 class="myth-text">"I need a 'dopamine detox' to fix my addiction."</h3>
                    <div class="flex items-center gap-3" style="margin-bottom: 1.5rem;">
                        <svg class="icon icon-lg icon-green" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                        <h3 class="truth-text">You build tolerance to stimulation, not addiction to a chemical.</h3>
                    </div>
                    <div class="description">
                        <p>You cannot "detox" from dopamine; you need it to move your muscles. However, you <em>can</em> desensitize your receptors through chronic overstimulation.</p>
                        <p>When you flood the brain with high-reward stimuli (porn, sugar, infinite scroll), the brain protects itself by reducing receptor sensitivity (down-regulation). A "detox" is simply a period of allowing these receptors to up-regulate back to baseline sensitivity.</p>
                    </div>
                    <div class="action-box">
                        <div class="protocol-label">
                            <svg class="icon icon-accent" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                            Protocol
                        </div>
                        <p class="protocol-title">Stimulation Fasting</p>
                        <p class="protocol-desc">Choose one day to avoid high-salience inputs. The goal isn't to suffer, but to lower your threshold for enjoyment so simple things become pleasurable again.</p>
                    </div>
                    <details>
                        <summary>
                            <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                            View Evidence & Sources
                        </summary>
                        <div class="citations-list">
                            <div class="citation-item"><span class="cite-num">[1]</span> Volkow, N. D., et al. (2016). Neurobiologic Advances from the Brain Disease Model of Addiction. NEJM.</div>
                        </div>
                    </details>
                </div>
            </div>
        </article>

        <!-- Myth 5 -->
        <article id="myth-5" class="myth-card">
            <div class="card-grid">
                <div class="col-visual">
                    <div class="gold-gradient-line"></div>
                    <div class="visual-container">
                        <div style="position: relative; width: 100%; height: 140px;">
                            <svg viewBox="0 0 200 100" class="arc-svg">
                                <path d="M 20 90 A 80 80 0 0 1 180 90" fill="none" stroke="#E5E7EB" stroke-width="12" stroke-linecap="round" />
                                <path d="M 85 28 A 80 80 0 0 1 115 28" fill="none" stroke="#C9A961" stroke-width="12" stroke-linecap="round" opacity="0.3" />
                                <!-- Needle -->
                                <g class="needle">
                                    <line x1="100" y1="90" x2="100" y2="20" stroke="#1F2937" stroke-width="4" stroke-linecap="round" />
                                    <circle cx="100" cy="90" r="6" fill="#1F2937" />
                                </g>
                            </svg>
                            <div style="position:absolute; bottom:0; left:0; font-size:10px; font-weight:bold; color:#9CA3AF; text-transform:uppercase;">Asceticism</div>
                            <div style="position:absolute; bottom:0; right:0; font-size:10px; font-weight:bold; color:#9CA3AF; text-transform:uppercase;">Indulgence</div>
                            <div style="position:absolute; top:0; left:50%; transform:translateX(-50%); text-align:center;">
                                <div style="font-size:0.75rem; font-weight:bold; color:var(--color-accent); background:var(--color-accent-faint); padding:0.25rem 0.75rem; border-radius:99px; border:1px solid rgba(201,169,97,0.2);">Middle Way</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-content">
                    <div class="myth-label">
                        <span class="myth-tag">Myth #5</span>
                        <div class="myth-line"></div>
                    </div>
                    <h3 class="myth-text">"Buddhism teaches us to be emotionless zombies."</h3>
                    <div class="flex items-center gap-3" style="margin-bottom: 1.5rem;">
                        <svg class="icon icon-lg icon-green" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                        <h3 class="truth-text">The goal is Equanimity and Balance, not emotional suppression.</h3>
                    </div>
                    <div class="description">
                        <p>The Buddha explicitly rejected extreme asceticism. The "Middle Way" is a path between indulgence in the senses and harsh self-denial.</p>
                        <p>Equanimity is not indifference. Indifference is a withdrawal from life (a "near enemy" of equanimity). True equanimity is a balanced engagement—feeling emotions fully without being tossed around by them.</p>
                    </div>
                    <div class="action-box">
                        <div class="protocol-label">
                            <svg class="icon icon-accent" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                            Protocol
                        </div>
                        <p class="protocol-title">Mindful Appreciation</p>
                        <p class="protocol-desc">Enjoy pleasant moments without anxiety about them ending. Feel unpleasant moments without fearing they will last forever. Stand in the center.</p>
                    </div>
                    <details>
                        <summary>
                            <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                            View Evidence & Sources
                        </summary>
                        <div class="citations-list">
                            <div class="citation-item"><span class="cite-num">[1]</span> Gethin, R. (1998). The Foundations of Buddhism. Oxford University Press.</div>
                        </div>
                    </details>
                </div>
            </div>
        </article>

    </main>

    <footer>
        <div class="container">
            <div class="footer-logo">
                <div class="logo-circle">
                    <div class="logo-dot"></div>
                </div>
                Project Dukkha
            </div>
            <p style="color:#78716C; font-size:0.875rem; margin-bottom:1.5rem;">Synthesizing ancient wisdom and modern neuroscience for the rewarded animal.</p>
            <div style="color:#A8A29E; font-size:0.75rem;">© 2024–2025 Project Dukkha. Educational purposes only.</div>
        </div>
    </footer>

</body>
</html>