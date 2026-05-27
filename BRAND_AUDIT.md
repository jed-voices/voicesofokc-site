# VOICES of OKC — Brand Compliance Audit

Audit scope: current local checkout on branch `cleanup/replace-hardcoded-youtube-fallback`. The scan was read-only except for writing this report file. It covered all `.html` files, all CSS in `assets/css/`, `assets/data/site-config.json`, `assets/data/episode-map.json`, and relevant `assets/js/*.js` files for color/font/copy tokens.

## 1. Summary
- Total HTML files scanned: 20
- Total CSS files scanned: 2
- Additional data/JS files scanned: 2 JSON + 3 JS
- Total deviations found: 624
- Severity breakdown: Critical 67 (off-brand color/font values), Moderate 95 (font weight, capitalization, tagline/copy issues), Minor 462 (black/white/system color usage and CSS structural issues)
- Counting rule: color deviations are counted per line occurrence; structural issues are counted per selector/property/variable occurrence. Brand RGB colors with alpha, such as `rgba(15,42,68,.14)`, are treated as brand-compliant because the base color is locked.
- Note: `assets/data/site-config.json` exists and was scanned; no root-level `site-config.json` exists.

## 2. Color Inventory

### 2.1 Brand-Compliant Color Usage
Found 219 brand-token or brand-color occurrences.
| File | Line | Value | Brand | Context |
| --- | --- | --- | --- | --- |
| about/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| contact/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| guests/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| podcast-team/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| sponsors/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| watch-listen/index.html | 17 | #0F2A44 | Civic Navy | <meta name="theme-color" content="#0F2A44" /> |
| assets/css/final-overrides.css | 93 | rgba(15,42,68,0.14) | Civic Navy | border: 1px solid rgba(15,42,68,0.14); |
| assets/css/final-overrides.css | 95 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 117 | --civic-navy | Civic Navy | background: var(--civic-navy); |
| assets/css/final-overrides.css | 119 | --cloud-white | Cloud White | color: var(--cloud-white); |
| assets/css/final-overrides.css | 120 | rgba(15,42,68,0.16) | Civic Navy | box-shadow: 0 12px 28px rgba(15,42,68,0.16); |
| assets/css/final-overrides.css | 136 | %230F2A44 | Civic Navy | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. |
| assets/css/final-overrides.css | 140 | %230F2A44 | Civic Navy | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. |
| assets/css/final-overrides.css | 156 | %235FA8D3 | Azure | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235FA8D3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 9.5L12 5l8 4.5-8 4.5-8-4.5Z'/%3E%3Cpath d='M8 |
| assets/css/final-overrides.css | 190 | rgba(244,247,250,0.24) | Cloud White | border-color: rgba(244,247,250,0.24); |
| assets/css/final-overrides.css | 191 | --cloud-white | Cloud White | color: var(--cloud-white); |
| assets/css/final-overrides.css | 197 | rgba(95,168,211,0.36) | Azure | border-color: rgba(95,168,211,0.36); |
| assets/css/final-overrides.css | 206 | rgba(244,247,250,0.16) | Cloud White | border-color: rgba(244,247,250,0.16); |
| assets/css/final-overrides.css | 218 | --cloud-white | Cloud White | color: var(--cloud-white); |
| assets/css/final-overrides.css | 224 | rgba(244,247,250,0.86) | Cloud White | color: rgba(244,247,250,0.86); |
| assets/css/final-overrides.css | 240 | rgba(244,247,250,0.66) | Cloud White | color: rgba(244,247,250,0.66); |
| assets/css/final-overrides.css | 353 | rgba(15, 42, 68, 0.08) | Civic Navy | border: 1px solid rgba(15, 42, 68, 0.08); |
| assets/css/final-overrides.css | 377 | rgba(15, 42, 68, 0.05) | Civic Navy | box-shadow: 0 8px 20px rgba(15, 42, 68, 0.05); |
| assets/css/final-overrides.css | 381 | --civic-navy | Civic Navy | background: var(--civic-navy); |
| assets/css/final-overrides.css | 382 | --civic-navy | Civic Navy | border-color: var(--civic-navy); |
| assets/css/final-overrides.css | 518 | --azure | Azure | --azure:#5FA8D3; |
| assets/css/final-overrides.css | 518 | #5FA8D3 | Azure | --azure:#5FA8D3; |
| assets/css/final-overrides.css | 537 | rgba(244,247,250,.96) | Cloud White | background:rgba(244,247,250,.96); |
| assets/css/final-overrides.css | 538 | rgba(244,247,250,.32) | Cloud White | border:1px solid rgba(244,247,250,.32); |
| assets/css/final-overrides.css | 550 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 554 | --ice-blue | Azure | color:var(--ice-blue); |
| assets/css/final-overrides.css | 559 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 564 | --slate | Slate | color:var(--slate); |
| assets/css/final-overrides.css | 627 | rgba(95,168,211,.32) | Azure | border:1px solid rgba(95,168,211,.32); |
| assets/css/final-overrides.css | 629 | rgba(95,168,211,.1) | Azure | background:rgba(95,168,211,.1); |
| assets/css/final-overrides.css | 630 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 652 | rgba(15,42,68,.105) | Civic Navy | border:1px solid rgba(15,42,68,.105); |
| assets/css/final-overrides.css | 655 | rgba(15,42,68,.06) | Civic Navy | box-shadow:0 18px 38px rgba(15,42,68,.06); |
| assets/css/final-overrides.css | 672 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 695 | rgba(95,168,211,.35) | Azure | border-color:rgba(95,168,211,.35) !important; |
| assets/css/final-overrides.css | 702 | --ice-blue | Azure | color:var(--ice-blue); |
| assets/css/final-overrides.css | 738 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 762 | rgba(95,168,211,.26) | Azure | border:1px solid rgba(95,168,211,.26); |
| assets/css/final-overrides.css | 764 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 765 | rgba(95,168,211,.08) | Azure | background:rgba(95,168,211,.08); |
| assets/css/final-overrides.css | 795 | --cloud-white | Cloud White | color:var(--cloud-white); |
| assets/css/final-overrides.css | 801 | rgba(15,42,68,.14) | Civic Navy | box-shadow:0 24px 48px rgba(15,42,68,.14); |
| assets/css/final-overrides.css | 806 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 807 | rgba(15,42,68,.11) | Civic Navy | border:1px solid rgba(15,42,68,.11); |
| assets/css/final-overrides.css | 840 | rgba(244,247,250,.82) | Cloud White | color:rgba(244,247,250,.82); |
| assets/css/final-overrides.css | 859 | rgba(15,42,68,.16) | Civic Navy | border:1px solid rgba(15,42,68,.16); |
| assets/css/final-overrides.css | 862 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 875 | rgba(15,42,68,.14) | Civic Navy | border:1px solid rgba(15,42,68,.14); |
| assets/css/final-overrides.css | 878 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 884 | --civic-navy | Civic Navy | background:var(--civic-navy); |
| assets/css/final-overrides.css | 885 | --cloud-white | Cloud White | color:var(--cloud-white); |
| assets/css/final-overrides.css | 886 | --civic-navy | Civic Navy | border-color:var(--civic-navy); |
| assets/css/final-overrides.css | 904 | rgba(15,42,68,.12) | Civic Navy | border:1px solid rgba(15,42,68,.12); |
| assets/css/final-overrides.css | 912 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 923 | rgba(15,42,68,.15) | Civic Navy | border:1px solid rgba(15,42,68,.15); |
| assets/css/final-overrides.css | 926 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 953 | --civic-navy | Civic Navy | color:var(--civic-navy); |
| assets/css/final-overrides.css | 958 | --slate | Slate | color:var(--slate); |
| assets/css/final-overrides.css | 982 | --ice-blue | Azure | background:var(--ice-blue); |
| assets/css/final-overrides.css | 1068 | --civic-navy | Civic Navy | background: var(--civic-navy); |
| assets/css/final-overrides.css | 1069 | --cloud-white | Cloud White | color: var(--cloud-white); |
| assets/css/final-overrides.css | 1183 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1216 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1219 | rgba(95,168,211,.58) | Azure | text-decoration-color: rgba(95,168,211,.58); |
| assets/css/final-overrides.css | 1226 | --azure | Azure | border-left: 4px solid var(--azure); |
| assets/css/final-overrides.css | 1238 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1247 | rgba(15,42,68,.075) | Civic Navy | border-bottom: 1px solid rgba(15,42,68,.075) !important; |
| assets/css/final-overrides.css | 1248 | rgba(15,42,68,.045) | Civic Navy | box-shadow: 0 10px 28px rgba(15,42,68,.045); |
| assets/css/final-overrides.css | 1297 | --ice-blue | Azure | background: var(--ice-blue); |
| assets/css/final-overrides.css | 1310 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1337 | rgba(15,42,68,.16) | Civic Navy | box-shadow: 0 30px 72px rgba(15,42,68,.16); |
| assets/css/final-overrides.css | 1357 | rgba(244,247,250,.22) | Cloud White | border: 1px solid rgba(244,247,250,.22); |
| assets/css/final-overrides.css | 1364 | rgba(15,42,68,.66) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.91), rgba(15,42,68,.66) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1364 | rgba(15,42,68,.2) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.91), rgba(15,42,68,.66) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1370 | rgba(15,42,68,.64) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 43%, rgba(15,42,68,.22) 74%), |
| assets/css/final-overrides.css | 1370 | rgba(15,42,68,.22) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 43%, rgba(15,42,68,.22) 74%), |
| assets/css/final-overrides.css | 1376 | rgba(15,42,68,.62) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.62) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1376 | rgba(15,42,68,.2) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.62) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1382 | rgba(15,42,68,.64) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1382 | rgba(15,42,68,.2) | Civic Navy | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 42%, rgba(15,42,68,.2) 74%), |
| assets/css/final-overrides.css | 1395 | rgba(244,247,250,.86) | Cloud White | color: rgba(244,247,250,.86); |
| assets/css/final-overrides.css | 1402 | rgba(244,247,250,.16) | Cloud White | border: 1px solid rgba(244,247,250,.16) !important; |
| assets/css/final-overrides.css | 1416 | rgba(244,247,250,.84) | Cloud White | color: rgba(244,247,250,.84); |
| assets/css/final-overrides.css | 1422 | --ice-blue | Azure | background: var(--ice-blue); |
| assets/css/final-overrides.css | 1440 | --ice-blue | Azure | background: var(--ice-blue); |
| assets/css/final-overrides.css | 1442 | rgba(95,168,211,.2) | Azure | box-shadow: 0 12px 24px rgba(95,168,211,.2); |
| assets/css/final-overrides.css | 1447 | --civic-navy | Civic Navy | background: var(--civic-navy) !important; |
| assets/css/final-overrides.css | 1448 | --cloud-white | Cloud White | color: var(--cloud-white) !important; |
| assets/css/final-overrides.css | 1450 | rgba(15,42,68,.16) | Civic Navy | box-shadow: 0 14px 30px rgba(15,42,68,.16); |
| assets/css/final-overrides.css | 1455 | rgba(15,42,68,.16) | Civic Navy | border: 1px solid rgba(15,42,68,.16); |
| assets/css/final-overrides.css | 1457 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1482 | rgba(244,247,250,.22) | Cloud White | border-color: rgba(244,247,250,.22); |
| assets/css/final-overrides.css | 1491 | rgba(15,42,68,.105) | Civic Navy | border: 1px solid rgba(15,42,68,.105) !important; |
| assets/css/final-overrides.css | 1492 | rgba(15,42,68,.065) | Civic Navy | box-shadow: 0 18px 38px rgba(15,42,68,.065) !important; |
| assets/css/final-overrides.css | 1515 | rgba(15,42,68,.09) | Civic Navy | border-color: rgba(15,42,68,.09) !important; |
| assets/css/final-overrides.css | 1516 | rgba(15,42,68,.075) | Civic Navy | box-shadow: 0 16px 36px rgba(15,42,68,.075); |
| assets/css/final-overrides.css | 1525 | rgba(15,42,68,0) | Civic Navy | background: linear-gradient(180deg, rgba(15,42,68,0), rgba(15,42,68,.12)); |
| assets/css/final-overrides.css | 1525 | rgba(15,42,68,.12) | Civic Navy | background: linear-gradient(180deg, rgba(15,42,68,0), rgba(15,42,68,.12)); |
| assets/css/final-overrides.css | 1556 | rgba(15,42,68,.07) | Civic Navy | border-top: 1px solid rgba(15,42,68,.07); |
| assets/css/final-overrides.css | 1557 | rgba(15,42,68,.06) | Civic Navy | border-bottom: 1px solid rgba(15,42,68,.06); |
| assets/css/final-overrides.css | 1606 | rgba(244,247,250,.76) | Cloud White | color: rgba(244,247,250,.76); |
| assets/css/final-overrides.css | 1612 | rgba(15,42,68,.14) | Civic Navy | box-shadow: 0 24px 48px rgba(15,42,68,.14); |
| assets/css/final-overrides.css | 1625 | --cloud-white | Cloud White | color: var(--cloud-white) !important; |
| assets/css/final-overrides.css | 1629 | rgba(244,247,250,.68) | Cloud White | color: rgba(244,247,250,.68) !important; |
| assets/css/final-overrides.css | 1642 | --cloud-white | Cloud White | color: var(--cloud-white); |
| assets/css/final-overrides.css | 1731 | --ice-blue | Azure | background: var(--ice-blue); |
| assets/css/final-overrides.css | 1790 | --civic-navy | Civic Navy | color: var(--civic-navy); |
| assets/css/final-overrides.css | 1797 | rgba(15,42,68,.12) | Civic Navy | border-color: rgba(15,42,68,.12); |
| assets/css/final-overrides.css | 1798 | rgba(15,42,68,.17) | Civic Navy | box-shadow: 0 18px 46px rgba(15,42,68,.17); |
| assets/css/final-overrides.css | 1822 | --ice-blue | Azure | background: linear-gradient(90deg, var(--ice-blue) var(--progress), rgba(15,42,68,.13) var(--progress)); |
| assets/css/final-overrides.css | 1822 | rgba(15,42,68,.13) | Civic Navy | background: linear-gradient(90deg, var(--ice-blue) var(--progress), rgba(15,42,68,.13) var(--progress)); |
| assets/css/final-overrides.css | 1830 | --civic-navy | Civic Navy | background: var(--civic-navy); |
| assets/css/final-overrides.css | 1831 | --cloud-white | Cloud White | border: 3px solid var(--cloud-white); |
| assets/css/final-overrides.css | 1832 | rgba(15,42,68,.22) | Civic Navy | box-shadow: 0 3px 10px rgba(15,42,68,.22); |
| assets/css/final-overrides.css | 1838 | --cloud-white | Cloud White | border: 3px solid var(--cloud-white); |
| assets/css/final-overrides.css | 1840 | --civic-navy | Civic Navy | background: var(--civic-navy); |
| assets/css/final-overrides.css | 1841 | rgba(15,42,68,.22) | Civic Navy | box-shadow: 0 3px 10px rgba(15,42,68,.22); |
| assets/css/site.css | 2 | --civic-navy | Civic Navy | --civic-navy:#0F2A44; |
| assets/css/site.css | 2 | #0F2A44 | Civic Navy | --civic-navy:#0F2A44; |
| assets/css/site.css | 3 | --slate | Slate | --slate:#3E4C59; |
| assets/css/site.css | 3 | #3E4C59 | Slate | --slate:#3E4C59; |
| assets/css/site.css | 4 | --cloud-white | Cloud White | --cloud-white:#F4F7FA; |
| assets/css/site.css | 4 | #F4F7FA | Cloud White | --cloud-white:#F4F7FA; |
| assets/css/site.css | 5 | --ice-blue | Azure | --ice-blue:#5FA8D3; |
| assets/css/site.css | 5 | #5FA8D3 | Azure | --ice-blue:#5FA8D3; |
| assets/css/site.css | 6 | --warm-signal-blue | Azure | --warm-signal-blue:#5FA8D3; |
| assets/css/site.css | 6 | #5FA8D3 | Azure | --warm-signal-blue:#5FA8D3; |
| assets/css/site.css | 10 | rgba(15,42,68,.12) | Civic Navy | --line:rgba(15,42,68,.12); |
| assets/css/site.css | 11 | rgba(15,42,68,.18) | Civic Navy | --line-strong:rgba(15,42,68,.18); |
| assets/css/site.css | 12 | rgba(15,42,68,.055) | Civic Navy | --shadow-sm:0 8px 22px rgba(15,42,68,.055); |
| assets/css/site.css | 13 | rgba(15,42,68,.075) | Civic Navy | --shadow-md:0 18px 44px rgba(15,42,68,.075); |
| assets/css/site.css | 14 | rgba(15,42,68,.14) | Civic Navy | --shadow-lg:0 28px 64px rgba(15,42,68,.14); |
| assets/css/site.css | 56 | --warm-signal-blue | Azure | color:var(--warm-signal-blue); |
| assets/css/site.css | 61 | --civic-navy | Civic Navy | color:var(--civic-navy); text-wrap:balance; |
| assets/css/site.css | 75 | --ice-blue | Azure | background:linear-gradient(90deg, var(--ice-blue) 0%, rgba(95,168,211,.92) 72%, rgba(95,168,211,0) 100%); |
| assets/css/site.css | 75 | rgba(95,168,211,.92) | Azure | background:linear-gradient(90deg, var(--ice-blue) 0%, rgba(95,168,211,.92) 72%, rgba(95,168,211,0) 100%); |
| assets/css/site.css | 75 | rgba(95,168,211,0) | Azure | background:linear-gradient(90deg, var(--ice-blue) 0%, rgba(95,168,211,.92) 72%, rgba(95,168,211,0) 100%); |
| assets/css/site.css | 76 | rgba(95,168,211,.12) | Azure | box-shadow:0 0 0 1px rgba(95,168,211,.12), 0 10px 22px rgba(95,168,211,.16); |
| assets/css/site.css | 76 | rgba(95,168,211,.16) | Azure | box-shadow:0 0 0 1px rgba(95,168,211,.12), 0 10px 22px rgba(95,168,211,.16); |
| assets/css/site.css | 80 | rgba(244,247,250,.12) | Cloud White | box-shadow:0 0 0 1px rgba(244,247,250,.12), 0 10px 22px rgba(95,168,211,.24); |
| assets/css/site.css | 80 | rgba(95,168,211,.24) | Azure | box-shadow:0 0 0 1px rgba(244,247,250,.12), 0 10px 22px rgba(95,168,211,.24); |
| assets/css/site.css | 100 | --civic-navy | Civic Navy | .button { min-height:50px; padding:0 22px; background:var(--ice-blue); color:var(--civic-navy); box-shadow:0 12px 28px rgba(95,168,211,.24); } |
| assets/css/site.css | 100 | --ice-blue | Azure | .button { min-height:50px; padding:0 22px; background:var(--ice-blue); color:var(--civic-navy); box-shadow:0 12px 28px rgba(95,168,211,.24); } |
| assets/css/site.css | 100 | rgba(95,168,211,.24) | Azure | .button { min-height:50px; padding:0 22px; background:var(--ice-blue); color:var(--civic-navy); box-shadow:0 12px 28px rgba(95,168,211,.24); } |
| assets/css/site.css | 101 | --civic-navy | Civic Navy | .button-secondary { min-height:50px; padding:0 22px; background:var(--civic-navy); color:var(--cloud-white); box-shadow:var(--shadow-sm); } |
| assets/css/site.css | 101 | --cloud-white | Cloud White | .button-secondary { min-height:50px; padding:0 22px; background:var(--civic-navy); color:var(--cloud-white); box-shadow:var(--shadow-sm); } |
| assets/css/site.css | 102 | --civic-navy | Civic Navy | .button-outline { min-height:46px; padding:0 18px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); } |
| assets/css/site.css | 102 | rgba(15,42,68,.14) | Civic Navy | .button-outline { min-height:46px; padding:0 18px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); } |
| assets/css/site.css | 103 | --cloud-white | Cloud White | .button-ghost { min-height:50px; padding:0 22px; border:1.5px solid rgba(244,247,250,.24); background:rgba(255,255,255,.06); color:var(--cloud-white); backdrop-filter:blur(10px); } |
| assets/css/site.css | 103 | rgba(244,247,250,.24) | Cloud White | .button-ghost { min-height:50px; padding:0 22px; border:1.5px solid rgba(244,247,250,.24); background:rgba(255,255,255,.06); color:var(--cloud-white); backdrop-filter:blur(10px); } |
| assets/css/site.css | 104 | rgba(244,247,250,.92) | Cloud White | .site-header { position:sticky; top:0; z-index:1000; background:rgba(244,247,250,.92); backdrop-filter:blur(16px); border-bottom:1px solid rgba(15,42,68,.08); } |
| assets/css/site.css | 104 | rgba(15,42,68,.08) | Civic Navy | .site-header { position:sticky; top:0; z-index:1000; background:rgba(244,247,250,.92); backdrop-filter:blur(16px); border-bottom:1px solid rgba(15,42,68,.08); } |
| assets/css/site.css | 109 | --civic-navy | Civic Navy | .brand-name { font-family:"Sora","Inter",sans-serif; font-size:1rem; font-weight:700; letter-spacing:-.03em; color:var(--civic-navy); line-height:1.02; } |
| assets/css/site.css | 110 | --slate | Slate | .brand-tag { font-size:.72rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--slate); margin-top:4px; } |
| assets/css/site.css | 113 | --civic-navy | Civic Navy | .nav a:hover { opacity:1; color:var(--civic-navy); } |
| assets/css/site.css | 119 | rgba(15,42,68,.58) | Civic Navy | background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), var(--hero-image, url('../images/hero-18.jpg')) center center / cover no-repeat; |
| assets/css/site.css | 119 | rgba(15,42,68,.22) | Civic Navy | background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), var(--hero-image, url('../images/hero-18.jpg')) center center / cover no-repeat; |
| assets/css/site.css | 119 | rgba(15,42,68,.14) | Civic Navy | background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), var(--hero-image, url('../images/hero-18.jpg')) center center / cover no-repeat; |
| assets/css/site.css | 122 | rgba(15,42,68,.58) | Civic Navy | .home-hero { background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), url('../images/featured-episode-8.jpg') center center / cover no-repeat; } |
| assets/css/site.css | 122 | rgba(15,42,68,.22) | Civic Navy | .home-hero { background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), url('../images/featured-episode-8.jpg') center center / cover no-repeat; } |
| assets/css/site.css | 122 | rgba(15,42,68,.14) | Civic Navy | .home-hero { background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), url('../images/featured-episode-8.jpg') center center / cover no-repeat; } |
| assets/css/site.css | 124 | --cloud-white | Cloud White | .hero-copy { color:var(--cloud-white); } |
| assets/css/site.css | 125 | --cloud-white | Cloud White | .hero-copy .title-xl,.hero-copy .title-lg,.hero-copy .title-md,.hero-copy .title-sm { color:var(--cloud-white); } |
| assets/css/site.css | 126 | --ice-blue | Azure | .hero-copy .eyebrow { color:var(--ice-blue); } |
| assets/css/site.css | 127 | rgba(244,247,250,.85) | Cloud White | .hero-copy .lede { color:rgba(244,247,250,.85); margin-top:20px; } |
| assets/css/site.css | 128 | --cloud-white | Cloud White | .hero-panel { background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.14); border-radius:var(--radius-xl); padding:24px; backdrop-filter:blur(12px); color:var(--cloud-white); } |
| assets/css/site.css | 129 | --cloud-white | Cloud White | .hero-panel h2,.hero-panel h3 { margin:0 0 12px; color:var(--cloud-white); font-family:"Sora","Inter",sans-serif; font-size:1.02rem; } |
| assets/css/site.css | 130 | rgba(244,247,250,.82) | Cloud White | .hero-panel p { margin:0 0 14px; color:rgba(244,247,250,.82); font-size:.95rem; } |
| assets/css/site.css | 133 | rgba(244,247,250,.68) | Cloud White | .hero-meta-item span:first-child { color:rgba(244,247,250,.68); } |
| assets/css/site.css | 136 | rgba(15,42,68,.08) | Civic Navy | .image-frame { position:relative; overflow:hidden; border-radius:var(--radius-xl); background:#e8eff5; border:1px solid rgba(15,42,68,.08); box-shadow:var(--shadow-md); } |
| assets/css/site.css | 145 | --warm-signal-blue | Azure | .episode-kicker { font-size:.8rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--warm-signal-blue); margin-bottom:14px; } |
| assets/css/site.css | 148 | --civic-navy | Civic Navy | letter-spacing:.04em; color:var(--civic-navy); text-transform:uppercase; text-wrap:balance; |
| assets/css/site.css | 158 | --civic-navy | Civic Navy | .mini-card h3 { margin:0 0 8px; font-family:"Sora","Inter",sans-serif; font-size:.98rem; letter-spacing:.04em; color:var(--civic-navy); text-transform:uppercase; } |
| assets/css/site.css | 162 | rgba(15,42,68,.18) | Civic Navy | .guest-card:hover { transform:translateY(-6px); box-shadow:var(--shadow-md); border-color:rgba(15,42,68,.18); } |
| assets/css/site.css | 165 | --warm-signal-blue | Azure | .guest-role { font-size:.74rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--warm-signal-blue); } |
| assets/css/site.css | 167 | --civic-navy | Civic Navy | .platform-section { background:var(--civic-navy); color:var(--cloud-white); } |
| assets/css/site.css | 167 | --cloud-white | Cloud White | .platform-section { background:var(--civic-navy); color:var(--cloud-white); } |
| assets/css/site.css | 168 | --cloud-white | Cloud White | .platform-section .title-lg,.platform-section .lede,.platform-section .eyebrow { color:var(--cloud-white); } |
| assets/css/site.css | 169 | --ice-blue | Azure | .platform-section .eyebrow { color:var(--ice-blue); } |
| assets/css/site.css | 174 | rgba(244,247,250,.72) | Cloud White | .platform-card span { color:rgba(244,247,250,.72); font-size:.91rem; text-wrap:pretty; } |
| assets/css/site.css | 176 | --cloud-white | Cloud White | background:linear-gradient(135deg,#112f4a,#183b5b); color:var(--cloud-white); border-radius:28px; |
| assets/css/site.css | 177 | rgba(15,42,68,.14) | Civic Navy | padding:40px clamp(24px,4vw,44px); display:grid; grid-template-columns:minmax(0,1fr) auto; gap:24px; align-items:center; box-shadow:0 24px 50px rgba(15,42,68,.14); |
| assets/css/site.css | 179 | --cloud-white | Cloud White | .cta-band .title-md,.cta-band p { margin:0; color:var(--cloud-white); } |
| assets/css/site.css | 180 | rgba(244,247,250,.82) | Cloud White | .cta-band p { margin-top:12px; color:rgba(244,247,250,.82); max-width:720px; text-wrap:pretty; } |
| assets/css/site.css | 181 | --cloud-white | Cloud White | .site-footer { background:#0c2238; color:var(--cloud-white); padding:64px 0 28px; margin-top:96px; } |
| assets/css/site.css | 183 | rgba(244,247,250,.75) | Cloud White | .footer-copy { color:rgba(244,247,250,.75); font-size:.95rem; margin:0; } |
| assets/css/site.css | 184 | --cloud-white | Cloud White | .footer-column h2 { margin:0 0 14px; font-family:"Sora","Inter",sans-serif; font-size:1rem; color:var(--cloud-white); } |
| assets/css/site.css | 185 | rgba(244,247,250,.76) | Cloud White | .footer-column a,.footer-column span { display:block; margin:0 0 10px; color:rgba(244,247,250,.76); font-size:.93rem; } |
| assets/css/site.css | 186 | rgba(244,247,250,.08) | Cloud White | .footer-bottom { margin-top:32px; padding-top:20px; border-top:1px solid rgba(244,247,250,.08); display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px 16px; color:rgba(244,247,250,.6); font-size:.88rem; } |
| assets/css/site.css | 186 | rgba(244,247,250,.6) | Cloud White | .footer-bottom { margin-top:32px; padding-top:20px; border-top:1px solid rgba(244,247,250,.08); display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px 16px; color:rgba(244,247,250,.6); font-size:.88rem; } |
| assets/css/site.css | 189 | rgba(244,247,250,.96) | Cloud White | width:min(calc(100% - 20px),1120px); background:rgba(244,247,250,.96); backdrop-filter:blur(16px); |
| assets/css/site.css | 190 | rgba(15,42,68,.1) | Civic Navy | border:1px solid rgba(15,42,68,.1); box-shadow:0 18px 40px rgba(15,42,68,.16); border-radius:22px; padding:14px; |
| assets/css/site.css | 190 | rgba(15,42,68,.16) | Civic Navy | border:1px solid rgba(15,42,68,.1); box-shadow:0 18px 40px rgba(15,42,68,.16); border-radius:22px; padding:14px; |
| assets/css/site.css | 193 | --civic-navy | Civic Navy | .audio-control { min-width:52px; min-height:52px; background:var(--civic-navy); color:var(--cloud-white); box-shadow:var(--shadow-sm); } |
| assets/css/site.css | 193 | --cloud-white | Cloud White | .audio-control { min-width:52px; min-height:52px; background:var(--civic-navy); color:var(--cloud-white); box-shadow:var(--shadow-sm); } |
| assets/css/site.css | 196 | --warm-signal-blue | Azure | .audio-label { display:block; font-size:.72rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--warm-signal-blue); margin-bottom:4px; } |
| assets/css/site.css | 198 | --civic-navy | Civic Navy | display:block; font-family:"Sora","Inter",sans-serif; font-size:.94rem; line-height:1.2; color:var(--civic-navy); |
| assets/css/site.css | 202 | --ice-blue | Azure | .audio-range { width:100%; margin:0; accent-color:var(--ice-blue); background:transparent; } |
| assets/css/site.css | 205 | --civic-navy | Civic Navy | .audio-link { min-height:40px; padding:0 14px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); font-size:.84rem; } |
| assets/css/site.css | 205 | rgba(15,42,68,.14) | Civic Navy | .audio-link { min-height:40px; padding:0 14px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); font-size:.84rem; } |

