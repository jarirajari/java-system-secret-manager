# Java system secret manager
From [https://jarirajari.wordpress.com](https://jarirajari.wordpress.com)

## Installation

Install and verify pass
```
sudo apt install pass
sudo pass --version
```

Switch user (generate if needed): 'javauser' for example
```
su - javauser
```

Generate new key that expires after n days or never (for example, 'changeme123')
```
gpg --full-generate-key
```

List keys and extract GPG KEY ID
```
gpg --list-keys
```

Initialize secret storage with key and check rights
```
pass init <GPG KEY ID>
ls -ld /home/$USER/.password-store
```

# Basic ops

Create secret, for example 'master/unlock'
```
pass insert master/unlock
```

Read secret
```
pass master/unlock
pass show master/unlock
```

Write secret
```
pass edit master/unlock
```

Destroy secret
```
pass rm master/unlock
```

# Turn pass into secret manager

Check that you are the correct user
```
whoami
```

Insert a secret that is used for "unlocking" the manager
```
pass insert master/unlock
pass master/unlock
```

Configure gpg-agent to cache passphrases by adding or modifying ~/.gnupg/gpg-agent.conf
```
default-cache-ttl 3600       # Cache passphrase for 1 hour
max-cache-ttl 7200           # Maximum time (in seconds) to cache
```

Start gpg-agent session
```
eval $(gpg-agent --daemon)
```

Alternatively, you could remove passphrase completely (but not recommended).

First, edit configuration by typing:
```
gpg --edit-key <your-key-id>
```

Then use the passwd command within GPG to remove the passphrase

# Java integration

see `SystemSecretManager.java` for static method.
