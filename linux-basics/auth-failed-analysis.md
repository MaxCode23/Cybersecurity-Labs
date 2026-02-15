# Authentication Log Analysis – Failed SU Attempts

## Log Location
Authentication logs are stored at:
- /var/log/auth.log

## Test Performed
Attempted to switch users using `su max` and entered incorrect password multiple times.

## Example Log Entry
FAILED SU (to max) max on pts/0
pam_unix(su:auth): authentication failure; logname=max uid=1000 euid=0 tty=/dev/pts/0 ruser=max rhost= user=max

## Important Fields
- Timestamp
- Service (su)
- Authentication failure
- Target user
- Terminal (tty)
- UID and EUID

## Detection Insight
Multiple failed authentication attempts within a short time window could indicate:
- Brute force attack
- Privilege escalation attempt
- Credential misuse
