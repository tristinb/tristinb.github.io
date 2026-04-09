---
title: India's foreign exchange intervention through T-Accounts
description: Understanding India's unconventional monetary policy
draft: True
date: 2026-04-06
---

The Indian rupee has been hit especially bad since the war in Iran began, leading the Reserve Bank of India (RBI) to conduct unconventional policies in an attempt to halt the currency's slide. After spending around [$40BN of their foreign exchange reserves](https://tradingeconomics.com/india/foreign-exchange-reserves) in March, The RBI enacted two major unconventional policies in the last week of the month to try to strengthen the currency. First they limited the net open positions on onshore deliverables to $100M per day. When that didn't work they then banned trades in non-deliverable forward contracts. This post breaks down the balance sheet implications of these policies, showing why they are unlikely to work, especially in the long term.

Before the war in Iran began, the rupee was already vulnerable. Beginning around January, the RBI began selling dollars to strengthen the rupee (INR). Because selling dollars reduces the supply of rupees, and therefore tightens credit conditions, the RBI *sterilized* this intervention by buying government bonds to neutralize the impact of their foreign exchange intervention on domestic credit. Sterilization kept it cheap to borrow rupees.

Domestic speculators continued shorting the rupee, taking advantage of loose credit conditions in India. To simplify their balance sheet, we can assume the other side of the INR is the USD. Speculators then had a balance sheet that looked something like 

**Bank (speculator)**
| **Assets** | **Liabilities** | 
|------------------|------------|
| USD | INR |

The bank's net open position here is just the difference between its assets and liabilities, denominated in USD. Notice that the position increased as the INR continued to fall. The RBI's first move was to limit this position to less than $100M at the end of each day. 

Presumably, to keep the position under the limit, the bank would sell USD and buy INR, thereby strengthening the INR. But banks didn't do this. Instead, they found others also willing to speculate against the rupee, which allowed them to directly offload their book to keep their net open positions under the $100M threshold. But even if they couldn't find domestic speculators, they could have found domestic corporates looking to hedge. An oil importer, for example, has receivables in INR but since oil is typically priced in dollars, they have USD-denominated payables. Another canonical example is a domestic company that borrowed in USD. Given the pressure on the rupee, this importer may look to hedge by locking in a forward agreement with the bank. The balance sheets would look as follows:

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
| INR | USD | Onshore deliverable from the bank |

Now since Assets are USD - INR, and liabilities are INR - USD, the bank's net open position could fall below $100M. However, here banks don't buy INR in order to meet the $100M threshold instead, they just swap assets and liabilities with others within the economy, leaving the aggregate USD/INR position the same. As such, this policy did little to stop the INR from continuing to fall.

After noticing this policy's ineffectiveness, the RBI then moved to ban offshore non-deliverable forwards (NDFs). These are effectively agreements for a forward between an offshore institution and either an onshore or offshore counterparty. Since these are non-deliverable, no INR changes hands, rather, the difference is paid in USD when the forward is due, making them especially helpful to those lacking access to currencies with capital controls, like INR. NDFs typically dominate offshore trading, which is largely made up of foreign bond investors looking to hedge currency risk (McCauley et al. 2014). This type of investor may have a T account that looks as follows:

**US Investor in India (offshore)**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| INR | USD | Indian bonds, USD loans |
| USD | INR | hedge with bank |

The RBI is trying to limit the ability to go forward with this hedge, as it results in a short INR position. This short requires someone to take a long INR position on the other side. However, the RBI has little control over this offshore NDF market. 

But even if they could, banning this trade in order to limit speculation, the RBI made it much more difficult for the offshore investor to hedge their exposure to INR. We can imagine a marginal Indian bond investor, who would only invest if they were able to hedge their foreign exchange risk. This investor may exit the market, leading to more downward pressure on the rupee.

Clea. this up/finish it on this note that it's unlikely to do much, but it could hurt.

Cut

This entity could be a speculator betting on INR appreciating. Or it could be a company naturally long USD, short INR looking to hedge by taking a long INR position. That is, a company that receives USD but needs to pay INR. Tata Consulting Services (TCS) is one of India's companies, which offers IT services for companies all over the world. In the US, its customers pay USD, but pays its workforce INR. TCS

The problem with TCS is they almost certainly have access to INR. I need a company like this who lacks access to INR for this to work. Financial flows dwarf trade flows. So I would need someone who can borrow INR and lend USD that would want to hedge. But have this be an NDF and off-shore. Unlikely to exist given they have cheap INR. So this must be a speculator on the other side. But an outright ban can harm an offshore investor.

**TCS**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| USD | INR | receivables, payables|
| INR | USD | hedge with bank|


This below is a hedged position for the bank, not a short. But again, this is someone who could be hurt by this.

Aside from an oil importer, banks may have found offshore counterparties naturally long INR looking to hedge exposure to INR depreciation. This could be a US investor in Indian companies or bonds, who borrows in USD to purchase Indian assets. Since the investor borrowed in dollars, they are happy to settle their forward contract in USD in order to cover losses from INR depreciation. This investor's balance sheet, below, has the same exposure as the onshore oil importer.

**US Investor in India (offshore)**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| INR | USD | receivables, payables|
| USD | INR | hedge with bank|

By banning this trade in order to limit speculation, the RBI made it much more difficult for the offshore investor to hedge their exposure to INR. We can imagine a marginal Indian bond investor, who would only invest if they were able to hedge their foreign exchange risk. This investor may exit the market, leading to more downward pressure on the rupee.

In the balance sheets above, the only player taking a speculative position was the bank. The others were simply looking for ways to hedge their natural long INR positions. Although the RBI is trying to limit the ability of speculators to short the INR, its efforts may just harm the ability of natural longs to hedge while having a limited overall impact on the rupee's value.

QUESTION: THE SPECULATORS ARE USING OFFSHORE MARKETS TO DEEPEN THEIR SHORT, THE LOGIC MISSES THIS. Need to think of who is really getting hurt here/would want to hedge and whether they have access to onshore deliverables or really would prefer offshore NDFs. I think the speculator may need to find someone offshore to take a short.
### Notes

Presumably, to keep the position under the limit, the bank would sell USD and buy INR, thereby strengthening the INR. But banks didn't do this. Instead, they apparently found domestic corporations that were naturally long USD and interested in a hedge. An onshore counterparty long USD would be something Tata Consulting Services (TCS), which provides IT services to countries like the US. TCS would then have receivables denominated in USD and payables denominated in INR. Since TCS may not want to engage in currency speculation, a deliverable forward contract with the bank let them hedge against currency risk. TCS's balance sheet then looks as follows.

Natural long USD, TCS
**TCS**
| **Assets** | **Liabilities** | |
|------------------|------------|------------|
| USD | INR | receivables, payables|
| INR | USD | hedge with bank|