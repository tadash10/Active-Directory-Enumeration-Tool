import ldap3

def enumerate_nested_groups(connection, base_dn, group_dn):
    try:
        # Search for nested groups within the specified group
        filter_str = '(memberOf=' + group_dn + ')'
        connection.search(search_base=base_dn, search_filter=filter_str, attributes=['sAMAccountName'])

        # Print the results
        print('Nested Groups:')
        for entry in connection.entries:
            print(f'- {entry.sAMAccountName.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# enumerate_nested_groups(connection, base_dn, group_dn)
