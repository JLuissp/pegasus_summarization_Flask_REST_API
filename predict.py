import requests
import json


url = 'http://127.0.0.1:5000/summarize'

data = {
    'TTS':"""Berkshire Hathaway (NYSE:BRKa) Inc on Monday disclosed it has begun investing in Capital One Financial Corp (NYSE:COF) while exiting investments in four other stocks, as the company run by Warren Buffett cut back its exposure to equities.

Buffett's company made its disclosures in a regulatory filing listing its U.S.-traded stocks as of March 31.

Capital One shares rose 5.4% in after-hours trading following Berkshire's disclosure of a 9.92 million share stake worth about $954 million.

The McLean, Virginia-based bank did not immediately respond to requests for comment.

In Monday's filing, Berkshire also revealed a new $41.3 million stake in Diageo (LON:DGE) Plc, the maker of alcoholic beverages including Johnnie Walker and Guinness.

Berkshire also shed its holdings in Bank of New York Mellon (NYSE:BK) Corp and US Bancorp (NYSE:USB), as well as Taiwanese chipmaker TSMC and furniture chain RH (NYSE:RH).

Buffett's company was a net seller of stocks in the quarter, buying $2.87 billion and selling $13.28 billion as it devoted resources elsewhere, including $8.2 billion to boost its stake in truck stop operator Pilot Travel Centers to 80% from 38.6%.

Close to half of its stock sales were in Chevron Corp (NYSE:CVX), though Berkshire still owns a 23.7% stake in another oil company, Occidental Petroleum Corp (NYSE:OXY).

The Omaha, Nebraska-based conglomerate ended March with $130.6 billion of cash and equivalents.

Monday's filing does not say which investments are Buffett's and which are from his portfolio managers Todd Combs and Ted Weschler, though larger investments are usually Buffett's.

Investors often try to piggyback on Berkshire's moves, reflecting Buffett's reputation.

Despite the selling, Berkshire still invests in several financial services companies.

These include Bank of America Corp (NYSE:BAC) and American Express (NYSE:AXP) Corp, where Berkshire's respective $29.5 billion and $25 billion stakes make them its largest stock holdings other than Apple (NASDAQ:AAPL) Corp.

Berkshire also has dozens of operating businesses including the BNSF railroad, Geico car insurance, and many energy, manufacturing and consumer units.

Buffett shed what remained of the TSMC stake six months after surprising investors by revealing a $4.1 billion investment.

He told investors this month he had reevaluated the risks of investing in Taiwan, on growing concern China might soon invade or try to reclaim the island nation."""
}

input_data = json.dumps(data)
#print(input_data)
header = {"Content-Type": 'application/json'}

response = requests.post(url, input_data, headers=header)
print(response.text)