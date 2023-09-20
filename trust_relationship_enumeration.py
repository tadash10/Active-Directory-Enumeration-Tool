import ldap3

def enumerate_trust_relationships(connection):
    try:
        # Search for trust relationships
        filter_str = '(objectClass=trustedDomain)'
        connection.search(search_base='DC=domain,DC=com', search_filter=filter_str, attributes=['cn'])

        # Print the results
        print('Trust Relationships:')
        for entry in connection.entries:
            print(f'- {entry.cn.value}')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# enumerate_trust_relationships(connection)
