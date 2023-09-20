import ldap3

def check_privilege_escalation(connection, base_dn):
    try:
        # Define a filter to search for high-privileged accounts (e.g., domain admins)
        filter_str = '(|(memberOf=cn=Domain Admins,CN=Users,' + base_dn + '))'

        # Search for accounts matching the filter
        connection.search(search_base=base_dn, search_filter=filter_str, attributes=['sAMAccountName'])

        # Print the results
        print('High-Privileged Accounts:')
        for entry in connection.entries:
            print(f'- {entry.sAMAccountName.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# check_privilege_escalation(connection, base_dn)
