# Lure: the marketing story (read before every post)

Use with the skills in `tools/ig/skills/`: product-marketing (positioning), marketing-psychology (why people act), content-strategy (what to make), copywriting (the words), social + video (the formats), launch (the sequence).

## Positioning
**For** young people who go out (students, internationals, friend groups),
**who** spend the evening in group chats asking "where is everyone?",
**Lure is** the live map of your city and your friends,
**that** turns "maybe later" into a plan and a meet-up.
**Unlike** Instagram and TikTok, which keep you scrolling at home, Lure exists to get you off the phone and out the door.

One line: **Your city is waiting.** Tagline: **Plan. Post. Meet.**

## The enemy (every story pushes against it)
The evening that dies in the group chat. Twenty messages, nobody decides, everyone stays in. Scrolling other people's nights instead of having your own.

## The promise
Open Lure, see where your city and your friends are tonight, make the plan in seconds, and actually meet.

## Proof we can show honestly
- The real app: the live map, the friends scan, plans, Lure Drop (use the App Store screenshots in `appstore/`).
- Real spots from the database, with Lure team tips.
- Real numbers only: cities and countries live (query them).
Never: invented users, reviews, quotes, follower counts, venue partnerships.

## Campaign arc (first 4 weeks)
Each week has one theme; every post that week tells a piece of it. Reels carry the story, carousels explain, photos spotlight.

| Week | Theme | Story beat | Hero post |
|---|---|---|---|
| 1 | **Launch: "Your city is waiting."** | Introduce the enemy (group chat paralysis) and the answer (Lure). | Brand Reel: "Your friends are out tonight. You just don't know where." → app → meet-up → Plan. Post. Meet. |
| 2 | **How it works** | Remove friction: scan to add, see who's out, make a plan, Lure Drop. | Carousel "4 taps to a night out" + Reel of the scan moment |
| 3 | **Cities** | Lure is where you are: city spotlights with real spots, new cities live. | Reel "Groningen tonight" / "Amsterdam tonight" with real spots |
| 4 | **The night itself** | Emotion: first night in a new city, the friend you met at an event, getting home safe. | Reel "New in town?" for exchange students (ESN season) |

After week 4: repeat the cycle with new cities, seasons and moments (exam week over, Friday, King's Day, summer terraces). Every post must answer: which beat of the story is this?

## Psychology we use (honestly)
- **Loss aversion / FOMO done right:** "Your friends are out tonight" is true for most users; never fake scarcity.
- **Social proof:** only real, e.g. real spots, real cities count.
- **Ease:** show how few taps it takes; less effort beats more features.
- **Identity:** "people who go out" and "new in town" are identities our audience wants.
- **Specificity:** a named café beats "great places".

## Creative standard (no AI slop)
- Hook in the first second: a line the viewer recognises from their own life.
- 12-18 second Reels, cuts on the beat, 5-7 shots, one idea.
- Mix: cinematic AI footage (Higgsfield Kling 3.0) for mood, the REAL app for proof, end card with logo and "Free on iPhone".
- On-screen text: max 6 words per shot, Poppins Bold, one word in Lure orange.
- Our own music (Higgsfield ElevenLabs Music, instrumental), never copyrighted tracks.
- AI shots: no recognisable faces, no logos, no text in the image, consistent warm orange/teal grade.
- Look at every frame before posting. If any shot looks fake, warped or cheap, regenerate or cut it.

## Tools
- `tools/ig/scenes.py`: brand scenes (real app in a phone, end card) and text layers for AI shots.
- `tools/ig/edit.py` + GitHub Action "Compose Instagram media": cuts the Reel with AI shots and music (put an `ig/jobs/<name>.edit.json`, push, wait ~2 min, pull).
- `tools/ig/render.py`: photos and carousels.
