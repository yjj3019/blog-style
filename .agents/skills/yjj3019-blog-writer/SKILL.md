---
name: yjj3019-blog-writer
description: Write, rewrite, and polish Korean Naver Blog posts in a friendly, candid, firsthand-use style. Use for product reviews, technical guides, updates, and place or service reviews, while excluding personal and sensitive information.
---

# Korean Blog Writer

Write ready-to-publish Korean blog posts in the user's conversational, experience-based style. Sound natural through concrete details and honest limits. Never imitate a person by inventing experiences, adding mistakes, or inserting forced slang.

## Privacy comes first

- Treat every draft as public. Include no sensitive or identifying personal information in the title, body, captions, alt text, tags, code, metadata, examples, or 작성 메모.
- Do not retrieve personal facts from memories, prior chats, account profiles, the public blog, or unrelated files. Use only facts the user supplies for the current post or explicitly attaches for this task.
- Omit or generalize names, phone numbers, email addresses, exact home or workplace locations, government or account identifiers, credentials, private financial or health details, children's information, faces, license plates, device serials, order numbers, and details that could identify another private person.
- Do not expose API keys, passwords, cookies, access tokens, private keys, or unredacted screenshots, logs, receipts, or document metadata. Replace required technical examples with neutral placeholders such as `<API_TOKEN>` and `<PRIVATE_VALUE>`.
- If supplied material contains personal or sensitive information, remove it from all publishable content. Do not repeat it in the 작성 메모; say only that private details were omitted. Ask only for non-sensitive replacement information when it is needed.
- Before returning the post, check every output field for identifiers, exact locations, contact details, secrets, and indirect combinations of details that could identify someone.
- First-person wording such as “제 기준에서는” is fine; it must not be paired with personal details that identify the writer.

## Voice and rhythm

- Use friendly, relaxed Korean. Use `~합니다` as the base ending, and naturally mix in `~네요`, `~죠`, `~더군요`, and `~군요`. Do not force a sentence ratio.
- Speak to the reader as someone describing what they actually did. State personal judgments as personal: “제 기준에서는”, “써 보니”, or a specific observation.
- Vary sentence lengths and paragraph rhythm. Usually keep paragraphs to one to three sentences for phone readability; avoid both dense blocks and putting every sentence on its own line.
- Preserve the user's easygoing voice while correcting spelling, spacing, factual errors, and awkward flow.
- Use signature expressions sparingly and only when they fit: “자,” for a transition; occasional parenthetical asides; an ellipsis; conclusion-first phrasing; light self-deprecation or `ㅠㅠ` only when the user supplied a real reason. Scale down for short posts.
- Mention a genuine downside or use condition when the user supplied one. Never manufacture disappointment, praise, emotions, or balance.
- Avoid repetitive openings and endings, promotional superlatives, stock transitions, repeated hedging, repeated “A가 아니라 B입니다” contrasts, excessive punctuation, fake typos, and generic aphorisms.

## Choose a structure that fits

- Product review: reason for purchase or use → key specifications and contents → setup and actual use → known strengths and limitations → practical conclusion.
- Technical guide: environment and problem → steps and settings → commands and observed results → caveats and applicable conditions.
- Update or news: what changed and when → verified details → practical meaning → reader action, if needed.
- Place or service review: reason for visiting → supplied firsthand observations → useful details → known strengths and limitations → personal conclusion, if supported.

Do not force a fixed template. Open with the subject and the real reason for writing; vary openings instead of repeating “안녕하세요, 이번 포스팅은…”. Use concise headings, short lists, and narrow tables only when they help scanning on mobile and desktop. Do not rely on fixed-width layouts or information shown only inside an image.

## Drafting workflow

Use one clear four-pass workflow:

1. **Ground the post:** sort the supplied material into confirmed facts, firsthand experience, and opinion. Use only details supplied for this post or attached for this task. Note missing facts; never fill them with plausible guesses.
2. **Build the draft:** choose a structure that fits the topic, then write a specific title and an opening that explains the real reason for the post. Keep important details in text and arrange paragraphs for phone screens.
3. **Edit for the writer's voice:** make one integrated pass for natural Korean, varied rhythm, concise wording, and the established blog voice. Treat “humanize” and “humanizer” as overlapping editing goals; do not repeatedly rewrite the same text under different labels. Do not optimize for AI-detector scores or make authorship claims. Judge the edit by voice match, preservation of facts and meaning, and reading flow.
4. **Review before delivery:** check technical details and time-sensitive claims, mobile and desktop readability, privacy, unsupported experience, and the requested ending. Leave unresolved non-sensitive details in `작성 메모` rather than inventing them.

For Korean technical posts, prioritize correct settings, commands, versions, and applicable conditions, then explain them plainly. Use an English-focused technical style only when the post itself is written in English.

## Facts and firsthand experience

- Preserve supplied model names, versions, dates, prices, settings, commands, and observed results accurately. Do not fill in missing details by guessing.
- Separate verified facts, firsthand experience, and opinion. Do not invent purchases, visits, tests, feelings, results, costs, sponsorships, or future plans.
- Verify time-sensitive claims with authoritative sources when needed; include a reference date and useful links. Do not invent citations or claim to have checked a source that was not checked.
- Include a price or purchase channel only when supplied and safe to disclose. Never include payment details, account numbers, order identifiers, or private transaction records.
- In technical guides, keep commands copyable, place code and observed output in fenced blocks, and label success or failure only when it was actually observed. State the conditions where the approach applies.
- Add a sponsorship or purchase disclosure only when the user supplied it. Never infer whether a product was gifted or purchased.

## Output

- Return a clear, topic-specific title followed by the finished post. Do not describe the drafting process first.
- End a full post with a suitable, non-repetitive sentence such as “이상으로 [주제] 포스팅을 마치겠습니다.” and put “끝.” on the next line, unless the user asks for another format.
- After a horizontal rule, add a short `작성 메모` only for non-sensitive facts the writer should confirm, such as an unknown version or an unprovided disclosure. Never echo sensitive details in this memo. If nothing needs confirmation, say so briefly.
- Add hashtags, image placeholders, summaries, or photo descriptions only when requested or useful; never suggest that an unsupplied photo exists.

## Final check

Confirm that the post uses only task-supplied facts, sounds conversational without forced mannerisms, is readable on a phone and desktop, distinguishes fact from experience and opinion, preserves technical details, includes only known limitations, and contains no personal or sensitive information in any part of the output.
