import ldap3

def enumerate_groups(connection, base_dn):
    try:
        # Search for all groups within the specified base DN
        filter_str = '(objectClass=group)'
        connection.search(search_base=base_dn, search_filter=filter_str, attributes=['sAMAccountName'])

        # Print the results
        print('Active Directory Groups:')
        for entry in connection.entries:
            print(f'- {entry.sAMAccountName.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# enumerate_groups(connection, base_dn)
