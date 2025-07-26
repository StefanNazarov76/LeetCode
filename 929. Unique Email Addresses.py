class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        qnique_emails = set()

        for email in emails:
            local, domain = email.split('@')

            local = local.split('+')[0]
            local = local.replace('.', '')

            qnique_emails.add(local + '@' + domain)

        return len(qnique_emails)
