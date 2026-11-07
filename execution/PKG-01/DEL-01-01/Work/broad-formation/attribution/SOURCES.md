# Attribution lane source account

TASK author examination, 2026-11-07. No experiment, code execution or source result
reproduction. Captures are local research evidence, not publication assets.

## Sources actually inspected

| Source | Actual coverage used | Identity / location |
|---|---|---|
| BLADE, 2610.18780v1 | Abstract/introduction; §3.4 global diagnosis; §4.1 setup and metrics; limitations; references relevant to replay/repair | Retained `../../primary-sources/blade.txt` and its PDF/capture. Public README additionally fetched in `sources/blade-readme.md`. |
| Who&When Pro, 2607.09996v2 | Abstract/introduction; failure injection account; Appendix A.1 single-error limitation; relevant method references | Retained `../../primary-sources/who-when-pro.txt` and PDF/capture. |
| TraceTrial-Bench, 2610.32285v1 | Abstract/introduction; limitations/future directions; references identifying REFLECT | Retained `../../primary-sources/trace-trial.txt` and PDF/capture. |
| FAMAS, 2509.13782v1 | Abstract, introduction, turn-based MAS and decisive-state formulation in §2 | `sources/famas.pdf`, extracted `.txt`, `.capture.json`. This is the 2025 preprint, not the full 2026 FSE version DOI10.1145/3797113. No exact later-version efficacy claim is made. |
| DoVer, 2512.06749v3 | Abstract/introduction, related work, attribution ambiguity discussion and §4 pipeline/interventions | `sources/dover.pdf`, `.txt`, `.capture.json`. OpenReview conference PDF returned403; identified arXiv v3 used. Supports multiple steps/alternative repairs, not merely one-step attribution. |
| REFLECT, 2606.09071v1 | Abstract/introduction, related-work distinctions, §§3.1–3.3 replay/attribution contract, Appendix R limitations, code-release statement | `sources/reflect.pdf`, `.txt`, `.capture.json`. Correction rates and source comparative priority claims are not independently verified or used as our results. |
| The Misattribution Gap, 2605.22842v1 | Abstract/introduction, §7 attribution setup, relevant §8 defense framing, limitation passages | `sources/misattribution.pdf`, `.txt`, `.capture.json`. Its model-versus-memory target differs from Who&When agent/step attribution; broad impossibility and immunity claims are not adopted. This is close prior work for memory-caused misdiagnosis, not evidence of our coalition-framing effect. |

The retained organizer-source synthesis and original event text supply Track 4
context. This lane does not claim to reread all fourteen organizer papers.

## Code and access facts

- DoVer project URL `https://aka.ms/DoVer` returned200 and redirected to
  `https://mbjinx.github.io/DoVer_Web/`; retained HTML/capture records its link to
  `https://github.com/microsoft/ACV/tree/main/misc/DoVer`.
- GitHub contents API for that directory returned the AG2, source, scripts,
  analysis and attribution directories; retained `sources/dover-tree.json` and
  capture. Files were not installed or run. A guessed `microsoft/DoVer` repository
  returned404; the actual source link above resolves that guess.
- GitHub metadata for `GXG-CS/BLADE` returned accessible main branch and MIT
  license; retained `sources/blade-repo.json`. README describes Jev-backed
  operations and a cached example. Exact backend access is unresolved.
- Search feeds `adversarial-attribution.xml`, `blame-framing.xml` and
  `dover-search.xml` are discovery observations. Entries were followed to the
  primary documents above before using consequential claims. Search coverage is
  bounded, not evidence of absence of other related work.

Individual `.capture.json` files preserve retrieval URL/time, content hash and
transformations for newly fetched bodies. Original retained source identities
remain in their owning capture files. PDF text extraction used `pdftotext -layout`;
no formula/proof conclusion requiring image inspection is relied upon here.

## Design consequence

Generic outcome-oriented attribution, replay and multiple interventions are
already well-supported research directions. They are not promoted as new options.
The single returned proposal instead asks about strategic coalition manipulation
of attribution and the actual recovery decision, including strong existing
intervention-based diagnostic baselines. Literature novelty remains qualified.
