# Lure Instagram: content plan and crew (approved by Jordy, 20 Nov 2026)

Post the next post in this list that is not yet in `ig/log.json` (match on the "plan" field). After post 10, write a new list of 10 in the same style, based on what performed best (likes, comments, shares in the log), and keep going.

## Budget
Jordy gives max **200 Higgsfield credits per month**. Up to 20 Nov, 110 were used; about 90 are left until 20 Dec. Before generating, check the balance and the estimate. If a post would leave less than the credits needed for the remaining planned crew videos, make the cheaper version (real app, design, one shot instead of three). Never buy credits.

## The crew (virtual, AI). Same faces every time.
Always start crew shots from these Higgsfield stills (use the job id as `start_image` with Kling 3.0, `sound: on`):

| Name | Role | Look | Still (job id) | Local copy |
|---|---|---|---|---|
| Daan | host, holds the mic | 23, curly brown hair, orange hoodie | 629b8a96-9533-4877-9839-44d95af6bc79 | ig/jobs/crew/host.png |
| Mila | cities | 24, dark hair in bun, round glasses, cream sweater | 9418c68c-1dbe-4bfd-abd7-649edd60ad06 | ig/jobs/crew/mila.png |
| Yusuf | product | 26, short beard, denim jacket, white tee | 241e7c5b-2857-4524-9d6f-1e12a670d3bb | ig/jobs/crew/yusuf.png |
| Lotte | community | 22, wavy blonde hair, striped colourful sweater | fd6bb0c5-43ee-4a2e-9911-ab43bce4aa15 | ig/jobs/crew/lotte.png |

Setting: Lure HQ, a startup office in an Amsterdam canal house (warm wood, plants, canal windows, orange wall with neon lines, wall screen with a city map). For scenes elsewhere (bar, street, event), generate a new still with nano_banana that describes the same person precisely, then animate it.

Rules: the crew may act out scripted stories ("I met my best friend at an ESN party, we scanned each other on Lure"), like actors in a commercial. Do NOT write anything about AI in the caption. Instagram has its own "AI-label toevoegen" switch for realistic AI photos and videos; Windsor.ai cannot set it, so Jordy switches it on himself. In your report, remind him which post needs the AI label. Facts they say about the app or numbers must be true (check the database).

Kling 3.0 costs: 6 s = 12 credits, 8 s = 16 credits (std, sound on). One speaker per shot works best; the interviewer can ask from off-screen. Interview layer: `scenes.py` type `caption` (question on top, name tag). Cut with `edit.py` (`"audio": true` keeps the speech, music at `"music_volume": 0.12`).

## The 10 posts
| # | plan id | Format | Idea | Credits |
|---|---|---|---|---|
| 1 | hq-interview | Reel 32 s | "Inside Lure HQ": Daan interviews Mila, Yusuf, Lotte. READY: ig/hq-interview.mp4 + .jpg, approved by Jordy. Post as is. | 0 |
| 2 | group-chat | Reel ~15 s | Lotte: "POV: it's 9 PM and the group chat still says 'idk, you guys?'" then opens Lure, plan made in 10 seconds. Mix crew shot + real app scenes. Caption asks: tag the friend who never decides. | ~24 |
| 3 | four-taps | Carousel 5 slides | "4 taps to a night out" with the real app screens (appstore/). Save-worthy. | 0 |
| 4 | guess-city | Reel ~12 s | Mila names 3 real spots from the database, asks "which city is this?". Answer in comments. | ~12 |
| 5 | vote-amsterdam | Post | "Where should Amsterdam go tonight?" 3 real spots, vote in the comments; ties into Lure Drop. | 0 |
| 6 | new-in-town | Reel ~15 s | Yusuf as an exchange student on his first night: scans someone at an ESN party, sees new friends on the map. | ~24 |
| 7 | privacy | Carousel | "Is Lure tracking me?" Q&A: friends only see you if you share, your code changes every 2 minutes, you choose. | 0 |
| 8 | groningen-tonight | Reel ~10 s | Real Groningen spots with Lure team tips, one AI mood shot. | ~5 |
| 9 | milas-story | Reel ~10 s | Mila: "I met my best friend at an ESN party. We scanned each other on Lure." | ~16 |
| 10 | crew-update | Reel or carousel | New cities and countries with real numbers + "what should we build next?" | 0-10 |
