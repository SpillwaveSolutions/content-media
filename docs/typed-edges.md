# Typed edges — Content Media

Direction matters. Packs follow outbound edges by default.

| `rel` | Meaning |
|-------|---------|
| `authored_by` | Writer identity |
| `belongs_to` | Article in a series |
| `promotes` | Article promotes an offer or idea |
| `engaged_with` | Subscriber engaged with article |
| `distributed_on` | Channel |
| `measured_by` | Has performance metrics |
| `originates_from` | Came from experiment or outline |
| `related_to` | Related pieces |
| `supersedes` | Updated version |
| `draws_from` | **Article → Finding** (RKC). Canonical stored edge. content-media owns the write. |

## Query-only inverse

| `rel` | Meaning |
|-------|---------|
| `informs` | Finding → Article. Derived by `research-graph`. **Never persist.** Validation fail-closes if this rel is stored. |

`draws_from` target must be a Finding id (`finding.<subject-slug>.<ulid>`). Do not auto-write it; use `/cme-bridge`.

Unknown in-pack `rel` values (other than `informs`) are treated as `info` by validation. Do not invent new names in this plugin.
