# 80% of Fortune 500 Companies Are Running AI Agents. Most Security Programs Aren't Ready.

*The visibility gap between AI deployment speed and security oversight is now an enterprise risk — not a future concern.*

**Matt Skeen · March 2026 · [theskeenadvantage.com](https://theskeenadvantage.com)**

---

There's a number from a recent Microsoft Security research report that every CISO should internalize before their next board presentation: **80% of Fortune 500 companies are now running active AI agents**. Not piloting. Not experimenting in a sandbox. Running. In production. Handling customer data, executing business transactions, and integrating with core enterprise infrastructure.

And only **21% of executives** have full visibility into what those agents are doing, what tools they're calling, or what data they're accessing.

Read that again: one in five executives knows what their AI agents are actually doing. That is not an AI problem. That is a governance problem — and it is happening at scale, right now, inside organizations with mature security programs. Organizations with SOC 2 attestations, NIST CSF implementations, and dedicated risk teams. The frameworks didn't fail them. The frameworks simply weren't designed for this.

## Why Your Existing Frameworks Are Insufficient (And What's Missing)

NIST AI RMF, ISO 42001, and the EU AI Act — which reached general application this year — all provide valuable organizational governance structures. Risk committees, documentation requirements, accountability structures. These are necessary foundations and I'm not dismissing them.

But here's the gap: none of them specify the *technical controls* that CISOs actually need for agentic deployments. There are no prescriptive requirements for tool call parameter validation. No standards for prompt injection logging. No guidance on containment testing for multi-agent orchestration systems. The regulatory landscape is telling you to *have a governance program* without telling you what the program should actually control.

This is the same challenge we faced with cloud adoption a decade ago. The frameworks said "secure your cloud environment." The practical work of defining what that meant — IAM least privilege, network segmentation, logging and monitoring requirements — had to be built by practitioners, often the hard way. We're at that same inflection point with agentic AI, just compressed into a much shorter timeline.

## Five Controls Every Organization Should Have Before Expanding Agentic AI

Based on what I'm seeing across enterprise deployments and what I'm actively building, here's a practical starting point for the technical control layer:

**1. Agent identity and least-privilege access.** Every agent needs a discrete identity — not a shared service account, not a human user's delegated credentials. Scope its permissions to exactly what it needs to complete its task. This sounds obvious. Almost nobody is doing it systematically.

**2. Tool call logging and anomaly detection.** If your agent is calling 21 tools per session, you need a log of every one with parameters. Not for audit theater — for the moment something goes wrong and you need to reconstruct exactly what happened. You cannot do incident response on a system you cannot observe.

**3. Prompt injection controls.** Agents that process external content — emails, documents, web pages, user input — are vulnerable to prompt injection attacks where malicious instructions are embedded in that content. This is an active attack vector, not a theoretical one. Input sanitization and output validation need to be part of your agent pipeline design, not afterthoughts.

**4. Containment boundaries for multi-agent systems.** When agents can spawn other agents or call orchestration services, the blast radius of a compromised agent expands dramatically. Define explicit trust boundaries between agents. Treat agent-to-agent communication with the same skepticism you apply to third-party API calls.

**5. Shadow AI discovery and governance onboarding.** Your organization almost certainly has AI agents running that your security team doesn't know about. Low-code and no-code platforms have made it trivial for any business unit to deploy an agent without involving IT. You need a discovery mechanism and a path to bring shadow deployments into your governance program — one that's lightweight enough that teams will actually use it.

## The SABSA Lens: Mapping Controls to Business Risk

For those working within enterprise security architecture frameworks, SABSA gives us a useful lens that most organizations haven't applied to their AI deployments yet. The contextual layer asks: what are we protecting, and why does it matter to the business? The logical layer asks: what policies and controls implement that protection?

Most organizations have done the contextual work — they know AI agents touch sensitive data, execute privileged actions, and operate in production environments. The gap is consistently in the logical layer: the specific, testable controls that implement the policy. The five controls above are a starting point for building that logical layer. They're not comprehensive, but they're the difference between a governance program that exists on paper and one that can actually detect and respond to an incident.

## Where to Start This Week

If you're a CISO or security architect, here's the conversation I'd prioritize: get in a room with your AI/ML engineering leads and your product owners and answer three questions together. What agents are running in production right now? What data do they access? Who owns their security posture?

The answers will tell you exactly where to focus. In my experience, most organizations discover they have significantly more agentic AI running than their security teams know about — and that discovery conversation is the prerequisite for everything that follows.

The window to get ahead of this is narrowing. The organizations building rigorous AI governance programs now will be the ones able to move faster and more confidently with AI capabilities in the next 18 months. The ones treating this as a future concern will be doing reactive work under much harder conditions.

---

*AI governance and threat modeling for agentic systems is something I'm actively building on. Visit [theskeenadvantage.com](https://theskeenadvantage.com) to see what I'm working on, or reach out directly to discuss how your organization is approaching this challenge.*