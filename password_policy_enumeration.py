import ldap3

def enumerate_password_policy(connection):
    try:
        # Bind with sufficient privileges to retrieve password policy
        connection.bind()

        # Retrieve password policy attributes
        response = connection.search(search_base='CN=Password Settings Container,CN=System,DC=domain,DC=com',
                                     search_filter='(objectClass=msDS-PasswordSettings)',
                                     attributes=['msDS-PasswordReversibleEncryptionEnabled',
                                                 'msDS-PasswordComplexityEnabled',
                                                 'msDS-PasswordHistoryLength',
                                                 'msDS-PasswordLockoutDuration',
                                                 'msDS-PasswordLockoutObservationWindow',
                                                 'msDS-PasswordLockoutThreshold',
                                                 'msDS-MinimumPasswordLength',
                                                 'msDS-MinimumPasswordAge',
                                                 'msDS-MaximumPasswordAge'])

        # Print password policy settings
        if response and len(connection.entries) > 0:
            entry = connection.entries[0]
            print('Password Policy Settings:')
            print(f'- Reversible Encryption Enabled: {entry.msDS_PasswordReversibleEncryptionEnabled.value}')
            print(f'- Complexity Enabled: {entry.msDS_PasswordComplexityEnabled.value}')
            print(f'- History Length: {entry.msDS_PasswordHistoryLength.value}')
            print(f'- Lockout Duration: {entry.msDS_PasswordLockoutDuration.value}')
            print(f'- Observation Window: {entry.msDS_PasswordLockoutObservationWindow.value}')
            print(f'- Lockout Threshold: {entry.msDS_PasswordLockoutThreshold.value}')
            print(f'- Minimum Password Length: {entry.msDS_MinimumPasswordLength.value}')
            print(f'- Minimum Password Age: {entry.msDS_MinimumPasswordAge.value}')
            print(f'- Maximum Password Age: {entry.msDS_MaximumPasswordAge.value}')
        else:
            print('Password policy not found.')

    except ldap3.core.exceptions.LDAPException as e:
        print(f'LDAP Error: {str(e)}')

# Usage example:
# enumerate_password_policy(connection)
