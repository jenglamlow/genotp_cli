# genotp_cli
Command Line Interface to generate One Time Password (OTP)

Usage:
  genotp INSTANCE USERNAME [SECRET]
  genotp INSTANCE USERNAME [-t TIME]
Options:
  -h --help     Show this screen.
  --version     Show version.
  INSTANCE      Instance eg. klrx010, bewx1551)
  USERNAME      Username
  SECRET        Secret key
  TIME          Generate TOTP at specific time, (Format: "YYYY-MM-DD-HH:MM:SS"). If not specified, local time is used
