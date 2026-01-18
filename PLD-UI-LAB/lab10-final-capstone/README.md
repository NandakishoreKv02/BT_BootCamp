# Personal Learning Dashboard (PLD) – UI Engineering Lab

## Overview
The Personal Learning Dashboard (PLD) is a responsive, UI-focused web application developed as part of the Multi-Level UI Engineering Lab. The application helps users visualize their learning progress, manage a profile, and view a gallery of learning activities.

This project focuses purely on frontend development using semantic HTML, CSS fundamentals, and a modern UI utility framework.

---

## Framework Chosen
**Tailwind CSS**

Tailwind CSS was used to:
- Build responsive layouts
- Style buttons, cards, grids, and forms
- Apply mobile-first responsive design

Custom CSS was retained alongside Tailwind to control:
- Global layout
- Cross-browser compatibility
- Dark mode theming
- UX polish and hover effects

---

## Responsive Design Strategy
The application follows a **mobile-first approach**:
- Layouts stack vertically on small screens
- Grid-based layouts expand for tablets and desktops
- Navigation adapts from vertical to horizontal using responsive utilities

Tailwind breakpoints used:
- `sm` – small devices
- `md` – tablets
- `lg` – desktops

A viewport meta tag is included to ensure proper scaling on mobile devices.

---

## Browser Compatibility
Cross-browser support was ensured by:
- Including Normalize CSS
- Avoiding browser-specific features
- Using vendor-safe CSS properties
- Testing on modern browsers

### Tested Browsers
- Google Chrome
- Microsoft Edge
- Mozilla Firefox

---

## Features Implemented
- Login page (UI only)
- Dashboard with:
  - Topics Explorer (Module → Unit → Topic)
  - CSS-only collapsible sections
  - Lab progress tracker
- Profile page with:
  - Personal details
  - Skills displayed as badges
  - Profile image upload (UI only)
- Responsive gallery with:
  - Grid layout
  - Hover captions
- UX enhancements:
  - Sticky header
  - Hover and focus states
  - Smooth transitions
  - System-based dark mode

---

## Notes
- This project is UI-only and does not include backend functionality.
- JavaScript was intentionally avoided as per lab requirements.
- All enhancements were implemented incrementally across lab levels.
