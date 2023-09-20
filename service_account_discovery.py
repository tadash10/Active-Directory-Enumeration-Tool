import ldap3

def discover_service_accounts(connection, base_dn):
    try:
        # Define a filter to search for service accounts (e.g., accounts with 'svc-' prefix)
        filter_str = '(&(objectClass=user)(sAMAccountName=svc-*))'

        # Search for service accounts matching the filter
        connection.search(search_base=base_dn, search_filter=filter_str, attributes=['sAMAccountName'])

        # Print the results
        print('Service Accounts:')
        for entry in connection.entries:
            print(f'- {entry.sAMAccountName.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# discover_service_accounts(connection, base_dn)
