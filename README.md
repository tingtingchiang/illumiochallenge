# illumiochallenge

## Current Implementation Details  
Program Language: Python  
Construction Runtime: O(n)  
Packet Process Runtime: O(n)  
Run Test: `python3 test.py`  
- all files (`firewall.py`, `test.py`, and the 3 csv files) must be in the same directory.

## Assumptions  
- csv files provided will not use headers
- ranges provided may not be CIDR ranges (aka more discriminatory than a mask)

## Testing process  
My test cases utilize Python's assert statements and can be found in `test.py`. I covered 3 types of tests that I thought would be important according to what the pdf mentioned: Common cases, edge cases, and latency.  
Notes:  
- The common case is just adapted from the pdf
- Assertions in the edge case are commented with the intention of the specific test. Since my particular implementation does first separates rules according to the direction and protocol of the packet (of which there are only 4 possible combinations), I choose to test edge cases using one combination though the last assertion is just to make sure ip address and port rules do not apply outside of the determined combination.
- The timed/latency test can be adjusted by time expected it to run and how many requests are made. The csv used is a little too large (3.41 MB vs 1 MB) but that can be easily fixed later.

## Interesting coding/design/algorithmic decisions
- Validation is its own method to future changes in making the search/validation more efficient will stay clean.

## Refinements and optimizations  
I have a few thoughts on optimizations:
- Tree-like data structure
  - First sort by IP address (using something similar to LPM) but needs to also account for ranges provided that are not describable by a single mask:
    - https://docs.google.com/presentation/d/1K8HUmKv_3cHsXUSrv0U8Pg3cXwnOCfY4y8KpwYXFrFI/edit#slide=id.p21 
  - Port ranges are described then by a list or even a similar tree structure at the end (duplicate leaf values everytime a node splits)
  - Personally regard this as most viable
- Sorted lists (by ip address first again)
  - Keep separate key sets (eg. ip_addr[0] and ip_addr[-1]) to constrict possible address/port ranges and then iterate as seen in the current implementation
  - https://docs.python.org/3/library/bisect.html#bisect.bisect
- Small cache of recently used ip/port ranges
  - Temporally dependent
  - Will be useful for high volume of packet requests (especially in tcp connections, where the same address and port will be used throughout the stream

## Others
While I'd be happy to work on any of the three teams, I am most interested in the Policy team and working to create efficient and accurate policy rules. Thank you!
