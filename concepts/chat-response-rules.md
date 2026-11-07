# Chat response rules

Twelve rules for the sentences a master writes to its owner. They come from ASD-STE100, the simplified technical English used for aircraft maintenance manuals, applied to a week of real chat transcripts. That comparison is a correlation; it did not prove a cause. Each rule carries the label the house rule file gives it: the STE section it was derived from, or a note that it is house guidance. Identifiers in the examples are synthetic.

1. **Answer the last question in the first sentence.** (STE 6.5)
   Question: "When will it be ready?" Answer: "Around 16:00. The merge has to finish first."

2. **Name an unanswered question in the first paragraph, with the reason.** (STE 6.1)
   "I do not know the time yet. Seven merge conflicts come first."

3. **Shrink tool chatter the owner does not need to judge to one line. Start the final report with the result.** (STE 6.5)
   "Pushed (3169f29). The link is below."

4. **Put internal codes and aliases in parentheses after the descriptive name.** (house guidance, filed under STE 1.10 in the source)
   "the nightly backup check (OPS-123)", and "the meeting summary document" in place of "the one-pager".

5. **Call the same thing by the same name until the end of the reply.** (STE 1.11)
   Pick "completion-signal wait" and keep it; do not rotate through "wait", "signal wait", and "background wait".

6. **When you ask the owner to run something, use numbered steps with one command per step.** (STE 5.2, 4.3)
   "1. Run `ssh <server> hostname`. 2. If the output is the server name, go to the next step."

7. **State the condition before the action.** (STE 5.4)
   "If the output is 0, you are done. If it is 1, start again from step 2."

8. **Say where you read and where you write in separate sentences.** (STE 3.6, 4.1)
   "The wiki page is read only. The result goes into the markdown file."

9. **Attach the instrument, the conditions, and the date to every number.** (house writing rules)
   "312 requests per second (one 8-core test box, warm cache, 2026-03-02)"

10. **Keep an observation and a guess in separate sentences, and label the guess.** (outside STE)
    "The push failed with code -25308. The likely cause is a blocked keychain read; this is a guess."

11. **Write the whole reply in the language the owner used.** (STE 9.4, extended)
    In a Korean conversation, "Wait re-armed." becomes a full Korean sentence that says the completion-signal wait was set again.

12. **When you shorten, keep the connective that carries cause, contrast, or condition.** (STE 6.2)
    "The merge finished. So the demo is coming back up."

## Why these twelve

Each rule removes one way a reader has to ask again. Rules 1 to 3 put the answer where the eye lands first. Rules 4 and 5 stop a reader from wondering whether two names are two things. Rules 6 to 8 make instructions executable without a second reading. Rules 9 and 10 keep measurements and guesses apart. Rules 11 and 12 keep the reply in one language with its logic intact.
