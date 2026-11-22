# Lure Instagram: content plan (approved by Jordy 20 Nov 2026, made human-first on 22 Nov 2026)

**Read `tools/ig/lure-marketing.md` section "Human-first" first. It overrides anything below that conflicts with it.**

Post the next post in this list that is not yet in `ig/log.json` (match on the "plan" field). After post 10, write a new list of 10 in the same style, based on what performed best (reach, shares, saves, comments in the log), and keep going.

## Budget
Jordy gives max **200 Higgsfield credits per month**. Up to 20 Nov, 110 were used; about 90 are left until 20 Dec. Before generating, check the balance and the estimate. If a post would leave less than the credits needed for the remaining planned crew videos, make the cheaper version (real app, design, one shot instead of three). Never buy credits.

## The crew (virtual, AI). PAUSED
> **Paused on 22 Nov 2026 (Jordy: more human, more professional).** Do not make new videos with the AI crew. Posts 1 and 2 used them; that's done. Keep this section only as a record and in case Jordy turns the crew back on.

Same faces every time.
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

## Realism first (Jordy, 21 Nov 2026)
Jordy wants the images AND the voices as realistic as possible. Treat this as a hard quality gate for every crew shot:
- **Images:** prompt like a real phone or documentary camera: natural daylight or practical lamps, slight handheld movement, real skin texture, no plastic glow, no over-smooth faces, no perfect symmetry, normal clothes with creases. Keep motion small and natural (talking, a nod, a hand gesture); no big camera moves or fast actions, those break faces and hands.
- **Voices:** describe the voice in the Kling prompt every time and keep it the same per person (Daan: warm, relaxed, young Dutch man speaking English with a light Dutch accent; Mila: calm, clear, light Dutch accent; Yusuf: friendly, low, Amsterdam accent; Lotte: bright, quick, light Dutch accent). Casual spoken English with small pauses and contractions; never announcer or ad-read tone. Lines short (max ~12 words per 6 s shot) so the speech isn't rushed.
- **Check before posting:** extract frames every 0.5 s around faces and hands; look for warped hands, teeth, eyes, jumping faces, a face that doesn't match the still, lips that don't move with the speech. If a shot fails, regenerate it once (within budget) or cut it and use app scenes instead. Never post a shot that looks fake. You cannot listen to audio yourself: keep the speech short and natural by prompt, check the lip movement on frames, and in your report ask Jordy to tell you if a voice sounds off.

## The 10 posts (revised 22 Nov 2026: no AI people, real app, real places, Jordy's own voice)
| # | plan id | Format | Idea | Credits |
|---|---|---|---|---|
| 1 | hq-interview | Reel 32 s | DONE 21 Nov (AI crew). | 0 |
| 2 | group-chat | Reel 13 s | DONE 22 Nov (AI crew, Lotte). | 17 |
| 3 | four-taps | Carousel 5-6 slides (1080x1350) | "4 taps to a night out" with the real App Store screens, one step per slide, clean and save-worthy. Last slide: "Save this for Friday." | 0 |
| 4 | founder-why | Carousel 5 slides, text-led | Series **"Notes from the founder"**. Jordy (19, Amsterdam) in first person, using only lines he wrote himself (his ESN mail: "social media that gets people outside and connects them", "Plan. Post. Meet."). Why he built Lure, what it is, what it is not. Signed "Jordy, founder". If Jordy has sent a photo or clip of himself (see Human-first), use it on slide 1. | 0 |
| 5 | guess-city | Carousel 4 slides | "Which city is this?" 3 real spots from the database (name + type + the Lure team tip), answer on the last slide and in the first comment-prompt of the caption. | 0 |
| 6 | vote-amsterdam | Single post 1080x1350 | "Where should Amsterdam go tonight?" 3 real spots, vote in the comments; ties into Lure Drop. | 0 |
| 7 | privacy | Carousel | "Is Lure tracking me?" Q&A from the real app: live location is off until you switch it on, your code changes every 2 minutes, friends only. | 0 |
| 8 | add-a-friend | Reel 10-12 s | The scan moment, real app only: phone scenes of the Friends screen (Your Lure code, Scan someone, Meet people, Get home safe), text that works without sound, end card. | 0 |
| 9 | groningen-tonight | Carousel or Reel | Real Groningen spots with Lure team tips, no AI shots. | 0 |
| 10 | build-in-public | Carousel | Series **"This week at Lure"**: real numbers from the database (cities, countries, spots live), what shipped (check the app repo/App Store version), and "what should we build next?" | 0 |

Any post may be swapped for a **Jordy clip** post as soon as footage from Jordy is available (see Human-first). His real footage always goes first.
