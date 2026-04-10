---
title: Why India's unconventional foreign exchange policies won't work
description: Understanding India's unconventional monetary policy through T-accounts
draft: False
date: 2026-04-10
---

India's currency fell sharply after the Iran war began, leading the Reserve Bank of India (RBI) to enact two major unconventional policies to strengthen the rupee (INR). First, the RBI [limited banks' net open positions on onshore deliverables](https://www.ft.com/content/afe09b9e-b951-42e2-a8fc-c7863c3338df?syn-25a6b1a6=1) to $100M per day. When that didn't work, they [banned domestic banks from offering non-deliverable forward contracts](https://www.ft.com/content/9fd5635f-26d4-488b-906e-5568338f512d?syn-25a6b1a6=1).

The rupee was already sliding before the war began. In January, the RBI began using conventional intervention techniques to strengthen the rupee -- selling dollars and buying rupees. In March alone, this intervention drew down around [$40bn in foreign currency reserves](https://tradingeconomics.com/india/foreign-exchange-reserves). Because buying rupees reduces their supply, and therefore tightens credit conditions, the RBI *sterilized* this intervention by also buying government bonds in order to neutralize the foreign exchange intervention's impact on domestic credit. Sterilization kept it cheap to borrow rupees.

Likely taking advantage of cheap INR funding within India, domestic speculators continued shorting the rupee. Consider a speculative bank that is short INR and long USD. They would have a T-account like the following:

**Bank (speculator)**
| **Assets** | **Liabilities** | 
|------------------|------------|
| USD | INR |

The bank's *net open position* is just the difference between its assets and liabilities, denominated in USD. This position increases if INR weakens relative to USD and decreases otherwise. The RBI's first unconventional policy limited net open positions to less than $100M at the end of each day. This policy could strengthen INR if speculators sold USD and bought rupees to keep the position under the limit. But banks didn't do this. Instead, they found others also willing to speculate against the rupee, which allowed them to offload their book to keep their net open positions under the $100M threshold. 

But even if they couldn't find domestic speculators, they could have found domestics looking to hedge. For example, Indian firms may borrow cheaply in USD and earn revenue in INR; oil importers have receivables in INR but since oil is typically priced in dollars, they have USD-denominated payables. These firms can hedge the risk of further INR depreciation by entering a forward agreement with the bank. Their balance sheets would look as follows:

**Indian Oil Importer (onshore)**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| INR | USD | receivables, payables |
| USD | INR | hedge with bank |

Which then feeds into the bank's balance sheet as:

**Bank (speculator)**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| USD | INR | Speculative position |
| INR | USD | hedge with oil importer |

Since the USD assets and INR liabilities are offset with the hedge, the bank's net open position could fall below the $100M threshold. But this swap would do nothing to impact the total short position against the rupee, as the bank never purchased INR. As such, this policy did little to stop the INR from continuing to fall.

After noticing this policy's ineffectiveness, the RBI then banned domestic institutions from offering offshore non-deliverable forwards (NDFs). These are forward contracts between an offshore institution and either an onshore or offshore counterparty. Since these are non-deliverable, no INR changes hands, rather the difference is paid in USD when the forward is due, making them especially helpful to those offshore who lack access to the currency. While most onshore trading is in deliverable forwards, NDFs dominate offshore trading, which is largely made up of [foreign bond investors looking to hedge currency risk](https://www.bis.org/publ/qtrpdf/r_qt1403h.htm). This offshore investor may have a T-account that looks as follows:

**US Investor in India (offshore)**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| INR | USD | Indian bonds, USD loans |
| USD | INR | currency hedge |

The rupee NDF market is nearly 4x the size of the deliverable forwards market, as the chart below shows.[^data] The RBI has little control over this market because they can only limit onshore institutions from taking this trade. Offshore speculators are free to trade with each other and don't need INR. During market turbulence, bans have often created gaps between the onshore deliverables and NDFs. These gaps eventually closed as [the onshore market converged to the offshore price](https://www.bis.org/publ/qtrpdf/r_qt1403h.htm). In other words, NDF prices, largely outside the central bank's purview, typically lead onshore prices during market instability.

{% image "./figures/ndf_vs_del.png", "NDF vs Deliverable Forwards, NDF is more than 3.7x deliverables." %}

Although NDF restrictions may have a short-term impact on exchange rates, they can also introduce new issues. Foreign institutions investing in Indian bonds may want to hedge their exposure to currency risk, shown in the T-account above. Speculators can allow this by taking the other side of the hedge. Without an opportunity to hedge currency risk, these investors may exit the market by selling their bonds and converting the proceeds to USD, resulting in more downward pressure on the rupee.

Although policies that attack speculation may look good politically, they are unlikely to boost the rupee and may end up making it fall even further.

[^data]: Data from the [BIS Triennial survey](https://www.bis.org/statistics/rpfx25_fx_annex.pdf) Table 3.2, which measures daily average turnover in April 2025 vs USD. Total INR outright forwards were $90B, of which $70.5B (78%) were non-deliverable.