### 2.2 Off-Brand Color Deviations
Found 67 non-brand color occurrences outside black/white/system keywords.
#### `assets/css/final-overrides.css`
| Line | Color value | Selector/context | Suggested brand replacement |
| --- | --- | --- | --- |
| 2 | #f8fbfe | background: #f8fbfe !important; | Use Cloud White (#F4F7FA) for light surfaces. |
| 144 | %23FF1200 | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect x='2' y='6.5' width='32' height='23' rx='8.5' fill='%23FF1200'/%3E%3Cpath d='M15 12.9 24 18l-9 5.1V12.9Z' fill='white'/%3E%3C/svg%3E") | Either document this as an external platform-brand exception or recolor to Azure/Civic Navy. |
| 148 | %23E95BFF | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | Either document this as an external platform-brand exception or recolor to Azure/Civic Navy. |
| 148 | %23C54EE8 | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | Either document this as an external platform-brand exception or recolor to Azure/Civic Navy. |
| 148 | %238432D9 | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | Either document this as an external platform-brand exception or recolor to Azure/Civic Navy. |
| 152 | %231ED760 | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Ccircle cx='18' cy='18' r='16' fill='%231ED760'/%3E%3Cpath d='M11 14.6c4.6-1.2 9.3-.8 13.5 1.2' stroke='white' stroke-width='2.6' stroke-lin | Either document this as an external platform-brand exception or recolor to Azure/Civic Navy. |
| 192 | rgba(6,20,33,0.14) | box-shadow: 0 12px 24px rgba(6,20,33,0.14); | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 196 | rgba(6,20,33,0.22) | box-shadow: 0 16px 30px rgba(6,20,33,0.22); | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 205 | rgba(11,23,36,0.44) | background: linear-gradient(180deg, rgba(11,23,36,0.44), rgba(11,23,36,0.28)); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 205 | rgba(11,23,36,0.28) | background: linear-gradient(180deg, rgba(11,23,36,0.44), rgba(11,23,36,0.28)); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 207 | rgba(6,20,33,0.18) | box-shadow: inset 0 1px 0 rgba(255,255,255,0.08), 0 18px 38px rgba(6,20,33,0.18); | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 355 | #111111 | color: #111111; | Use Slate (#3E4C59) for body text, Civic Navy for headings, Azure for accents, or Cloud White on dark surfaces. |
| 376 | #f7f8fa | background: #f7f8fa; | Use Cloud White (#F4F7FA) for light surfaces. |
| 388 | #133553 | background: #133553; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 389 | #133553 | border-color: #133553; | Use Slate/Civic Navy at a consistent opacity, or Azure for intentional focus/accent states. |
| 516 | #f3f7fb | --surface-soft:#f3f7fb; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 517 | #eef6fb | --surface-tint:#eef6fb; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 519 | #10283f | --ink:#10283f; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 520 | #5d6f7f | --muted:#5d6f7f; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 521 | #1b6f9f | --focus:#1b6f9f; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 539 | rgba(6,20,33,.28) | box-shadow:0 28px 58px rgba(6,20,33,.28); | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 606 | #10283f | background:#10283f; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 719 | #e7eef5 | background:#e7eef5; | Use Cloud White (#F4F7FA) for light surfaces. |
| 794 | #102b45 | background:linear-gradient(135deg,#102b45 0%,#173a59 100%); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 794 | #173a59 | background:linear-gradient(135deg,#102b45 0%,#173a59 100%); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1055 | #fbfdff | linear-gradient(180deg, #fbfdff 0%, #f7fbfe 44%, #f3f8fc 100%) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1055 | #f7fbfe | linear-gradient(180deg, #fbfdff 0%, #f7fbfe 44%, #f3f8fc 100%) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1055 | #f3f8fc | linear-gradient(180deg, #fbfdff 0%, #f7fbfe 44%, #f3f8fc 100%) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1079 | rgba(27,111,159,.45) | outline: 3px solid rgba(27,111,159,.45); | Use Slate/Civic Navy at a consistent opacity, or Azure for intentional focus/accent states. |
| 1246 | rgba(251,253,255,.88) | background: rgba(251,253,255,.88) !important; | Use Cloud White (#F4F7FA) for light surfaces. |
| 1286 | rgba(16,40,63,.82) | color: rgba(16,40,63,.82); | Use Slate (#3E4C59) for body text, Civic Navy for headings, Azure for accents, or Cloud White on dark surfaces. |
| 1347 | rgba(6,20,33,.22) | linear-gradient(90deg, rgba(6,20,33,.22), rgba(6,20,33,0) 44%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1347 | rgba(6,20,33,0) | linear-gradient(90deg, rgba(6,20,33,.22), rgba(6,20,33,0) 44%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1348 | rgba(6,20,33,.04) | linear-gradient(180deg, rgba(6,20,33,.04), rgba(6,20,33,.28)); | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1348 | rgba(6,20,33,.28) | linear-gradient(180deg, rgba(6,20,33,.04), rgba(6,20,33,.28)); | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1364 | rgba(6,20,33,.91) | linear-gradient(105deg, rgba(6,20,33,.91), rgba(15,42,68,.66) 42%, rgba(15,42,68,.2) 74%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1370 | rgba(6,20,33,.9) | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 43%, rgba(15,42,68,.22) 74%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1376 | rgba(6,20,33,.9) | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.62) 42%, rgba(15,42,68,.2) 74%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1382 | rgba(6,20,33,.9) | linear-gradient(105deg, rgba(6,20,33,.9), rgba(15,42,68,.64) 42%, rgba(15,42,68,.2) 74%), | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1401 | rgba(8,22,35,.54) | background: linear-gradient(180deg, rgba(8,22,35,.54), rgba(8,22,35,.32)) !important; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1401 | rgba(8,22,35,.32) | background: linear-gradient(180deg, rgba(8,22,35,.54), rgba(8,22,35,.32)) !important; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1403 | rgba(6,20,33,.2) | box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 22px 48px rgba(6,20,33,.2); | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 1441 | #071b2d | color: #071b2d; | Use Slate (#3E4C59) for body text, Civic Navy for headings, Azure for accents, or Cloud White on dark surfaces. |
| 1555 | rgba(238,246,251,.78) | linear-gradient(180deg, rgba(238,246,251,.78), rgba(255,255,255,.92)) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1593 | #0d263d | linear-gradient(180deg, #0d263d 0%, #102d47 100%) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1593 | #102d47 | linear-gradient(180deg, #0d263d 0%, #102d47 100%) !important; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 1611 | #102b45 | background: linear-gradient(135deg, #102b45 0%, #173a59 100%); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1611 | #173a59 | background: linear-gradient(135deg, #102b45 0%, #173a59 100%); | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1634 | #0b2137 | background: #0b2137; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 1664 | #e7eef5 | background: #e7eef5; | Use Cloud White (#F4F7FA) for light surfaces. |
| 1759 | #e8eff5 | background: #e8eff5; | Use Cloud White (#F4F7FA) for light surfaces. |
| 1796 | rgba(251,253,255,.94) | background: rgba(251,253,255,.94); | Use Cloud White (#F4F7FA) for light surfaces. |

#### `assets/css/site.css`
| Line | Color value | Selector/context | Suggested brand replacement |
| --- | --- | --- | --- |
| 7 | #FF5A5F | --electric-coral:#FF5A5F; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 8 | #183044 | --text:#183044; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 9 | #506273 | --text-soft:#506273; | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |
| 30 | #fbfdff | background:linear-gradient(180deg,#ffffff,#fbfdff 42%,#f8fbfe 100%); | Use Cloud White (#F4F7FA) for light surfaces. |
| 30 | #f8fbfe | background:linear-gradient(180deg,#ffffff,#fbfdff 42%,#f8fbfe 100%); | Use Cloud White (#F4F7FA) for light surfaces. |
| 119 | rgba(6,20,33,.84) | background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), var(--hero-image, url('../images/hero-18.jpg')) center center / cover no-repeat; | Use Civic Navy (#0F2A44) for dark surfaces. |
| 122 | rgba(6,20,33,.84) | .home-hero { background:linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), url('../images/featured-episode-8.jpg') center center / cover no-repeat; } | Use Civic Navy (#0F2A44) for dark surfaces. |
| 136 | #e8eff5 | .image-frame { position:relative; overflow:hidden; border-radius:var(--radius-xl); background:#e8eff5; border:1px solid rgba(15,42,68,.08); box-shadow:var(--shadow-md); } | Retokenize shadow with Civic Navy or Azure opacity, or use an approved shadow variable. |
| 142 | #f9fbfd | background:linear-gradient(180deg,#ffffff,#f9fbfd); border:1px solid var(--line); border-radius:var(--radius-xl); | Use Slate/Civic Navy at a consistent opacity, or Azure for intentional focus/accent states. |
| 151 | #f7fbff | .student-section { background:linear-gradient(180deg,#f7fbff,#ffffff); } | Use Cloud White, Civic Navy, or Azure depending on surface/accent role. |
| 163 | #ebf2f8 | .guest-card-image { aspect-ratio:4/3; background:#ebf2f8; overflow:hidden; } | Use Cloud White (#F4F7FA) for light surfaces. |
| 176 | #112f4a | background:linear-gradient(135deg,#112f4a,#183b5b); color:var(--cloud-white); border-radius:28px; | Use Slate/Civic Navy at a consistent opacity, or Azure for intentional focus/accent states. |
| 176 | #183b5b | background:linear-gradient(135deg,#112f4a,#183b5b); color:var(--cloud-white); border-radius:28px; | Use Slate/Civic Navy at a consistent opacity, or Azure for intentional focus/accent states. |
| 181 | #0c2238 | .site-footer { background:#0c2238; color:var(--cloud-white); padding:64px 0 28px; margin-top:96px; } | Use Civic Navy (#0F2A44) for dark surfaces. |

#### `assets/js/episodes.js`
| Line | Color value | Selector/context | Suggested brand replacement |
| --- | --- | --- | --- |
| 33 | #039 | .replace(/'/g, '&#039;'); | Map to the nearest locked token: Civic Navy, Azure, Slate, or Cloud White. |

### 2.3 Black/White Usage
Found 56 pure black/white occurrences and 5 system color keyword occurrences (`transparent` / `currentColor`). These are separated from wrong-brand color deviations as requested.
#### Pure Black/White
| File | Line | Value | Context | Classification |
| --- | --- | --- | --- | --- |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 94 | Black | <p>• The nuance behind fatherhood in Black communities<br /> | named pure black/white |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 94 | White | <p>His journey from Putnam City North to the White House</p> | named pure black/white |
| assets/css/final-overrides.css | 94 | rgba(255,255,255,0.92) | background: rgba(255,255,255,0.92); | pure black/white with alpha |
| assets/css/final-overrides.css | 136 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 136 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 136 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 136 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 140 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 140 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 140 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 140 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect width='36' height='36' rx='10' fill='%230F2A44'/%3E%3Cpath d='M11.5 9.5h9l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 10.5 25V11a1. | named pure black/white |
| assets/css/final-overrides.css | 144 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Crect x='2' y='6.5' width='32' height='23' rx='8.5' fill='%23FF1200'/%3E%3Cpath d='M15 12.9 24 18l-9 5.1V12.9Z' fill='white'/%3E%3C/svg%3E") | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 148 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Cdefs%3E%3CradialGradient id='g' cx='0' cy='0' r='1' gradientUnits='userSpaceOnUse' gradientTransform='translate(11 8) rotate(45) scale(30)' | named pure black/white |
| assets/css/final-overrides.css | 152 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Ccircle cx='18' cy='18' r='16' fill='%231ED760'/%3E%3Cpath d='M11 14.6c4.6-1.2 9.3-.8 13.5 1.2' stroke='white' stroke-width='2.6' stroke-lin | named pure black/white |
| assets/css/final-overrides.css | 152 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Ccircle cx='18' cy='18' r='16' fill='%231ED760'/%3E%3Cpath d='M11 14.6c4.6-1.2 9.3-.8 13.5 1.2' stroke='white' stroke-width='2.6' stroke-lin | named pure black/white |
| assets/css/final-overrides.css | 152 | white | background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 36' fill='none'%3E%3Ccircle cx='18' cy='18' r='16' fill='%231ED760'/%3E%3Cpath d='M11 14.6c4.6-1.2 9.3-.8 13.5 1.2' stroke='white' stroke-width='2.6' stroke-lin | named pure black/white |
| assets/css/final-overrides.css | 189 | rgba(255,255,255,0.08) | background: rgba(255,255,255,0.08); | pure black/white with alpha |
| assets/css/final-overrides.css | 207 | rgba(255,255,255,0.08) | box-shadow: inset 0 1px 0 rgba(255,255,255,0.08), 0 18px 38px rgba(6,20,33,0.18); | pure black/white with alpha |
| assets/css/final-overrides.css | 354 | #ffffff | background: #ffffff; | pure black/white |
| assets/css/final-overrides.css | 383 | #ffffff | color: #ffffff; | pure black/white |
| assets/css/final-overrides.css | 515 | #ffffff | --surface:#ffffff; | pure black/white |
| assets/css/final-overrides.css | 654 | rgba(255,255,255,.94) | background:rgba(255,255,255,.94); | pure black/white with alpha |
| assets/css/final-overrides.css | 696 | #fff | background:#fff; | pure black/white |
| assets/css/final-overrides.css | 805 | #ffffff | background:#ffffff; | pure black/white |
| assets/css/final-overrides.css | 861 | #fff | background:#fff; | pure black/white |
| assets/css/final-overrides.css | 877 | #fff | background:#fff; | pure black/white |
| assets/css/final-overrides.css | 906 | #fff | background:#fff; | pure black/white |
| assets/css/final-overrides.css | 925 | #fff | background:#fff; | pure black/white |
| assets/css/final-overrides.css | 1403 | rgba(255,255,255,.08) | box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 22px 48px rgba(6,20,33,.2); | pure black/white with alpha |
| assets/css/final-overrides.css | 1456 | rgba(255,255,255,.94) | background: rgba(255,255,255,.94); | pure black/white with alpha |
| assets/css/final-overrides.css | 1481 | rgba(255,255,255,.1) | background: rgba(255,255,255,.1); | pure black/white with alpha |
| assets/css/final-overrides.css | 1497 | rgba(255,255,255,.94) | background: rgba(255,255,255,.94) !important; | pure black/white with alpha |
| assets/css/final-overrides.css | 1531 | rgba(255,255,255,.96) | background: rgba(255,255,255,.96); | pure black/white with alpha |
| assets/css/final-overrides.css | 1549 | rgba(255,255,255,.92) | background: rgba(255,255,255,.92); | pure black/white with alpha |
| assets/css/final-overrides.css | 1555 | rgba(255,255,255,.92) | linear-gradient(180deg, rgba(238,246,251,.78), rgba(255,255,255,.92)) !important; | pure black/white with alpha |
| assets/css/final-overrides.css | 1601 | rgba(255,255,255,.065) | background: rgba(255,255,255,.065); | pure black/white with alpha |
| assets/css/final-overrides.css | 1847 | rgba(255,255,255,.9) | background: rgba(255,255,255,.9); | pure black/white with alpha |
| assets/css/site.css | 30 | #ffffff | background:linear-gradient(180deg,#ffffff,#fbfdff 42%,#f8fbfe 100%); | pure black/white |
| assets/css/site.css | 102 | #fff | .button-outline { min-height:46px; padding:0 18px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); } | pure black/white |
| assets/css/site.css | 103 | rgba(255,255,255,.06) | .button-ghost { min-height:50px; padding:0 22px; border:1.5px solid rgba(244,247,250,.24); background:rgba(255,255,255,.06); color:var(--cloud-white); backdrop-filter:blur(10px); } | pure black/white with alpha |
| assets/css/site.css | 128 | rgba(255,255,255,.08) | .hero-panel { background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.14); border-radius:var(--radius-xl); padding:24px; backdrop-filter:blur(12px); color:var(--cloud-white); } | pure black/white with alpha |
| assets/css/site.css | 128 | rgba(255,255,255,.14) | .hero-panel { background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.14); border-radius:var(--radius-xl); padding:24px; backdrop-filter:blur(12px); color:var(--cloud-white); } | pure black/white with alpha |
| assets/css/site.css | 132 | rgba(255,255,255,.12) | .hero-meta-item { display:flex; align-items:center; justify-content:space-between; gap:16px; padding-top:10px; border-top:1px solid rgba(255,255,255,.12); font-size:.9rem; } | pure black/white with alpha |
| assets/css/site.css | 142 | #ffffff | background:linear-gradient(180deg,#ffffff,#f9fbfd); border:1px solid var(--line); border-radius:var(--radius-xl); | pure black/white |
| assets/css/site.css | 151 | #ffffff | .student-section { background:linear-gradient(180deg,#f7fbff,#ffffff); } | pure black/white |
| assets/css/site.css | 157 | #fff | .mini-card { background:#fff; border:1px solid var(--line); border-radius:20px; padding:20px; box-shadow:var(--shadow-sm); } | pure black/white |
| assets/css/site.css | 161 | #fff | .guest-card { overflow:hidden; background:#fff; border:1px solid var(--line); border-radius:24px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; transition:transform var(--ease), box-shadow var(--ease), border-color var(--ease); } | pure black/white |
| assets/css/site.css | 171 | rgba(255,255,255,.07) | .platform-card { background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.12); border-radius:20px; padding:20px; text-align:center; transition:transform var(--ease), background var(--ease); } | pure black/white with alpha |
| assets/css/site.css | 171 | rgba(255,255,255,.12) | .platform-card { background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.12); border-radius:20px; padding:20px; text-align:center; transition:transform var(--ease), background var(--ease); } | pure black/white with alpha |
| assets/css/site.css | 172 | rgba(255,255,255,.1) | .platform-card:hover { transform:translateY(-3px); background:rgba(255,255,255,.1); } | pure black/white with alpha |
| assets/css/site.css | 205 | #fff | .audio-link { min-height:40px; padding:0 14px; border:1px solid rgba(15,42,68,.14); background:#fff; color:var(--civic-navy); font-size:.84rem; } | pure black/white |
#### System Keywords
| File | Line | Value | Context | Classification |
| --- | --- | --- | --- | --- |
| assets/css/final-overrides.css | 118 | transparent | border-color: transparent; | system/non-palette keyword |
| assets/css/final-overrides.css | 1449 | transparent | border-color: transparent !important; | system/non-palette keyword |
| assets/css/site.css | 47 | transparent | button { font:inherit; border:0; background:transparent; cursor:pointer; } | system/non-palette keyword |
| assets/css/site.css | 58 | currentColor | .eyebrow::before { content:""; width:32px; height:1px; background:currentColor; opacity:.55; } | system/non-palette keyword |
| assets/css/site.css | 202 | transparent | .audio-range { width:100%; margin:0; accent-color:var(--ice-blue); background:transparent; } | system/non-palette keyword |

## 3. Typography Inventory

### 3.1 Font Families Currently Loaded
Found 40 font-load declarations. All HTML pages load the same Google Fonts URL for Inter and Sora; no `@font-face` declarations were found.
| File | Line | Declaration |
| --- | --- | --- |
| about/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| about/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| contact/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| contact/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| guests/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| guests/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| podcast-team/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| podcast-team/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| sponsors/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| sponsors/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| watch-listen/index.html | 24 | <link rel="preconnect" href="https://fonts.googleapis.com"> |
| watch-listen/index.html | 26 | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |

Loaded-but-not-aligned notes:
| File | Line | Issue | Declaration |
| --- | --- | --- | --- |
| about/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| about/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| contact/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| contact/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| guests/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| guests/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| podcast-team/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| podcast-team/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| sponsors/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| sponsors/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| watch-listen/index.html | 26 | Inter loads 700 and 800; locked Inter weights are 400/500/600. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |
| watch-listen/index.html | 26 | Sora loads 300/400/500; locked Sora weights are 600/700/800. | <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"> |

Used but not loaded: no used brand font family was missing from the loaded Google Fonts. `Bebas Neue` is allowed but not loaded or used.

### 3.2 Brand-Compliant Font Usage
Found 14 brand-compliant `font-family` declarations.
| File | Line | font-family | Selector/context |
| --- | --- | --- | --- |
| assets/css/final-overrides.css | 212 | "Inter", system-ui, sans-serif | font-family: "Inter", system-ui, sans-serif; |
| assets/css/final-overrides.css | 673 | "Sora","Inter",sans-serif | font-family:"Sora","Inter",sans-serif; |
| assets/css/final-overrides.css | 739 | "Sora","Inter",sans-serif | font-family:"Sora","Inter",sans-serif; |
| assets/css/final-overrides.css | 1184 | "Sora", "Inter", system-ui, sans-serif | font-family: "Sora", "Inter", system-ui, sans-serif; |
| assets/css/final-overrides.css | 1409 | "Sora", "Inter", sans-serif | font-family: "Sora", "Inter", sans-serif; |
| assets/css/site.css | 28 | "Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif | font-family:"Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; |
| assets/css/site.css | 60 | "Sora","Inter",sans-serif | margin:0; font-family:"Sora","Inter",sans-serif; letter-spacing:-.035em; line-height:1.06; |
| assets/css/site.css | 109 | "Sora","Inter",sans-serif | .brand-name |
| assets/css/site.css | 129 | "Sora","Inter",sans-serif | .hero-panel h2,.hero-panel h3 |
| assets/css/site.css | 147 | "Sora","Inter",sans-serif | margin:0 0 16px; font-family:"Sora","Inter",sans-serif; font-size:clamp(1.45rem,2.1vw,2.15rem); line-height:1.1; |
| assets/css/site.css | 158 | "Sora","Inter",sans-serif | .mini-card h3 |
| assets/css/site.css | 173 | "Sora","Inter",sans-serif | .platform-card strong |
| assets/css/site.css | 184 | "Sora","Inter",sans-serif | .footer-column h2 |
| assets/css/site.css | 198 | "Sora","Inter",sans-serif | display:block; font-family:"Sora","Inter",sans-serif; font-size:.94rem; line-height:1.2; color:var(--civic-navy); |

### 3.3 Off-Brand Font Declarations
No off-brand primary `font-family` declarations found. System stacks appear only as fallbacks after Inter/Sora or as generic fallback tokens.

### 3.4 Font Weights in Use
Declared `font-weight` values:
| Weight | Occurrences |
| --- | --- |
| 600 | 3 |
| 700 | 13 |
| 800 | 12 |

Line-level font-weight inventory:
| File | Line | Weight | Selector/context |
| --- | --- | --- | --- |
| assets/css/final-overrides.css | 97 | 700 | font-weight: 700; |
| assets/css/final-overrides.css | 214 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 242 | 700 | font-weight: 700; |
| assets/css/final-overrides.css | 363 | 700 | font-weight: 700; |
| assets/css/final-overrides.css | 632 | 800 | font-weight:800; |
| assets/css/final-overrides.css | 704 | 800 | font-weight:800; |
| assets/css/final-overrides.css | 767 | 800 | font-weight:800; |
| assets/css/final-overrides.css | 880 | 800 | font-weight:800; |
| assets/css/final-overrides.css | 914 | 800 | font-weight:800; |
| assets/css/final-overrides.css | 1070 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1185 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1217 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1239 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1276 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1435 | 800 | font-weight: 800; |
| assets/css/final-overrides.css | 1690 | 700 | font-weight: 700; |
| assets/css/final-overrides.css | 1739 | 700 | font-weight: 700; |
| assets/css/final-overrides.css | 1786 | 700 | font-weight: 700; |
| assets/css/site.css | 55 | 700 | font-size:12px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; |
| assets/css/site.css | 96 | 700 | border-radius:999px; font-weight:700; |
| assets/css/site.css | 109 | 700 | .brand-name |
| assets/css/site.css | 110 | 600 | .brand-tag |
| assets/css/site.css | 112 | 700 | .nav a |
| assets/css/site.css | 145 | 700 | .episode-kicker |
| assets/css/site.css | 150 | 600 | .episode-meta |
| assets/css/site.css | 165 | 700 | .guest-role |
| assets/css/site.css | 196 | 700 | .audio-label |
| assets/css/site.css | 203 | 600 | .audio-times |

Non-aligned weight flags:
| File | Line | Weight | Selector/context | Why flagged |
| --- | --- | --- | --- | --- |
| assets/css/site.css | 112 | 700 | .nav a | Inter/UI text appears heavier than locked 400/500/600 range. |
| assets/css/site.css | 165 | 700 | .guest-role | Inter/UI text appears heavier than locked 400/500/600 range. |
| assets/css/site.css | 196 | 700 | .audio-label | Inter/UI text appears heavier than locked 400/500/600 range. |

## 4. Capitalization Audit

### 4.1 Section Headers (h1–h6 inside main content)
| File | Line | Tag | Exact text | Current case |
| --- | --- | --- | --- | --- |
| about/index.html | 61 | h1 | A PODCAST ROOTED IN OKLAHOMA CITY AND BUILT WITH STUDENTS. | ALL CAPS |
| about/index.html | 69 | h2 | What makes VOICES of OKC distinct | Title/Natural/Mixed |
| about/index.html | 82 | h2 | Thoughtful conversations with real civic weight. | Title/Natural/Mixed |
| about/index.html | 97 | h3 | ROOTED IN OKLAHOMA CITY | ALL CAPS |
| about/index.html | 101 | h3 | CONNECTED TO CITY CENTER | ALL CAPS |
| about/index.html | 105 | h3 | BUILT FOR DEPTH | ALL CAPS |
| contact/index.html | 59 | h1 | LET'S KEEP THE CONVERSATION GROUNDED AND USEFUL. | ALL CAPS |
| contact/index.html | 67 | h2 | General Contact Form | Title/Natural/Mixed |
| contact/index.html | 79 | h2 | Direct contact | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 65 | h1 | BEFORE THEY BREAK: GNWY ON MENTAL HEALTH, PURPOSE & HOPE | ALL CAPS |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 65 | h1 | BEYOND QUICK FIX: FUNCTIONAL MEDICINE AND REAL HEALING IN OKLAHOMA CITY | ALL CAPS |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 65 | h1 | BEYOND WINNING: BRYAN FETZER ON PRESSURE AND PERSPECTIVE IN OKC | ALL CAPS |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 65 | h1 | COMMUNITY THROUGH CONVERSATION: MIKE HEARNE ON STORYTELLING IN OKLAHOMA CITY | ALL CAPS |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 65 | h1 | CUTTING WEIGHT, CUTTING DRAMA: VICTORIA’S STORY OF HOPE | ALL CAPS |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 65 | h1 | FROM MISNOMER TO MENTORSHIP: DERRICK SIER ON REBUILDING IDENTITY IN OKLAHOMA CITY | ALL CAPS |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 65 | h1 | FROM POLICY TO PEOPLE: THE PRIVILEGE OF LEADING OKLAHOMA CITY | ALL CAPS |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 65 | h1 | HOPE IN HARD PLACES: JABEE WILLIAMS ON OKC, VIOLENCE, AND HOPE | ALL CAPS |
| episodes/index.html | 58 | h1 | CONVERSATIONS SHAPING OKLAHOMA CITY. | ALL CAPS |
| episodes/index.html | 73 | h2 | LOADING EPISODES... | ALL CAPS |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 65 | h1 | LIFE NEEDS VISION: CAREY CONLEY ON VISION, MENTAL HEALTH, AND YOUNG ADULTS | ALL CAPS |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 65 | h1 | OVER 22,000 BABIES LATER: WHAT ONE DOCTOR LEARNED ABOUT LIFE AND HOPE | ALL CAPS |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 65 | h1 | RETHINKING JUSTICE IN OKLAHOMA: PUBLIC SAFETY, REAL REFORM, AND REDEMPTION | ALL CAPS |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 65 | h1 | USE WISELY: ADAM COURY ON LEADERSHIP, LEARNING, AND THE NEXT GENERATION | ALL CAPS |
| guests/index.html | 59 | h1 | KNOW A VOICE OKLAHOMA CITY SHOULD HEAR? | ALL CAPS |
| guests/index.html | 67 | h2 | What makes a strong nomination | Title/Natural/Mixed |
| guests/index.html | 79 | h2 | Guest Nomination Form | Title/Natural/Mixed |
| index.html | 61 | h1 | STORIES THAT HELP US SEE OKLAHOMA CITY MORE CLEARLY. | ALL CAPS |
| index.html | 73 | h2 | Long-form video + audio from Oklahoma City | Title/Natural/Mixed |
| index.html | 93 | h2 | FROM POLICY TO PEOPLE: MAYOR DAVID HOLT ON LEADERSHIP, YOUTH, AND OKLAHOMA CITY | ALL CAPS |
| index.html | 111 | h2 | A civic platform, not just a podcast feed. | Title/Natural/Mixed |
| index.html | 116 | h3 | Long-form video + audio | Title/Natural/Mixed |
| index.html | 120 | h3 | Student production experience | Title/Natural/Mixed |
| index.html | 124 | h3 | Civic leadership conversations | Title/Natural/Mixed |
| index.html | 128 | h3 | Local stories with dignity | Title/Natural/Mixed |
| index.html | 139 | h2 | A growing archive of city-shaping conversations. | Title/Natural/Mixed |
| index.html | 143 | h3 | Civic Leadership | Title/Natural/Mixed |
| index.html | 144 | h3 | Business & Entrepreneurship | Title/Natural/Mixed |
| index.html | 145 | h3 | Arts & Culture | Title/Natural/Mixed |
| index.html | 146 | h3 | Restoration & Second Chances | Title/Natural/Mixed |
| index.html | 147 | h3 | Youth & Family | Title/Natural/Mixed |
| index.html | 148 | h3 | Faith, Purpose & Resilience | Title/Natural/Mixed |
| index.html | 149 | h3 | Sports, Mindset & Performance | Title/Natural/Mixed |
| index.html | 150 | h3 | Community Builders | Title/Natural/Mixed |
| index.html | 159 | h2 | A podcast rooted in Oklahoma City. | Title/Natural/Mixed |
| index.html | 178 | h2 | Produced with students. Built for real growth. | Title/Natural/Mixed |
| index.html | 196 | h3 | Student hosts | Title/Natural/Mixed |
| index.html | 200 | h3 | Production experience | Title/Natural/Mixed |
| index.html | 204 | h3 | Civic access | Title/Natural/Mixed |
| index.html | 208 | h3 | Long-term impact | Title/Natural/Mixed |
| index.html | 219 | h2 | The beginning of a real Oklahoma City archive. | Title/Natural/Mixed |
| index.html | 227 | h3 | FROM POLICY TO PEOPLE: THE PRIVILEGE OF LEADING OKLAHOMA CITY | ALL CAPS |
| index.html | 237 | h3 | 16 YEARS OLD... AND ALREADY TEACHING US ABOUT HOPE | ALL CAPS |
| index.html | 247 | h3 | FROM MISNOMER TO MENTORSHIP: REBUILDING IDENTITY IN OKC | ALL CAPS |
| index.html | 257 | h3 | USE WISELY: LEADERSHIP, LEARNING, AND THE NEXT GENERATION | ALL CAPS |
| index.html | 274 | h2 | Wherever you are, start here. | Title/Natural/Mixed |
| index.html | 293 | h2 | PARTNER WITH STORIES THAT STRENGTHEN THE CITY. | ALL CAPS |
| index.html | 311 | h2 | KNOW A VOICE OKLAHOMA CITY SHOULD HEAR? | ALL CAPS |
| podcast-team/index.html | 62 | h1 | THE PEOPLE BEHIND VOICES of OKC. | Title/Natural/Mixed |
| podcast-team/index.html | 71 | h2 | What this page holds | Title/Natural/Mixed |
| podcast-team/index.html | 88 | h2 | JED CHAPPELL | ALL CAPS |
| podcast-team/index.html | 107 | h2 | REAL EXPERIENCE. REAL RESPONSIBILITY. REAL GROWTH. | ALL CAPS |
| podcast-team/index.html | 125 | h3 | Storytelling | Title/Natural/Mixed |
| podcast-team/index.html | 129 | h3 | Confidence | Title/Natural/Mixed |
| podcast-team/index.html | 133 | h3 | Civic Access | Title/Natural/Mixed |
| podcast-team/index.html | 137 | h3 | Future Skills | Title/Natural/Mixed |
| podcast-team/index.html | 151 | h2 | BO WRIGHT + BONUS CREATIVE | ALL CAPS |
| sponsors/index.html | 61 | h1 | SUPPORT CONVERSATIONS THAT MATTER AND THE STUDENTS HELPING PRODUCE THEM. | ALL CAPS |
| sponsors/index.html | 69 | h2 | What your sponsorship supports | Title/Natural/Mixed |
| sponsors/index.html | 83 | h2 | More than ad placement. | Title/Natural/Mixed |
| sponsors/index.html | 91 | h3 | COMMON SPONSOR OPPORTUNITIES | ALL CAPS |
| sponsors/index.html | 112 | h2 | A good sponsor does not interrupt the story. It helps make the story possible. | Title/Natural/Mixed |
| sponsors/index.html | 116 | h2 | Sponsor Inquiry Form | Title/Natural/Mixed |
| watch-listen/index.html | 59 | h1 | FOLLOW THE CONVERSATIONS WHERE YOU ALREADY ARE. | ALL CAPS |
| watch-listen/index.html | 77 | h2 | Start with the latest episode, then explore by theme. | Title/Natural/Mixed |

Flagged capitalization issues:
| File | Line | Tag | Exact text | Current case | Why flagged |
| --- | --- | --- | --- | --- | --- |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 65 | h1 | BEFORE THEY BREAK: GNWY ON MENTAL HEALTH, PURPOSE & HOPE | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 65 | h1 | BEYOND QUICK FIX: FUNCTIONAL MEDICINE AND REAL HEALING IN OKLAHOMA CITY | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 65 | h1 | BEYOND WINNING: BRYAN FETZER ON PRESSURE AND PERSPECTIVE IN OKC | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 65 | h1 | COMMUNITY THROUGH CONVERSATION: MIKE HEARNE ON STORYTELLING IN OKLAHOMA CITY | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 65 | h1 | CUTTING WEIGHT, CUTTING DRAMA: VICTORIA’S STORY OF HOPE | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 65 | h1 | FROM MISNOMER TO MENTORSHIP: DERRICK SIER ON REBUILDING IDENTITY IN OKLAHOMA CITY | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 65 | h1 | FROM POLICY TO PEOPLE: THE PRIVILEGE OF LEADING OKLAHOMA CITY | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 65 | h1 | HOPE IN HARD PLACES: JABEE WILLIAMS ON OKC, VIOLENCE, AND HOPE | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 65 | h1 | LIFE NEEDS VISION: CAREY CONLEY ON VISION, MENTAL HEALTH, AND YOUNG ADULTS | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 65 | h1 | OVER 22,000 BABIES LATER: WHAT ONE DOCTOR LEARNED ABOUT LIFE AND HOPE | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 65 | h1 | RETHINKING JUSTICE IN OKLAHOMA: PUBLIC SAFETY, REAL REFORM, AND REDEMPTION | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 65 | h1 | USE WISELY: ADAM COURY ON LEADERSHIP, LEARNING, AND THE NEXT GENERATION | ALL CAPS | Episode title rendered in all caps; publishing titles should use Title Case or natural sentence case. |

### 4.2 Episode Titles
| File | Line | Episode title as rendered | Current case | Flag |
| --- | --- | --- | --- | --- |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 65 | BEFORE THEY BREAK: GNWY ON MENTAL HEALTH, PURPOSE & HOPE | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 65 | BEYOND QUICK FIX: FUNCTIONAL MEDICINE AND REAL HEALING IN OKLAHOMA CITY | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 65 | BEYOND WINNING: BRYAN FETZER ON PRESSURE AND PERSPECTIVE IN OKC | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 65 | COMMUNITY THROUGH CONVERSATION: MIKE HEARNE ON STORYTELLING IN OKLAHOMA CITY | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 65 | CUTTING WEIGHT, CUTTING DRAMA: VICTORIA’S STORY OF HOPE | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 65 | FROM MISNOMER TO MENTORSHIP: DERRICK SIER ON REBUILDING IDENTITY IN OKLAHOMA CITY | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 65 | FROM POLICY TO PEOPLE: THE PRIVILEGE OF LEADING OKLAHOMA CITY | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 65 | HOPE IN HARD PLACES: JABEE WILLIAMS ON OKC, VIOLENCE, AND HOPE | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 65 | LIFE NEEDS VISION: CAREY CONLEY ON VISION, MENTAL HEALTH, AND YOUNG ADULTS | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 65 | OVER 22,000 BABIES LATER: WHAT ONE DOCTOR LEARNED ABOUT LIFE AND HOPE | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 65 | RETHINKING JUSTICE IN OKLAHOMA: PUBLIC SAFETY, REAL REFORM, AND REDEMPTION | ALL CAPS | Flag: publishing title is ALL CAPS |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 65 | USE WISELY: ADAM COURY ON LEADERSHIP, LEARNING, AND THE NEXT GENERATION | ALL CAPS | Flag: publishing title is ALL CAPS |

### 4.3 Button/CTA Text
Found 104 button/link-styled-as-button instances.
| File | Line | Text | Class | Case |
| --- | --- | --- | --- | --- |
| about/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| about/index.html | 64 | Watch the Show | button | Title/Natural/Mixed |
| about/index.html | 65 | Sponsor the Show | button-secondary | Title/Natural/Mixed |
| contact/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| contact/index.html | 74 | Send Message | button-secondary | Title/Natural/Mixed |
| contact/index.html | 82 | info@voicesofokc.com | button-secondary | lower/sentence |
| contact/index.html | 83 | Nominate a Guest | button-outline | Title/Natural/Mixed |
| contact/index.html | 84 | Sponsor the Show | button-outline | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 74 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 75 | Apple | action-pill | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 76 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 77 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/index.html | 75 | Back Home | button-outline | Title/Natural/Mixed |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 52 | Watch Now | button-secondary | Title/Natural/Mixed |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 75 | YouTube | action-pill | Title/Natural/Mixed |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 76 | Apple | action-pill | Title/Natural/Mixed |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 77 | Spotify | action-pill | Title/Natural/Mixed |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 78 | Podbean | action-pill action-pill--primary | Title/Natural/Mixed |
| guests/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| guests/index.html | 89 | Nominate a Guest | button-secondary | Title/Natural/Mixed |
| index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| index.html | 64 | WATCH EPISODES | button | ALL CAPS |
| index.html | 65 | BECOME A SPONSOR | button-ghost | ALL CAPS |
| index.html | 66 | HOW STUDENTS ARE INVOLVED | button-ghost | ALL CAPS |
| index.html | 98 | Watch on YouTube | action-pill | Title/Natural/Mixed |
| index.html | 99 | Spotify | action-pill | Title/Natural/Mixed |
| index.html | 100 | Apple Podcasts | action-pill | Title/Natural/Mixed |
| index.html | 101 | Show Notes | action-pill action-pill--primary | Title/Natural/Mixed |
| index.html | 165 | ABOUT VOICES of OKC | button-secondary | Title/Natural/Mixed |
| index.html | 230 | View Episode | button-outline | Title/Natural/Mixed |
| index.html | 240 | Explore Archive | button-outline | Title/Natural/Mixed |
| index.html | 250 | View Episode | button-outline | Title/Natural/Mixed |
| index.html | 260 | View Episode | button-outline | Title/Natural/Mixed |
| index.html | 265 | EXPLORE ALL EPISODES | button-secondary | ALL CAPS |
| index.html | 266 | NOMINATE A GUEST | button-outline | ALL CAPS |
| index.html | 284 | WATCH + LISTEN OPTIONS | button | ALL CAPS |
| index.html | 297 | VIEW SPONSOR OPPORTUNITIES | button | ALL CAPS |
| index.html | 298 | CONTACT US | button-ghost | ALL CAPS |
| index.html | 315 | NOMINATE A GUEST | button-secondary | ALL CAPS |
| podcast-team/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| podcast-team/index.html | 65 | The Host | button | Title/Natural/Mixed |
| podcast-team/index.html | 66 | Student Production | button-secondary | Title/Natural/Mixed |
| podcast-team/index.html | 67 | Bonus Creative | button-outline | Title/Natural/Mixed |
| podcast-team/index.html | 159 | Visit Bonus Creative | button-secondary | Title/Natural/Mixed |
| sponsors/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| sponsors/index.html | 64 | Become a Sponsor | button | Title/Natural/Mixed |
| sponsors/index.html | 65 | Watch the Show | button-secondary | Title/Natural/Mixed |
| sponsors/index.html | 102 | Start a Conversation | button-secondary | Title/Natural/Mixed |
| sponsors/index.html | 103 | Give Through City Center | button-outline | Title/Natural/Mixed |
| sponsors/index.html | 127 | Submit Sponsor Inquiry | button-secondary | Title/Natural/Mixed |
| watch-listen/index.html | 50 | Watch Now | button-secondary | Title/Natural/Mixed |
| watch-listen/index.html | 81 | Explore Episodes | button | Title/Natural/Mixed |

CTA casing observations: most primary navigation CTAs use Title/Natural case (`Watch Now`, `Show Notes`, `View Episode`), while platform labels are short Title/Natural labels. No direct same-context casing drift was found.

### 4.4 Navigation
Found nav menus in 20 HTML files.
| Occurrences | Nav items |
| --- | --- |
| 20 | Episodes / About / Podcast Team / Guests / Sponsors / Contact |

Navigation drift: no text drift found in primary nav labels across pages. Active `aria-current` differs by page as expected.

## 5. Tagline Audit
- Required tagline: `Stories that help us see Oklahoma City more clearly.`
- Exact tagline instances with locked casing found: 0
- Same words found with casing drift:
| File | Line | Current text/context |
| --- | --- | --- |
| index.html | 61 | <h1 class="title-xl title-with-rule title-with-rule--wide title-with-rule--light">STORIES THAT HELP US SEE OKLAHOMA CITY MORE CLEARLY.</h1> |
- Places where a tagline/descriptor appears but is different:
| File | Line | Text | Context |
| --- | --- | --- | --- |
| about/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| about/index.html | 119 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| contact/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| contact/index.html | 99 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/before-they-break-gnwy-on-mental-health-purpose-hope/index.html | 147 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/beyond-quick-fix-functional-medicine-and-real-healing-in-oklahoma-city/index.html | 106 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc/index.html | 105 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city/index.html | 119 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/cutting-weight-cutting-drama-victorias-story-of-hope/index.html | 133 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city/index.html | 115 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/from-policy-to-people-the-privilege-of-leading-oklahoma-city/index.html | 131 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/hope-in-hard-places-jabee-williams-on-okc-violence-and-hope/index.html | 156 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/index.html | 90 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/life-needs-vision-carey-conley-on-vision-mental-health-and-young-adults/index.html | 138 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope/index.html | 115 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption/index.html | 109 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 40 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| episodes/use-wisely-adam-coury-on-leadership-learning-and-the-next-generation/index.html | 105 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| guests/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| guests/index.html | 105 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| index.html | 329 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| podcast-team/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| podcast-team/index.html | 174 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| sponsors/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| sponsors/index.html | 142 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
| watch-listen/index.html | 38 | A CITY CENTER PODCAST | <span class="brand-tag">A CITY CENTER PODCAST</span> |
| watch-listen/index.html | 95 | A CITY CENTER PODCAST | <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span> |
- Suggested missing or mismatched locations: homepage hero currently uses the right words but not the locked casing; footer brand block, `assets/data/site-config.json` brand metadata, and default social/meta descriptions do not carry the locked tagline. These currently use page-specific positioning copy or the repeated descriptor `A CITY CENTER PODCAST`.

## 6. Voice / Copy Red Flags
No exact matches found for the requested red-flag phrases, excessive exclamation patterns, or sales-style CTA examples in scanned HTML/JSON/CSS/JS files.

## 7. Inline Styles
Inline `<style>` blocks found: 0
Inline `style="..."` attributes found: 0

## 8. Stylesheet Structural Issues
### `!important` Declarations
| File | Count |
| --- | --- |
| assets/css/final-overrides.css | 130 |
| assets/css/site.css | 0 |

### Duplicate Selectors
Found 93 selectors defined multiple times.
| Selector | Locations |
| --- | --- |
| .about-image | assets/css/final-overrides.css:293, assets/css/final-overrides.css:324, assets/css/site.css:140 |
| .action-pill | assets/css/final-overrides.css:84, assets/css/final-overrides.css:1431, assets/css/final-overrides.css:1454, assets/css/final-overrides.css:2044 |
| .action-pill--primary | assets/css/final-overrides.css:116, assets/css/final-overrides.css:1446 |
| .action-pill:hover | assets/css/final-overrides.css:111, assets/css/final-overrides.css:1466 |
| .archive-toolbar | assets/css/final-overrides.css:847, assets/css/final-overrides.css:1039 |
| .audio-control | assets/css/final-overrides.css:1807, assets/css/final-overrides.css:2077, assets/css/site.css:193 |
| .audio-grid | assets/css/final-overrides.css:1802, assets/css/final-overrides.css:1876, assets/css/final-overrides.css:2072, assets/css/site.css:192, assets/css/site.css:212, assets/css/site.css:232 |
| .audio-label | assets/css/final-overrides.css:1274, assets/css/site.css:196 |
| .audio-link | assets/css/final-overrides.css:75, assets/css/final-overrides.css:467, assets/css/final-overrides.css:1844, assets/css/final-overrides.css:2105, assets/css/site.css:205, assets/css/site.css:233 |
| .audio-links | assets/css/final-overrides.css:60, assets/css/final-overrides.css:462, assets/css/final-overrides.css:1881, assets/css/final-overrides.css:2095, assets/css/final-overrides.css:2099, assets/css/site.css:204, assets/css/site.css:213 |
| .audio-meta | assets/css/final-overrides.css:2082, assets/css/site.css:195 |
| .audio-player | assets/css/final-overrides.css:1793, assets/css/final-overrides.css:2066, assets/css/site.css:41, assets/css/site.css:187 |
| .audio-progress-wrap | assets/css/final-overrides.css:1813, assets/css/site.css:201 |
| .audio-range | assets/css/final-overrides.css:1817, assets/css/site.css:202 |
| .audio-status-note | assets/css/final-overrides.css:2086, assets/css/site.css:206 |
| .audio-title | assets/css/final-overrides.css:2090, assets/css/site.css:197 |
| .body-copy p | assets/css/final-overrides.css:1135, assets/css/site.css:92 |
| .brand | assets/css/final-overrides.css:1256, assets/css/site.css:106, assets/css/site.css:217 |
| .brand-mark | assets/css/final-overrides.css:1260, assets/css/final-overrides.css:1988, assets/css/site.css:107 |
| .brand-name | assets/css/final-overrides.css:1265, assets/css/site.css:109 |
| .button | assets/css/final-overrides.css:1439, assets/css/site.css:100 |
| .button-row | assets/css/final-overrides.css:67, assets/css/final-overrides.css:415, assets/css/site.css:93 |
| .card | assets/css/final-overrides.css:1496, assets/css/final-overrides.css:2024 |
| .card-surface .episode-actions | assets/css/final-overrides.css:329, assets/css/final-overrides.css:489 |
| .card-surface .episode-actions .action-pill | assets/css/final-overrides.css:347, assets/css/final-overrides.css:495 |
| .card-surface .episode-actions .platform-icon-img | assets/css/final-overrides.css:393, assets/css/final-overrides.css:505 |
| .container | assets/css/final-overrides.css:1943, assets/css/site.css:49 |
| .cta-band | assets/css/final-overrides.css:1609, assets/css/site.css:175 |
| .detail-card-visual | assets/css/final-overrides.css:21, assets/css/final-overrides.css:433, assets/css/final-overrides.css:455, assets/css/final-overrides.css:2029 |
| .episode-archive-card p | assets/css/final-overrides.css:1678, assets/css/final-overrides.css:2058 |
| .episode-archive-grid | assets/css/final-overrides.css:1651, assets/css/final-overrides.css:1868, assets/css/final-overrides.css:2048 |
| .episode-card-actions | assets/css/final-overrides.css:1693, assets/css/final-overrides.css:2036 |
| .episode-notes a | assets/css/final-overrides.css:1169, assets/css/final-overrides.css:1215 |
| .episode-notes blockquote | assets/css/final-overrides.css:1199, assets/css/final-overrides.css:1223 |
| .footer-grid | assets/css/final-overrides.css:1923, assets/css/site.css:182 |
| .form-embed textarea | assets/css/final-overrides.css:919, assets/css/final-overrides.css:930 |
| .guest-card | assets/css/final-overrides.css:1529, assets/css/site.css:161 |
| .guest-card-copy | assets/css/final-overrides.css:1539, assets/css/site.css:164 |
| .guest-card-image | assets/css/final-overrides.css:1534, assets/css/site.css:163 |
| .guest-grid | assets/css/site.css:160, assets/css/site.css:210 |
| .guest-nomination-cta | assets/css/final-overrides.css:792, assets/css/final-overrides.css:804, assets/css/final-overrides.css:1004, assets/css/final-overrides.css:1044 |
| .guest-nomination-cta p | assets/css/final-overrides.css:837, assets/css/final-overrides.css:843 |
| .header-cta | assets/css/final-overrides.css:1979, assets/css/site.css:114, assets/css/site.css:218, assets/css/site.css:235 |
| .header-cta .button-secondary | assets/css/final-overrides.css:1314, assets/css/final-overrides.css:1984, assets/css/site.css:115 |
| .header-inner | assets/css/final-overrides.css:1251, assets/css/final-overrides.css:1887, assets/css/final-overrides.css:1974, assets/css/site.css:105, assets/css/site.css:216, assets/css/site.css:234 |
| .hero | assets/css/final-overrides.css:10, assets/css/final-overrides.css:1330, assets/css/final-overrides.css:2013, assets/css/site.css:116 |
| .hero-actions | assets/css/final-overrides.css:179, assets/css/final-overrides.css:419, assets/css/final-overrides.css:448 |
| .hero-actions .action-pill | assets/css/final-overrides.css:187, assets/css/final-overrides.css:1480 |
| .hero-card | assets/css/final-overrides.css:1334, assets/css/final-overrides.css:1915, assets/css/site.css:117, assets/css/site.css:220 |
| .hero-content | assets/css/final-overrides.css:14, assets/css/final-overrides.css:1386, assets/css/final-overrides.css:1860, assets/css/final-overrides.css:1919, assets/css/final-overrides.css:2017, assets/css/site.css:123, assets/css/site.css:221 |
| .hero-copy .lede | assets/css/final-overrides.css:1393, assets/css/site.css:127 |
| .hero-panel | assets/css/final-overrides.css:1864, assets/css/site.css:128 |
| .hero-panel-balanced | assets/css/final-overrides.css:28, assets/css/final-overrides.css:200, assets/css/final-overrides.css:471, assets/css/final-overrides.css:1399, assets/css/final-overrides.css:1503 |
| .hero-panel-balanced .hero-meta | assets/css/final-overrides.css:230, assets/css/final-overrides.css:479 |
| .hero-panel-copy | assets/css/final-overrides.css:221, assets/css/final-overrides.css:437, assets/css/final-overrides.css:1415 |
| .hero-panel-cta | assets/css/final-overrides.css:251, assets/css/final-overrides.css:483 |
| .hero-panel-title | assets/css/final-overrides.css:210, assets/css/final-overrides.css:475, assets/css/final-overrides.css:1100, assets/css/final-overrides.css:1408 |
| .home-hero | assets/css/final-overrides.css:1362, assets/css/site.css:122 |
| .home-hero .hero-content | assets/css/final-overrides.css:169, assets/css/final-overrides.css:443 |
| .lede | assets/css/final-overrides.css:1124, assets/css/final-overrides.css:1969, assets/css/site.css:91 |
| .mini-card | assets/css/final-overrides.css:1548, assets/css/site.css:157 |
| .nav | assets/css/final-overrides.css:1279, assets/css/final-overrides.css:1898, assets/css/final-overrides.css:1993, assets/css/site.css:111, assets/css/site.css:219, assets/css/site.css:236 |
| .nav a | assets/css/final-overrides.css:1283, assets/css/final-overrides.css:2003, assets/css/site.css:112 |
| .nav a::after | assets/css/final-overrides.css:1289, assets/css/final-overrides.css:1903 |
| .platform-card | assets/css/final-overrides.css:1489, assets/css/final-overrides.css:1600, assets/css/site.css:171 |
| .platform-card span | assets/css/final-overrides.css:1605, assets/css/site.css:174 |
| .platform-row | assets/css/final-overrides.css:1596, assets/css/final-overrides.css:1872, assets/css/final-overrides.css:2053, assets/css/site.css:170 |
| .platform-section | assets/css/final-overrides.css:1591, assets/css/site.css:167 |
| .resource-links | assets/css/final-overrides.css:651, assets/css/final-overrides.css:663, assets/css/final-overrides.css:1030 |
| .section | assets/css/final-overrides.css:1320, assets/css/final-overrides.css:1947, assets/css/site.css:50, assets/css/site.css:226 |
| .section-tight | assets/css/final-overrides.css:5, assets/css/final-overrides.css:1325, assets/css/final-overrides.css:1952, assets/css/site.css:51 |
| .site-footer | assets/css/final-overrides.css:1632, assets/css/final-overrides.css:2062, assets/css/site.css:181 |
| .site-header | assets/css/final-overrides.css:1245, assets/css/site.css:104 |
| .student-grid | assets/css/final-overrides.css:1560, assets/css/site.css:153 |
| .student-note | assets/css/final-overrides.css:1581, assets/css/site.css:156 |
| .student-primary | assets/css/final-overrides.css:1565, assets/css/site.css:154, assets/css/site.css:209 |
| .student-section | assets/css/final-overrides.css:1553, assets/css/site.css:151 |
| .student-side | assets/css/final-overrides.css:1570, assets/css/final-overrides.css:1927, assets/css/final-overrides.css:2009, assets/css/site.css:155, assets/css/site.css:231 |
| .student-side article | assets/css/final-overrides.css:286, assets/css/final-overrides.css:1513, assets/css/final-overrides.css:1576, assets/css/final-overrides.css:1933 |
| .team-image img | assets/css/final-overrides.css:315, assets/css/final-overrides.css:1770 |
| .title-lg | assets/css/final-overrides.css:1109, assets/css/final-overrides.css:1856, assets/css/final-overrides.css:1911, assets/css/final-overrides.css:1961, assets/css/site.css:64, assets/css/site.css:228 |
| .title-md | assets/css/final-overrides.css:1114, assets/css/final-overrides.css:1965, assets/css/site.css:65 |
| .title-sm | assets/css/final-overrides.css:1119, assets/css/site.css:66 |
| .title-with-rule--wide::after | assets/css/site.css:78, assets/css/site.css:222, assets/css/site.css:238 |
| .title-with-rule::after | assets/css/final-overrides.css:1419, assets/css/site.css:68, assets/css/site.css:237 |
| .title-xl | assets/css/final-overrides.css:1104, assets/css/final-overrides.css:1852, assets/css/final-overrides.css:1907, assets/css/final-overrides.css:1957, assets/css/site.css:63, assets/css/site.css:227 |
| .watch-listen-grid | assets/css/final-overrides.css:993, assets/css/final-overrides.css:1012 |
| :root | assets/css/final-overrides.css:514, assets/css/site.css:1 |
| @media (max-width: 1180px) | assets/css/final-overrides.css:431, assets/css/final-overrides.css:999, assets/css/final-overrides.css:1851 |
| @media (max-width: 680px) | assets/css/final-overrides.css:453, assets/css/final-overrides.css:1022, assets/css/final-overrides.css:1938 |
| @media (max-width: 920px) | assets/css/final-overrides.css:442, assets/css/final-overrides.css:1886 |
| body | assets/css/final-overrides.css:1, assets/css/final-overrides.css:1053, assets/css/final-overrides.css:1939, assets/css/site.css:26, assets/css/site.css:225 |
| html | assets/css/final-overrides.css:1049, assets/css/site.css:25 |

### Potential Contradictions
Found 154 selector/property pairs with multiple declared values. These are not all bugs; some are responsive or cascade overrides, but they deserve review.
| Selector | Property | Sample declarations |
| --- | --- | --- |
| body | background | assets/css/final-overrides.css:2=#f8fbfe !important; assets/css/final-overrides.css:1054=; assets/css/site.css:30=linear-gradient(180deg,#ffffff,#fbfdff 42%,#f8fbfe 100%) |
| body | color | assets/css/final-overrides.css:1056=var(--ink); assets/css/site.css:29=var(--text) |
| body | padding-bottom | assets/css/final-overrides.css:1940=154px; assets/css/site.css:34=calc(var(--audio-height) + 18px); assets/css/site.css:225=124px |
| .section-tight | padding-top | assets/css/final-overrides.css:6=72px !important; assets/css/final-overrides.css:1326=76px !important; assets/css/final-overrides.css:1953=62px !important; assets/css/site.css:51=var(--space-20) |
| .section-tight | padding-bottom | assets/css/final-overrides.css:7=72px !important; assets/css/final-overrides.css:1327=76px !important; assets/css/final-overrides.css:1954=62px !important; assets/css/site.css:51=var(--space-20) |
| .hero | padding | assets/css/final-overrides.css:11=32px 0 12px !important; assets/css/final-overrides.css:1331=28px 0 20px !important; assets/css/site.css:116=40px 0 8px |
| .hero-content | align-items | assets/css/final-overrides.css:15=center !important; assets/css/site.css:123=end |
| .hero-content | gap | assets/css/final-overrides.css:1389=42px; assets/css/site.css:123=32px |
| .hero-content | padding | assets/css/final-overrides.css:1390=70px clamp(28px,4vw,56px) 60px !important; assets/css/final-overrides.css:1920=52px 26px 40px !important; assets/css/final-overrides.css:2018=42px 20px 28px !important; assets/css/site.css:123=64px clamp(24px,4vw,48px) 48px; assets/css/site.css:221=48px 24px 32px |
| .hero-content | grid-template-columns | assets/css/final-overrides.css:1861=1fr; assets/css/site.css:123=minmax(0,1.08fr) minmax(300px,390px) |
| .detail-card-visual | margin | assets/css/final-overrides.css:22=0 var(--space-4); assets/css/final-overrides.css:434=0 var(--space-2); assets/css/final-overrides.css:456=0 |
| .hero-panel-balanced | padding | assets/css/final-overrides.css:29=32px !important; assets/css/final-overrides.css:472=24px !important; assets/css/final-overrides.css:1504=34px !important |
| .hero-panel-balanced | background | assets/css/final-overrides.css:205=linear-gradient(180deg, rgba(11,23,36,0.44), rgba(11,23,36,0.28)); assets/css/final-overrides.css:1401=linear-gradient(180deg, rgba(8,22,35,.54), rgba(8,22,35,.32)) !important |
| .hero-panel-balanced | box-shadow | assets/css/final-overrides.css:207=inset 0 1px 0 rgba(255,255,255,0.08), 0 18px 38px rgba(6,20,33,0.18); assets/css/final-overrides.css:1403=inset 0 1px 0 rgba(255,255,255,.08), 0 22px 48px rgba(6,20,33,.2) |
| .audio-links | display | assets/css/final-overrides.css:61=flex; assets/css/final-overrides.css:2100=grid; assets/css/site.css:204=flex |
| .audio-links | gap | assets/css/final-overrides.css:64=12px; assets/css/final-overrides.css:463=10px; assets/css/final-overrides.css:2102=6px; assets/css/site.css:204=8px |
| .button-row | flex-wrap | assets/css/final-overrides.css:416=nowrap; assets/css/site.css:93=wrap |
| .audio-link | min-height | assets/css/final-overrides.css:77=52px !important; assets/css/final-overrides.css:1845=38px !important; assets/css/final-overrides.css:2106=34px !important; assets/css/site.css:205=40px |
| .audio-link | padding | assets/css/final-overrides.css:78=0 22px !important; assets/css/final-overrides.css:1846=0 13px !important; assets/css/final-overrides.css:2107=0 8px !important; assets/css/site.css:205=0 14px |
| .audio-link | background | assets/css/final-overrides.css:1847=rgba(255,255,255,.9); assets/css/site.css:205=#fff |
| .audio-link | font-size | assets/css/final-overrides.css:1848=.78rem; assets/css/final-overrides.css:2108=.72rem; assets/css/site.css:205=.84rem |
| .action-pill | min-height | assets/css/final-overrides.css:90=52px !important; assets/css/final-overrides.css:1432=48px !important |
| .action-pill | border | assets/css/final-overrides.css:93=1px solid rgba(15,42,68,0.14); assets/css/final-overrides.css:1455=1px solid rgba(15,42,68,.16) |
| .action-pill | background | assets/css/final-overrides.css:94=rgba(255,255,255,0.92); assets/css/final-overrides.css:1456=rgba(255,255,255,.94) |
| .action-pill | font-size | assets/css/final-overrides.css:96=0.9rem; assets/css/final-overrides.css:1434=.86rem |
| .action-pill | font-weight | assets/css/final-overrides.css:97=700; assets/css/final-overrides.css:1435=800 |
| .action-pill:hover | transform | assets/css/final-overrides.css:112=translateY(-2px); assets/css/final-overrides.css:1467=translateY(-1px) |
| .action-pill--primary | box-shadow | assets/css/final-overrides.css:120=0 12px 28px rgba(15,42,68,0.16); assets/css/final-overrides.css:1450=0 14px 30px rgba(15,42,68,.16) |
| .hero-actions | grid-template-columns | assets/css/final-overrides.css:181=1fr; assets/css/final-overrides.css:420=repeat(2, minmax(248px, 1fr)) |
| .hero-actions | max-width | assets/css/final-overrides.css:184=620px; assets/css/final-overrides.css:421=560px; assets/css/final-overrides.css:449=none |
| .hero-actions .action-pill | background | assets/css/final-overrides.css:189=rgba(255,255,255,0.08); assets/css/final-overrides.css:1481=rgba(255,255,255,.1) |
| .hero-actions .action-pill | border-color | assets/css/final-overrides.css:190=rgba(244,247,250,0.24); assets/css/final-overrides.css:1482=rgba(244,247,250,.22) |
| .hero-panel-title | font-family | assets/css/final-overrides.css:212="Inter", system-ui, sans-serif; assets/css/final-overrides.css:1409="Sora", "Inter", sans-serif |
| .hero-panel-title | font-size | assets/css/final-overrides.css:213=0.9rem; assets/css/final-overrides.css:1410=.98rem |
| .hero-panel-title | letter-spacing | assets/css/final-overrides.css:215=0.14em; assets/css/final-overrides.css:1101=0 !important |
| .hero-panel-title | line-height | assets/css/final-overrides.css:216=1.2; assets/css/final-overrides.css:1411=1.22 |
| .hero-panel-copy | max-width | assets/css/final-overrides.css:223=34ch; assets/css/final-overrides.css:438=none |
| .hero-panel-copy | color | assets/css/final-overrides.css:224=rgba(244,247,250,0.86); assets/css/final-overrides.css:1416=rgba(244,247,250,.84) |
| .hero-panel-cta | margin-top | assets/css/final-overrides.css:252=30px; assets/css/final-overrides.css:484=22px |
| .hero-panel-cta | min-width | assets/css/final-overrides.css:254=236px; assets/css/final-overrides.css:485=0 |
| .about-image | aspect-ratio | assets/css/final-overrides.css:325=3 / 2 !important; assets/css/site.css:140=4/3.8 |
| .card-surface .episode-actions .action-pill | min-height | assets/css/final-overrides.css:350=46px !important; assets/css/final-overrides.css:497=44px !important |
| .card-surface .episode-actions .action-pill | padding | assets/css/final-overrides.css:351=0 12px !important; assets/css/final-overrides.css:498=0 11px !important |
| .card-surface .episode-actions .action-pill | gap | assets/css/final-overrides.css:360=8px; assets/css/final-overrides.css:500=7px |
| .card-surface .episode-actions .action-pill | font-size | assets/css/final-overrides.css:362=0.82rem; assets/css/final-overrides.css:499=0.8rem |
| .card-surface .episode-actions .platform-icon-img | width | assets/css/final-overrides.css:394=18px; assets/css/final-overrides.css:506=17px |
| .card-surface .episode-actions .platform-icon-img | height | assets/css/final-overrides.css:395=18px; assets/css/final-overrides.css:507=17px |
| .card-surface .episode-actions .platform-icon-img | min-width | assets/css/final-overrides.css:396=18px; assets/css/final-overrides.css:508=17px |
| .resource-links | padding | assets/css/final-overrides.css:664=24px; assets/css/final-overrides.css:1031=20px |
| .guest-nomination-cta | background | assets/css/final-overrides.css:794=linear-gradient(135deg,#102b45 0%,#173a59 100%); assets/css/final-overrides.css:805=#ffffff |
| .guest-nomination-cta | color | assets/css/final-overrides.css:795=var(--cloud-white); assets/css/final-overrides.css:806=var(--civic-navy) |
| .guest-nomination-cta | padding | assets/css/final-overrides.css:796=44px clamp(24px,4vw,48px); assets/css/final-overrides.css:1045=30px 22px |
| .guest-nomination-cta | grid-template-columns | assets/css/final-overrides.css:798=minmax(0,1fr) auto; assets/css/final-overrides.css:1005=1fr |
| .guest-nomination-cta p | color | assets/css/final-overrides.css:840=rgba(244,247,250,.82); assets/css/final-overrides.css:844=var(--muted) |
| .archive-toolbar | grid-template-columns | assets/css/final-overrides.css:849=minmax(220px,360px) 1fr; assets/css/final-overrides.css:1040=1fr |
| .form-embed textarea | min-height | assets/css/final-overrides.css:921=46px; assets/css/final-overrides.css:931=126px |
| .watch-listen-grid | grid-template-columns | assets/css/final-overrides.css:995=repeat(5,minmax(0,1fr)); assets/css/final-overrides.css:1013=repeat(2,minmax(0,1fr)) |
| .title-xl | font-size | assets/css/final-overrides.css:1105=4.55rem !important; assets/css/final-overrides.css:1853=3.7rem !important; assets/css/final-overrides.css:1908=3rem !important; assets/css/final-overrides.css:1958=2.3rem !important; assets/css/site.css:63=clamp(2.45rem,5vw,4.85rem); assets/css/site.css:227=clamp(2.1rem,10vw,3rem) |
| .title-lg | font-size | assets/css/final-overrides.css:1110=2.75rem !important; assets/css/final-overrides.css:1857=2.35rem !important; assets/css/final-overrides.css:1912=2.05rem !important; assets/css/final-overrides.css:1962=1.72rem !important; assets/css/site.css:64=clamp(1.9rem,3.6vw,3rem); assets/css/site.css:228=clamp(1.65rem,7vw,2.2rem) |
| .title-md | font-size | assets/css/final-overrides.css:1115=1.72rem !important; assets/css/final-overrides.css:1966=1.42rem !important; assets/css/site.css:65=clamp(1.4rem,2.2vw,1.9rem) |
| .title-sm | font-size | assets/css/final-overrides.css:1120=1rem !important; assets/css/site.css:66=1.06rem |
| .lede | max-width | assets/css/final-overrides.css:1125=720px; assets/css/site.css:91=760px |
| .lede | color | assets/css/final-overrides.css:1126=var(--muted); assets/css/site.css:91=var(--text-soft) |
| .lede | font-size | assets/css/final-overrides.css:1127=1.08rem !important; assets/css/final-overrides.css:1970=1rem !important; assets/css/site.css:91=clamp(1.02rem,1.25vw,1.16rem) |
| .lede | line-height | assets/css/final-overrides.css:1128=1.72; assets/css/final-overrides.css:1971=1.64 |
| .body-copy p | color | assets/css/final-overrides.css:1136=inherit; assets/css/site.css:92=var(--text-soft) |
| .body-copy p | font-size | assets/css/final-overrides.css:1137=1rem; assets/css/site.css:92=1.02rem |
| .site-header | background | assets/css/final-overrides.css:1246=rgba(251,253,255,.88) !important; assets/css/site.css:104=rgba(244,247,250,.92) |
| .site-header | border-bottom | assets/css/final-overrides.css:1247=1px solid rgba(15,42,68,.075) !important; assets/css/site.css:104=1px solid rgba(15,42,68,.08) |
| .header-inner | gap | assets/css/final-overrides.css:1252=22px; assets/css/site.css:105=20px |
| .header-inner | min-height | assets/css/final-overrides.css:1253=76px; assets/css/site.css:105=var(--header-height) |
| .header-inner | align-items | assets/css/final-overrides.css:1888=start; assets/css/site.css:105=center |
| .header-inner | grid-template-columns | assets/css/final-overrides.css:1975=1fr; assets/css/site.css:105=auto 1fr auto; assets/css/site.css:216=auto auto; assets/css/site.css:234=1fr |
| .header-inner | grid-template-areas | assets/css/final-overrides.css:1976="brand" "nav" "cta"; assets/css/site.css:216="brand cta" "nav nav"; assets/css/site.css:234="brand" "nav" "cta" |
| .brand | gap | assets/css/final-overrides.css:1257=12px; assets/css/site.css:106=14px |
| .brand-mark | width | assets/css/final-overrides.css:1261=36px; assets/css/final-overrides.css:1989=34px; assets/css/site.css:107=40px |
| .brand-mark | height | assets/css/final-overrides.css:1262=36px; assets/css/final-overrides.css:1990=34px; assets/css/site.css:107=40px |
| .brand-name | font-size | assets/css/final-overrides.css:1266=.98rem; assets/css/site.css:109=1rem |
| .brand-name | line-height | assets/css/final-overrides.css:1267=1.08; assets/css/site.css:109=1.02 |
| .audio-label | font-weight | assets/css/final-overrides.css:1276=800; assets/css/site.css:196=700 |
| .nav | gap | assets/css/final-overrides.css:1280=24px; assets/css/final-overrides.css:1899=14px 18px; assets/css/final-overrides.css:1997=10px 8px; assets/css/site.css:111=28px; assets/css/site.css:219=20px 22px; assets/css/site.css:236=14px 18px |
| .nav | padding-top | assets/css/final-overrides.css:1900=6px; assets/css/final-overrides.css:1999=4px; assets/css/site.css:219=8px |
| .nav | display | assets/css/final-overrides.css:1994=grid; assets/css/site.css:111=flex |
| .nav | justify-content | assets/css/site.css:111=flex-end; assets/css/site.css:219=flex-start |
| .nav a | font-size | assets/css/final-overrides.css:1285=.76rem; assets/css/final-overrides.css:2005=.72rem; assets/css/site.css:112=.78rem |
| .nav a | color | assets/css/final-overrides.css:1286=rgba(16,40,63,.82); assets/css/site.css:112=var(--text) |
| .nav a::after | bottom | assets/css/final-overrides.css:1294=-13px; assets/css/final-overrides.css:1904=-7px |
| .header-cta .button-secondary | min-height | assets/css/final-overrides.css:1315=42px !important; assets/css/site.css:115=44px |
| .header-cta .button-secondary | padding | assets/css/final-overrides.css:1316=0 17px !important; assets/css/site.css:115=0 18px |
| .header-cta .button-secondary | font-size | assets/css/final-overrides.css:1317=.78rem; assets/css/site.css:115=.84rem |
| .section | padding-top | assets/css/final-overrides.css:1321=96px !important; assets/css/final-overrides.css:1948=72px !important |
| .section | padding-bottom | assets/css/final-overrides.css:1322=96px !important; assets/css/final-overrides.css:1949=72px !important |
| .section | padding | assets/css/site.css:50=var(--space-24) 0; assets/css/site.css:226=80px 0 |
| .hero-card | min-height | assets/css/final-overrides.css:1335=min(82vh, 760px); assets/css/final-overrides.css:1916=auto; assets/css/site.css:118=min(84vh,780px); assets/css/site.css:220=680px |
| .hero-card | border-radius | assets/css/final-overrides.css:1336=var(--radius-hero) !important; assets/css/site.css:118=30px |
| .hero-card | box-shadow | assets/css/final-overrides.css:1337=0 30px 72px rgba(15,42,68,.16); assets/css/site.css:120=var(--shadow-lg) |
| .home-hero | background | assets/css/final-overrides.css:1363=; assets/css/site.css:122=linear-gradient(110deg, rgba(6,20,33,.84), rgba(15,42,68,.58) 38%, rgba(15,42,68,.22) 70%, rgba(15,42,68,.14)), url('../images/featured-episode-8.jpg') center center / cover no-repeat |
| .hero-copy .lede | color | assets/css/final-overrides.css:1395=rgba(244,247,250,.86); assets/css/site.css:127=rgba(244,247,250,.85) |
| .title-with-rule::after | height | assets/css/final-overrides.css:1420=3px; assets/css/site.css:72=4px |
| .title-with-rule::after | border-radius | assets/css/final-overrides.css:1421=0; assets/css/site.css:74=999px |
| .title-with-rule::after | background | assets/css/final-overrides.css:1422=var(--ice-blue); assets/css/site.css:75=linear-gradient(90deg, var(--ice-blue) 0%, rgba(95,168,211,.92) 72%, rgba(95,168,211,0) 100%) |
| .title-with-rule::after | box-shadow | assets/css/final-overrides.css:1423=none; assets/css/site.css:76=0 0 0 1px rgba(95,168,211,.12), 0 10px 22px rgba(95,168,211,.16) |
| .title-with-rule::after | width | assets/css/site.css:71=min(168px,42vw); assets/css/site.css:237=min(120px,42vw) |
| .title-with-rule::after | margin-top | assets/css/site.css:73=18px; assets/css/site.css:237=14px |
| .button | color | assets/css/final-overrides.css:1441=#071b2d; assets/css/site.css:100=var(--civic-navy) |
| .button | box-shadow | assets/css/final-overrides.css:1442=0 12px 24px rgba(95,168,211,.2); assets/css/site.css:100=0 12px 28px rgba(95,168,211,.24) |
| .platform-card | border-radius | assets/css/final-overrides.css:1490=var(--radius-card) !important; assets/css/site.css:171=20px |
| .platform-card | border | assets/css/final-overrides.css:1491=1px solid rgba(15,42,68,.105) !important; assets/css/site.css:171=1px solid rgba(255,255,255,.12) |
| .platform-card | box-shadow | assets/css/final-overrides.css:1492=0 18px 38px rgba(15,42,68,.065) !important; assets/css/final-overrides.css:1602=none !important |
| .platform-card | background | assets/css/final-overrides.css:1601=rgba(255,255,255,.065); assets/css/site.css:171=rgba(255,255,255,.07) |
| .guest-card | background | assets/css/final-overrides.css:1531=rgba(255,255,255,.96); assets/css/site.css:161=#fff |
| .guest-card-image | aspect-ratio | assets/css/final-overrides.css:1536=16 / 10; assets/css/site.css:163=4/3 |
| .guest-card-copy | padding | assets/css/final-overrides.css:1540=22px; assets/css/site.css:164=20px |
| .mini-card | background | assets/css/final-overrides.css:1549=rgba(255,255,255,.92); assets/css/site.css:157=#fff |
| .mini-card | padding | assets/css/final-overrides.css:1550=22px; assets/css/site.css:157=20px |
| .student-section | background | assets/css/final-overrides.css:1554=; assets/css/site.css:151=linear-gradient(180deg,#f7fbff,#ffffff) |
| .student-grid | gap | assets/css/final-overrides.css:1561=20px; assets/css/site.css:153=24px |
| .student-grid | align-items | assets/css/final-overrides.css:1562=start; assets/css/site.css:153=stretch |
| .student-primary | min-height | assets/css/final-overrides.css:1566=0 !important; assets/css/site.css:154=560px; assets/css/site.css:209=460px |
| .student-side | grid-template-rows | assets/css/final-overrides.css:1571=none; assets/css/final-overrides.css:1929=none; assets/css/site.css:155=1fr 1fr; assets/css/site.css:231=none |
| .student-side | grid-template-columns | assets/css/final-overrides.css:1928=repeat(2, minmax(0, 1fr)); assets/css/final-overrides.css:2010=1fr |
| .student-note | margin-top | assets/css/final-overrides.css:1582=26px; assets/css/site.css:156=24px |
| .platform-section | background | assets/css/final-overrides.css:1592=; assets/css/site.css:167=var(--civic-navy) |
| .platform-row | grid-template-columns | assets/css/final-overrides.css:1597=repeat(5,minmax(0,1fr)); assets/css/final-overrides.css:1873=repeat(2,minmax(0,1fr)); assets/css/final-overrides.css:2054=1fr; assets/css/site.css:170=repeat(4,minmax(0,1fr)) |
| .platform-card span | color | assets/css/final-overrides.css:1606=rgba(244,247,250,.76); assets/css/site.css:174=rgba(244,247,250,.72) |
| .cta-band | border-radius | assets/css/final-overrides.css:1610=var(--radius-panel); assets/css/site.css:176=28px |
| .cta-band | background | assets/css/final-overrides.css:1611=linear-gradient(135deg, #102b45 0%, #173a59 100%); assets/css/site.css:176=linear-gradient(135deg,#112f4a,#183b5b) |
| .cta-band | box-shadow | assets/css/final-overrides.css:1612=0 24px 48px rgba(15,42,68,.14); assets/css/site.css:177=0 24px 50px rgba(15,42,68,.14) |
| .site-footer | margin-top | assets/css/final-overrides.css:1633=72px; assets/css/site.css:181=96px |
| .site-footer | background | assets/css/final-overrides.css:1634=#0b2137; assets/css/site.css:181=#0c2238 |
| .episode-archive-grid | grid-template-columns | assets/css/final-overrides.css:1653=repeat(3, minmax(0, 1fr)); assets/css/final-overrides.css:1869=repeat(2, minmax(0, 1fr)); assets/css/final-overrides.css:2049=1fr |
| .episode-archive-grid | gap | assets/css/final-overrides.css:1654=22px; assets/css/final-overrides.css:2050=18px |
| .episode-archive-card p | min-height | assets/css/final-overrides.css:1680=5.2em; assets/css/final-overrides.css:2059=auto |
| .audio-player | width | assets/css/final-overrides.css:1794=min(calc(100% - 24px), 1160px); assets/css/final-overrides.css:2068=min(calc(100% - 16px), 420px); assets/css/site.css:189=min(calc(100% - 20px),1120px) |
| .audio-player | border-radius | assets/css/final-overrides.css:1795=var(--radius-panel); assets/css/site.css:190=22px |
| .audio-player | background | assets/css/final-overrides.css:1796=rgba(251,253,255,.94); assets/css/site.css:189=rgba(244,247,250,.96) |
| .audio-player | box-shadow | assets/css/final-overrides.css:1798=0 18px 46px rgba(15,42,68,.17); assets/css/site.css:190=0 18px 40px rgba(15,42,68,.16) |
| .audio-player | padding | assets/css/final-overrides.css:1799=12px; assets/css/final-overrides.css:2069=10px; assets/css/site.css:190=14px |
| .audio-player | bottom | assets/css/final-overrides.css:2067=10px; assets/css/site.css:188=12px |
| .audio-player | position | assets/css/site.css:42=relative; assets/css/site.css:188=fixed |
| .audio-player | z-index | assets/css/site.css:43=1; assets/css/site.css:188=1400 |
| .audio-grid | grid-template-columns | assets/css/final-overrides.css:1803=auto minmax(190px, 300px) minmax(180px, 1fr) auto; assets/css/final-overrides.css:1877=auto minmax(0, 1fr); assets/css/final-overrides.css:2073=auto minmax(0, 1fr); assets/css/site.css:192=auto minmax(0,280px) 1fr auto; assets/css/site.css:212=auto minmax(0,1fr); assets/css/site.css:232=1fr |
| .audio-grid | gap | assets/css/final-overrides.css:1804=14px; assets/css/final-overrides.css:2074=10px 12px; assets/css/site.css:192=16px |
| .audio-control | min-width | assets/css/final-overrides.css:1808=50px; assets/css/final-overrides.css:2078=44px; assets/css/site.css:193=52px |
| .audio-control | min-height | assets/css/final-overrides.css:1809=50px; assets/css/final-overrides.css:2079=44px; assets/css/site.css:193=52px |
| .audio-progress-wrap | gap | assets/css/final-overrides.css:1814=9px; assets/css/site.css:201=8px |
| .audio-range | background | assets/css/final-overrides.css:1822=linear-gradient(90deg, var(--ice-blue) var(--progress), rgba(15,42,68,.13) var(--progress)); assets/css/site.css:202=transparent |
| .footer-grid | gap | assets/css/final-overrides.css:1924=34px; assets/css/site.css:182=28px |
| .container | width | assets/css/final-overrides.css:1944=min(100% - 28px, var(--section-width)); assets/css/site.css:49=min(100% - 32px, var(--section-width)) |
| .header-cta | justify-self | assets/css/final-overrides.css:1980=stretch; assets/css/site.css:218=end; assets/css/site.css:235=start |
| .header-cta | margin-left | assets/css/site.css:114=8px; assets/css/site.css:235=0 |
| .audio-title | font-size | assets/css/final-overrides.css:2091=.84rem; assets/css/site.css:198=.94rem |
| .title-with-rule--wide::after | width | assets/css/site.css:78=min(320px,58vw); assets/css/site.css:222=min(220px,56vw); assets/css/site.css:238=min(168px,52vw) |
| .guest-grid | grid-template-columns | assets/css/site.css:160=repeat(4,minmax(0,1fr)); assets/css/site.css:210=repeat(2,minmax(0,1fr)) |

### CSS Custom Properties
- Custom properties defined: 51
- Custom properties referenced: 29
- Defined but never referenced: 23
| Variable | Defined at |
| --- | --- |
| --electric-coral | assets/css/site.css:7 |
| --focus | assets/css/final-overrides.css:521 |
| --light | assets/css/site.css:79 |
| --line-strong | assets/css/site.css:11 |
| --primary | assets/css/final-overrides.css:387 |
| --radius-2xl | assets/css/site.css:19 |
| --radius-lg | assets/css/site.css:19 |
| --radius-md | assets/css/site.css:19 |
| --radius-sm | assets/css/site.css:19 |
| --space-1 | assets/css/site.css:15 |
| --space-10 | assets/css/site.css:16 |
| --space-12 | assets/css/site.css:16 |
| --space-14 | assets/css/site.css:16 |
| --space-16 | assets/css/site.css:16 |
| --space-18 | assets/css/site.css:17 |
| --space-5 | assets/css/site.css:15 |
| --space-6 | assets/css/site.css:15 |
| --space-7 | assets/css/site.css:16 |
| --space-8 | assets/css/site.css:16 |
| --surface | assets/css/final-overrides.css:515 |
| --surface-soft | assets/css/final-overrides.css:516 |
| --surface-tint | assets/css/final-overrides.css:517 |
| --wide | assets/css/site.css:78, assets/css/site.css:222, assets/css/site.css:238 |
- Referenced but never defined: 1
| Variable | Referenced at |
| --- | --- |
| --hero-image | assets/css/site.css:119 |

## 9. Recommended Punch List (Priority Order)
1. Normalize page background and light-surface tints to Cloud White instead of near-whites such as `#f8fbfe`, `#fbfdff`, `#f7fbfe`, and `#f3f8fc`. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: M.
2. Replace near-navy darks such as `#10283f`, `#102b45`, `#173a59`, `#0c2238`, and `#0b2137` with Civic Navy. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: M.
3. Decide whether embedded platform SVG colors (`#FF1200`, `#1ED760`, purple podcast gradient) are approved exceptions; otherwise recolor to Azure/Civic Navy. File path: `assets/css/final-overrides.css`. Complexity: S.
4. Remove or retokenize legacy variables `--electric-coral`, `--text`, `--text-soft`, `--surface`, `--surface-soft`, `--surface-tint`, `--ink`, `--muted`, and `--focus`. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: M.
5. Change episode detail H1 text from ALL CAPS to natural title case while preserving visual strength through CSS if needed. File path: `episodes/*/index.html`. Complexity: M.
6. Normalize the homepage hero tagline to the locked casing or move all-caps styling into CSS if the visual treatment should remain uppercase. File path: `index.html`. Complexity: S.
7. Add the locked tagline to the footer brand block so it appears globally. File path: `all HTML footers or shared generator/template`. Complexity: M.
8. Add the locked tagline to brand metadata in `assets/data/site-config.json`. File path: `assets/data/site-config.json`. Complexity: S.
9. Reduce Inter UI weights from 700/800 to 600 where used for nav, badges, guest-role labels, and button-like UI. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: M.
10. Trim Google Fonts loads to allowed weights only: Inter 400/500/600 and Sora 600/700/800. File path: `all HTML font links`. Complexity: M.
11. Replace pure white card fills (`#fff`, `#ffffff`, `rgba(255,255,255,...)`) with Cloud White unless the white is intentionally a transparency overlay. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: M.
12. Retokenize focus outline `rgba(27,111,159,.45)` to Azure-based focus styling. File path: `assets/css/final-overrides.css`. Complexity: S.
13. Review duplicate selector blocks and keep the later intentional override or consolidate repeated declarations. File path: `assets/css/final-overrides.css`. Complexity: M.
14. Review `!important` usage and remove cases that only compensate for duplicate cascade ordering. File path: `assets/css/final-overrides.css`. Complexity: M.
15. Document allowed exceptions for YouTube/Spotify/Apple brand icons if external platform colors are retained. File path: `brand guidelines and assets/css/final-overrides.css`. Complexity: S.
16. Replace off-brand placeholder media backgrounds `#e7eef5`, `#e8eff5`, and `#ebf2f8` with Cloud White or Slate-tinted brand-approved treatment. File path: `assets/css/site.css; assets/css/final-overrides.css`. Complexity: S.
17. Audit meta descriptions after tagline placement so social snippets stay civic-minded and avoid generic platform language. File path: `all HTML `<meta name="description">` and `og:description``. Complexity: M.
18. Separate design all-caps section labels from publishing titles by applying all-caps in CSS only for design headings, not hardcoded episode/article title text. File path: `episode detail pages and CSS heading utilities`. Complexity: M.

---
Generated by read-only audit scanner. No source files were modified by this audit besides this report file.


## 10. Decorative Brand Elements

### 10.1 Azure Thin-Line Treatment (decorative rule)

A thin Azure horizontal line appears beneath select headings and eyebrow text across the site. It is a signature element of the VOICES of OKC brand. Used correctly, it anchors visual weight on the most important word or phrase in each heading.

#### Specification

| Property | Value |
| --- | --- |
| Color | Azure `#5FA8D3` |
| Thickness | 3px (exact — never 2px, never 4px) |
| Width | Matches the underlined word or phrase exactly — not shorter, not longer |
| Vertical padding | `--space-2` (8px) between the baseline of the underlined text and the top of the line |
| Border-radius | 0 (square ends) |
| Box-shadow | None |

#### Placement rule (deterministic)

The line sits under the **last meaningful word or phrase before the period** in a heading or eyebrow. "Meaningful" means a noun or noun phrase that names what the heading is about — never under verbs, articles, or filler.

**Single concept word — line spans just that word:**
- "A growing archive of city-shaping <u>conversations</u>."
- "Built for real <u>growth</u>."
- "A civic platform, not just a podcast <u>feed</u>."

**Proper-noun units (1-2 words) — line spans the unit:**
- "Stories that help us see <u>Oklahoma City</u> more clearly."
- "A podcast rooted in <u>Oklahoma City</u>."
- "The beginning of a real <u>Oklahoma City</u> archive."

**Call-to-action phrases (1-2 words) — line spans the action phrase:**
- "Wherever you are, <u>start here</u>."

#### Eyebrow text

The same rule applies to eyebrows. For short eyebrows where the whole phrase is the focus, the line spans the last 1-2 meaningful words.

Examples:
- "STUDENT-PRODUCED · OKLAHOMA <u>CITY</u>"
- "FEATURED <u>CONVERSATION</u>"
- "WHY THIS <u>MATTERS</u>"

#### Where the treatment is used

- Hero `<h1>` headings
- Section `<h2>` headings (anywhere the `title-with-rule` class is applied)
- Eyebrow text (the `<span class="eyebrow">` element)

#### Where the treatment is NEVER used

- Body paragraphs
- Image captions or `.guest-role` labels
- Navigation links
- Button text
- Episode titles in the `.episode-card-title` style (those have their own visual hierarchy)

#### Current implementation status (as of this brand-guide update)

The current code has the line treatment partially implemented but with drift from this specification:

1. **Token name mismatch:** The CSS currently references `var(--ice-blue)` for the line color. Per brand spec, this should be `var(--azure)` (or whatever the canonical Azure token name is). Both names appear to map to the same color value (`#5FA8D3`) but the naming inconsistency is a maintenance hazard. Future cleanup should standardize on one name.

2. **Thickness drift:** `assets/css/site.css` declares the line `height: 4px`. `assets/css/final-overrides.css` overrides it to `3px`. Per spec, `3px` is correct. The base rule in `site.css` should be updated to `3px` and the override removed.

3. **Width is currently fixed by viewport, not by content:** Current CSS uses `width: min(168px, 42vw)` (and variants for `--wide`) — i.e., the line is sized relative to viewport width, not the width of the word it should sit under. Per the new spec, width must match the underlined word/phrase exactly. This requires either:
   - Wrapping the target word/phrase in a `<span class="rule-target">` and styling the line as a `border-bottom` on that span (preferred)
   - Or using inline styles per heading to manually set the line width (rejected — too fragile)

4. **Style variants:** The codebase has `title-with-rule`, `title-with-rule--wide`, and `title-with-rule--light` variants. Per the new spec, the `--wide` variant should be deprecated (no full-headline-width treatment). The `--light` variant (which adjusts color for dark backgrounds) can remain but should also follow the 3px thickness and target-word-width rules.

These drifts should be resolved in a focused implementation pass (separate from this brand-guide update).


### 10.2 Azure as a Decorative-Only Color

Per the brand standards in `system.md`, Azure `#5FA8D3` is the brand's accent color. However, due to WCAG AA contrast requirements, **Azure must never be used as a body or label text color on a light background** (Cloud White or White).

#### Why

Azure on Cloud White has a contrast ratio of approximately **2.7:1**, which fails WCAG AA's 4.5:1 minimum for normal-sized text. Lighthouse and other accessibility audits will flag Azure text as inaccessible.

#### Where Azure IS allowed

- **Decorative rules** (the thin Azure line treatment documented in §10.1)
- **Hover state transitions** (e.g., a link briefly turning Azure on hover is fine — momentary, not body text)
- **Icons and small accent graphics** where there is sufficient visual context (the color is contextual, not the primary information carrier)
- **Background fills behind dark text** (Azure as a section background with Civic Navy or white text on top)
- **Audio waveform / range slider accent colors** (UI controls, not text)
- **Text on a DARK background** (Azure on Civic Navy is approximately 5.2:1 — passes WCAG AA)
  - Example: the eyebrow on the `#platforms` section (Civic Navy background) may remain Azure

#### Where Azure is NOT allowed

- Body paragraphs
- Eyebrows on light backgrounds (use Civic Navy `#0F2A44` instead)
- Episode kickers on light backgrounds (use Slate `#3E4C59`)
- Guest-role meta lines on light backgrounds (use Slate)
- CTA labels on light backgrounds (use Civic Navy)
- Any small text where contrast against the background falls below 4.5:1

#### Color substitution mapping (for reference)

| Context | Use |
|---|---|
| Prominent label (eyebrow, audio-label) | Civic Navy `#0F2A44` |
| Card kicker / guest-role / meta | Slate `#3E4C59` |
| CTA text in a card | Civic Navy `#0F2A44` |

This rule was applied to the codebase in audit fix batch E (commit history will identify it). Future stylesheets and components should follow this rule from the start.


### 10.3 Implementation status (post-G3)

The Azure line spec is implemented site-wide via the `.rule-target` span technique, with two documented exclusions.

#### Implementation pattern

A target word or phrase in each `title-with-rule` heading is wrapped in:
```html
<span class="rule-target">word or phrase</span>
```

CSS in `final-overrides.css` draws the line as a `border-bottom: 3px solid var(--azure)` with `padding-bottom: var(--space-2)` on the span. When a `.rule-target` is present inside a `.title-with-rule`, the old `::after` pseudo-element is suppressed via `:has()` selector.

This produces the spec-correct content-width line behavior automatically as long as authors wrap a target span.

#### Exclusions (known tech debt)

1. **Episode pages** (`episodes/*/index.html`, 12 files): The H1 on each episode page is auto-generated by the Podbean pipeline. Adding `<span class="rule-target">` manually would be overwritten on the next pipeline run. These pages currently use the default `::after` treatment with the viewport-relative width. Two future paths: (a) update the pipeline to auto-wrap a target word in generated titles, or (b) accept the slight inconsistency as a low-priority issue.

2. **Home page featured episode H2** (`index.html` `#featuredEpisodeTitle`): Content is dynamically overwritten at runtime by `assets/js/player.js`. Any `.rule-target` span would be lost on title update. This heading retains the default `::after` treatment.

#### Deprecation: `title-with-rule--wide`

The `--wide` variant has been removed from all HTML on non-episode pages. The CSS still defines the class to avoid breakage but treats it as a no-op (width: auto). The variant can be fully deleted from CSS in a future cleanup pass once we confirm nothing else depends on it.
