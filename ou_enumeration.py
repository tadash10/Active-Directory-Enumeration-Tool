import ldap3

def enumerate_organizational_units(connection, base_dn):
    try:
        # Search for Organizational Units (OUs)
        filter_str = '(objectClass=organizationalUnit)'
        connection.search(search_base=base_dn, search_filter=filter_str, attributes=['ou'])

        # Print the results
        print('Organizational Units:')
        for entry in connection.entries:
            print(f'- {entry.ou.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# enumerate_organizational_units(connection, base_dn)
