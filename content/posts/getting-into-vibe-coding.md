+++
title = "Getting Into Vibe Coding"
date = 2025-08-15T12:41:59-05:00
draft = false
summary = "Vibe coding is making developing software fun again."
tags = ["ai", "vibe", "typescript"]
categories = ["development"]
type = "posts"
+++
I've been toying with some ideas for websites and apps for several years now but never really felt like I had the time to invest in building them. The dream has always been to create web applications that not only help me learn something new but that I can potentially use as a revenue stream. That's all changed with the advent of agentic-powered software development.
<!--more-->
## What is Vibe Coding?

(Header suggested by Claude). Vibe coding, according to [good old Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding) is:

>*It describes a chatbot-based approach to creating software where the developer describes a project or task to a large language model (LLM), which generates code based on the prompt. The developer evaluates the result and asks the LLM for improvements. Unlike traditional AI-assisted coding or pair programming, the human developer avoids micromanaging the code, accepts AI-suggested completions liberally, and focuses more on iterative experimentation than code correctness or structure.*

Or, in my experience, driving the AI through prompting and using a light set of rules and context. I've had some great success so far creating several [Python click-based CLIs](https://click.palletsprojects.com/en/stable/) for work that have turned out really well with minimal input on my part. Liberally trusting the AI to write quality code can be dangerous if you don't understand what its actually creating. Doing this in production is not necessarily something I'd recommend.

## A Simple Framework for Vibe Coding

I've been experimenting with several iterations of [AI prompts](https://github.com/richardboydii/ai-prompts) based on some of the [prompt engineering best practices from Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices). I've found that building an Architecture Decision Report helps me better articulate what I want the agent to build and keep in on track with the feature at hand. I've found that interrupting the agent doesn't derail it too often, but you want to be careful about leading it on a tangent while you're in the middle of developing a feature.

The ADR format that I've been using is also fairly simple but does a decent enough job of focusing the agent and developing incrementally. I tuck these away in a `docs/adrs` subfolder in my project along with a `rules.md` file that has my [AI prompt](https://github.com/richardboydii/ai-prompts) rules.

    # ADR 001 - Name of ADR

    ## Status

    Planned | Accepted | Implemented

    ## Date

    YYYY-MM-DD

    ## Context

    Detailed description of what we are building.

    ## Consequences

    ### Positive

    - Benefits of the new feature.

    ### Negative

    - Downsides of the new feature.

    ## User Stories

    Filled out by the agent.

    ## Tasks

    Filled out by the agent.

## Next Steps

I just learned about a new way to run multiple agents in a project, the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD). On first look it seems to create a whole team of agents that are specialized in different tasks. An orchestrator agent then manages the team of sub-agents in order to build software. I feel like software developers are slowly transforming into engineering managers and product owners at this rate. I'll make sure to write up another blog post on what I learn from this new method.
