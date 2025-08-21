# Project Dukkha — A Field Guide to the Rewarded Animal

**Mastering your mind in a distracting economy through evidence-based protocols and dopamine science.**

Project Dukkha is a comprehensive field guide that bridges ancient Buddhist wisdom with modern neuroscience to help readers understand motivation, attention, and desire in the digital age. This repository contains both the research foundation and a complete static website with practical protocols for reclaiming focus and building sustainable habits.

## 🎯 What You'll Find Here

- **Evidence-Based Protocols**: Practical, time-bound interventions grounded in peer-reviewed research
- **Dopamine Science**: Clear explanations of how reward systems actually work (not pop-science myths)
- **Buddhist Philosophy**: Accurate translations and applications of concepts like *dukkha* and *taṇhā*
- **Interactive Site**: A beautiful, accessible website with diagrams, citations, and printable guides
- **Research Foundation**: Curated academic sources with claims, evidence, and quotations

## 🌐 Live Site

The main site is generated from this repository and includes:

- **Focus & Attention**: Understanding the ping-scroll loop and attention hijacking
- **Recovery & Baseline**: Sleep, stress, and dopamine recalibration strategies  
- **Five Myths**: Debunking common misconceptions about dopamine and Buddhism
- **The Model**: A comprehensive framework for understanding reward systems
- **Protocols**: Step-by-step guides for digital detox, mindfulness, stress management, and more
- **Research Library**: Full citations and academic sources

## 📁 Repository Structure

### Source-First Architecture
```
dukkha/
├── src/                          # Source files (single source of truth)
│   ├── protocols/               # Protocol markdown files with YAML front-matter
│   └── templates/               # HTML templates for build system
├── docs/                        # Static site output
│   ├── site/                   # Generated HTML pages (DO NOT EDIT DIRECTLY)
│   ├── index.html              # Homepage
│   ├── variables.css           # Design tokens & CSS custom properties
│   ├── styles.css              # Main component & layout styles
│   ├── utilities.css           # Utility classes & helpers
│   ├── print.css               # Print-optimized styles
│   └── images/                 # Diagrams and assets
├── research/                    # Academic research foundation
│   ├── R1/ ... R7/            # Research clusters with claims, evidence, refs
│   └── diagrams/              # Research on visual design
├── scripts/                     # Build system and utilities
│   ├── build_site.py          # Main site generator
│   ├── extract_protocols.py   # Migration utilities
│   └── qa_check.ps1           # Quality assurance
└── tests/                      # Automated testing
```

### CSS Architecture (Modular Design)
The stylesheet is split into focused, maintainable modules:
- **`variables.css`** (2.5KB) - Design tokens, color schemes, spacing system
- **`styles.css`** (32.3KB) - Core components, layout, page-specific styles  
- **`utilities.css`** (3.6KB) - Utility classes, loading states, diagram helpers
- **`print.css`** (1.2KB) - Print-optimized styles (loaded only when printing)

### Research Organization
Each `research/Rn/` folder contains:
- `claims.yaml` – Distilled claims with confidence scores and references
- `evidence.md` – Supporting academic excerpts with page numbers  
- `quotes.md` – Key quotations for prose development
- `refs.bib` – BibTeX citations and PDFs

## 🚀 Getting Started

### For Readers
1. **Browse the Site**: Start with `docs/index.html` or explore individual pages
2. **Try the Protocols**: Check `docs/site/protocols/` for practical interventions
3. **Read the Research**: Explore `research/R1/` through `research/R7/` for academic foundations

### For Developers
1. **Edit Source Content**: Modify protocols in `src/protocols/*.md` (Markdown with YAML front-matter)
2. **Rebuild Site**: Run `python scripts/build_site.py` to regenerate HTML
3. **Test Changes**: Use `pytest tests/` for automated validation
4. **Quality Check**: Run `pwsh scripts/qa_check.ps1` for link validation

### Example Commands (PowerShell)
```powershell
# View a research claim file
Get-Content .\research\R1\claims.yaml

# Open a PDF source
start .\research\R6\"R6 - Attention & Drive in a Distracting Economy.pdf"

# Rebuild the entire site
python .\scripts\build_site.py

# Run quality assurance
pwsh .\scripts\qa_check.ps1 -CheckUrls

# Run all tests
pytest .\tests\
```

## 🛠️ Development Workflow

### Standard Practice (Source-First)
1. **Edit** protocol content in `src/protocols/*.md`
2. **Build** by running `python scripts/build_site.py`
3. **Test** with `pytest tests/test_site_functionality.py`
4. **Validate** with `pwsh scripts/qa_check.ps1`
5. **Commit** both source and generated files

### Key Files
- `src/protocols/*.md` - Protocol source files with YAML front-matter
- `scripts/build_site.py` - Main site generator (Protocol dataclass, SiteBuilder)
- `scripts/extract_protocols.py` - Migration utility (HTML → Markdown)
- `tests/test_site_functionality.py` - Automated smoke tests
- `docs/BUILD_WORKFLOW.md` - Detailed build system documentation

**⚠️ Important**: Never edit files in `docs/site/` directly - they are generated and will be overwritten.

## 🎨 Content Architecture

### Recent Improvements (August 2025)
- **CSS Architecture Overhaul**: Split monolithic stylesheet into modular files
  - `variables.css` - Design tokens and color schemes
  - `styles.css` - Core components and layouts  
  - `utilities.css` - Helper classes and interactive elements
  - `print.css` - Print-optimized styles with selective loading
