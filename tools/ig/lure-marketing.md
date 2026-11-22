# Lure: the marketing story (read before every post)

## Human-first (Jordy, 22 Nov 2026). This overrides older rules below.
Jordy wants the content **more human and more professional**. Research on how the big AI/software companies do it (Nov 2026):
- **OpenAI (ChatGPT, first global campaign, Sept 2025):** dropped abstract tech visuals for real young people in everyday moments (road trip, cooking for a date, a pull-up). Shot on 35mm film for warmth; "unpolished in-between moments", "humanity... a clear focus on people".
- **Anthropic (Claude, "Keep Thinking", Sept 2025 and 2026):** real employees (researchers) and real users on the posters; honest, calm tone that names doubts instead of hyping.
- **Perplexity:** grows through hundreds of real creators who *show* the product in use; analysts say audiences push back when it feels insincere or too corporate.
- **Duolingo:** employees are the face; low-budget, office-shot, relatable videos outperform polished ads; a recurring character and series.
- **Audience data:** when people *suspect* content is AI, it is rated 48% less trustworthy, 57% less authentic, with 60% lower emotional connection (Raptive, 3,000 US adults, 2025), even when it wasn't AI. Only 26% of consumers think AI-made creator content performs better, down from 60% in 2023 (Billion Dollar Boy).

What that means for Lure from now on:
1. **No realistic AI people.** The AI crew (Daan, Mila, Yusuf, Lotte) is paused. No AI faces, no AI voices. AI may only be used for small non-human details (a texture, a background), never as "proof".
2. **Real proof only:** the real app (App Store screens, phone scenes), real spots and real numbers from the database, Jordy's own words.
3. **A real face:** Jordy is the founder and the face. Content in his voice ("Notes from the founder"), only with sentences he actually wrote or said. Never invent quotes, opinions or stories for him. When Jordy sends real footage or photos (himself, friends who agreed, Amsterdam streets, a night out), that footage goes first: cut it with `edit.py`, add text and the end card.
4. **Professional = consistent:** fixed series ("Notes from the founder", "This week at Lure", "City tonight", "How Lure works"), one design system (dark #0C0B12, Lure orange, teal, Poppins Bold), every cover readable in the grid, carousels 1080x1350, max ~6 words per slide headline, alt text on images.
5. **Calm, specific copy:** like a friend who knows the city, not an ad. No hype words, no fake urgency, no emoji at the start of every line. One question per caption that people can actually answer.
6. **Engagement goal per post:** a save (useful carousel), a share (relatable moment) or a comment (a real question). Pick one per post.


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
- Mix: real footage from Jordy when available, the REAL app for proof, end card with logo and "Free on iPhone". (No AI footage of people since 22 Nov 2026.)
- On-screen text: max 6 words per shot, Poppins Bold, one word in Lure orange.
- Our own music (Higgsfield ElevenLabs Music, instrumental), never copyrighted tracks.
- AI shots: only small non-human details if at all; no people, no logos, no text in the image.
- Look at every frame before posting. If any shot looks fake, warped or cheap, regenerate or cut it.

## Tools
- `tools/ig/scenes.py`: brand scenes (real app in a phone, end card) and text layers for AI shots.
- `tools/ig/edit.py` + GitHub Action "Compose Instagram media": cuts the Reel with AI shots and music (put an `ig/jobs/<name>.edit.json`, push, wait ~2 min, pull).
- `tools/ig/render.py`: photos and carousels.
