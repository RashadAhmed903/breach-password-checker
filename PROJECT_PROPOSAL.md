# Project Proposal: Breach & Password Health Checker

## Problem Statement
People reuse weak or already-breached passwords without knowing it.
This tool lets a user check whether a password has appeared in known
breaches and how strong it actually is, so they can make an informed
decision about changing it.

## Goals (v1 scope)
- Check a password against the HIBP Pwned Passwords database (free,
  no API key required — uses k-anonymity so the real password never
  leaves the user's machine in full)
- Score the password's crackability (length, character variety,
  common patterns)
- Simple web UI: type a password, see the verdict

## Non-Goals (explicitly out of scope for v1)
- Email breach lookup (requires a paid HIBP key — stretch goal,
  toggleable if the user supplies their own key)
- User accounts, login, or saving any history
- A database — the app is stateless; nothing is stored

## User Stories
- As a user, I want to enter a password and see if it's been
  breached, so I know if I need to change it.
- As a user, I want to see how strong my password is (not just
  "breached or not"), so I understand *why* it's weak if it is.


## Tech Stack
- Backend: Python 3.12 + FastAPI
- Frontend: HTML/CSS/JavaScript (no framework for v1)
- Containerization: Docker
- Testing: pytest
- Version control: Git + GitHub
- Task tracking: Jira

## Architecture (high level)
Browser (HTML/JS) --fetch--> FastAPI backend --calls--> HIBP Pwned
Passwords API. Password strength scoring happens locally in the
backend, no external call needed for that part.

## Milestones
1. Repo scaffold + Git set up
2. Backend endpoint: check password against HIBP
3. Backend logic: crackability scoring
4. Frontend: form + results display
5. Tests
6. Docker
7. (Stretch) Email lookup behind an API key toggle
