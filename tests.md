# Manual test record

**Status:** Planned, not run. No Gemini key or runtime was available during project preparation. Run these six questions in the app and replace each observation/status with the actual result before claiming completion.

| # | Type | Question | Expected answer | Observed answer | Result |
|---|---|---|---|---|---|
| 1 | Fact | What type represents an ordered, changeable collection? | A list (`list`) is ordered and mutable. | Not run | Pending |
| 2 | Fact | How is a function defined in Python? | With `def`, followed by its name and parameters. | Not run | Pending |
| 3 | Fact | What does `range(5)` produce for a loop? | Values 0 through 4; the stop value 5 is excluded. | Not run | Pending |
| 4 | Fact | How do you access a dictionary value by key? | Use square brackets with the key, e.g. `person["name"]`; `.get()` is another option. | Not run | Pending |
| 5 | Unknown | What is the official Python release date scheduled for next year? | The guides do not contain a scheduled future release date; the bot should say it does not know. | Not run | Pending |
| 6 | Tricky, two chunks | How can a function process a group of names and safely handle one missing from a mapping? | Iterate through the names and use a dictionary `.get()` lookup (with a default if appropriate). Both function/loop and dictionary coverage should be cited. | Not run | Pending |

Record the sources shown under each response and explain failures. Do not convert pending rows into passes without running them.
