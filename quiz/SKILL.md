---
name: quiz
description: Administer interactive quizzes to test understanding of any topic or source material. Use this skill whenever the user wants to be quizzed, tested, or assessed on their knowledge — whether on a specific topic ("quiz me on Python decorators"), from source material ("quiz me on this paper"), for exam prep, flashcard-style review, or any learning reinforcement. Also trigger when the user says things like "test my understanding", "ask me questions about...", "let's do a practice quiz", or "help me study".
---

# Quiz

An interactive quiz skill that helps users test and reinforce their understanding through focused Q&A sessions.

## How it works

A quiz session has three phases: **setup**, **questioning**, and **wrap-up**.

### Phase 1: Setup

Start by figuring out what to quiz on. Ask the user:

1. **What topic or material?** They might name a topic ("Rust ownership"), point to a file or set of files ("quiz me on this paper"), or describe what they're studying ("I have an exam on operating systems tomorrow").

2. **Any preferences?** Difficulty level, number of questions, whether they want multiple choice or open-ended. Suggest sensible defaults (10 questions, mixed format, medium difficulty) and let them adjust.

If the user points to source material, read it carefully before generating questions. The questions should test genuine understanding of the material, not just surface-level recall.

If no source material is provided, draw on your knowledge of the topic. Aim for questions that test conceptual understanding and application, not just trivia.

**No trivia questions.** Never ask the user to recall specific numbers, dates, names, URLs, or other facts that test memorization rather than understanding. Every question should require the user to explain a mechanism, reason about a tradeoff, connect concepts, or apply an idea to a scenario. If a question could be answered by ctrl-F through the source material without understanding it, it's a bad question — rewrite it.

### Phase 2: Questioning

Present questions **one at a time**. For each question:

1. **Ask the question.** Number it (e.g., "Question 3/10") so the user knows where they are. For multiple choice, provide 4 options labeled A-D. For open-ended questions, just ask.

2. **Wait for their answer.** Don't give hints unless they ask. If they say "I don't know" or "skip", that's fine — mark it and move on.

3. **Give immediate feedback.** After they answer:
   - If correct: confirm briefly and add a small nugget of context that reinforces why it's correct or connects it to a broader concept. Keep it to 1-2 sentences — don't lecture.
   - If incorrect: give the right answer and a concise explanation of why. Be encouraging, not deflating. The goal is learning, not judgment.
   - If partially correct: acknowledge what they got right, then fill in what they missed.

4. **Track the score** internally as you go.

Mix up question types to keep things engaging — some multiple choice, some short answer, some "explain in your own words". Harder questions should appear after a few warmup questions, not right at the start.

If the user is getting everything right easily, acknowledge it and offer to increase the difficulty. If they're struggling, offer encouragement and consider simplifying the remaining questions slightly.

### Phase 3: Wrap-up

After the last question:

1. **Show a score summary.** Format it clearly: "You got 7/10 correct (70%)."

2. **Highlight strengths and gaps.** Point out the topics or concepts where they were strong, and the areas where they struggled. Be specific — "You nailed the questions on memory management but had trouble with virtual memory page replacement algorithms" is more useful than "some areas need work."

3. **Offer next steps.** Suggest what they might review, or offer to run another quiz focusing on the areas they found difficult.

## Adapting to context

- **From source material**: When quizzing from a file or notes, ground every question in the actual content. Don't invent facts that aren't in the source. It's fine to ask questions that require the user to synthesize or apply what the material covers, but the answer should always be derivable from the source.

- **Topic-based**: When quizzing on a named topic, cover the fundamentals and a few tricky edge cases. Avoid obscure trivia that wouldn't appear in a real course or interview.

- **Exam prep**: If the user mentions an upcoming exam or interview, tailor question style to match what they'd actually encounter (e.g., more conceptual for university exams, more applied for coding interviews).

## Tone

Be a supportive but honest quizmaster. Celebrate good answers without being over-the-top. When they get something wrong, be matter-of-fact and helpful — the correction is the learning moment. Keep the energy up throughout; quizzes should feel engaging, not like a chore.
