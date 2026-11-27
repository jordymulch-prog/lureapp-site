# Lure Instagram: content plan (approved by Jordy 20 Nov 2026, made human-first on 22 Nov 2026)

**Read `tools/ig/lure-marketing.md` section "Comments + selling" (24 Nov 2026) first. It overrides anything below that conflicts with it.** Then read `ig/learnings.md` (playbook + open experiment) and follow `tools/ig/skills/learning/SKILL.md`; the loop may rework upcoming posts below when the data says so.

Post the next post in this list that is not yet in `ig/log.json` (match on the "plan" field). After post 10, write a new list of 10 in the same style, based on what performed best (reach, shares, saves, comments in the log), and keep going.

## Budget
Jordy gives max **200 Higgsfield credits per month**. Up to 20 Nov, 110 were used; about 90 are left until 20 Dec. Before generating, check the balance and the estimate. If a post would leave less than the credits needed for the remaining planned crew videos, make the cheaper version (real app, design, one shot instead of three). Never buy credits.

## The crew (virtual, AI). BACK ON (24 Nov 2026)
> Paused 22 Nov, switched back on by Jordy on 24 Nov: followable characters got the most reach. Use them in fixed series (see the posts below), one 6 s Kling shot per Reel (12 credits) to stay in budget.

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

## The 10 posts (revised 24 Nov 2026: crew series, every post asks for comments and sells Lure)
Budget on 24 Nov: 73 credits until 20 Dec. One 6 s Kling 3.0 shot = 12 credits, a nano_banana still = 1. Posts 4-8 use ~61. If the balance is below what a post needs, make the 0-credit version: the crew still (subtle zoom in `scenes.py`/`edit.py`), real app scenes, text on screen, same comment prompt. Never buy credits.

| # | plan id | Format | Idea | Comment prompt | Credits |
|---|---|---|---|---|---|
| 1 | hq-interview | Reel 32 s | DONE 21 Nov (crew interview). Best so far: 81 reach, 1 share. | | 0 |
| 2 | group-chat | Reel 13 s | DONE 22 Nov (Lotte). | | 17 |
| 3 | four-taps | Carousel | DONE 23 Nov (real app). 1 reach after a day: plain info carousels don't work. | | 0 |
| 4 | ask-hq-2 | Reel 15 s | Series **"Ask Lure HQ"** ep. 2. Daan asks from off-screen: "First thing you do in a new city?" Mila (6 s): "I open Lure and check where everyone's going tonight." → real map scene → prompt → end card. | "Your first move in a new city? And what should we ask the crew next?" (caption keeps one question: the first) | 12 |
| 5 | daans-pick | Reel 15 s | Series **"Daan's pick"**. Daan (6 s) holds up two fingers: "Two spots for tonight. You pick." → two REAL Amsterdam spots from the database (name + type), shown on the real map → "A or B?" | "A or B? Comment the letter." | 12 |
| 6 | lotte-friday-1 | Reel 15 s, post on Friday | Series **"Lotte's Friday"** ep. 1. 8 PM, group chat silent. Lotte on her sofa (6 s): "Nobody decides. So I'm opening the vote." → real Lure Drop vote scene ("Where are we going tonight?", vote till 21:00) → "Bar or club? You decide where she goes next Friday." | "Bar or club?" | 12 |
| 7 | mila-maps | Reel 15 s | Series **"Mila maps the city"**. New nano_banana still of Mila by an Amsterdam canal at night (same look), animated 6 s: "Three spots in Amsterdam I'd send you to." → 3 real spots from the database with the Lure team tip, on the real map → "Which city should I do next?" | "Which city next? Name it." | 13 |
| 8 | yusuf-feature | Reel 12 s | Series **"Yusuf, feature of the week"**. Yusuf (6 s): "You can send one friend your live location until you're home." → real Get home safe / Friends screen → "What should we build next?" (no promise that we will). | "What should we build next? One sentence." | 12 |
| 9 | results-1 | Reel or carousel, 0 credits | **"You picked"**: results of posts 5 and 6 from the REAL comments (counts only, no usernames). No votes? Say so honestly and ask again. Crew stills + real app + end card. | "Next round: vote again below." | 0 |
| 10 | lotte-friday-2 | Reel 15 s, post on Friday | "Lotte's Friday" ep. 2: Lotte goes where the comments sent her (bar or club; if no votes: she picked, say so). New still + 6 s shot only if the balance allows, else the 0-credit version. Ends with the next A/B choice. | next A/B | 0-13 |

**Ready posts (24 Nov):** an entry in `ig/log.json` with `"status": "ready"` is already made (video, cover, caption). On its `ready_for` date (or later, if a run was missed) the run posts THAT file via Windsor instead of making a new post, then sets `"status": "posted"` and the media_id. First check with Windsor that nothing was posted today already (no double posts). Posts marked "post on Friday" are only used on a Friday; on other days take the next post.

**MORE LIFE update (27 Nov, Jordy):** every post below is now made in the lively format of `lure-marketing.md` "MORE LIFE" (outdoors, multi-shot, cuts every 1-2 s, push-ins, loud beat, our own open-world HUD; trend hooks allowed by name, never their assets). Budget stays 200/month: Higgsfield balance 26 credits on 27 Nov until 20 Dec = **one more full crew Reel (~15 cr)**, the rest 0-5 credit lively posts that re-cut footage we already have. Reworked queue:
- Fri 27 Nov: **daans-pick-2** (ready; GTA 6 hook, Daan street → bar → club, "A or B?").
- Sat 28: **mila-maps** as 0-2 credit version: real Lure map zooms into 3 real Amsterdam spots (database, team tips), kinetic text, HUD "Side quests", "Which city next? Name it." No new Kling.
- Sun 29: **yusuf-feature** 0-credit: Get home safe / Friends screens with motion + kinetic text "You can send one friend your live location until you're home" (check the app first), "What should we build next?"
- Mon 30: **results-1** 0-credit: re-cut daans-pick-2 footage: "You picked A/B" with the REAL comment counts (or honestly: "No votes yet, so Daan picked"), then the winner shot.
- Tue 1-Thu 3 Dec: new list (posts 11+), lively 0-5 credit versions, December hooks (exam week, Sinterklaas 5 Dec, Christmas markets).
- Fri 4 Dec: **lotte-friday-1** = the one full crew Reel left (~15 cr, multi-shot: sofa → vote on Lure → bar), with E4.
Old order notes below stay for reference.

**Order update (26 Nov):** the 25 Nov run was missed, so ask-hq-2 went out on Thu 26 Nov. Fri 27 Nov: daans-pick (ready, Friday "tonight" fits). Then Sat 28 mila-maps, Sun 29 yusuf-feature, Mon 30 results-1 (real comments of daans-pick only, and say so honestly; lotte-friday-1 is not out yet), Fri 4 Dec lotte-friday-1 (with E4). Tue 1-Thu 3 Dec need posts 11+: write the new list of 10 by the 30 Nov run (December ideas in `ig/learnings.md` research log). Budget 26 Nov: Higgsfield balance 41 credits; lotte-friday-1 + mila-maps + yusuf-feature need ~37, so the new list starts with 0-credit versions until 20 Dec.

After post 10: write the next 10 from what brought the most **comments per reach** (series + prompt type), keep the same rules.
