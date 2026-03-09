class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()

        for email in emails:
            local_name, domain_name = email.split('@')

            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')

            valid_emails.add(local_name + '@' + domain_name)

        return len(valid_emails)
