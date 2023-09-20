# Active-Directory-Enumeration-Tool

Disclaimer: This tool is intended for educational and ethical use only. Unauthorized or malicious use of this tool is prohibited.
Overview

The Active Directory Enumeration Tool is a Python script designed to enumerate information from Active Directory environments. It can be used for security assessments, auditing, and penetration testing. The tool leverages LDAP queries and various techniques to gather data that can be valuable for further analysis and testing.
Installation

    Clone the repository to your local machine:

    bash

git clone https://github.com/your-username/active-directory-enumeration.git

Navigate to the tool's directory:

bash

cd active-directory-enumeration

Install the required Python libraries:

bash

    pip install -r requirements.txt

Usage

The tool offers various functionalities for enumerating Active Directory information. Here are the available functions and their descriptions:

    attack_path_analysis.py: Analyzes trust relationships and group memberships to identify potential attack paths for lateral movement and privilege escalation.

    exploitable_services.py: Identifies services running on discovered systems that are known to be vulnerable, allowing for targeted exploitation.

    group_enumeration.py: Enumerates Active Directory groups and their memberships, aiding in the identification of privileged groups and potential lateral movement paths.

    nested_group_enumeration.py: Recursively enumerates nested group memberships to capture all group memberships, even those within nested groups.

    ou_enumeration.py: Enumerates Organizational Units (OUs) within Active Directory to understand the organizational structure and potential security boundaries.

    pass_the_hash.py: Implements Pass-the-Hash (PtH) and Pass-the-Ticket (PtT) attacks to demonstrate lateral movement possibilities.

    password_policy_enumeration.py: Enumerates Active Directory password policy settings, such as complexity requirements, lockout policies, and expiration policies.

    privil3ge_3scalation.py (Privilege Escalation Checks): Finds specific accounts with elevated privileges, such as administrators, and targets them for further exploitation.

    privilege_escalation.py: Additional privilege escalation checks to identify accounts with elevated privileges.

    service_account_discovery.py: Identifies service accounts used in the Active Directory environment, which can be potential targets for compromise.

    session_enumeration.py: Enumerates active sessions on systems to see who is currently logged in, useful for detecting active administrative sessions.

    trust_relationship_enumeration.py: Enumerates trust relationships with other domains or forests, valuable for assessing the security of trust configurations.

Example Usage:

bash

python attack_path_analysis.py

Replace attack_path_analysis.py with the name of the function you want to execute.
Contributions

Contributions to this tool are welcome. Please follow ethical guidelines and best practices when using and contributing to this project.
