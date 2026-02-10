class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])

                if subdomain not in visit_count:
                    visit_count[subdomain] = 0

                visit_count[subdomain] += count

        ans = []
        for subdomain, count in visit_count.items():
            ans.append(f'{count} {subdomain}')

        return ans
