# Legend "pre-breakout setup" chart (set 2026-10-23)

Ryan, live turn 2026-10-23: *"see if you can use legends to start charting setups"*.

**Where:** the CHART widget in Ryan's **Default** Legend layout (chart_id
`1f99f21f-5df5-4a04-9c8d-b5e8b9601aac`), daily candles, 1-year view. His **Stock trading** layout
(5-minute TSLA) was left untouched.

**How to use it:** the chart's symbol follows the layout's linked watchlist, so clicking
through the 🤖 **Buy Zone - Quality at 200d**, **Re-buy Watch** or **Joint Holdings** list
shows every name with the same setup overlays. The agent cannot change the symbol or draw
trend lines (the connector does not allow either); it can add, restyle and remove indicators
and set the interval.

**What each overlay reads, mapped to the scores the routines already compute:**

| Overlay | Settings | Reads | Used by |
|---|---|---|---|
| SMA 200 (red, thick) | 200, close | The line the Quality @ 200-day watch alerts on (touch / reclaim) | quality_watch.py band, rebuy BUY stage |
| SMA 50 (peach, thick) | 50, close | Re-buy EARLY stage (price back over the 50-day) | quality_watch.rebuy_status |
| SMA 20 (aqua) | 20, close | Pre-breakout trait "below the 20-day" | setups.prebreakout |
| Donchian Channel | 60, dashed | 60-day high and low: traits "fresh 60-day low" and ">= 8% off the 60-day high" | setups.prebreakout |
| Volume + 20-day MA | 20 | Trait "volume drying up" (bars under the MA) | setups.prebreakout |
| RSI (lower pane) | 14, oversold line at **40** (not 30) | Trait "RSI(14) < 40" | setups.prebreakout |
| MACD (lower pane) | 12 / 26 / 9 | Re-buy TURNING stage (MACD over signal) | quality_watch.rebuy_status |

Indicator ids (for a session that needs to restyle or remove them): SMA200
`fcef3d75-a6a4-4212-b921-69281f735f65`, SMA50 `13de4260-659b-4e6f-b9de-6944c2f2fd63`, SMA20
`486da85c-d688-487c-b30d-16823770438e`, Donchian `51983f2a-73dc-4a07-a934-e0ee1a1cd78e`, RSI
`8924ecbd-998b-43f0-b93d-5cc5c37c01e7`, MACD `97ff3834-9eb7-4010-b7ec-f304c5464a8f`, Volume (his)
`89aa9e52-fb27-4a6e-aec0-62ed11b182c0`. The chart now holds 7 of its 10 indicator slots (2 of 5
lower panes).

**Not done, on purpose:** no routine touches Legend. A chart is something Ryan looks at; the
alerts and lists are what notify him. Changing it needs a live Ryan turn.
