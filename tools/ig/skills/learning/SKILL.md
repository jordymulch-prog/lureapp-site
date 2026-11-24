---
name: learning
description: "Daily learning loop for @lureapp.nl (Jordy, 24 Nov 2026). Use in EVERY Instagram run: read the playbook before making the post, and after posting measure what worked, find why, research, run one experiment at a time and update the strategy. Keeps the autonomous account improving instead of repeating itself."
metadata:
  version: 1.0.0
---

# Learning loop: become the marketing expert for Lure

Jordy (24 Nov 2026): "If you don't have a learning mechanism, there's no point in letting you do everything autonomously. Learn from everything you post, what works and what doesn't. Keep researching every day, follow trends. If something doesn't work, find a way to make it work. Don't drift off."

**The one goal you learn for:** more people who download Lure because of @lureapp.nl. Everything you measure, research and change must serve the funnel below. Anything else is drifting off: skip it.

```
Distribution  → Hook        → Hold          → Reaction              → Conversion
reach,          skip rate     avg watch time   comments, shares,       follows, profile visits,
non-follower    (first 3 s)   (vs length)      saves per reach         new Lure accounts
views
```

The memory of this loop is **`ig/learnings.md`** (playbook, experiments, research log, changelog). Numbers per post live in `ig/log.json`.

## Every run: two moments

### A. Before you make the post (2 minutes, so you still post on time)
1. Read `ig/learnings.md` → "Current playbook" and "Open experiments".
2. Apply every playbook rule to today's post, and build in the next open experiment (one variable only).
3. Write in today's log entry: `"experiment": "<id>"` and what you changed.

### B. After the post is live (this is the learning part)
1. **Measure.** Windsor `get_data`, connector `instagram`, account 17841480599771280:
   - per post (last 14 days): `media_reach, media_views, media_reel_skip_rate, media_reel_avg_watch_time, media_reel_total_watch_time, media_comments_count, media_shares, media_saved, media_follows, media_profile_visits, media_type, timestamp`
   - per day: `reach, views, views_non_followers, accounts_engaged, total_interactions`, plus `followers_count`
   - comment texts: `comment_text, comment_timestamp, media_id` (read the real answers; report new ones to Jordy, never reply)
   - new Lure accounts in the last 24 h (Supabase project fuhahxmkimqqvllxdtuy, `public.profiles`; check the date column first; exclude 'Lure Team', 'Jordy', 'Lisa' test accounts, as the daily update does)
   Store the numbers in `ig/log.json` under `stats` for every post, with `checked` date and the post's age in hours. A post is judged at **≥48 h** old; younger ones are only "early".
2. **Diagnose.** For every judged post, walk the funnel and name the **weakest stage** compared with our own median (see the baseline table in `learnings.md`). One stage, one sentence of why ("92 % skipped in 3 s: the first frame is a still face with no line on screen").
3. **Judge the experiment** whose post is now judged: did the target metric beat the baseline? Verdict: `keep` (becomes a playbook rule), `kill`, or `retest` (signal too weak). With our small numbers (<200 reach per post) one post is a signal, not proof: a rule needs **2 posts pointing the same way**, or 1 post plus solid research.
4. **Research (max 3 searches, ~10 minutes, every day).** Use WebSearch (standard; extended only if thin).
   - One question about **today's weakest stage** (e.g. "Instagram Reels first 3 seconds retention 2026", "how to get comments on Reels small account").
   - One **trend scan** for our audience (students and young people going out, Europe): Reel formats, meme formats, topics and moments this week (exam period, Sinterklaas, Christmas markets, New Year, ESN events, Friday night). Only formats we can make honestly: no copyrighted audio, no brands, no real people, no fake claims. Note when a trend peaks; a trend older than ~2 weeks is usually gone.
   - Prefer primary sources (Instagram/@creators, Mosseri, Meta docs) and large datasets; note source + date. Treat vendor blogs as weaker evidence.
   - Log it in "Research log": date, question, source, takeaway, **how we use it** (if there is no way to use it, it was drifting off).
5. **Decide and change.** Pick the single biggest fix for the weakest stage and turn it into the next experiment (hypothesis, change, metric, target). If the same thing failed twice, don't repeat it: change the approach (other hook type, other series, other format) and say so.
6. **Update the strategy files**, small and concrete:
   - `ig/learnings.md`: playbook (max 15 rules, each with its evidence), experiments, research log, changelog line ("2026-11-26: rule 4 added because …").
   - `tools/ig/plan.md`: change upcoming posts when a learning requires it (drop or rework a series that failed twice, move what works up).
   - Commit and push with the post.
7. **Report** to Jordy in the run summary: one line "Learned today: …" and one line "Changing: …".

## Experiments
- One variable per post: hook type, first frame, on-screen text, length, series/character, comment-prompt type, posting time, format.
- **Trial Reels for hook tests (no extra credits):** cut a second version of the same video with a different first 2 seconds and publish it with `create_video_post` + `trial_params: {"graduation_strategy": "SS_PERFORMANCE"}` (shown only to non-followers; Instagram shares it with followers if it performs). Compare skip rate and watch time of the two versions. Log both media ids.
- Targets are relative to our own baseline (median of judged posts), not industry numbers.

## Weekly review (Sunday run)
- Compare per series, per hook type, per comment-prompt type, per format and per time slot.
- Rewrite the next posts in `plan.md` from the winners; drop losers.
- Update the baseline table.
- Send Jordy the 3 most important learnings and what changes next week.

## Guardrails (learning never changes these)
- The hard rules in the run prompt and `lure-marketing.md` stay: true facts only, no invented comments, votes, users, reviews or quotes, no AI in captions, no buying, max 200 Higgsfield credits a month, nothing deleted, comments are not answered.
- Jordy's own decisions (crew on/off, posting frequency, budget, tone) are not changed by the loop. If the data says one of them should change, **propose it to Jordy** in the report with the numbers; don't apply it.
- Never game the numbers (engagement pods, buying, follow/unfollow, fake accounts).
- Stay on Lure and Instagram growth. No side projects, no other platforms unless Jordy asks.
