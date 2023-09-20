import ldap3

# Define Active Directory server connection parameters
server_url = 'ldap://your-ad-server'
username = 'your-username'
password = 'your-password'
base_dn = 'dc=your,dc=domain,dc=com'

# Define the attributes you want to retrieve (e.g., user accounts, groups, computers)
attributes = ['sAMAccountName', 'displayName', 'userPrincipalName']

def enumerate_active_directory():
    try:
        # Establish a connection to the Active Directory server
        server = ldap3.Server(server_url)
        connection = ldap3.Connection(server, user=username, password=password, auto_bind=True)

        # Search for Active Directory objects
        search_filter = '(objectClass=*)'  # You can customize the filter as needed
        connection.search(search_base=base_dn, search_filter=search_filter, attributes=attributes)

        # Retrieve and print the results
        for entry in connection.entries:
            print(f'DN: {entry.entry_dn}')
            for attribute in attributes:
                if attribute in entry:
                    values = entry[attribute]
                    if len(values) == 1:
                        print(f'{attribute}: {values[0]}')
                    else:
                        print(f'{attribute}: {", ".join(values)}')
            print('')

        # Close the connection
        connection.unbind()

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    print('Active Directory Enumeration Tool')
    print('----------------------------------\n')
    enumerate_active_directory()
