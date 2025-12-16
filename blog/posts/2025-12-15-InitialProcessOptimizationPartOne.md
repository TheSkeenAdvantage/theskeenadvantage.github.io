# Automating SaaS Security Assessments with AI: Part 1 - The Problem and the Search for a Solution

*How I built an AI-powered solution to streamline SaaS security control assessments*

---

## The Problem: Too Much Manual Work, Too Little Time

SaaS security control assessments were becoming a bottleneck. What should have been a straightforward process was taking far too long, requiring:

- **Manual research** across multiple vendor websites
- **Email exchanges** with vendors to clarify security controls
- **Data entry** across multiple systems and spreadsheets
- **Time-consuming analysis** to compile findings into assessment reports

Each assessment was eating up hours of valuable time that could be better spent on strategic security initiatives. I knew there had to be a better way.

The question was: could AI help automate this process if given the right framework and search criteria?

---

## The First Attempt: OpenAI API

My initial approach was to leverage OpenAI's API directly. It seemed like the perfect solution—feed it questions about a vendor's security controls and get structured answers back.

**The reality was disappointing.**

The standard OpenAI API responses were:
- **Outdated**: The training data didn't include current information about vendors
- **Incomplete**: Responses lacked the depth and specificity I needed
- **Inconsistent**: The quality varied significantly from what I could get by manually querying the OpenAI UI

It became clear that the standard API wasn't accessing live, current information from the internet. For security assessments, having the most up-to-date information is critical—vendor security pages change, new certifications are announced, and security incidents happen in real-time.

---

## The Second Attempt: DuckDuckGo Search API

If OpenAI's standard API wasn't cutting it, maybe I could combine it with a search engine API to get live results. DuckDuckGo seemed like a good option—it's privacy-focused and offers a search API.

I integrated DuckDuckGo's search API to pull current information from the web, then feed those results to an LLM for summarization.

**This approach also fell short:**

- **Inconsistent results**: The quality and relevance of search results varied dramatically
- **Unreliable responses**: Sometimes the API would return nothing, other times it would return irrelevant content
- **Limited control**: I couldn't effectively scope searches to specific domains or ensure I was getting authoritative sources

The inconsistency made it unsuitable for a production solution where reliability is paramount.

---

## The Breakthrough: OpenAI's `web_search_preview` Endpoint

After these setbacks, I discovered OpenAI's `web_search_preview` endpoint—a paid API feature that actually queries the live internet, not just training data.

This was promising, but I wanted validation before committing to this approach. I reached out to other development teams in my organization who were already building production solutions with AI and LLMs. Their feedback was unanimous: **`web_search_preview` was the tool they were using in production deployments for exactly this type of use case.**

That confirmation gave me the confidence to move forward.

---

## The Challenge: Too Much Noise, Not Enough Signal

With `web_search_preview` working, I started getting results. But there was a new problem: **the search results were pulling from everywhere.**

The AI was finding information from:
- ✅ The vendor's official security documentation (what I wanted)
- ❌ Reddit threads and community forums (often outdated or speculative)
- ❌ Third-party review sites (potentially unreliable)
- ❌ Competitor websites (completely irrelevant)
- ❌ Random blog posts (questionable authority)

While some of these sources might have value, for a security assessment, I needed authoritative, vendor-provided information. I couldn't risk basing risk decisions on Reddit comments or unverified third-party claims.

---

## The Solution: Enforcing Search Scope

The key insight was learning how to **enforce URL, subsite, and folder paths** in the search queries.

By using search operators like `site:vendor.com`, I could scope searches to only the vendor's domain. This meant:
- ✅ Only official vendor documentation
- ✅ Current security pages and compliance information
- ✅ Authoritative sources I could reference in assessments
- ❌ No more Reddit threads or unreliable third-party sites

The implementation was straightforward but crucial:

```python
site_filter = f"site:{url.rstrip('/')}"
scoped_query = f"{question} {site_filter}"
```

This simple addition transformed the quality of results. Now, when I asked "Does this vendor support Single Sign-On?", the search would only look within the vendor's official website, returning their actual security documentation rather than random forum discussions.

---

## What This Enabled

With scoped searches working, I could now:
1. **Query specific security controls** (SSO, MFA, encryption, compliance certifications)
2. **Get authoritative answers** directly from vendor documentation
3. **Reference official sources** in the final assessment reports
4. **Ensure consistency** across multiple assessments

The foundation was in place. But this was just the beginning—I still needed to structure the responses, create a framework for risk assessment, and integrate it all into a production workflow.

---

## Coming Next: Part 2

In the next part of this series, I'll cover:
- Building the risk assessment framework
- Structuring AI responses into actionable reports
- Integrating with Power Automate and Microsoft Forms
- Deploying to Azure Functions
- Lessons learned and best practices

Stay tuned for Part 2, where we'll dive into the technical implementation and see how all these pieces came together into a production-ready solution.

---

*Have you faced similar challenges with AI-powered automation? What approaches worked (or didn't work) for you? I'd love to hear about your experiences in the comments.*