- **Enhanced Myths Page**: Added complete truth statements with visual distinction
  - Interactive checkmark icons and hover animations
  - Professional gradient backgrounds and typography hierarchy
  - Dark mode support and responsive design
- **Improved Content Completion**: Full five myths with proper academic citations
- **Navigation Consistency**: Fixed protocol page navigation across all 12 HTML files

### Page Types
- **Hero Pages**: Focus & Attention, Recovery & Baseline, Five Myths, Model, Library
- **Protocol Pages**: Time-bound, actionable interventions with research backing
- **Diagrams**: Interactive SVG visualizations of key concepts

### Design Principles
- **Evidence-Based**: Every claim backed by peer-reviewed research
- **Accessible**: Clean typography, semantic HTML, screen reader friendly
- **Printable**: CSS optimized for both screen and print
- **Progressive**: Works without JavaScript, enhanced with JS
- **Modular CSS**: Split architecture for maintainability and performance

### Content Standards
- Academic citations with DOI links where available
- Smooth-scroll footnotes with highlight animation
- Consistent hero sections with themed styling
- Action-oriented takeaways in every protocol
- Enhanced truth statements with visual distinction and interactive elements

## 🧪 Quality Assurance

### Automated Testing
```powershell
# Run all tests
pytest tests/

# Check links and references
pwsh scripts/qa_check.ps1 -CheckUrls

# Validate HTML structure
python -c "import scripts.build_site; print('Build system OK')"
```

### Manual Checks
- [ ] All protocol pages have proper footnotes and citations
- [ ] Navigation links work across all pages  
- [ ] Images and diagrams load correctly
- [ ] Print styles render cleanly
- [ ] Accessibility standards met (ARIA labels, semantic HTML)

## 🤝 Contributing

### Adding Research
1. **Create Research Folder**: Follow pattern `research/R8/` with required files
2. **Add Claims**: Update `claims.yaml` with atomic claims, confidence scores, and references
3. **Document Evidence**: Add supporting excerpts to `evidence.md` with page numbers
4. **Include Sources**: Add BibTeX entries to `refs.bib` and place PDFs in folder
5. **Test Integration**: Ensure new research integrates with existing content

### Adding Protocols  
1. **Create Source File**: Add new protocol as `src/protocols/your-protocol.md`
2. **YAML Front-Matter**: Include title, description, duration, tags, and slug
3. **Markdown Content**: Write protocol with proper headings and footnote references
4. **Rebuild Site**: Run `python scripts/build_site.py` to generate HTML
5. **Validate**: Check output in `docs/site/protocols/your-protocol.html`

### Content Standards
- **Academic Rigor**: Every claim must link to research with proper citations
- **Actionable Advice**: Include concrete "One Action" suggestions
- **Accessibility**: Use semantic HTML, alt text, and ARIA labels
- **Consistency**: Follow established patterns for headings, footnotes, and styling

### Pull Request Checklist
- [ ] Updated source files in `src/` (not generated files in `docs/site/`)
- [ ] Added proper citations to `research/` if introducing new claims
- [ ] Ran build system: `python scripts/build_site.py`
- [ ] Passed tests: `pytest tests/`
- [ ] Validated links: `pwsh scripts/qa_check.ps1`
- [ ] Tested accessibility and print styles
- [ ] Updated relevant documentation

## 🗺️ Current Status & Roadmap

### ✅ Completed
- **Complete Static Site**: 7 main pages + 5 protocol pages with full navigation
- **Source-First Build System**: Python-based generator with YAML front-matter support  
- **Research Foundation**: 7 research clusters with 50+ academic sources
- **Quality Assurance**: Automated testing and link validation
- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation
- **Citation System**: Footnotes with smooth scroll and academic references
- **Modular CSS Architecture**: Split into focused, maintainable modules for better performance
- **Enhanced Content**: Complete myths page with 5 debunked misconceptions
- **Professional Styling**: Interactive truth statements, action boxes, and visual hierarchy

### 🚧 In Progress  
- **Visual Enhancements**: Progress indicators, reading prompts, protocol dropdown navigation
- **Content Expansion**: Additional protocols for sleep, nutrition, exercise
- **Diagram Updates**: Interactive SVG enhancements and new visualizations
- **Performance Optimization**: Further CSS optimization and selective loading strategies

### 🔮 Planned
- **Search Functionality**: Full-text search across all content
- **PDF Generation**: Automated generation of printable protocol guides  
- **API Integration**: Dynamic citation validation and reference management
- **Internationalization**: Multi-language support for global accessibility

### 📊 Metrics
- **7** Main content pages (attention, recovery, myths, model, protocols, library)
- **5** Evidence-based protocols with implementation guides
- **50+** Academic citations with DOI links and full references
- **100%** Automated test coverage for critical site functionality
- **4** Modular CSS files for maintainable styling (40KB total, split by purpose)
- **12** HTML files updated with optimized CSS architecture

## 📄 License

This project is released under the MIT License - see the LICENSE file for details.

**Academic Use**: All research sources are properly cited. Please maintain attribution when using or building upon this work.

**Commercial Use**: The protocols and frameworks may be adapted for commercial applications with proper attribution.

---

*Project Dukkha bridges ancient wisdom with modern science to help you master your mind in a distracting economy.*

