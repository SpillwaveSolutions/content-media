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

Unknown `rel` values are treated as `info` by validation. Do not invent new names in this plugin.
