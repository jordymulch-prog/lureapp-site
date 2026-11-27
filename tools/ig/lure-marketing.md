# Lure: the marketing story (read before every post)

## MORE LIFE (Jordy, 27 Nov 2026). This goes before everything below.
Jordy, after ask-hq-2: "Still a bit boring. It needs more life. It attracts too few people. Change the strategy." He had said the same on 20 Nov ("lively, no boring mood shots with text"). What was boring: every Reel was one person standing still for 6 s in the same office, then the same static map screenshot twice, then a dark end card. Nothing happens, we never show a night out, quiet music.

The format from now on (first one: daans-pick-2, 27 Nov):
1. **Show the night, not the office.** The crew is outside: canal street, bike, bar, club queue, dance floor, terrace. The office only as a rare contrast.
2. **Something changes every 1-2 seconds:** 5-8 cuts in 12-16 s, slow push-ins on every shot, text that slams in, whooshes on the cuts (made with ffmpeg, no third-party audio), upbeat music loud after the speech (ElevenLabs Music, ~2 credits).
3. **One Kling 3.0 Omni multi-shot generation per crew Reel** (`kling_o3_image_reference`, 10 s, 3 shots, sound on, crew still as reference, ~12.5 credits): shot 1 the crew member talking (max ~8 words), shots 2-3 the payoff (the bar, the club, the meet-up). Gives 3 locations for the price of 1.
4. **Story with a payoff:** problem or choice → the real Lure app (map zoom with a pulsing pin, `scenes.py` type `mapzoom`) → the night actually happens → the one-word question (`ab` card) → end card.
5. **Ride what people talk about this week** (game launches, Sinterklaas, exams, Christmas markets, a meme format), honestly: our own visuals only. **Trend hooks may name the thing** (Jordy asked for GTA 6 on 27 Nov), but never use its footage, logo, characters, music, fonts or signature screens ("Mission passed", wanted stars). Our own open-world HUD (`scenes.py` type `hud`: mission box + the real Lure map as minimap) is the series look: **"Real-life open world"**.
6. **Budget stays 200 a month (Jordy, 27 Nov).** Alternate: a full crew Reel (~15 credits) every other day, and in between lively 0-5 credit posts: re-cut crew footage we already have (fetch it with a `*.fetch.json` job), the real app with motion, kinetic text, HUD. Never a static post.
7. Cut locally with `tools/ig/compose_local.py` (segments, timed overlays, push-ins, music volume steps, whooshes) after fetching the Higgsfield media into `ig/jobs/<name>/`.
8. Keep the instagram safe zones: nothing important in the bottom ~420 px (caption, username) or the right edge (buttons).


## Learning loop (Jordy, 24 Nov 2026)
Every run follows `tools/ig/skills/learning/SKILL.md`: read `ig/learnings.md` (playbook + open experiment) before making the post; after posting measure, diagnose the weakest funnel stage, research (incl. trends), run one experiment at a time and update `ig/learnings.md` and `plan.md`. The playbook rules there apply on top of this file, never against its hard rules or Jordy's own decisions.

## Comments + selling (Jordy, 24 Nov 2026). This is the strategy now; it overrides "Human-first" where they conflict.
Jordy, after the first 4 posts: the crew interview Reel (81 reach, 98 views, 1 share) beat everything; photos and carousels barely moved (four-taps carousel: 1 reach after a day). His words: the content must make the viewer react, and at the same time sell Lure. So every post has **two jobs, both required: get comments, and sell Lure.**

1. **The crew is back** (Daan, Mila, Yusuf, Lotte; stills and voices in `plan.md`) as recurring characters people follow in fixed series. Realistic AI people and voices are allowed again, for the crew only. Jordy switches on Instagram's AI label himself: name the post that needs it in every report. Never write about AI in the caption.
2. **Comments:** the post asks the viewer something they can answer in one word or a few seconds, and the answer *matters*: it decides the next episode, the next city, the next question. The question is on screen in the last seconds AND is the caption's one question.
   - Prompts that work (pick one per post): A or B ("Bar or club?"); you decide what happens next; name your city; fill in the blank ("The group chat always dies when ___"); the question for the next episode.
   - Avoid: "What do you think?", "Thoughts?", tag-a-friend as the only prompt, anything that needs a long answer.
3. **Selling:** the real app is the turning point of every story: the crew's problem gets solved on a real Lure screen (phone scene from `appstore/` via `scenes.py`). Then the end card "Free on iPhone" and the caption CTA. Say one concrete thing the app does (vote till 21:00, scan to add, see the map), not "download now".
4. **Reel formula (12-20 s):** hook line the viewer recognises (1st second) → crew moment (one 6 s Higgsfield Kling 3.0 shot from the crew still) → real app scene solves it → comment prompt on screen → end card.
5. **Close the loop:** the next episode uses what people actually commented ("You picked club."), without names or usernames. If nobody answered, say so honestly ("No votes yet, so Lotte picked.") and ask again. Never invent comments or votes.
6. **Format mix:** mostly crew Reels. A carousel or photo only when it carries a vote or a result, never as plain info.
7. **Measure:** log comments and comments per reach for every post. Every 5 posts, compare which series and which prompt type brought the most comments and make more of that.
8. **Still true from Human-first:** facts about the app and numbers must be real (check the app repo/database); real spots from the database; no fake reviews or testimonials: the crew are characters in scenes, never presented as customers praising Lure; never invent quotes from Jordy; footage Jordy sends himself still goes first (add the comment prompt and the app moment to it).

## Human-first (Jordy, 22 Nov 2026). Partly replaced on 24 Nov by "Comments + selling" above (crew and AI people are back); the honesty rules still apply.
Jordy wants the content **more human and more professional**. Research on how the big AI/software companies do it (Nov 2026):
- **OpenAI (ChatGPT, first global campaign, Sept 2025):** dropped abstract tech visuals for real young people in everyday moments (road trip, cooking for a date, a pull-up). Shot on 35mm film for warmth; "unpolished in-between moments", "humanity... a clear focus on people".
- **Anthropic (Claude, "Keep Thinking", Sept 2025 and 2026):** real employees (researchers) and real users on the posters; honest, calm tone that names doubts instead of hyping.
- **Perplexity:** grows through hundreds of real creators who *show* the product in use; analysts say audiences push back when it feels insincere or too corporate.
- **Duolingo:** employees are the face; low-budget, office-shot, relatable videos outperform polished ads; a recurring character and series.
- **Audience data:** when people *suspect* content is AI, it is rated 48% less trustworthy, 57% less authentic, with 60% lower emotional connection (Raptive, 3,000 US adults, 2025), even when it wasn't AI. Only 26% of consumers think AI-made creator content performs better, down from 60% in 2023 (Billion Dollar Boy).

What that means for Lure from now on:
1. ~~No realistic AI people.~~ (Replaced 24 Nov: the crew is back, see above.) The AI crew (Daan, Mila, Yusuf, Lotte) was paused. No AI faces, no AI voices. AI may only be used for small non-human details (a texture, a background), never as "proof".
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
