class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()

        for cp in cpdomains:
            times, domain = cp.split()
            times = int(times)

            counter[domain] += times

            for i, ch in enumerate(domain):
                if ch == '.':
                    counter[domain[i + 1:]] += times

        return [f'{times} {domain}' for domain, times in counter.items()]
